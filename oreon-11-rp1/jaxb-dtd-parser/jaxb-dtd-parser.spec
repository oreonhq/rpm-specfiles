%global source0_hash 9c84a170e3f88b0281870ee9425311f2c3b5e1464a66c62657e269a29dcb6920

Name:           jaxb-dtd-parser
Version:        1.5.1
Release:        %autorelease
Summary:        SAX-like API for parsing XML DTDs
License:        BSD-3-Clause
URL:            https://github.com/eclipse-ee4j/jaxb-dtd-parser
BuildArch:      noarch
ExclusiveArch:  %{java_arches} noarch

Source0:        https://github.com/eclipse-ee4j/jaxb-dtd-parser/archive/1.5.1/jaxb-dtd-parser-1.5.1.tar.gz

BuildRequires:  maven-local-openjdk25
BuildRequires:  mvn(junit:junit)
BuildRequires:  mvn(org.apache.felix:maven-bundle-plugin)
BuildRequires:  mvn(org.codehaus.mojo:build-helper-maven-plugin)
# TODO Remove in Fedora 46
Obsoletes:      %{name}-javadoc < 1.5.1-14

%description
SAX-like API for parsing XML DTDs.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%autosetup -p1

pushd dtd-parser

# -Werror is considered harmful for downstream package builds
sed -i /-Werror/d pom.xml

%pom_remove_parent

%pom_remove_plugin :buildnumber-maven-plugin
%pom_remove_plugin :glassfish-copyright-maven-plugin
%pom_remove_plugin :maven-enforcer-plugin
popd

%build
pushd dtd-parser
%mvn_build -j
popd

%install
pushd dtd-parser
%mvn_install
popd

%files -f dtd-parser/.mfiles
%license LICENSE.md NOTICE.md
%doc README.md

%changelog
* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 1.5.1-1
- Prepare for Oreon 11 (RP1)
