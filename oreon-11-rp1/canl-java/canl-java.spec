%global source0_hash 0627ae2e5a2d488c421b16abd277f06290478f5f75f08597663034737ec28545
Name:		canl-java
Version:	2.8.3
Release:        12%{?dist}
Summary:        EMI Common Authentication library - bindings for Java
License:	BSD-3-Clause AND Apache-2.0 AND MIT
URL:		https://github.com/eu-emi/%{name}/
Source0:        https://github.com/eu-emi/%{name}/archive/canl-%{version}/%{name}-%{version}.tar.gz
Patch0:		%{name}-test.patch
BuildArch:	noarch
ExclusiveArch:	%{java_arches} noarch
Requires:	mvn(org.bouncycastle:bcpkix-jdk18on) >= 1.69
# oreon:deps
BuildRequires:  maven-local-openjdk25
BuildRequires:  mvn(commons-io:commons-io)
BuildRequires:  mvn(junit:junit)
BuildRequires:  mvn(org.assertj:assertj-core)
BuildRequires:  mvn(org.bouncycastle:bcpkix-jdk18on)
# /oreon:deps
%description
This is the Java part of the EMI caNl -- the Common Authentication Library.

%package javadoc
Summary:	Javadoc documentation for %{name}
%description javadoc
Javadoc documentation for EMI caNl.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n %{name}-canl-%{version}
%patch -P 0 -p1

# Remove maven-wagon-webdav-jackrabbit dependency
%pom_xpath_remove pom:build/pom:extensions

# GPG signing requires a GPG key
%pom_remove_plugin org.apache.maven.plugins:maven-gpg-plugin

# F33+ and EPEL8+ doesn't use the maven-javadoc-plugin to generate javadoc
# Remove maven-javadoc-plugin configuration to avoid build failure
%pom_remove_plugin org.apache.maven.plugins:maven-javadoc-plugin

# Do not create source jars
%pom_remove_plugin org.apache.maven.plugins:maven-source-plugin

# Do not stage
%pom_remove_plugin org.sonatype.plugins:nexus-staging-maven-plugin

%build

%mvn_build
%install
%mvn_install
%oreon_autofiles canl-java-javadoc usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%files -f %{oreon_filedir}/main.list
%files -n canl-java-javadoc -f %{oreon_filedir}/canl-java-javadoc.list

%changelog

%autochangelog
