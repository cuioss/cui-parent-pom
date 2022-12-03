# cui-parent-pom

## Status
[![Java CI with Maven](https://github.com/cuioss/cui-parent-pom/actions/workflows/maven.yml/badge.svg)](https://github.com/cuioss/cui-parent-pom/actions/workflows/maven.yml)
[![License](http://img.shields.io/:license-apache-blue.svg)](http://www.apache.org/licenses/LICENSE-2.0.html)
[![Maven](https://img.shields.io/maven-metadata/v/http/central.maven.org/maven2/com/github/cuioss/cui-parent-pom/maven-metadata.xml.svg)](http://central.maven.org/maven2/com/github/cuioss/cui-parent-pom/)

## What is it?
Parent pom for open-source-projects. It defines and configures a number of maven-plugins, unifying the descendant modules.
It aims at modules being at least Java 8. It defines the sonatype-repositories as read and deploy repositories.

## Maven Coordinates
### General parent pom
```xml
<parent>
   <groupId>com.github.cuioss</groupId>
   <artifactId>cui-parent-pom</artifactId>
   <version>1.0</version>
</parent>
```

### Parent pom for java-projects
```xml
<parent>
   <groupId>com.github.cuioss</groupId>
   <artifactId>cui-parent-java</artifactId>
   <version>1.0</version>
</parent>
```

### Including dependency-management
```xml
<dependencyManagement>
    <dependencies>
        <dependency>
            <groupId>com.github.cuioss</groupId>
            <artifactId>cui-dependency-management</artifactId>
            <version>${cui.dependencies.version}</version>
            <type>pom</type>
            <scope>import</scope>
        </dependency>
    </dependencies>
</dependencyManagement>
```
