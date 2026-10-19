%global source0_hash f3ce29efde338707241d47ab4784b19a1e3658bfa0564b5bc5f80c27e5118728
%global forgeurl https://github.com/TooTallNate/Java-WebSocket
Name:       Java-WebSocket
Version:    1.6.0
Release:        1%{?dist}
Summary:        A barebones WebSocket client and server implementation written in 100% Java
%forgemeta
License:    MIT AND LicenseRef-Fedora-Public-Domain
URL:        %{forgeurl}
Source0:        %{forgeurl}/archive/v%{version}/%{name}-%{version}.tar.gz
BuildArch:      noarch
ExclusiveArch:  %{java_arches} noarch
Requires:   java-headless
Requires:   javapackages-filesystem
Provides:   bundled(net.iharder:base64) = 2.3.7
# oreon:deps
BuildRequires:  maven-local-openjdk25
BuildRequires:  mvn(biz.aQute.bnd:bnd-maven-plugin)
BuildRequires:  mvn(org.apache.maven.plugins:maven-source-plugin)
# /oreon:deps
%description
A barebones WebSocket server and client implementation written in 100% Java.
The underlying classes are implemented java.nio, which allows for a non-blocking
event-driven model (similar to the WebSocket API for web browsers).

%package javadoc
Summary: Javadoc for %{name}
%description javadoc
This package contains the API documentation for %{name}.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%forgesetup

sed -i -e s#\<release\>7\</release\>#\<release\>21\</release\># pom.xml

%pom_remove_plugin :maven-checkstyle-plugin

%build

%mvn_build -f
%install
%mvn_install
%oreon_autofiles Java-WebSocket-javadoc usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%files -f %{oreon_filedir}/main.list
%files -n Java-WebSocket-javadoc -f %{oreon_filedir}/Java-WebSocket-javadoc.list

%changelog

%autochangelog
