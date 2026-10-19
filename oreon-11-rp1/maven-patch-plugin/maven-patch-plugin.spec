%global source0_hash 44d52f6106ab8d2d71d9a643aa5810ba9baacc03f7bf513e8ca256c38c8a3e98
Name:           maven-patch-plugin
Version:        1.2
Release:        33%{?dist}
Summary:        Maven Patch Plugin
License:        Apache-2.0
URL:            http://maven.apache.org/plugins/maven-patch-plugin/
Source0:        http://repo1.maven.org/maven2/org/apache/maven/plugins/%{name}/%{version}/%{name}-%{version}-source-release.zip
BuildArch:      noarch
ExclusiveArch:  %{java_arches} noarch
# oreon:deps
BuildRequires:  maven-local-openjdk25
BuildRequires:  mvn(junit:junit)
BuildRequires:  mvn(org.apache.maven.plugins:maven-plugins:pom:)
BuildRequires:  mvn(org.apache.maven:maven-plugin-api)
BuildRequires:  mvn(org.codehaus.plexus:plexus-utils)
# /oreon:deps
%description
The Patch Plugin is used to apply patches to source files.

%package javadoc
Summary:        Javadoc for %{name}
%description javadoc
API documentation for %{name}.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q

%build

%mvn_build
%install
%mvn_install
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%files -f %{oreon_filedir}/main.list
%files -n maven-patch-plugin-javadoc -f %{oreon_filedir}/maven-patch-plugin-javadoc.list

%changelog

%autochangelog
