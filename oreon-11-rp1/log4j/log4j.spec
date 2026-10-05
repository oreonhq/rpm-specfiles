%global source0_hash 9a27844f4bea314fa3add288c1705360d59d9b7f1ca129062f07d0477d3effc5

%{lua:
if macros.orbs_chain_plan == nil and macros._without_bootstrap == nil then
  local spec
  local cmd = io.open("/proc/self/cmdline", "rb")
  if cmd then
    local data = cmd:read("*a") or ""
    cmd:close()
    local cur = ""
    local function take(arg)
      if string.sub(arg, -5) == ".spec" then spec = arg end
    end
    for i = 1, #data do
      local c = string.sub(data, i, i)
      if string.byte(c) == 0 then
        take(cur)
        cur = ""
      else
        cur = cur .. c
      end
    end
    take(cur)
  end
  local function trim(s)
    local a, b = 1, #s
    while a <= b do
      local c = string.sub(s, a, a)
      if c ~= " " and string.byte(c) ~= 9 then break end
      a = a + 1
    end
    while b >= a do
      local c = string.sub(s, b, b)
      if c ~= " " and string.byte(c) ~= 9 then break end
      b = b - 1
    end
    return string.sub(s, a, b)
  end
  local function miss(dep)
    local p = io.popen("dnf -q install --assumeno '" .. dep .. "' 2>&1")
    if not p then return true end
    local out = p:read("*a") or ""
    p:close()
    if string.find(out, "nothing provides", 1, true) then return true end
    if string.find(out, "No match", 1, true) then return true end
    if string.find(out, "Failed to resolve", 1, true) then return true end
    if string.find(out, "Nothing to do", 1, true) then return false end
    if string.find(out, "Operation aborted", 1, true) then return false end
    if string.find(out, "already installed", 1, true) then return false end
    return true
  end
  if spec then
    local f = io.open(spec, "r")
    if f then
      local depth, in_else, armed = 0, false, false
      for line in f:lines() do
        local s = trim(line)
        if not armed then
          if string.sub(s, 1, 3) == "%%if" and string.find(s, "{with bootstrap}", 1, true) then
            armed = true
            depth = 1
          end
        elseif string.sub(s, 1, 3) == "%%if" then
          depth = depth + 1
        elseif string.sub(s, 1, 6) == "%%endif" then
          depth = depth - 1
          if depth == 0 then break end
        elseif depth == 1 and string.sub(s, 1, 5) == "%%else" then
          in_else = true
        elseif in_else and depth == 1 and string.lower(string.sub(s, 1, 14)) == "buildrequires:" then
          local dep = trim(string.sub(s, 15))
          if dep ~= "" and string.sub(dep, 1, 1) ~= "%%" and miss(dep) then
            rpm.define("_with_bootstrap 1")
            break
          end
        end
      end
      f:close()
    end
  end
end
}
%bcond_with bootstrap
%bcond_without jp_minimal

Name:           log4j
Version:        2.20.0
Release:        %autorelease
Summary:        Java logging package
BuildArch:      noarch
ExclusiveArch:  %{java_arches} noarch
License:        Apache-2.0

URL:            https://logging.apache.org/%{name}

# ./generate-tarball.sh
Source0:        https://archive.apache.org/dist/logging/%{name}/%{version}/apache-%{name}-%{version}-src.tar.gz

Patch:          logging-log4j-Remove-unsupported-EventDataConverter.patch
Patch:          0002-Remove-usage-of-toolchains.patch

