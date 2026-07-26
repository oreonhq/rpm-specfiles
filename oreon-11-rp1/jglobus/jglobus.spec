%global source0_hash 004b19a420718d12e77f5a6aa964a2e5d23a635d30dd372d041958412d27d609

Name:		jglobus
Version:	2.1.0
Release:	42%{?dist}
Summary:	Globus Java client libraries

#		Everything is Apache 2.0 except for one file that is MIT:
#		ssl-proxies/src/main/java/org/globus/tools/GridCertRequest.java
License:	Apache-2.0 AND MIT
URL:		http://github.com/%{name}/JGlobus
Source0:	%{url}/archive/JGlobus-Release-%{version}.tar.gz
#		DERObjectIdentifier is obsolete
#		https://github.com/jglobus/JGlobus/pull/149
Patch0:		%{name}-DERObjectIdentifier-is-obsolete.patch
#		Don't force SSLv3 in myproxy, allow TLS
#		Backport from git (trunk)
Patch1:		%{name}-dont-force-SSLv3.patch
#		Relax proxy validation to be RFC-3820 compliant
#		https://github.com/jglobus/JGlobus/issues/160
#		https://github.com/jglobus/JGlobus/pull/165
Patch2:		%{name}-key-usage.patch
#		Fix javadoc
#		https://github.com/jglobus/JGlobus/pull/162
Patch3:		%{name}-javadoc.patch
#		Do not accumulate matches in
#		GlobusPathMatchingResourcePatternResolver
#		https://github.com/jglobus/JGlobus/pull/157
Patch4:		%{name}-do-not-accumulate-matches-in-GlobusPathMatchingResou.patch
#		Compatibility with clients that request minimum TLS version 1.2
#		https://github.com/jglobus/JGlobus/pull/166
Patch5:		%{name}-do-not-force-SSLv3-TLSv1-allow-TLSv1.1-TLSv1.2.patch
#		Remove synchronization on CRL in CRLChecker
#		Drop workaround for race condition in BouncyCastle < 1.46
#		Reduced lock contention leads to higher request throughput
#		Backport from git (trunk and 2.1 branch)
Patch6:		%{name}-remove-synchronization-on-CRL-in-CRLChecker.patch
#		Fix "no key" error for PKCS#8 encoded keys
#		https://github.com/jglobus/JGlobus/issues/118
#		https://github.com/jglobus/JGlobus/issues/146
#		https://github.com/jglobus/JGlobus/pull/164
Patch7:		%{name}-support-PKCS8-key-format.patch
#		Only allow TLSv1 and TLSv1.2 (not TLSv1.1)
#		https://github.com/jglobus/JGlobus/pull/166
Patch8:		%{name}-only-allow-TLSv1-and-TLSv1.2-not-TLSv1.1.patch
#		Remove unused FORCE_SSLV3_AND_CONSTRAIN_CIPHERSUITES_FOR_GRAM
#		https://github.com/jglobus/JGlobus/pull/166
Patch9:		%{name}-remove-unused-FORCE_SSLV3_AND_CONSTRAIN_CIPHERSUITES.patch
#		Adapt to changes in bouncycastle 1.61
#		https://github.com/jglobus/JGlobus/pull/168
Patch10:	%{name}-adapt-to-changes-in-PrivateKeyInfo-class.patch
#		DERInteger is obsolete
#		https://github.com/jglobus/JGlobus/pull/177
Patch11:	%{name}-DERInteger-is-obsolete.patch
#		DEROutputStream is private
#		https://github.com/jglobus/JGlobus/pull/177
Patch12:	%{name}-DEROutputStream-is-private.patch
#		ASN1OutputStream constructor is private - use create() method
#		https://github.com/jglobus/JGlobus/pull/183
Patch13:	%{name}-constructor-not-public.patch
#		DERBoolean is obsolete
#		https://github.com/jglobus/JGlobus/pull/185
Patch14:	%{name}-DERBoolean-is-obsolete.patch
#		DERTaggedObject.getObject() was removed - use .getInstance() instead
#		https://github.com/jglobus/JGlobus/pull/186
Patch15:	%{name}-DERTaggedObject.getObject-was-removed-use-.getInstan.patch
#		Reformat file to make linian happy
#		https://github.com/jglobus/JGlobus/pull/187
Patch16:	%{name}-Reformat-package.html-file.patch

BuildArch:	noarch
ExclusiveArch:	%{java_arches} noarch

BuildRequires:	maven-local-openjdk25
BuildRequires:	mvn(commons-codec:commons-codec)
BuildRequires:	mvn(commons-io:commons-io)
BuildRequires:	mvn(commons-logging:commons-logging)
BuildRequires:	mvn(junit:junit)
BuildRequires:	mvn(log4j:log4j)
BuildRequires:	mvn(org.apache.httpcomponents:httpclient)
BuildRequires:	mvn(org.apache.maven.plugins:maven-compiler-plugin)
BuildRequires:	mvn(org.apache.maven.plugins:maven-surefire-plugin)
BuildRequires:	mvn(org.bouncycastle:bcprov-jdk18on)

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
# Many tests requires network connections and a valid proxy certificate
%mvn_build -f -s -- -Dproject.build.sourceEncoding=UTF-8 -Dmaven.compiler.source=1.8 -Dmaven.compiler.target=1.8

%install
%mvn_install

%files parent -f .mfiles-parent 
%license LICENSE

%files ssl-proxies -f .mfiles-ssl-proxies
%doc README.textile
%license LICENSE

%files jsse -f .mfiles-jsse

%files gss -f .mfiles-gss

%files gram -f .mfiles-gram

%files gridftp -f .mfiles-gridftp

%files io -f .mfiles-io

%files myproxy -f .mfiles-myproxy

%files javadoc -f .mfiles-javadoc

%changelog
%autochangelog
