# cui-parent-pom

## Status
[![Java CI with Maven](https://github.com/cuioss/cui-parent-pom/actions/workflows/maven.yml/badge.svg)](https://github.com/cuioss/cui-parent-pom/actions/workflows/maven.yml)
[![License](http://img.shields.io/:license-apache-blue.svg)](http://www.apache.org/licenses/LICENSE-2.0.html)
[![Maven](https://img.shields.io/maven-metadata/v/http/central.maven.org/maven2/com/github/cuioss/cui-parent-pom/maven-metadata.xml.svg)](http://central.maven.org/maven2/io/github/cuioss/cui-parent-pom/)

## What is it?
Parent pom for open-source-projects. It defines and configures a number of maven-plugins, unifying the descendant modules.
It aims at modules being at least Java 11. It defines the sonatype-repositories as read and deploy repositories.

## Maven Coordinates
### General parent pom
```xml
<parent>
   <groupId>io.github.cuioss</groupId>
   <artifactId>cui-parent-pom</artifactId>
   <version>1.0</version>
</parent>
```

### Including dependency-management
```xml
<dependencyManagement>
    <dependencies>
        <dependency>
            <groupId>io.github.cuioss</groupId>
            <artifactId>cui-dependency-bom</artifactId>
            <version>${cui.dependency.bom.version}</version>
            <type>pom</type>
            <scope>import</scope>
        </dependency>
    </dependencies>
</dependencyManagement>
```
## Usage for Standard java-modules
```xml
<project xmlns="http://maven.apache.org/POM/4.0.0" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xsi:schemaLocation="http://maven.apache.org/POM/4.0.0 http://maven.apache.org/xsd/maven-4.0.0.xsd">
    <modelVersion>4.0.0</modelVersion>
    <parent>
        <groupId>io.github.cuioss</groupId>
        <artifactId>cui-parent-pom</artifactId>
        <version>1.0-SNAPSHOT</version>
        <relativePath>..</relativePath>
    </parent>
    <artifactId>cui-java-sample</artifactId>
    <name>cui java sample</name>
    <packaging>pom</packaging>
    <description>Providing configuration for default maven-plugins</description>
    <dependencyManagement>
        <dependencies>
            <dependency>
                <groupId>io.github.cuioss</groupId>
                <artifactId>cui-dependency-bom</artifactId>
                <!-- Defined at cui-parent-pom-->
                <version>${cui.dependency.bom.version}</version>
                <type>pom</type>
                <scope>import</scope>
            </dependency>
        </dependencies>
    </dependencyManagement>
    <dependencies>
        <!-- Provided-->
        <dependency>
            <groupId>org.projectlombok</groupId>
            <artifactId>lombok</artifactId>
        </dependency>
        <!-- Unit testing -->
        <dependency>
            <groupId>org.junit.jupiter</groupId>
            <artifactId>junit-jupiter</artifactId>
        </dependency>
    </dependencies>
    <build>
        <plugins>
            <plugin>
                <artifactId>maven-source-plugin</artifactId>
            </plugin>
            <plugin>
                <artifactId>maven-javadoc-plugin</artifactId>
            </plugin>
            <plugin>
                <groupId>org.codehaus.mojo</groupId>
                <artifactId>build-helper-maven-plugin</artifactId>
            </plugin>
            <plugin>
                <groupId>org.codehaus.mojo</groupId>
                <artifactId>buildnumber-maven-plugin</artifactId>
            </plugin>
            <plugin>
                <groupId>org.jboss.jandex</groupId>
                <artifactId>jandex-maven-plugin</artifactId>
            </plugin>
        </plugins>
    </build>
</project>
```