%if %{with bootstrap}
BuildRequires:  javapackages-bootstrap
%else
BuildRequires:  maven-local-openjdk25
BuildRequires:  mvn(com.lmax:disruptor)
BuildRequires:  mvn(commons-logging:commons-logging)
BuildRequires:  mvn(jakarta.activation:jakarta.activation-api)
BuildRequires:  mvn(jakarta.mail:jakarta.mail-api)
BuildRequires:  mvn(javax.servlet:javax.servlet-api)
BuildRequires:  mvn(org.apache.commons:commons-compress)
BuildRequires:  mvn(org.apache.felix:maven-bundle-plugin)
BuildRequires:  mvn(org.apache.maven.plugins:maven-assembly-plugin)
BuildRequires:  mvn(org.apache.maven.plugins:maven-dependency-plugin)
BuildRequires:  mvn(org.codehaus.mojo:build-helper-maven-plugin)
BuildRequires:  mvn(org.fusesource.jansi:jansi)
BuildRequires:  mvn(org.jctools:jctools-core)
BuildRequires:  mvn(org.osgi:osgi.core)
BuildRequires:  mvn(org.slf4j:slf4j-api)
%endif

%if %{without jp_minimal}
BuildRequires:  mvn(com.datastax.cassandra:cassandra-driver-core)
BuildRequires:  mvn(com.fasterxml.jackson.core:jackson-annotations)
BuildRequires:  mvn(com.fasterxml.jackson.core:jackson-core)
BuildRequires:  mvn(com.fasterxml.jackson.core:jackson-databind)
BuildRequires:  mvn(com.fasterxml.jackson.dataformat:jackson-dataformat-xml)
BuildRequires:  mvn(com.fasterxml.jackson.dataformat:jackson-dataformat-yaml)
BuildRequires:  mvn(com.fasterxml.woodstox:woodstox-core)
BuildRequires:  mvn(com.lmax:disruptor)
BuildRequires:  mvn(jakarta.mail:jakarta.mail-api)
BuildRequires:  mvn(jakarta.servlet:jakarta.servlet-api)
BuildRequires:  mvn(javax.servlet.jsp:jsp-api)
BuildRequires:  mvn(org.apache.commons:commons-csv)
BuildRequires:  mvn(org.apache.logging:logging-parent:pom:)
BuildRequires:  mvn(org.apache.tomcat:tomcat-catalina)
BuildRequires:  mvn(org.codehaus.mojo:build-helper-maven-plugin)
BuildRequires:  mvn(org.eclipse.jetty:jetty-util)
BuildRequires:  mvn(org.eclipse.persistence:javax.persistence)
BuildRequires:  mvn(org.fusesource.jansi:jansi:1)
BuildRequires:  mvn(org.jboss.spec.javax.jms:jboss-jms-api_1.1_spec)
BuildRequires:  mvn(org.jctools:jctools-core)
BuildRequires:  mvn(org.lightcouch:lightcouch)
BuildRequires:  mvn(org.osgi:osgi.core)
BuildRequires:  mvn(org.slf4j:slf4j-api)
BuildRequires:  mvn(org.slf4j:slf4j-ext)
BuildRequires:  mvn(org.zeromq:jeromq)
BuildRequires:  mvn(sun.jdk:jconsole)

# Also needs:
# - Various Spring dependencies
# - javax.jms
# - io.fabric8.kubernetes-client
%endif

# TODO Remove in Fedora 46
Obsoletes:      %{name}-javadoc < 2.2.0-18

%description
Log4j is a tool to help the programmer output log statements to a
variety of output targets.

%package slf4j
Summary:        Binding between LOG4J 2 API and SLF4J

%description slf4j
Binding between LOG4J 2 API and SLF4J.

%package jcl
Summary:        Apache Log4j Commons Logging Bridge

%description jcl
Apache Log4j Commons Logging Bridge.

%package web
Summary:        Apache Log4j Web

%description web
Support for Log4j in a web servlet container.

%package bom
Summary:        Apache Log4j BOM

%description bom
Apache Log4j 2 Bill of Material

%if %{without jp_minimal}
%package osgi
Summary:        Apache Log4J Core OSGi Bundles

%description osgi
Apache Log4J Core OSGi Bundles.

%package taglib
Summary:        Apache Log4j Tag Library

%description taglib
Apache Log4j Tag Library for Web Applications.

%package jmx-gui
Summary:        Apache Log4j JMX GUI
Requires:       java-25-devel

%description jmx-gui
Swing-based client for remotely editing the log4j configuration and remotely
monitoring StatusLogger output. Includes a JConsole plug-in.

