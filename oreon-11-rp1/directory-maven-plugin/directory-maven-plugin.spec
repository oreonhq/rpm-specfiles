%global source0_hash 89936bd705abf6a70828d743374c3f716802699852c1d03361394d690850c964
Name:       directory-maven-plugin
Version:    1.0
Release:        1%{?dist}
Summary:        Establish locations for files in multi-module builds
License:    Apache-2.0
URL:        https://github.com/jdcasey/directory-maven-plugin
Source0:        https://github.com/jdcasey/directory-maven-plugin/archive/refs/tags/directory-maven-plugin-%{version}.tar.gz#/directory-maven-plugin-%{version}.tar.gz
Patch0:     directory-maven-plugin-fix-no-mojo-definition.patch
BuildArch:  noarch
ExclusiveArch:  %{java_arches} noarch
# oreon:deps
BuildRequires:  maven-local-openjdk25
BuildRequires:  mvn(junit:junit)
BuildRequires:  mvn(org.apache.maven.plugins:maven-plugin-plugin)
BuildRequires:  mvn(org.apache.maven:maven-core)
BuildRequires:  mvn(org.apache.maven:maven-model)
BuildRequires:  mvn(org.apache.maven:maven-parent:pom:)
BuildRequires:  mvn(org.apache.maven:maven-plugin-api)
# /oreon:deps
%description
The Directory Plugin for Maven is used to discover various project-related 
paths, such as the execution root directory, the directory for a specific 
project in the current build session, or the highest project base directory 
(closest to the filesystem root directory) available in the projects loaded 
from disk (not resolved from a remote repository). The plugin will then reflect
this value to the console, and also inject it into each project's properties 
using the value of the property plugin parameter.

%package javadoc
Summary:  Javadoc for %{name}
%description javadoc
%{summary}.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%autosetup -n directory-maven-plugin-directory-maven-plugin-%{version}

%pom_remove_parent

# Bump Java source option
sed -i 's/1.7/1.8/g' pom.xml

%build

%mvn_build
%install
%mvn_install
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%files -f %{oreon_filedir}/main.list
%files -n directory-maven-plugin-javadoc -f %{oreon_filedir}/directory-maven-plugin-javadoc.list

%changelog

* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 1.0-8
- Prepare for Oreon 11 (RP1)
