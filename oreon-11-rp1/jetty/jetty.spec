# Copyright (c) 2000-2007, JPackage Project
# All rights reserved.
#
# Redistribution and use in source and binary forms, with or without
# modification, are permitted provided that the following conditions
# are met:
#
# 1. Redistributions of source code must retain the above copyright
#    notice, this list of conditions and the following disclaimer.
# 2. Redistributions in binary form must reproduce the above copyright
#    notice, this list of conditions and the following disclaimer in the
#    documentation and/or other materials provided with the
#    distribution.
# 3. Neither the name of the JPackage Project nor the names of its
#    contributors may be used to endorse or promote products derived
#    from this software without specific prior written permission.
#
# THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS
# "AS IS" AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT
# LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR
# A PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT
# OWNER OR CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL,
# SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT
# LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS OF USE,
# DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY
# THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT
# (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE
# OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.
#

%global jtuid       110
%global username    %{name}
%global confdir     %{_sysconfdir}/%{name}
%global logdir      %{_localstatedir}/log/%{name}
%global homedir     %{_datadir}/%{name}
%global jettycachedir %{_localstatedir}/cache/%{name}
%global tempdir     %{jettycachedir}/temp
%global rundir      %{_localstatedir}/run/%{name}
%global jettylibdir %{_localstatedir}/lib/%{name}
%global appdir      %{jettylibdir}/webapps


%global addver  .v20210413

# minimal version required to build eclipse and thermostat
# eclipse needs: util, server, http, continuation, io, security, servlet
# thermostat needs: server, jaas, webapp
# above modules need: jmx, xml
%bcond_without  jp_minimal

Name:           jetty
Version:        9.4.40
Release:        18%{?dist}
Summary:        Java Webserver and Servlet Container

# Jetty is dual licensed under both ASL 2.0 and EPL 1.0, see NOTICE.txt
# Automatically converted from old format: ASL 2.0 or EPL-1.0 - review is highly recommended.
License:        Apache-2.0 OR EPL-1.0
URL:            http://www.eclipse.org/jetty/
Source0:        https://github.com/eclipse/%{name}.project/archive/%{name}-%{version}%{addver}.tar.gz
Source1:        jetty.sh
Source3:        jetty.logrotate
Source5:        %{name}.service
# MIT license text taken from Utf8Appendable.java
Source6:        LICENSE-MIT

Patch1:         0001-Distro-jetty.home.patch
Patch2:         0002-Port-to-servlet-api-4-5.patch
# oreon url source checksums begin
%global source0_sha256 11b612ef3489f350c9d8eeeff3227e76752b089facad7507b831d822e091d9c0
%global source0_file jetty-9.4.40.v20210413.tar.gz
# oreon url source checksums end

BuildRequires:  maven-local-openjdk25
BuildRequires:  mvn(javax.servlet:javax.servlet-api)
BuildRequires:  mvn(org.apache.felix:maven-bundle-plugin)
BuildRequires:  mvn(org.apache.maven.plugins:maven-shade-plugin)
BuildRequires:  mvn(org.codehaus.mojo:build-helper-maven-plugin)
BuildRequires:  mvn(org.slf4j:slf4j-api)

