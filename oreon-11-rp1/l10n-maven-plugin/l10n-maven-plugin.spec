%global source0_hash aa7821b8952139cdbc860f3f3f77a4c65fe8203b1f9756ad80fdb51220373b00
%global giturl  https://github.com/mojohaus/l10n-maven-plugin
Name:           l10n-maven-plugin
Version:        1.2.0
Release:        1%{?dist}
Summary:        Localization Tools Maven Plugin
License:        Apache-2.0
URL:            https://www.mojohaus.org/l10n-maven-plugin/
VCS:            git:%{giturl}.git
Source0:        %{giturl}/archive/%{name}-%{version}.tar.gz
BuildArch:      noarch
ExclusiveArch:  %{java_arches} noarch
# oreon:deps
BuildRequires:  maven-local-openjdk25
BuildRequires:  mvn(commons-io:commons-io)
BuildRequires:  mvn(org.apache.maven.doxia:doxia-sink-api)
BuildRequires:  mvn(org.apache.maven.plugin-tools:maven-plugin-annotations)
BuildRequires:  mvn(org.apache.maven.plugins:maven-plugin-plugin)
BuildRequires:  mvn(org.apache.maven.reporting:maven-reporting-api)
BuildRequires:  mvn(org.apache.maven.reporting:maven-reporting-impl)
BuildRequires:  mvn(org.apache.maven:maven-core)
BuildRequires:  mvn(org.apache.maven:maven-model)
BuildRequires:  mvn(org.apache.maven:maven-plugin-api)
BuildRequires:  mvn(org.codehaus.mojo:mojo-parent:pom:)
BuildRequires:  mvn(org.codehaus.plexus:plexus-archiver)
BuildRequires:  mvn(org.codehaus.plexus:plexus-utils)
# /oreon:deps
%description
The Localization Tools Maven Plugin helps with internationalization and
localization of your projects.

%package        javadoc
License:        Apache-2.0 AND MIT AND GPL-2.0-only WITH Classpath-exception-2.0
Summary:        API documentation for %{name}
Provides:       bundled(js-jquery) = 3.7.1
%description    javadoc
API documentation for %{name}.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%global oreon_srcdir %{name}-%{name}-%{version}
%oreon_prep
%build

%mvn_build
%install
%mvn_install
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%files -f %{oreon_filedir}/main.list
%files -n l10n-maven-plugin-javadoc -f %{oreon_filedir}/l10n-maven-plugin-javadoc.list

%changelog

%autochangelog
