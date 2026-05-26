Name:          javapoet
Version:       1.7.0
Release:       29%{?dist}
Summary:       A Java API for generating .java source files
# Automatically converted from old format: ASL 2.0 - review is highly recommended.
License:       Apache-2.0
URL:           https://github.com/square/javapoet
Source0:       https://github.com/square/%{name}/archive/%{name}-%{version}.tar.gz
# oreon url source checksums begin
%global source0_sha256 1632e64e80360fb3a52e53212cfdff5e623e55f461945704479de87bd92892dc
%global source0_file javapoet-1.7.0.tar.gz
# oreon url source checksums end

BuildRequires: maven-local-openjdk25

%if 0
# test dependencies
BuildRequires: mvn(junit:junit)
BuildRequires: mvn(org.eclipse.jdt.core.compiler:ecj:4.4.2)
BuildRequires: mvn(org.mockito:mockito-core:1.10.16)
# missing test dependencies
BuildRequires: mvn(com.google.jimfs:jimfs:1.0)
BuildRequires: mvn(com.google.testing.compile:compile-testing:0.6)
BuildRequires: mvn(com.google.truth:truth:0.25)
%endif

BuildArch:     noarch
ExclusiveArch:  %{java_arches} noarch

%description
A utility class which aids in generating Java source files.

%package javadoc
Summary:       Javadoc for %{name}

%description javadoc
This package contains javadoc for %{name}.

%prep
# oreon verify url source checksums begin
%(f=%{_sourcedir}/javapoet-1.7.0.tar.gz; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "1632e64e80360fb3a52e53212cfdff5e623e55f461945704479de87bd92892dc" || { echo "oreon: Source0 SHA256 mismatch for javapoet-1.7.0.tar.gz" >&2; exit 1; })
# oreon verify url source checksums end
%setup -q -n %{name}-%{name}-%{version}
sed 's;<java.version>1.7</java.version>;<java.version>1.8</java.version>;' -i pom.xml
# remove unnecessary dependency on parent POM
%pom_remove_parent

%pom_remove_plugin :maven-checkstyle-plugin

%mvn_file : %{name}

%build
# skip tests due to missing test dependencies
%mvn_build -f

%install
%mvn_install

%files -f .mfiles
%doc CHANGELOG.md README.md
%license LICENSE.txt

%files javadoc -f .mfiles-javadoc
%license LICENSE.txt

%changelog
* Mon May 25 2026 Oreon Packaging Team <packaging@oreonhq.com> - 1.7.0-29
- Import