%if %{without jp_minimal}
BuildRequires:  maven-local-openjdk25
BuildRequires:  mvn(com.github.jnr:jnr-unixsocket)
BuildRequires:  mvn(javax.annotation:javax.annotation-api)
BuildRequires:  mvn(javax.enterprise:cdi-api)
BuildRequires:  mvn(javax.servlet:javax.servlet-api)
BuildRequires:  mvn(javax.servlet.jsp:javax.servlet.jsp-api)
BuildRequires:  mvn(javax.servlet:jstl)
BuildRequires:  mvn(javax.transaction:javax.transaction-api)
BuildRequires:  mvn(javax.websocket:javax.websocket-api)
BuildRequires:  mvn(javax.websocket:javax.websocket-client-api)
BuildRequires:  mvn(org.apache.ant:ant)
BuildRequires:  mvn(org.apache.ant:ant-launcher)
BuildRequires:  mvn(org.apache.felix:maven-bundle-plugin)
BuildRequires:  mvn(org.apache.maven:maven-artifact)
BuildRequires:  mvn(org.apache.maven:maven-core)
BuildRequires:  mvn(org.apache.maven:maven-plugin-api)
BuildRequires:  mvn(org.apache.maven:maven-project)
BuildRequires:  mvn(org.apache.maven.plugins:maven-antrun-plugin)
BuildRequires:  mvn(org.apache.maven.plugins:maven-assembly-plugin)
BuildRequires:  mvn(org.apache.maven.plugins:maven-dependency-plugin)
BuildRequires:  mvn(org.apache.maven.plugins:maven-failsafe-plugin)
BuildRequires:  mvn(org.apache.maven.plugins:maven-plugin-plugin)
BuildRequires:  mvn(org.apache.maven.plugins:maven-remote-resources-plugin)
BuildRequires:  mvn(org.apache.maven.plugins:maven-shade-plugin)
BuildRequires:  mvn(org.apache.maven.plugins:maven-war-plugin)
BuildRequires:  mvn(org.apache.maven.plugin-tools:maven-plugin-annotations)
BuildRequires:  mvn(org.apache.maven.plugin-tools:maven-plugin-tools-api)
BuildRequires:  mvn(org.apache.maven.shared:maven-artifact-transfer)
BuildRequires:  mvn(org.apache.taglibs:taglibs-standard-impl)
BuildRequires:  mvn(org.apache.taglibs:taglibs-standard-spec)
BuildRequires:  mvn(org.apache.tomcat:tomcat-jasper)
BuildRequires:  mvn(org.codehaus.mojo:build-helper-maven-plugin)
BuildRequires:  mvn(org.codehaus.mojo:exec-maven-plugin)
BuildRequires:  mvn(org.eclipse.jetty.alpn:alpn-api)
BuildRequires:  mvn(org.eclipse.jetty.orbit:javax.mail.glassfish)
BuildRequires:  mvn(org.eclipse.jetty.orbit:javax.security.auth.message)
BuildRequires:  mvn(org.eclipse.jetty.toolchain:jetty-assembly-descriptors)
BuildRequires:  mvn(org.eclipse.jetty.toolchain:jetty-schemas)
BuildRequires:  mvn(org.eclipse.jetty.toolchain:jetty-test-helper)
BuildRequires:  mvn(org.jboss.weld.servlet:weld-servlet-core)
BuildRequires:  mvn(org.mongodb:mongo-java-driver)
BuildRequires:  mvn(org.ow2.asm:asm)
BuildRequires:  mvn(org.ow2.asm:asm-commons)
BuildRequires:  mvn(org.slf4j:slf4j-api)

BuildRequires:  mvn(org.mortbay.jetty.alpn:alpn-boot)
BuildRequires:  mvn(org.eclipse.jetty.toolchain:jetty-artifact-remote-resources)
BuildRequires:  mvn(org.eclipse.jetty.toolchain:jetty-distribution-remote-resources)
BuildRequires:  mvn(org.eclipse.jetty.toolchain:jetty-test-policy)
#BuildRequires:  mvn(org.eclipse.jetty.toolchain.setuid:jetty-setuid-java)
BuildRequires:  maven-javadoc-plugin
BuildRequires:  glassfish-el
BuildRequires:  systemd
BuildRequires:  junit5

# duplicate providers, choose one
BuildRequires:  jboss-websocket-1.0-api
Requires:       jboss-websocket-1.0-api
%endif

BuildArch:      noarch
ExclusiveArch:  %{java_arches} noarch

# jp_minimal doesn't have main package
%if %{without jp_minimal}
# Explicit requires for javapackages-tools since jetty.sh script
# uses /usr/share/java-utils/java-functions
Requires:       javapackages-tools
Requires:       %{name}-annotations = %{version}-%{release}
Requires:       %{name}-ant = %{version}-%{release}
Requires:       %{name}-client = %{version}-%{release}
Requires:       %{name}-continuation = %{version}-%{release}
Requires:       %{name}-deploy = %{version}-%{release}
Requires:       %{name}-fcgi-client = %{version}-%{release}
Requires:       %{name}-fcgi-server = %{version}-%{release}
Requires:       %{name}-http = %{version}-%{release}
Requires:       %{name}-http-spi = %{version}-%{release}
Requires:       %{name}-io = %{version}-%{release}
Requires:       %{name}-jaas = %{version}-%{release}
Requires:       %{name}-jaspi = %{version}-%{release}
Requires:       %{name}-jmx = %{version}-%{release}
Requires:       %{name}-jndi = %{version}-%{release}
Requires:       %{name}-jsp = %{version}-%{release}
Requires:       %{name}-jspc-maven-plugin = %{version}-%{release}
Requires:       %{name}-maven-plugin = %{version}-%{release}
Requires:       %{name}-plus = %{version}-%{release}
Requires:       %{name}-proxy = %{version}-%{release}
Requires:       %{name}-rewrite = %{version}-%{release}
Requires:       %{name}-security = %{version}-%{release}
Requires:       %{name}-server = %{version}-%{release}
Requires:       %{name}-servlet = %{version}-%{release}
Requires:       %{name}-servlets = %{version}-%{release}
Requires:       %{name}-start = %{version}-%{release}
Requires:       %{name}-unixsocket = %{version}-%{release}
Requires:       %{name}-util = %{version}-%{release}
Requires:       %{name}-util-ajax = %{version}-%{release}
Requires:       %{name}-webapp = %{version}-%{release}
Requires:       %{name}-xml = %{version}-%{release}
Requires:       %{name}-cdi = %{version}-%{release}
Requires:       %{name}-websocket-api = %{version}-%{release}
Requires:       %{name}-websocket-client = %{version}-%{release}
Requires:       %{name}-websocket-common = %{version}-%{release}
Requires:       %{name}-websocket-server = %{version}-%{release}
Requires:       %{name}-websocket-servlet = %{version}-%{release}
Requires:       %{name}-javax-websocket-client-impl = %{version}-%{release}
Requires:       %{name}-javax-websocket-server-impl = %{version}-%{release}
Requires:       %{name}-nosql = %{version}-%{release}
Requires:       %{name}-quickstart = %{version}-%{release}
Requires:       %{name}-jstl = %{version}-%{release}
Requires:       %{name}-alpn-client = %{version}-%{release}
Requires:       %{name}-alpn-server = %{version}-%{release}
Requires:       %{name}-http2-client = %{version}-%{release}
Requires:       %{name}-http2-common = %{version}-%{release}
Requires:       %{name}-http2-hpack = %{version}-%{release}
Requires:       %{name}-http2-http-client-transport = %{version}-%{release}
Requires:       %{name}-http2-server = %{version}-%{release}