%package nosql
Summary:        Apache Log4j NoSql

%description nosql
Use NoSQL databases such as MongoDB and CouchDB to append log messages.
%endif

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%autosetup -p1 -n apache-%{name}-%{version}-src

%pom_remove_plugin -r :apache-rat-plugin
%pom_remove_plugin -r :maven-site-plugin
%pom_remove_plugin -r :maven-source-plugin
%pom_remove_plugin -r :maven-toolchains-plugin
%pom_remove_plugin -r :maven-enforcer-plugin
%pom_remove_plugin -r com.diffplug.spotless:spotless-maven-plugin
%pom_remove_plugin -r org.apache.logging.log4j:log4j-changelog-maven-plugin
%pom_remove_plugin -r org.codehaus.mojo:xml-maven-plugin

# remove all the stuff we'll build ourselves
find -name '*.jar' -o -name '*.class' -delete
rm -rf docs/api

%pom_disable_module %{name}-distribution
%pom_disable_module %{name}-samples

# Apache Flume is not in Fedora yet
%pom_disable_module %{name}-flume-ng

# artifact for upstream testing of log4j itself, shouldn't be distributed
%pom_disable_module %{name}-perf

%pom_remove_dep -r org.codehaus.groovy:groovy-bom
%pom_remove_dep -r com.fasterxml.jackson:jackson-bom
%pom_remove_dep -r jakarta.platform:jakarta.jakartaee-bom
%pom_remove_dep -r org.eclipse.jetty:jetty-bom
%pom_remove_dep -r org.junit:junit-bom
%pom_remove_dep -r io.fabric8:kubernetes-client-bom
%pom_remove_dep -r io.netty:netty-bom
%pom_remove_dep -r org.springframework:spring-framework-bom

# unavailable com.conversantmedia:disruptor
rm log4j-core/src/main/java/org/apache/logging/log4j/core/async/DisruptorBlockingQueueFactory.java
%pom_remove_dep -r com.conversantmedia:disruptor

# kafka not available
rm -r log4j-core/src/main/java/org/apache/logging/log4j/core/appender/mom/kafka
%pom_remove_dep -r :kafka-clients

%pom_remove_dep -r javax.jms:javax.jms-api

# we don't have commons-dbcp2
%pom_disable_module %{name}-jdbc-dbcp2

# We don't have mmongo-java
%pom_disable_module %{name}-mongodb3
%pom_disable_module %{name}-mongodb4

# System scoped dep provided by JDK
%pom_remove_dep :jconsole %{name}-jmx-gui
%pom_add_dep sun.jdk:jconsole %{name}-jmx-gui

# old AID is provided by felix, we want osgi-core
%pom_change_dep -r org.osgi:org.osgi.core org.osgi:osgi.core

# tests are disabled
%pom_remove_plugin :maven-failsafe-plugin

# Remove deps on slf4j-ext, it is no longer available in Fedora 35
%pom_remove_dep -r :slf4j-ext
%pom_remove_parent
%pom_remove_parent log4j-bom

# Make compiled code compatible with OpenJDK 8
%pom_xpath_inject 'pom:plugin[pom:artifactId="maven-compiler-plugin"]/pom:configuration' "<release>8</release>"

%pom_disable_module %{name}-api-test
%pom_disable_module %{name}-core-test
%pom_disable_module %{name}-layout-template-json-test
%pom_disable_module %{name}-slf4j2-impl

%if %{with jp_minimal}
%pom_disable_module %{name}-taglib
%pom_disable_module %{name}-jmx-gui
%pom_disable_module %{name}-jakarta-web
%pom_disable_module %{name}-iostreams
%pom_disable_module %{name}-jul
%pom_disable_module %{name}-core-its
%pom_disable_module %{name}-jpa
%pom_disable_module %{name}-couchdb
%pom_disable_module %{name}-cassandra
%pom_disable_module %{name}-appserver
%pom_disable_module %{name}-spring-cloud-config
%pom_disable_module %{name}-spring-boot
%pom_disable_module %{name}-docker
%pom_disable_module %{name}-kubernetes
%pom_disable_module %{name}-layout-template-json

