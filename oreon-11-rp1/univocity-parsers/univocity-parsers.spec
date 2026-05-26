# oreon source sha256 begin
# URL sources: global sourceN_sha256 = 64-char hex from sha256sum. Omit a sourceN_sha256 line to skip verify for that source.
%global source0_sha256 d9f377d6fb2e98afd2e83a544ee0762885816908cb3b909679bcc9ef4175dd35
%global oreon_verify_sources \
%{?source0_sha256:%(test -z "%{source0_sha256}" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_sha256}" || { echo "oreon: Source0 sha256 mismatch" >&2; exit 1; }; })}
%(true)
# oreon source sha256 end

%bcond_with bootstrap

Name:           univocity-parsers
Version:        2.9.1
Release:        %autorelease
Summary:        Collection of parsers for Java
License:        Apache-2.0
URL:            https://github.com/uniVocity/univocity-parsers
BuildArch:      noarch
ExclusiveArch:  %{java_arches} noarch

Source0:        https://github.com/uniVocity/univocity-parsers/archive/v%{version}.tar.gz

Patch:          0001-Resolve-import-clash-with-OpenJDK-17.patch

%if %{with bootstrap}
BuildRequires:  javapackages-bootstrap
%else
BuildRequires:  maven-local-openjdk25
BuildRequires:  mvn(org.apache.felix:maven-bundle-plugin)
BuildRequires:  mvn(org.apache.maven.plugins:maven-source-plugin)
%endif
# TODO Remove in Fedora 46
Obsoletes:      %{name}-javadoc < 2.9.1-31

%description
uniVocity-parsers is a suite of extremely fast and reliable parsers
for Java.  It provides a consistent interface for handling different
file formats, and a solid framework for the development of new
parsers.

%prep
%oreon_verify_sources
%autosetup -p1 -C

%pom_remove_plugin :nexus-staging-maven-plugin
%pom_remove_plugin :maven-compiler-plugin
%pom_remove_plugin :maven-javadoc-plugin

%build
# Tests require univocity-output-tester, which is not packaged yet.
%mvn_build -j -f -- -Dmaven.compiler.source=1.8 -Dmaven.compiler.target=1.8

%install
%mvn_install

%files -f .mfiles
%doc README.md
%license LICENSE-2.0.html

%changelog
* Mon May 25 2026 Oreon Packaging Team <packaging@oreonhq.com> - 2.9.1-1
- Import