%{?systemd_ordering}


Provides:       group(%username) = %jtuid
Provides:       user(%username)  = %jtuid
%endif

# Hazelcast in Fedora is too old for jetty to build against (Added in F29)
Obsoletes:      %{name}-hazelcast < 9.4.18-1
# Infinispan in Fedora is too old for jetty to build against (Added in F31)
Obsoletes:      %{name}-infinispan < 9.4.18-1
# Eclipse no longer available (Added in F31)
Obsoletes:      %{name}-osgi-alpn < 9.4.18-1
Obsoletes:      %{name}-osgi-boot < 9.4.18-1
Obsoletes:      %{name}-osgi-boot-jsp < 9.4.18-1
Obsoletes:      %{name}-osgi-boot-warurl < 9.4.18-1
# Spring framework removed from Fedora (Added in F32)
Obsoletes:      %{name}-spring < 9.4.24-1

%if %{with jp_minimal}
# Remove left-over packages that would have broken deps when built in minimal mode
Obsoletes:      %{name}-project < 9.4.20-1
Obsoletes:      %{name}-annotations < 9.4.20-1
Obsoletes:      %{name}-ant < 9.4.20-1
Obsoletes:      %{name}-cdi < 9.4.20-1
Obsoletes:      %{name}-deploy < 9.4.20-1
Obsoletes:      %{name}-fcgi-client < 9.4.20-1
Obsoletes:      %{name}-fcgi-server < 9.4.20-1
Obsoletes:      %{name}-http-spi < 9.4.20-1
Obsoletes:      %{name}-jaspi < 9.4.20-1
Obsoletes:      %{name}-jndi < 9.4.20-1
Obsoletes:      %{name}-jsp < 9.4.20-1
Obsoletes:      %{name}-jstl < 9.4.20-1
Obsoletes:      %{name}-jspc-maven-plugin < 9.4.20-1
Obsoletes:      %{name}-maven-plugin < 9.4.20-1
Obsoletes:      %{name}-plus < 9.4.20-1
Obsoletes:      %{name}-proxy < 9.4.20-1
Obsoletes:      %{name}-quickstart < 9.4.20-1
Obsoletes:      %{name}-rewrite < 9.4.20-1
Obsoletes:      %{name}-servlets < 9.4.20-1
Obsoletes:      %{name}-start < 9.4.20-1
Obsoletes:      %{name}-unixsocket < 9.4.20-1
Obsoletes:      %{name}-websocket-api < 9.4.20-1
Obsoletes:      %{name}-websocket-client < 9.4.20-1
Obsoletes:      %{name}-websocket-common < 9.4.20-1
Obsoletes:      %{name}-websocket-server < 9.4.20-1
Obsoletes:      %{name}-websocket-servlet < 9.4.20-1
Obsoletes:      %{name}-javax-websocket-client-impl < 9.4.20-1
Obsoletes:      %{name}-javax-websocket-server-impl < 9.4.20-1
Obsoletes:      %{name}-alpn-client < 9.4.20-1
Obsoletes:      %{name}-alpn-server < 9.4.20-1
Obsoletes:      %{name}-http2-client < 9.4.20-1
Obsoletes:      %{name}-http2-common < 9.4.20-1
Obsoletes:      %{name}-http2-hpack < 9.4.20-1
Obsoletes:      %{name}-http2-http-client-transport < 9.4.20-1
Obsoletes:      %{name}-http2-server < 9.4.20-1
Obsoletes:      %{name}-nosql < 9.4.20-1
%endif

