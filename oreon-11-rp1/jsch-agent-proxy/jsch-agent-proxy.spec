%global source0_hash 98fc68c5299e78ccb5ddc6e5c29740d575fc7cf2dc3c86bfdb7d06b6a479380a
Name:           jsch-agent-proxy
Version:        0.0.8
Release:        1%{?dist}
Summary:        Proxy to ssh-agent and Pageant in Java
License:        LicenseRef-Callaway-BSD
URL:            http://www.jcraft.com/jsch-agent-proxy/
BuildArch:      noarch
ExclusiveArch:  %{java_arches} noarch
Source0:        https://github.com/ymnk/jsch-agent-proxy/archive/%{version}.tar.gz#/%{name}-%{version}.tar.gz
Obsoletes: %{name}-sshj <= 0.0.8-11
# oreon:deps
BuildRequires:  maven-local-openjdk25
BuildRequires:  mvn(com.jcraft:jsch)
BuildRequires:  mvn(com.trilead:trilead-ssh2)
BuildRequires:  mvn(net.java.dev.jna:jna)
BuildRequires:  mvn(net.java.dev.jna:platform)
BuildRequires:  mvn(org.apache.felix:maven-bundle-plugin)
# /oreon:deps
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
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%files -f %{oreon_filedir}/main.list
%files -n jsch-agent-proxy-connector-factory -f %{oreon_filedir}/jsch-agent-proxy-connector-factory.list
%files -n jsch-agent-proxy-core -f %{oreon_filedir}/jsch-agent-proxy-core.list
%files -n jsch-agent-proxy-jsch -f %{oreon_filedir}/jsch-agent-proxy-jsch.list
%files -n jsch-agent-proxy-pageant -f %{oreon_filedir}/jsch-agent-proxy-pageant.list
%files -n jsch-agent-proxy-sshagent -f %{oreon_filedir}/jsch-agent-proxy-sshagent.list
%files -n jsch-agent-proxy-trilead-ssh2 -f %{oreon_filedir}/jsch-agent-proxy-trilead-ssh2.list
%files -n jsch-agent-proxy-usocket-jna -f %{oreon_filedir}/jsch-agent-proxy-usocket-jna.list
%files -n jsch-agent-proxy-usocket-nc -f %{oreon_filedir}/jsch-agent-proxy-usocket-nc.list
%files -n jsch-agent-proxy-javadoc -f %{oreon_filedir}/jsch-agent-proxy-javadoc.list

%changelog

%autochangelog
