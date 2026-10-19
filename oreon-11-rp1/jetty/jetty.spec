%global source0_hash 11b612ef3489f350c9d8eeeff3227e76752b089facad7507b831d822e091d9c0
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
%bcond_without  jp_minimal
Name:           jetty
Version:        9.4.40
Release:        1%{?dist}
Summary:        Java Webserver and Servlet Container
License:        Apache-2.0 OR EPL-1.0
URL:            http://www.eclipse.org/jetty/
Source0:        https://github.com/eclipse/%{name}.project/archive/refs/tags/%{name}-%{version}%{addver}.tar.gz#/%{name}-%{version}.tar.gz
Source1:        jetty.sh
Source3:        jetty.logrotate
Source5:        %{name}.service
Source6:        LICENSE-MIT
Patch1:         0001-Distro-jetty.home.patch
Patch2:         0002-Port-to-servlet-api-4-5.patch
%if %{without jp_minimal}
Requires:       jboss-websocket-1.0-api
%endif
BuildArch:      noarch
ExclusiveArch:  %{java_arches} noarch
%if %{without jp_minimal}
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
Obsoletes:      %{name}-hazelcast < 9.4.18-1
Obsoletes:      %{name}-infinispan < 9.4.18-1
Obsoletes:      %{name}-osgi-alpn < 9.4.18-1
Obsoletes:      %{name}-osgi-boot < 9.4.18-1
Obsoletes:      %{name}-osgi-boot-jsp < 9.4.18-1
Obsoletes:      %{name}-osgi-boot-warurl < 9.4.18-1
Obsoletes:      %{name}-spring < 9.4.24-1
%if %{with jp_minimal}
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
# oreon:deps
BuildRequires:  maven-local-openjdk25
BuildRequires:  mvn(javax.servlet:javax.servlet-api)
BuildRequires:  mvn(org.apache.felix:maven-bundle-plugin)
BuildRequires:  mvn(org.apache.maven.plugins:maven-shade-plugin)
BuildRequires:  mvn(org.codehaus.mojo:build-helper-maven-plugin)
BuildRequires:  mvn(org.slf4j:slf4j-api)
# /oreon:deps
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
Obsoletes:      %{name}-httpservice < 9.4.18-1
%description    servlet
%{extdesc} %{summary}.

%package        util
Summary:        util module for Jetty
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
License:        (Apache-2.0 OR EPL-1.0) AND LicenseRef-Callaway-MIT
%description    javadoc
%{summary}.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
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
%if %{without jp_minimal}
%mvn_package ':*-project' project
%mvn_package ':*-parent' project
%mvn_package ':*-bom' project
%else
%mvn_package ':*-project' __noinstall
%mvn_package ':*-parent' __noinstall
%mvn_package ':*-bom' __noinstall
%endif
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
%mvn_build -f -s
%install
%mvn_install
%if %{without jp_minimal}
cp -pr jetty-distribution/target/distribution %{buildroot}%{homedir}
install -dm 755 %{buildroot}%{_bindir}
install -dm 755 %{buildroot}%{_sysconfdir}/logrotate.d
install -dm 755 %{buildroot}%{confdir}
install -dm 755 %{buildroot}%{homedir}/start.d
install -dm 755 %{buildroot}%{logdir}
install -dm 755 %{buildroot}%{rundir}
install -dm 755 %{buildroot}%{tempdir}
install -dm 755 %{buildroot}%{jettylibdir}
install -dm 755 %{buildroot}%{_unitdir}
cp %{SOURCE5} %{buildroot}%{_unitdir}/
install -pm 644 %{SOURCE3} %{buildroot}%{_sysconfdir}/logrotate.d/%{name}
echo '# Placeholder configuration file.  No default is provided.' > \
     %{buildroot}%{confdir}/jetty.conf
build-jar-repository %{buildroot}%{homedir}/lib/apache-jsp \
           tomcat/jasper tomcat/tomcat-juli \
           tomcat/tomcat-jsp-2.3-api tomcat/tomcat-api tomcat/tomcat-util \
           tomcat-taglibs-standard/taglibs-standard-compat \
           tomcat-taglibs-standard/taglibs-standard-impl \
           tomcat/tomcat-util-scan glassfish-el-api glassfish-el
ecj=`echo %{buildroot}%{homedir}/lib/apache-jsp/org.eclipse.jdt.ecj-*.jar`
rm $ecj
xmvn-subst -s -L -R %{buildroot} %{buildroot}%{homedir}/lib
ln -sf %{_javadir}/ecj.jar $ecj
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
ln -sf %{rundir} %{buildroot}%{homedir}/work
cp -p %{SOURCE1} %{buildroot}%{homedir}/bin/jetty.sh
install -m0644 -D jetty.sysusers.conf %{buildroot}%{_sysusersdir}/jetty.conf
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%post

%systemd_post jetty.service
%preun

%systemd_preun jetty.service
%postun

%systemd_postun_with_restart jetty.service
%endif
%files -f %{oreon_filedir}/main.list
%files -n jetty-client -f %{oreon_filedir}/jetty-client.list
%files -n jetty-continuation -f %{oreon_filedir}/jetty-continuation.list
%files -n jetty-http -f %{oreon_filedir}/jetty-http.list
%files -n jetty-http-spi -f %{oreon_filedir}/jetty-http-spi.list
%files -n jetty-io -f %{oreon_filedir}/jetty-io.list
%files -n jetty-jaas -f %{oreon_filedir}/jetty-jaas.list
%files -n jetty-jsp -f %{oreon_filedir}/jetty-jsp.list
%files -n jetty-security -f %{oreon_filedir}/jetty-security.list
%files -n jetty-server -f %{oreon_filedir}/jetty-server.list
%files -n jetty-servlet -f %{oreon_filedir}/jetty-servlet.list
%files -n jetty-util -f %{oreon_filedir}/jetty-util.list
%files -n jetty-util-ajax -f %{oreon_filedir}/jetty-util-ajax.list
%files -n jetty-webapp -f %{oreon_filedir}/jetty-webapp.list
%files -n jetty-jmx -f %{oreon_filedir}/jetty-jmx.list
%files -n jetty-xml -f %{oreon_filedir}/jetty-xml.list
%files -n jetty-javadoc -f %{oreon_filedir}/jetty-javadoc.list

%changelog

* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 9.4.40-18
- Prepare for Oreon 11 (RP1)