%description
%global desc \
Jetty is a 100% Java HTTP Server and Servlet Container. This means that you\
do not need to configure and run a separate web server (like Apache) in order\
to use Java, servlets and JSPs to generate dynamic content. Jetty is a fully\
featured web server for static and dynamic content. Unlike separate\
server/container solutions, this means that your web server and web\
application run in the same process, without interconnection overheads\
and complications. Furthermore, as a pure java component, Jetty can be simply\
included in your application for demonstration, distribution or deployment.\
Jetty is available on all Java supported platforms.
%{desc}
%global extdesc %{desc}\
\
This package contains

# packages in jp_minimal set
%package        client
Summary:        client module for Jetty

%description    client
%{extdesc} %{summary}.

%package        continuation
Summary:        continuation module for Jetty

%description    continuation
%{extdesc} %{summary}.

%package        http
Summary:        http module for Jetty

%description    http
%{extdesc} %{summary}.

%package        http-spi
Summary:        http-spi module for Jetty

%description    http-spi
%{extdesc} %{summary}.

%package        io
Summary:        io module for Jetty

%description    io
%{extdesc} %{summary}.

%package        jaas
Summary:        jaas module for Jetty

%description    jaas
%{extdesc} %{summary}.

%package        jsp
Summary:        jsp module for Jetty
Requires:       glassfish-el

%description    jsp
%{extdesc} %{summary}.

%package        security
Summary:        security module for Jetty

%description    security
%{extdesc} %{summary}.

%package        server
Summary:        server module for Jetty

%description    server
%{extdesc} %{summary}.

%package        servlet
Summary:        servlet module for Jetty
# Eclipse no longer available (Added in F31)
Obsoletes:      %{name}-httpservice < 9.4.18-1

%description    servlet
%{extdesc} %{summary}.

%package        util
Summary:        util module for Jetty
# Utf8Appendable.java is additionally under MIT license
# Automatically converted from old format: (ASL 2.0 or EPL-1.0) and MIT - review is highly recommended.
License:        (Apache-2.0 OR EPL-1.0) AND LicenseRef-Callaway-MIT

%description    util
%{extdesc} %{summary}.

%package        util-ajax
Summary:        util-ajax module for Jetty

%description    util-ajax
%{extdesc} %{summary}.

%package        webapp
Summary:        webapp module for Jetty

%description    webapp
%{extdesc} %{summary}.

%package        jmx
Summary:        jmx module for Jetty

%description    jmx
%{extdesc} %{summary}.

%package        xml
Summary:        xml module for Jetty

%description    xml
%{extdesc} %{summary}.



%if %{without jp_minimal}
%package        project
Summary:        POM files for Jetty
Obsoletes:      %{name}-websocket-parent < 9.4.0-0.4
Provides:       %{name}-websocket-parent = %{version}-%{release}
Obsoletes:      %{name}-osgi-project < 9.4.0-0.4
Provides:       %{name}-osgi-project = %{version}-%{release}

%description    project
%{extdesc} %{summary}.

%package        deploy
Summary:        deploy module for Jetty

%description    deploy
%{extdesc} %{summary}.

%package        annotations
Summary:        annotations module for Jetty

%description    annotations
%{extdesc} %{summary}.

%package        ant
Summary:        ant module for Jetty

%description    ant
%{extdesc} %{summary}.

%package cdi
Summary:        Jetty CDI Configuration

%description cdi
%{extdesc} %{summary}.

%package        fcgi-client
Summary:        FastCGI client module for Jetty

%description    fcgi-client
%{extdesc} %{summary}.

%package        fcgi-server
Summary:        FastCGI client module for Jetty

%description    fcgi-server
%{extdesc} %{summary}.

%package        jaspi
Summary:        jaspi module for Jetty

%description    jaspi
%{extdesc} %{summary}.

%package        jndi
Summary:        jndi module for Jetty

%description    jndi
%{extdesc} %{summary}.

%package        jspc-maven-plugin
Summary:        jspc-maven-plugin module for Jetty

%description    jspc-maven-plugin
%{extdesc} %{summary}.

%package        maven-plugin
Summary:        maven-plugin module for Jetty

%description    maven-plugin
%{extdesc} %{summary}.

%package        plus
Summary:        plus module for Jetty

%description    plus
%{extdesc} %{summary}.

%package        proxy
Summary:        proxy module for Jetty

%description    proxy
%{extdesc} %{summary}.

%package        rewrite
Summary:        rewrite module for Jetty

%description    rewrite
%{extdesc} %{summary}.

%package        servlets
Summary:        servlets module for Jetty

%description    servlets
%{extdesc} %{summary}.

%package        start
Summary:        start module for Jetty

%description    start
%{extdesc} %{summary}.

%package        unixsocket
Summary:        unixsocket module for Jetty

%description    unixsocket
%{extdesc} %{summary}.

%package        websocket-api
Summary:        websocket-api module for Jetty