%pom_remove_dep -r :jackson-core
%pom_remove_dep -r :jackson-databind
%pom_remove_dep -r :jackson-dataformat-yaml
%pom_remove_dep -r :jackson-dataformat-xml
%pom_remove_dep -r :woodstox-core
%pom_remove_dep -r :jeromq
%pom_remove_dep -r :commons-csv

rm -r log4j-core/src/main/java/org/apache/logging/log4j/core/{jackson,config/yaml,config/json,parser}
rm -r log4j-core/src/main/java/org/apache/logging/log4j/core/appender/{db,mom,nosql}
rm log4j-core/src/main/java/org/apache/logging/log4j/core/layout/*{Csv,Jackson,Xml,Yaml,Json,Gelf}*.java
rm log4j-1.2-api/src/main/java/org/apache/log4j/builders/layout/*Xml*.java
rm log4j-api/src/main/java/org/apache/logging/log4j/util/Activator.java
rm -r log4j-1.2-api/src/main/java/org/apache/log4j/or/jms
%endif

%mvn_alias :%{name}-1.2-api %{name}:%{name}

# Note that packages using the compatibility layer still need to have log4j-core
# on the classpath to run. This is there to prevent build-classpath from putting
# whole dir on the classpath which results in loading incorrect provider
%mvn_file ':{%{name}-1.2-api}' %{name}/@1 %{name}

%mvn_package ':%{name}-slf4j-impl' slf4j
%mvn_package ':%{name}-to-slf4j' slf4j
%mvn_package ':%{name}-taglib' taglib
%mvn_package ':%{name}-jcl' jcl
%mvn_package ':%{name}-jmx-gui' jmx-gui
%mvn_package ':%{name}-web' web
%mvn_package ':%{name}-bom' bom
%mvn_package ':%{name}-cassandra' nosql
%mvn_package ':%{name}-couchdb' nosql

%mvn_package :log4j-core-its __noinstall

%mvn_package ::zip: __noinstall

%pom_remove_dep com.sun.mail:javax.mail log4j-core
%pom_remove_dep javax.mail:javax.mail-api log4j-core
%pom_remove_dep javax.activation:javax.activation-api log4j-core
rm log4j-core/src/main/java/org/apache/logging/log4j/core/net/MimeMessageBuilder.java
rm log4j-core/src/main/java/org/apache/logging/log4j/core/net/SmtpManager.java
rm log4j-core/src/main/java/org/apache/logging/log4j/core/appender/SmtpAppender.java
rm log4j-core/src/main/java/org/apache/logging/log4j/core/filter/MutableThreadContextMapFilter.java

%pom_remove_dep org.eclipse.angus:angus-activation log4j-jakarta-smtp
%pom_remove_dep org.eclipse.angus:jakarta.mail log4j-jakarta-smtp

%pom_remove_plugin -r org.apache.maven.plugins:maven-failsafe-plugin
%pom_remove_plugin -r org.ops4j.pax.exam:exam-maven-plugin

%build
# missing test deps (mockejb)
%mvn_build -j -f

%install
%mvn_install

%if %{without jp_minimal}
%jpackage_script org.apache.logging.log4j.jmx.gui.ClientGUI '' '' %{name}/%{name}-jmx-gui:%{name}/%{name}-core %{name}-jmx false
%endif

%files -f .mfiles
%license LICENSE.txt NOTICE.txt

%files slf4j -f .mfiles-slf4j
%files jcl -f .mfiles-jcl
%files web -f .mfiles-web
%files bom -f .mfiles-bom
%if %{without jp_minimal}
%files taglib -f .mfiles-taglib
%files nosql -f .mfiles-nosql
%files jmx-gui -f .mfiles-jmx-gui
%{_bindir}/%{name}-jmx
%endif

%changelog
* Mon May 25 2026 Oreon Packaging Team <packaging@oreonhq.com> - 2.20.0-1
- Import
