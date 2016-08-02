Scripts for Jenkins maintenance.

## plugins_discover.py
Lists all bundled plugins and their appropriate versions in jenkins.war. This is useful before upgrading to a new version
of Jenkins, especially if there are pinned plugins that override the current version bundled plugins.

Usage:
```shell
./plugins_discover.py --jenkins_war /path/to/jenkins.war
```

Example:
```shell
> wget https://updates.jenkins-ci.org/download/war/2.16/jenkins.war
> ./plugins_discover.py --jenkins_war jenkins.war

script-security : 1.13
antisamy-markup-formatter : 1.1
windows-slaves : 1.0
ssh-slaves : 1.9
ssh-credentials : 1.10
javadoc : 1.1
pam-auth : 1.1
cvs : 2.11
external-monitor-job : 1.4
translation : 1.10
mailer : 1.11
ldap : 1.11
ant : 1.2
junit : 1.2-beta-4
matrix-project : 1.4.1
maven-plugin : 2.7.1
subversion : 1.54
credentials : 1.18
bouncycastle-api : 2.16.0
matrix-auth : 1.1
```