%description    websocket-api
%{extdesc} %{summary}.

%package        websocket-client
Summary:        websocket-client module for Jetty

%description    websocket-client
%{extdesc} %{summary}.

%package        websocket-common
Summary:        websocket-common module for Jetty

%description    websocket-common
%{extdesc} %{summary}.

%package        websocket-server
Summary:        websocket-server module for Jetty

%description    websocket-server
%{extdesc} %{summary}.

%package        websocket-servlet
Summary:        websocket-servlet module for Jetty

%description    websocket-servlet
%{extdesc} %{summary}.

%package        javax-websocket-client-impl
Summary:        javax-websocket-client-impl module for Jetty

%description    javax-websocket-client-impl
%{extdesc} %{summary}.

%package        javax-websocket-server-impl
Summary:        javax-websocket-server-impl module for Jetty

%description    javax-websocket-server-impl
%{extdesc} %{summary}.

%package        nosql
Summary:        nosql module for Jetty

%description    nosql
%{extdesc} %{summary}.

%package        quickstart
Summary:        quickstart module for Jetty

%description    quickstart
%{extdesc} %{summary}.

%package        alpn-client
Summary:        alpn-client module for Jetty

%description    alpn-client
%{extdesc} %{summary}.

%package        alpn-server
Summary:        alpn-server module for Jetty

%description    alpn-server
%{extdesc} %{summary}.

%package        http2-client
Summary:        http2-client module for Jetty

%description    http2-client
%{extdesc} %{summary}.

%package        http2-common
Summary:        http2-common module for Jetty

%description    http2-common
%{extdesc} %{summary}.

%package        http2-hpack
Summary:        http2-hpack module for Jetty

%description    http2-hpack
%{extdesc} %{summary}.

%package        http2-http-client-transport
Summary:        http2-http-client-transport module for Jetty

%description    http2-http-client-transport
%{extdesc} %{summary}.

%package        http2-server
Summary:        http2-server module for Jetty

%description    http2-server
%{extdesc} %{summary}.

%package        jstl
Summary:        jstl module for Jetty

%description    jstl
%{extdesc} %{summary}.

%endif

%package        javadoc
Summary:        Javadoc for %{name}
# some MIT-licensed code (from Utf8Appendable) is used to generate javadoc
# Automatically converted from old format: (ASL 2.0 or EPL-1.0) and MIT - review is highly recommended.
License:        (Apache-2.0 OR EPL-1.0) AND LicenseRef-Callaway-MIT

%description    javadoc
%{summary}.

%prep
# oreon verify url source checksums begin
%(f=%{_sourcedir}/jetty-9.4.40.v20210413.tar.gz; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "11b612ef3489f350c9d8eeeff3227e76752b089facad7507b831d822e091d9c0" || { echo "oreon: Source0 SHA256 mismatch for jetty-9.4.40.v20210413.tar.gz" >&2; exit 1; })
# oreon verify url source checksums end
%setup -q -n %{name}.project-%{name}-%{version}%{addver}

%patch -P1 -p1
%patch -P2 -p1

find . -name "*.?ar" -exec rm {} \;
find . -name "*.class" -exec rm {} \;

# Plugins irrelevant or harmful to building the package
%pom_remove_plugin -r :maven-checkstyle-plugin
%pom_remove_plugin -r :spotbugs-maven-plugin
%pom_remove_plugin -r :maven-enforcer-plugin
%pom_remove_plugin -r :maven-eclipse-plugin
%pom_remove_plugin -r :license-maven-plugin
%pom_remove_plugin -r :maven-site-plugin
%pom_remove_plugin -r :maven-source-plugin
%pom_remove_plugin -r :maven-deploy-plugin
%pom_remove_plugin -r :jacoco-maven-plugin
%pom_remove_plugin -r :maven-release-plugin
%pom_remove_plugin -r :buildnumber-maven-plugin
%pom_remove_plugin -r :h2spec-maven-plugin

# Unnecessary pom flattening can be skipped
%pom_remove_plugin -r :flatten-maven-plugin jetty-bom

%pom_disable_module aggregates/jetty-all

# Reflective use of classes that might not be present in the JDK should be optional OSGi-wise
%pom_xpath_inject "pom:configuration/pom:instructions" \
"<Import-Package>sun.misc;resolution:=optional,com.sun.nio.file;resolution:=optional,*</Import-Package>"

%pom_remove_dep "com.sun.net.httpserver:http" jetty-http-spi

%pom_change_dep -r org.mortbay.jasper:apache-jsp org.apache.tomcat:tomcat-jasper

%pom_add_dep 'org.junit.jupiter:junit-jupiter-engine:${junit.version}' tests/test-sessions/test-sessions-common

# provided by glassfish-jsp-api that has newer version
%pom_change_dep -r javax.servlet.jsp:jsp-api javax.servlet.jsp:javax.servlet.jsp-api

