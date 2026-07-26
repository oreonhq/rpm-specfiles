# adoptium-temurin-java-repository

The adoptium-temurin-java-repository package

https://fedoraproject.org/wiki/Changes/ThirdPartyLegacyJdks

This package adds Eclipse Adoptium JDKs as a replacement for JDKs which are no longer included in Fedora

https://adoptium.net/installation/linux/

This package adds configuration to add a remote repository
of https://adoptium.net/installation/linux/#_centosrhelfedora_instructions ,
if third-party repositories are enabled on a Fedora Linux system.
This repository contains all JDKS which are live and not available in fedora 
as per https://fedoraproject.org/wiki/Changes/ThirdPartyLegacyJdks .
It (4.11.2024) installs: temurin-11-jdk temurin-11-jre temurin-17-jdk temurin-17-jre temurin-21-jdk
 temurin-21-jre temurin-22-jdk temurin-22-jre temurin-23-jdk temurin-23-jre temurin-8-jdk
 temurin-8-jre
Warning, jdk contains both jre and jdk, so if you install jdk and jre (of same version)
you will have two java alternatives masters, and one javac master.
Since f42 it will be obsoleting retired java-(1.8.0,11,17)-openjdk-*


Obsoletes:
 * java-1.8.0-openjdk
 * java-1.8.0-openjdk-demo
 * java-1.8.0-openjdk-demo-fastdebug
 * java-1.8.0-openjdk-demo-slowdebug
 * java-1.8.0-openjdk-demo-unstripped
 * java-1.8.0-openjdk-devel
 * java-1.8.0-openjdk-devel-fastdebug
 * java-1.8.0-openjdk-devel-slowdebug
 * java-1.8.0-openjdk-devel-unstripped
 * java-1.8.0-openjdk-docs
 * java-1.8.0-openjdk-docs-fastdebug
 * java-1.8.0-openjdk-docs-slowdebug
 * java-1.8.0-openjdk-docs-unstripped
 * java-1.8.0-openjdk-fastdebug
 * java-1.8.0-openjdk-headless
 * java-1.8.0-openjdk-headless-fastdebug
 * java-1.8.0-openjdk-headless-slowdebug
 * java-1.8.0-openjdk-headless-unstripped
 * java-1.8.0-openjdk-javadoc
 * java-1.8.0-openjdk-javadoc-fastdebug
 * java-1.8.0-openjdk-javadoc-slowdebug
 * java-1.8.0-openjdk-javadoc-unstripped
 * java-1.8.0-openjdk-javadoc-zip
 * java-1.8.0-openjdk-javadoc-zip-fastdebug
 * java-1.8.0-openjdk-javadoc-zip-slowdebug
 * java-1.8.0-openjdk-javadoc-zip-unstripped
 * java-1.8.0-openjdk-portable
 * java-1.8.0-openjdk-portable-demo
 * java-1.8.0-openjdk-portable-demo-fastdebug
 * java-1.8.0-openjdk-portable-demo-slowdebug
 * java-1.8.0-openjdk-portable-demo-unstripped
 * java-1.8.0-openjdk-portable-devel
 * java-1.8.0-openjdk-portable-devel-fastdebug
 * java-1.8.0-openjdk-portable-devel-slowdebug
 * java-1.8.0-openjdk-portable-devel-unstripped
 * java-1.8.0-openjdk-portable-docs
 * java-1.8.0-openjdk-portable-docs-fastdebug
 * java-1.8.0-openjdk-portable-docs-slowdebug
 * java-1.8.0-openjdk-portable-docs-unstripped
 * java-1.8.0-openjdk-portable-fastdebug
 * java-1.8.0-openjdk-portable-headless
 * java-1.8.0-openjdk-portable-headless-fastdebug
 * java-1.8.0-openjdk-portable-headless-slowdebug
 * java-1.8.0-openjdk-portable-headless-unstripped
 * java-1.8.0-openjdk-portable-javadoc
 * java-1.8.0-openjdk-portable-javadoc-fastdebug
 * java-1.8.0-openjdk-portable-javadoc-slowdebug
 * java-1.8.0-openjdk-portable-javadoc-unstripped
 * java-1.8.0-openjdk-portable-javadoc-zip
 * java-1.8.0-openjdk-portable-javadoc-zip-fastdebug
 * java-1.8.0-openjdk-portable-javadoc-zip-slowdebug
 * java-1.8.0-openjdk-portable-javadoc-zip-unstripped
 * java-1.8.0-openjdk-portable-slowdebug
 * java-1.8.0-openjdk-portable-sources
 * java-1.8.0-openjdk-portable-sources-fastdebug
 * java-1.8.0-openjdk-portable-sources-slowdebug
 * java-1.8.0-openjdk-portable-sources-unstripped
 * java-1.8.0-openjdk-portable-src
 * java-1.8.0-openjdk-portable-src-fastdebug
 * java-1.8.0-openjdk-portable-src-slowdebug
 * java-1.8.0-openjdk-portable-src-unstripped
 * java-1.8.0-openjdk-portable-unstripped
 * java-1.8.0-openjdk-slowdebug
 * java-1.8.0-openjdk-sources
 * java-1.8.0-openjdk-sources-fastdebug
 * java-1.8.0-openjdk-sources-slowdebug
 * java-1.8.0-openjdk-sources-unstripped
 * java-1.8.0-openjdk-src
 * java-1.8.0-openjdk-src-fastdebug
 * java-1.8.0-openjdk-src-slowdebug
 * java-1.8.0-openjdk-src-unstripped
 * java-1.8.0-openjdk-unstripped
 * java-11-openjdk
 * java-11-openjdk-demo
 * java-11-openjdk-demo-fastdebug
 * java-11-openjdk-demo-slowdebug
 * java-11-openjdk-demo-unstripped
 * java-11-openjdk-devel
 * java-11-openjdk-devel-fastdebug
 * java-11-openjdk-devel-slowdebug
 * java-11-openjdk-devel-unstripped
 * java-11-openjdk-docs
 * java-11-openjdk-docs-fastdebug
 * java-11-openjdk-docs-slowdebug
 * java-11-openjdk-docs-unstripped
 * java-11-openjdk-fastdebug
 * java-11-openjdk-headless
 * java-11-openjdk-headless-fastdebug
 * java-11-openjdk-headless-slowdebug
 * java-11-openjdk-headless-unstripped
 * java-11-openjdk-javadoc
 * java-11-openjdk-javadoc-fastdebug
 * java-11-openjdk-javadoc-slowdebug
 * java-11-openjdk-javadoc-unstripped
 * java-11-openjdk-javadoc-zip
 * java-11-openjdk-javadoc-zip-fastdebug
 * java-11-openjdk-javadoc-zip-slowdebug
 * java-11-openjdk-javadoc-zip-unstripped
 * java-11-openjdk-portable
 * java-11-openjdk-portable-demo
 * java-11-openjdk-portable-demo-fastdebug
 * java-11-openjdk-portable-demo-slowdebug
 * java-11-openjdk-portable-demo-unstripped
 * java-11-openjdk-portable-devel
 * java-11-openjdk-portable-devel-fastdebug
 * java-11-openjdk-portable-devel-slowdebug
 * java-11-openjdk-portable-devel-unstripped
 * java-11-openjdk-portable-docs
 * java-11-openjdk-portable-docs-fastdebug
 * java-11-openjdk-portable-docs-slowdebug
 * java-11-openjdk-portable-docs-unstripped
 * java-11-openjdk-portable-fastdebug
 * java-11-openjdk-portable-headless
 * java-11-openjdk-portable-headless-fastdebug
 * java-11-openjdk-portable-headless-slowdebug
 * java-11-openjdk-portable-headless-unstripped
 * java-11-openjdk-portable-javadoc
 * java-11-openjdk-portable-javadoc-fastdebug
 * java-11-openjdk-portable-javadoc-slowdebug
 * java-11-openjdk-portable-javadoc-unstripped
 * java-11-openjdk-portable-javadoc-zip
 * java-11-openjdk-portable-javadoc-zip-fastdebug
 * java-11-openjdk-portable-javadoc-zip-slowdebug
 * java-11-openjdk-portable-javadoc-zip-unstripped
 * java-11-openjdk-portable-slowdebug
 * java-11-openjdk-portable-sources
 * java-11-openjdk-portable-sources-fastdebug
 * java-11-openjdk-portable-sources-slowdebug
 * java-11-openjdk-portable-sources-unstripped
 * java-11-openjdk-portable-src
 * java-11-openjdk-portable-src-fastdebug
 * java-11-openjdk-portable-src-slowdebug
 * java-11-openjdk-portable-src-unstripped
 * java-11-openjdk-portable-unstripped
 * java-11-openjdk-slowdebug
 * java-11-openjdk-sources
 * java-11-openjdk-sources-fastdebug
 * java-11-openjdk-sources-slowdebug
 * java-11-openjdk-sources-unstripped
 * java-11-openjdk-src
 * java-11-openjdk-src-fastdebug
 * java-11-openjdk-src-slowdebug
 * java-11-openjdk-src-unstripped
 * java-11-openjdk-unstripped
 * java-17-openjdk
 * java-17-openjdk-demo
 * java-17-openjdk-demo-fastdebug
 * java-17-openjdk-demo-slowdebug
 * java-17-openjdk-demo-unstripped
 * java-17-openjdk-devel
 * java-17-openjdk-devel-fastdebug
 * java-17-openjdk-devel-slowdebug
 * java-17-openjdk-devel-unstripped
 * java-17-openjdk-docs
 * java-17-openjdk-docs-fastdebug
 * java-17-openjdk-docs-slowdebug
 * java-17-openjdk-docs-unstripped
 * java-17-openjdk-fastdebug
 * java-17-openjdk-headless
 * java-17-openjdk-headless-fastdebug
 * java-17-openjdk-headless-slowdebug
 * java-17-openjdk-headless-unstripped
 * java-17-openjdk-javadoc
 * java-17-openjdk-javadoc-fastdebug
 * java-17-openjdk-javadoc-slowdebug
 * java-17-openjdk-javadoc-unstripped
 * java-17-openjdk-javadoc-zip
 * java-17-openjdk-javadoc-zip-fastdebug
 * java-17-openjdk-javadoc-zip-slowdebug
 * java-17-openjdk-javadoc-zip-unstripped
 * java-17-openjdk-portable
 * java-17-openjdk-portable-demo
 * java-17-openjdk-portable-demo-fastdebug
 * java-17-openjdk-portable-demo-slowdebug
 * java-17-openjdk-portable-demo-unstripped
 * java-17-openjdk-portable-devel
 * java-17-openjdk-portable-devel-fastdebug
 * java-17-openjdk-portable-devel-slowdebug
 * java-17-openjdk-portable-devel-unstripped
 * java-17-openjdk-portable-docs
 * java-17-openjdk-portable-docs-fastdebug
 * java-17-openjdk-portable-docs-slowdebug
 * java-17-openjdk-portable-docs-unstripped
 * java-17-openjdk-portable-fastdebug
 * java-17-openjdk-portable-headless
 * java-17-openjdk-portable-headless-fastdebug
 * java-17-openjdk-portable-headless-slowdebug
 * java-17-openjdk-portable-headless-unstripped
 * java-17-openjdk-portable-javadoc
 * java-17-openjdk-portable-javadoc-fastdebug
 * java-17-openjdk-portable-javadoc-slowdebug
 * java-17-openjdk-portable-javadoc-unstripped
 * java-17-openjdk-portable-javadoc-zip
 * java-17-openjdk-portable-javadoc-zip-fastdebug
 * java-17-openjdk-portable-javadoc-zip-slowdebug
 * java-17-openjdk-portable-javadoc-zip-unstripped
 * java-17-openjdk-portable-slowdebug
 * java-17-openjdk-portable-sources
 * java-17-openjdk-portable-sources-fastdebug
 * java-17-openjdk-portable-sources-slowdebug
 * java-17-openjdk-portable-sources-unstripped
 * java-17-openjdk-portable-src
 * java-17-openjdk-portable-src-fastdebug
 * java-17-openjdk-portable-src-slowdebug
 * java-17-openjdk-portable-src-unstripped
 * java-17-openjdk-portable-unstripped
 * java-17-openjdk-slowdebug
 * java-17-openjdk-sources
 * java-17-openjdk-sources-fastdebug
 * java-17-openjdk-sources-slowdebug
 * java-17-openjdk-sources-unstripped
 * java-17-openjdk-src
 * java-17-openjdk-src-fastdebug
 * java-17-openjdk-src-slowdebug
 * java-17-openjdk-src-unstripped
 * java-17-openjdk-unstripped < 10000

