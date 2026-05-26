Name:           jaxb-dtd-parser
Version:        1.5.1
Release:        %autorelease
Summary:        SAX-like API for parsing XML DTDs
License:        BSD-3-Clause
URL:            https://github.com/eclipse-ee4j/jaxb-dtd-parser
BuildArch:      noarch
ExclusiveArch:  %{java_arches} noarch

Source0:        https://github.com/eclipse-ee4j/jaxb-dtd-parser/archive/1.5.1/jaxb-dtd-parser-1.5.1.tar.gz
# oreon url source checksums begin
%global source0_sha256 9c84a170e3f88b0281870ee9425311f2c3b5e1464a66c62657e269a29dcb6920
%global source0_file jaxb-dtd-parser-1.5.1.tar.gz
# oreon url source checksums end

BuildRequires:  maven-local-openjdk25
BuildRequires:  mvn(junit:junit)
BuildRequires:  mvn(org.apache.felix:maven-bundle-plugin)
BuildRequires:  mvn(org.codehaus.mojo:build-helper-maven-plugin)
# TODO Remove in Fedora 46
Obsoletes:      %{name}-javadoc < 1.5.1-14

%description
SAX-like API for parsing XML DTDs.

%prep
# oreon verify url source checksums begin
%(f=%{_sourcedir}/jaxb-dtd-parser-1.5.1.tar.gz; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "9c84a170e3f88b0281870ee9425311f2c3b5e1464a66c62657e269a29dcb6920" || { echo "oreon: Source0 SHA256 mismatch for jaxb-dtd-parser-1.5.1.tar.gz" >&2; exit 1; })
# oreon verify url source checksums end
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