# txt artifact - not installable
%pom_remove_plugin ":jetty-version-maven-plugin"
%pom_xpath_remove "pom:artifactItem[pom:classifier='version']" jetty-home

# Disable building source release
%pom_xpath_remove 'pom:execution[pom:id="sources"]' jetty-home

# Unwanted JS in javadoc
sed -i '/^\s*\*.*<script>/d' jetty-util/src/main/java/org/eclipse/jetty/util/resource/Resource.java

# only used for integration tests
%pom_remove_plugin :maven-invoker-plugin jetty-jspc-maven-plugin

# These bundles have a dep on Eclipse that is not available on every arch
%pom_disable_module jetty-osgi

# We don't have asciidoctor-maven-plugin
%pom_disable_module jetty-documentation
%pom_remove_dep -r :jetty-documentation
%pom_xpath_remove 'pom:execution[pom:id="unpack-documentation"]' jetty-distribution

%pom_xpath_remove 'pom:artifactItem[pom:artifactId="libsetuid-osx"]' jetty-home/pom.xml

# TODO remove when jetty-setuid is packaged
%pom_xpath_remove "pom:execution[pom:id[text()='copy-setuid-deps']]" jetty-home/pom.xml

# We don't have gcloud-java-datastore in Fedora
%pom_disable_module jetty-gcloud
%pom_disable_module test-gcloud-sessions tests/test-sessions
%pom_remove_dep :jetty-gcloud-session-manager jetty-home

# we don't have com.googlecode.xmemcached:xmemcached yet
%pom_disable_module jetty-memcached
%pom_disable_module test-memcached-sessions tests/test-sessions
%pom_remove_dep :jetty-memcached-sessions jetty-home

# Hazelcast in Fedora is too old to build against
%pom_disable_module jetty-hazelcast
%pom_disable_module test-hazelcast-sessions tests/test-sessions
%pom_remove_dep :jetty-hazelcast jetty-home

# Infinispan in Fedora is too old to build against
%pom_disable_module jetty-infinispan
%pom_disable_module test-infinispan-sessions tests/test-sessions
%pom_remove_dep :infinispan-embedded jetty-home
%pom_remove_dep :infinispan-embedded-query jetty-home
%pom_remove_dep :infinispan-remote jetty-home
%pom_remove_dep :infinispan-remote-query jetty-home
%pom_xpath_remove "pom:execution[pom:id='unpack-infinispan-config']" jetty-home

# Springframework not available in Fedora
%pom_disable_module jetty-spring

# Not currently able to build tests, so can't build benchmarks
%pom_disable_module jetty-jmh

# Distribution tests require internet access, so disable
%pom_disable_module test-distribution tests

# missing conscrypt
%pom_disable_module jetty-alpn-conscrypt-server jetty-alpn
%pom_disable_module jetty-alpn-conscrypt-client jetty-alpn
%pom_remove_dep -r :jetty-alpn-conscrypt-server
%pom_remove_dep -r :jetty-alpn-conscrypt-client
rm -fr examples/embedded/src/main/java/org/eclipse/jetty/embedded/ManyConnectors.java

cp %{SOURCE6} .

# the default location is not allowed by SELinux
sed -i '/<SystemProperty name="jetty.state"/d' \
    jetty-home/src/main/resources/etc/jetty-started.xml

%if %{with jp_minimal}
# remote-resources only copies about.html
%pom_remove_plugin :maven-remote-resources-plugin
# packages module configs, we don't need those in minimal
%pom_remove_plugin :maven-assembly-plugin
# only useful when tests are enabled (copies test deps)
%pom_remove_plugin :maven-dependency-plugin jetty-client

%pom_disable_module jetty-ant
%pom_disable_module jetty-http2
%pom_disable_module jetty-fcgi
%pom_disable_module jetty-websocket
%pom_disable_module jetty-servlets
%pom_disable_module apache-jsp
%pom_disable_module apache-jstl
%pom_disable_module jetty-maven-plugin
%pom_disable_module jetty-jspc-maven-plugin
%pom_disable_module jetty-deploy
%pom_disable_module jetty-start
%pom_disable_module jetty-plus
%pom_disable_module jetty-annotations
%pom_disable_module jetty-jndi
%pom_disable_module jetty-cdi
%pom_disable_module jetty-proxy
%pom_disable_module jetty-jaspi
%pom_disable_module jetty-rewrite
%pom_disable_module jetty-nosql
%pom_disable_module jetty-unixsocket
%pom_disable_module tests
%pom_disable_module examples
%pom_disable_module jetty-quickstart
%pom_disable_module jetty-distribution
%pom_disable_module jetty-runner
%pom_disable_module jetty-http-spi
%pom_disable_module jetty-alpn
%pom_disable_module jetty-home
%pom_disable_module jetty-openid

