%global source0_hash 40ab650e7ab9a7c63b570e6bf0529c95835ec09d213f834dc17ea292d431498e

Name:           jsch-agent-proxy
Version:        0.0.8
Release:        31%{?dist}
Summary:        Proxy to ssh-agent and Pageant in Java
# Automatically converted from old format: BSD - review is highly recommended.
License:        LicenseRef-Callaway-BSD
URL:            http://www.jcraft.com/jsch-agent-proxy/
BuildArch:      noarch
ExclusiveArch:  %{java_arches} noarch

Source0:        https://github.com/ymnk/jsch-agent-proxy/archive/%{version}.tar.gz#/%{name}-%{version}.tar.gz

BuildRequires:  maven-local-openjdk25
BuildRequires:  mvn(com.jcraft:jsch)
BuildRequires:  mvn(com.trilead:trilead-ssh2)
BuildRequires:  mvn(net.java.dev.jna:jna)
BuildRequires:  mvn(net.java.dev.jna:platform)
BuildRequires:  mvn(org.apache.felix:maven-bundle-plugin)

# SSHj is not longer available in Fedora
Obsoletes: %{name}-sshj <= 0.0.8-11

%description
jsch-agent-proxy is a proxy program to OpenSSH ssh-agent and Pageant
included Putty.  It will be easily integrated into JSch, and users
will be allowed to use those programs in authentications.  This
software has been developed for JSch, but it will be easily applicable
to other ssh2 implementations in Java.  This software is licensed
under BSD style license.

%package connector-factory
Summary:        Connector factory for jsch-agent-proxy

%description connector-factory
%{summary}.

%package core
Summary:        jsch-agent-proxy core module

%description core
%{summary}.

%package jsch
Summary:        JSch connector for jsch-agent-proxy

%description jsch
%{summary}.

%package pageant
Summary:        Pageant connector for jsch-agent-proxy

%description pageant
%{summary}.

%package sshagent
Summary:        ssh-agent connector for jsch-agent-proxy

%description sshagent
%{summary}.

%package trilead-ssh2
Summary:        trilead-ssh2 connector for jsch-agent-proxy

%description trilead-ssh2
%{summary}.

%package usocket-jna
Summary:        USocketFactory implementation using JNA

%description usocket-jna
%{summary}.

%package usocket-nc
Summary:        USocketFactory implementation using Netcat

%description usocket-nc
%{summary}.

%package        javadoc
Summary:        API documentation for %{name}

%description    javadoc
This package provides %{summary}.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q

# remove unnecessary dependency on parent POM
%pom_remove_parent

# Put parent POM together with core module
%mvn_package :jsch.agentproxy jsch.agentproxy.core

# Unnecessary for RPM builds
%pom_remove_plugin ":maven-javadoc-plugin"
%pom_remove_plugin ":maven-source-plugin"
%pom_xpath_remove pom:build/pom:extensions

# Remove hard-coded compiler configuration
%pom_remove_plugin ":maven-compiler-plugin"

# SSHj not available in Fedora
%pom_disable_module jsch-agent-proxy-sshj

%build
%mvn_build -s -- -Dmaven.compiler.release=8 -Dsource=1.8 -DdetectJavaApiLink=false

%install
%mvn_install

%files core -f .mfiles-jsch.agentproxy.core
%doc README README.md
%license LICENSE.txt

%files connector-factory -f .mfiles-jsch.agentproxy.connector-factory
%files jsch -f .mfiles-jsch.agentproxy.jsch
%files pageant -f .mfiles-jsch.agentproxy.pageant
%files sshagent -f .mfiles-jsch.agentproxy.sshagent
%files trilead-ssh2 -f .mfiles-jsch.agentproxy.svnkit-trilead-ssh2
%files usocket-jna -f .mfiles-jsch.agentproxy.usocket-jna
%files usocket-nc -f .mfiles-jsch.agentproxy.usocket-nc

%files javadoc -f .mfiles-javadoc
%license LICENSE.txt

%changelog
%autochangelog
