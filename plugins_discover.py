#!/usr/bin/env python
import zipfile
import io
import re
import argparse


def discover_plugins(jenkins_war):
    """
    discover_plugins
    extracts metadata for each plugin included in jenkins.war

    :param jenkins_war: path to jenkins.war
    :returns: a list of dicts for each plugin

    """
    plugins = []
    with zipfile.ZipFile(jenkins_war) as j_war:
        for pn_hpi in j_war.infolist():
            regex = r'^WEB-INF/(detached-plugins|plugins)/(.*).hpi$'
            if re.match(regex, pn_hpi.filename):
                pn_data = j_war.read(pn_hpi.filename)
                pn_stm = io.BytesIO(pn_data)
                with zipfile.ZipFile(pn_stm) as pn_zip:
                    meta_inf = pn_zip.read('META-INF/MANIFEST.MF')
                    plugin = {}
                    for line in meta_inf.split('\n'):
                        kv_rx = '^(?P<key>.*):(?P<value>.*?)$'
                        res = re.match(kv_rx, line)
                        if res:
                            key = res.group('key')
                            value = res.group('value')
                            plugin[key.strip()] = value.strip()
                    plugins.append(plugin)
    return plugins


def main():
    """main"""
    parser = argparse.ArgumentParser()
    parser.add_argument('--jenkins_war', required=True,
                        help='path to jenkins.war')
    args = parser.parse_args()
    plugins = discover_plugins(args.jenkins_war)
    for plugin in plugins:
        print('%s : %s' % (plugin.get('Short-Name'),
                           plugin.get('Plugin-Version')))


if __name__ == '__main__':
    main()