%endif

# Create a sysusers.d config file
cat >jetty.sysusers.conf <<EOF
u jetty %jtuid 'Jetty web server' %homedir -
EOF

%build
%mvn_package :jetty-home __noinstall
%mvn_package :jetty-distribution __noinstall
%mvn_package :build-resources __noinstall

# Separate package for POMs
%if %{without jp_minimal}
%mvn_package ':*-project' project
%mvn_package ':*-parent' project
%mvn_package ':*-bom' project
%else
%mvn_package ':*-project' __noinstall
%mvn_package ':*-parent' __noinstall
%mvn_package ':*-bom' __noinstall
%endif

# artifact used by demo
%mvn_package :test-mock-resources

%mvn_package ':test-*' __noinstall
%mvn_package ':*-tests' __noinstall
%mvn_package ':*-it' __noinstall
%mvn_package ':example-*' __noinstall
%mvn_package org.eclipse.jetty.tests: __noinstall
%mvn_package ::war: __noinstall
%mvn_package :jetty-runner __noinstall

%mvn_package org.eclipse.jetty.cdi: jetty-cdi

%mvn_package ':jetty-alpn*-client' jetty-alpn-client
%mvn_package ':jetty-alpn*-server' jetty-alpn-server


%mvn_package :apache-jsp jetty-jsp
%mvn_alias :apache-jsp :jetty-jsp

# we don't have all necessary dependencies to run tests
# missing test dep: org.eclipse.jetty.toolchain:jetty-perf-helper
%mvn_build -f -s


%install
%mvn_install

# jp_minimal version doesn't contain main package
%if %{without jp_minimal}
# Install jetty home
cp -pr jetty-distribution/target/distribution %{buildroot}%{homedir}

# dirs
install -dm 755 %{buildroot}%{_bindir}
install -dm 755 %{buildroot}%{_sysconfdir}/logrotate.d
install -dm 755 %{buildroot}%{confdir}
install -dm 755 %{buildroot}%{homedir}/start.d
install -dm 755 %{buildroot}%{logdir}
install -dm 755 %{buildroot}%{rundir}
install -dm 755 %{buildroot}%{tempdir}
install -dm 755 %{buildroot}%{jettylibdir}
install -dm 755 %{buildroot}%{_unitdir}

# systemd unit file
cp %{SOURCE5} %{buildroot}%{_unitdir}/

install -pm 644 %{SOURCE3} %{buildroot}%{_sysconfdir}/logrotate.d/%{name}
echo '# Placeholder configuration file.  No default is provided.' > \
     %{buildroot}%{confdir}/jetty.conf

# add dependencies that are missing due to artifact coordinates changes
build-jar-repository %{buildroot}%{homedir}/lib/apache-jsp \
           tomcat/jasper tomcat/tomcat-juli \
           tomcat/tomcat-jsp-2.3-api tomcat/tomcat-api tomcat/tomcat-util \
           tomcat-taglibs-standard/taglibs-standard-compat \
           tomcat-taglibs-standard/taglibs-standard-impl \
           tomcat/tomcat-util-scan glassfish-el-api glassfish-el

# ecj doesn't have javapackages metadata in manifest, remove when fixed
ecj=`echo %{buildroot}%{homedir}/lib/apache-jsp/org.eclipse.jdt.ecj-*.jar`
rm $ecj

# substitute dependency jars (keep start.jar with shaded jetty util)
xmvn-subst -s -L -R %{buildroot} %{buildroot}%{homedir}/lib

# ecj doesn't have javapackages metadata in manifest, remove when fixed
ln -sf %{_javadir}/ecj.jar $ecj

# TODO uncomment when jetty-setuid is packaged
# test -e %{_jnidir}/jetty-setuid/libsetuid-linux.so
# ln -sf %{_jnidir}/jetty-setuid/libsetuid-linux.so %{buildroot}%{homedir}/lib/setuid/

( cat << EO_RC
JAVA_HOME=/usr/lib/jvm/java
JAVA_OPTIONS=
JETTY_HOME=%{homedir}
JETTY_CONSOLE=%{logdir}/jetty-console.log
JETTY_PORT=8080
JETTY_RUN=%{_localstatedir}/run/%{name}
JETTY_PID=\$JETTY_RUN/jetty.pid
EO_RC
) > %{buildroot}%{homedir}/.jettyrc

mkdir -p %{buildroot}%{_tmpfilesdir}
( cat << EOF
D %{rundir} 0755 %username %{username} -
EOF
) > %{buildroot}%{_tmpfilesdir}/%{name}.conf

rm -r %{buildroot}%{homedir}/logs
ln -s %{logdir} %{buildroot}%{homedir}/logs

