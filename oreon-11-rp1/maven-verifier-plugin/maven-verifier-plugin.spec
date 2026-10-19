%global source0_hash 71e2b04a50f965a5e4de4c14f85c295190d3a8ecc889efbfb073b6d904132a81
Name:           maven-verifier-plugin
Version:        1.1
Release:        1%{?dist}
Summary:        Maven Verifier Plugin
License:        Apache-2.0
URL:            http://maven.apache.org/plugins/maven-verifier-plugin/
Source0:        https://archive.apache.org/dist/maven/plugins/%{name}-%{version}-source-release.zip
BuildArch: noarch
ExclusiveArch:  %{java_arches} noarch
# oreon:deps
BuildRequires:  java-25-devel
BuildRequires:  jpackage-utils
BuildRequires:  maven-local-openjdk25
BuildRequires:  mvn(junit:junit)
BuildRequires:  mvn(org.apache.maven.plugins:maven-plugins:pom:)
BuildRequires:  mvn(org.codehaus.modello:modello-maven-plugin)
BuildRequires:  mvn(org.codehaus.plexus:plexus-utils)
# /oreon:deps
%description
Assists in integration testing by means of evaluating 
success/error conditions read from a configuration file.

%package javadoc
Summary:        Javadoc for %{name}
%description javadoc
API documentation for %{name}.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%setup -q 

%mvn_file :%{name} %{name}
%pom_remove_parent
%pom_add_parent org.apache.maven.plugins:maven-plugins:34
%pom_xpath_inject "pom:dependencies/pom:dependency[pom:artifactId='maven-plugin-api']" '<scope>provided</scope>'

%build

%mvn_build
%install
%mvn_install
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%files -f %{oreon_filedir}/main.list
%files -n maven-verifier-plugin-javadoc -f %{oreon_filedir}/maven-verifier-plugin-javadoc.list

%changelog

* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 1.1-12
- Prepare for Oreon 11 (RP1)
