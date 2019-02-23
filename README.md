# oss-parent-pom

## Status
[![Build Status](https://travis-ci.org/cuioss/oss-parent-pom.svg?branch=master)](https://travis-ci.org/cuioss/oss-parent-pom)
[![License](http://img.shields.io/:license-apache-blue.svg)](http://www.apache.org/licenses/LICENSE-2.0.html)
[![Maven](https://img.shields.io/maven-metadata/v/http/central.maven.org/maven2/com/github/cuioss/cuioss-parent-pom/maven-metadata.xml.svg)](http://central.maven.org/maven2/com/github/cuioss/cuioss-parent-pom/)

## What is it?
Parent pom for open-source-projects. It defines and configures a number of maven-plugins, unifying the descendant modules.
It aims at modules being at least Java 8. It defines the sonatype-repositories as read and deploy repositories.

## Maven Coordinates
```xml
<parent>
   <groupId>com.github.cuioss</groupId>
   <artifactId>cuioss-parent-pom</artifactId>
   <version>1.0.0.3</version>
</parent>
```

## Configured Plugins
- [maven-ant-plugin](https://maven.apache.org/plugins/maven-ant-plugin/): 1.8
- [maven-assembly-plugin](https://maven.apache.org/plugins/maven-assembly-plugin/): 3.1.1
- [maven-clean-plugin](https://maven.apache.org/plugins/maven-clean-plugin/): 3.1.0
	- Source and target are configured to Java 8
- [maven-dependency-plugin](https://maven.apache.org/plugins/maven-dependency-plugin/): 3.1.1	
- [maven-deploy-plugin](https://maven.apache.org/plugins/maven-deploy-plugin/): 2.8.2	
- [maven-enforcer-plugin](https://maven.apache.org/plugins/maven-enforcer-plugin/): 1.4.1
	- Ammended with org.codehaus.mojo:extra-enforcer-rules
- [maven-failsafe-plugin](https://maven.apache.org/plugins/maven-failsafe-plugin/): 2.22.1
- [maven-gpg-plugin](https://maven.apache.org/plugins/maven-gpg-plugin/): 1.6
- [maven-install-plugin](https://maven.apache.org/plugins/maven-install-plugin/): 2.5.2	
- [maven-jar-plugin](https://maven.apache.org/plugins/maven-jar-plugin/): 3.1.1
- [maven-javadoc-plugin](https://maven.apache.org/plugins/maven-javadoc-plugin/): 3.0.1
- [maven-release-plugin](https://maven.apache.org/plugins/maven-release-plugin/): 2.5.3
- [maven-resources-plugin](https://maven.apache.org/plugins/maven-resources-plugin/): 3.1.0
- [maven-shade-plugin](https://maven.apache.org/plugins/maven-shade-plugin/): 3.2.1
- [maven-site-plugin](https://maven.apache.org/plugins/maven-site-plugin/): 3.7.1
- [maven-source-plugin](https://maven.apache.org/plugins/maven-source-plugin/): 3.0.1
- [maven-surefire-plugin](https://maven.apache.org/plugins/maven-surefire-plugin/): 2.22.1
- [maven-surefire-report-plugin](https://maven.apache.org/plugins/maven-surefire-report-plugin/): 2.22.1
- [maven-war-plugin](https://maven.apache.org/plugins/maven-war-plugin/): 3.2.2
- [org.codehaus.mojo:build-helper-maven-plugin](https://www.mojohaus.org/build-helper-maven-plugin/): 3.0.0
- [org.codehaus.mojo:buildnumber-maven-plugin](https://www.mojohaus.org/buildnumber-maven-plugin/): 1.4
- [org.codehaus.mojo:versions-maven-plugin](https://www.mojohaus.org/versions-maven-plugin/): 2.7
- [jandex-maven-plugin](https://github.com/wildfly/jandex-maven-plugin): 1.0.5

## Activated Plugins
By using this parent there is only the enforcer plugin activated. The others are only configured
