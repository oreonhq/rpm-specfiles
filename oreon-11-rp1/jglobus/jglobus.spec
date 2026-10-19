%global source0_hash 004b19a420718d12e77f5a6aa964a2e5d23a635d30dd372d041958412d27d609
Name:		jglobus
Version:	2.1.0
Release:        1%{?dist}
Summary:        Globus Java client libraries
License:	Apache-2.0 AND MIT
URL:		http://github.com/%{name}/JGlobus
Source0:        http://github.com/%{name}/JGlobus/archive/JGlobus-Release-%{version}.tar.gz
Patch0:		%{name}-DERObjectIdentifier-is-obsolete.patch
Patch1:		%{name}-dont-force-SSLv3.patch
Patch2:		%{name}-key-usage.patch
Patch3:		%{name}-javadoc.patch
Patch4:		%{name}-do-not-accumulate-matches-in-GlobusPathMatchingResou.patch
Patch5:		%{name}-do-not-force-SSLv3-TLSv1-allow-TLSv1.1-TLSv1.2.patch
Patch6:		%{name}-remove-synchronization-on-CRL-in-CRLChecker.patch
Patch7:		%{name}-support-PKCS8-key-format.patch
Patch8:		%{name}-only-allow-TLSv1-and-TLSv1.2-not-TLSv1.1.patch
Patch9:		%{name}-remove-unused-FORCE_SSLV3_AND_CONSTRAIN_CIPHERSUITES.patch
Patch10:	%{name}-adapt-to-changes-in-PrivateKeyInfo-class.patch
Patch11:	%{name}-DERInteger-is-obsolete.patch
Patch12:	%{name}-DEROutputStream-is-private.patch
Patch13:	%{name}-constructor-not-public.patch
Patch14:	%{name}-DERBoolean-is-obsolete.patch
Patch15:	%{name}-DERTaggedObject.getObject-was-removed-use-.getInstan.patch
Patch16:	%{name}-Reformat-package.html-file.patch
BuildArch:	noarch
ExclusiveArch:	%{java_arches} noarch
# oreon:deps
BuildRequires:  maven-local-openjdk25
BuildRequires:  mvn(commons-codec:commons-codec)
BuildRequires:  mvn(commons-io:commons-io)
BuildRequires:  mvn(commons-logging:commons-logging)
BuildRequires:  mvn(junit:junit)
BuildRequires:  mvn(log4j:log4j)
BuildRequires:  mvn(org.apache.httpcomponents:httpclient)
BuildRequires:  mvn(org.apache.maven.plugins:maven-compiler-plugin)
BuildRequires:  mvn(org.apache.maven.plugins:maven-surefire-plugin)
BuildRequires:  mvn(org.bouncycastle:bcprov-jdk18on)
# /oreon:deps
%description
%{name} is a collection of Java client libraries for Globus Toolkit security,
GRAM, GridFTP and MyProxy.

%package parent
Summary:	Globus Java - parent pom file
License:	Apache-2.0
%description parent
Globus Java libraries parent maven pom file

%package ssl-proxies
Summary:	Globus Java - SSL and proxy certificate support
License:	Apache-2.0 AND MIT
Obsoletes:	%{name}-axisg < %{version}-%{release}
Obsoletes:	%{name}-ssl-proxies-tomcat < %{version}-%{release}
%description ssl-proxies
Globus Java library with SSL and proxy certificate support

%package jsse
Summary:	Globus Java - SSL support
License:	Apache-2.0
Requires:	%{name}-ssl-proxies = %{version}-%{release}
%description jsse
Globus Java library with SSL support

%package gss
Summary:	Globus Java - GSS-API implementation for SSL with proxies
License:	Apache-2.0
Requires:	%{name}-jsse = %{version}-%{release}
%description gss
Globus Java GSS-API implementation for SSL with proxies

%package gram
Summary:	Globus Java - Grid Resource Allocation and Management (GRAM)
License:	Apache-2.0
Requires:	%{name}-gss = %{version}-%{release}
%description gram
Globus Java library with GRAM support

%package gridftp
Summary:	Globus Java - GridFTP
License:	Apache-2.0
Requires:	%{name}-gss = %{version}-%{release}
%description gridftp
Globus Java library with GridFTP support

%package io
Summary:	Globus Java - IO
License:	Apache-2.0
Requires:	%{name}-gram = %{version}-%{release}
Requires:	%{name}-gridftp = %{version}-%{release}
%description io
Globus Java library with IO utilities

%package myproxy
Summary:	Globus Java - MyProxy
License:	Apache-2.0
Requires:	%{name}-gss = %{version}-%{release}
%description myproxy
Globus Java library with MyProxy support

%package javadoc
Summary:	Javadoc for %{name}
License:	Apache-2.0 AND MIT
%description javadoc
This package contains the API documentation for %{name}.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n JGlobus-JGlobus-Release-%{version}
%patch -P 0 -p1
%patch -P 1 -p1
%patch -P 2 -p1
%patch -P 3 -p1
%patch -P 4 -p1
%patch -P 5 -p1
%patch -P 6 -p1
%patch -P 7 -p1
%patch -P 8 -p1
%patch -P 9 -p1
%patch -P 10 -p1
%patch -P 11 -p1
%patch -P 12 -p1
%patch -P 13 -p1
%patch -P 14 -p1
%patch -P 15 -p1
%patch -P 16 -p1

# Do not package test classes
%mvn_package org.jglobus:container-test-utils __noinstall
%mvn_package org.jglobus:test-utils __noinstall

# Avoid build dependency bloat
%pom_remove_parent

# Don't do source and release
%pom_remove_plugin org.apache.maven.plugins:maven-release-plugin
%pom_remove_plugin org.apache.maven.plugins:maven-source-plugin

# Remove source ant target settings (Java 1.5)
%pom_remove_plugin org.apache.maven.plugins:maven-compiler-plugin

# The gaxis module requires axis version 1.x
%pom_disable_module axis

# The tomcat module is not compatible with tomcat 8.5 or later
%pom_disable_module ssl-proxies-tomcat

# Update bouncycastle version
%pom_change_dep -r org.bouncycastle:bcprov-jdk15on org.bouncycastle:bcprov-jdk18on

%build

%mvn_build -f -s -- -Dproject.build.sourceEncoding=UTF-8 -Dmaven.compiler.source=1.8 -Dmaven.compiler.target=1.8
%install
%mvn_install
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%files -f %{oreon_filedir}/main.list
%files -n jglobus-parent -f %{oreon_filedir}/jglobus-parent.list
%files -n jglobus-ssl-proxies -f %{oreon_filedir}/jglobus-ssl-proxies.list
%files -n jglobus-jsse -f %{oreon_filedir}/jglobus-jsse.list
%files -n jglobus-gss -f %{oreon_filedir}/jglobus-gss.list
%files -n jglobus-gram -f %{oreon_filedir}/jglobus-gram.list
%files -n jglobus-gridftp -f %{oreon_filedir}/jglobus-gridftp.list
%files -n jglobus-io -f %{oreon_filedir}/jglobus-io.list
%files -n jglobus-myproxy -f %{oreon_filedir}/jglobus-myproxy.list
%files -n jglobus-javadoc -f %{oreon_filedir}/jglobus-javadoc.list

%changelog

%autochangelog
