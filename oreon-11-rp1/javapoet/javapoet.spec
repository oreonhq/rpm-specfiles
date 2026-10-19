%global source0_hash 1632e64e80360fb3a52e53212cfdff5e623e55f461945704479de87bd92892dc
Name:          javapoet
Version:       1.7.0
Release:        1%{?dist}
Summary:        A Java API for generating .java source files
License:       Apache-2.0
URL:           https://github.com/square/javapoet
Source0:        https://github.com/square/%{name}/archive/%{name}-%{version}.tar.gz#/javapoet-1.7.0.tar.gz
BuildArch:     noarch
ExclusiveArch:  %{java_arches} noarch
# oreon:deps
BuildRequires:  maven-local-openjdk25
# /oreon:deps
%description
A utility class which aids in generating Java source files.

%package javadoc
Summary:       Javadoc for %{name}
%description javadoc
This package contains javadoc for %{name}.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%setup -q -n %{name}-%{name}-%{version}
sed 's;<java.version>1.7</java.version>;<java.version>1.8</java.version>;' -i pom.xml
# remove unnecessary dependency on parent POM
%pom_remove_parent

%pom_remove_plugin :maven-checkstyle-plugin

%mvn_file : %{name}

%build

%mvn_build -f
%install
%mvn_install
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%files -f %{oreon_filedir}/main.list
%files -n javapoet-javadoc -f %{oreon_filedir}/javapoet-javadoc.list

%changelog

* Mon May 25 2026 Oreon Packaging Team <packaging@oreonhq.com> - 1.7.0-29
- Import