mv %{buildroot}%{homedir}/etc/* %{buildroot}/%{confdir}/
rm -r %{buildroot}%{homedir}/etc
ln -s %{confdir} %{buildroot}%{homedir}/etc

mv %{buildroot}%{homedir}/webapps %{buildroot}%{appdir}
ln -s %{appdir} %{buildroot}%{homedir}/webapps

rm %{buildroot}%{homedir}/*.txt  %{buildroot}%{homedir}/*.html

# Here jetty is going to put its runtime data.
# See: https://bugzilla.redhat.com/show_bug.cgi?id=845993
ln -sf %{rundir} %{buildroot}%{homedir}/work

# replace the startup script with ours
cp -p %{SOURCE1} %{buildroot}%{homedir}/bin/jetty.sh

# NOTE: %if %{without jp_minimal} still in effect

install -m0644 -D jetty.sysusers.conf %{buildroot}%{_sysusersdir}/jetty.conf

%post
%systemd_post jetty.service

%preun
%systemd_preun jetty.service

%postun
%systemd_postun_with_restart jetty.service


%endif

%files client -f .mfiles-jetty-client
%files continuation -f .mfiles-jetty-continuation
%files jaas -f .mfiles-jetty-jaas
%files io -f .mfiles-jetty-io
%files server -f .mfiles-jetty-server
%files servlet -f .mfiles-jetty-servlet
%files util -f .mfiles-jetty-util
%license LICENSE NOTICE.txt LICENSE-MIT
%files util-ajax -f .mfiles-jetty-util-ajax
%files webapp -f .mfiles-jetty-webapp
%files jmx -f .mfiles-jetty-jmx
%files xml -f .mfiles-jetty-xml
%files http -f .mfiles-jetty-http
%files security -f .mfiles-jetty-security

%if %{with jp_minimal}
%files
# Empty metapackage in minimal mode
%endif

%if %{without jp_minimal}
%files -f .mfiles
%{_tmpfilesdir}/%{name}.conf
%config(noreplace) %attr(644, root, root) %{_sysconfdir}/logrotate.d/%{name}
%config(noreplace) %{confdir}
%dir %{jettylibdir}
%dir %{jettycachedir}
%{homedir}
%attr(744, jetty, jetty) %{homedir}/bin/jetty.sh
%attr(755, jetty, jetty) %{logdir}
%attr(755, jetty, jetty) %{tempdir}
%ghost %dir %attr(755, jetty, jetty) %{rundir}
%{appdir}
%{_unitdir}/%{name}.service
%{_sysusersdir}/jetty.conf

%files project -f .mfiles-project
%doc README.md VERSION.txt
%license LICENSE NOTICE.txt LICENSE-MIT

%files annotations -f .mfiles-jetty-annotations
%files ant -f .mfiles-jetty-ant
%files cdi -f .mfiles-jetty-cdi
%files deploy -f .mfiles-jetty-deploy
%files fcgi-client -f .mfiles-fcgi-client
%files fcgi-server -f .mfiles-fcgi-server
%files http-spi -f .mfiles-jetty-http-spi
%files jaspi -f .mfiles-jetty-jaspi
%files jndi -f .mfiles-jetty-jndi
%files jsp -f .mfiles-jetty-jsp
%files jstl -f .mfiles-apache-jstl
%files jspc-maven-plugin -f .mfiles-jetty-jspc-maven-plugin
%files maven-plugin -f .mfiles-jetty-maven-plugin
%files plus -f .mfiles-jetty-plus
%files proxy -f .mfiles-jetty-proxy
%files quickstart -f .mfiles-jetty-quickstart
%files rewrite -f .mfiles-jetty-rewrite
%files servlets -f .mfiles-jetty-servlets
%files start -f .mfiles-jetty-start
%files unixsocket -f .mfiles-jetty-unixsocket
%files websocket-api -f .mfiles-websocket-api
%files websocket-client -f .mfiles-websocket-client
%files websocket-common -f .mfiles-websocket-common
%files websocket-server -f .mfiles-websocket-server
%files websocket-servlet -f .mfiles-websocket-servlet
%files javax-websocket-client-impl -f .mfiles-javax-websocket-client-impl
%files javax-websocket-server-impl -f .mfiles-javax-websocket-server-impl
%files alpn-client -f .mfiles-jetty-alpn-client
%files alpn-server -f .mfiles-jetty-alpn-server
%files http2-client -f .mfiles-http2-client
%files http2-common -f .mfiles-http2-common
%files http2-hpack -f .mfiles-http2-hpack
%files http2-http-client-transport -f .mfiles-http2-http-client-transport
%files http2-server -f .mfiles-http2-server
%files nosql -f .mfiles-jetty-nosql
%endif

%files javadoc -f .mfiles-javadoc
%license LICENSE NOTICE.txt LICENSE-MIT

%changelog
* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 9.4.40-18
- Prepare for Oreon 11 (RP1)
