%bcond_without bootstrap

Name:           maven-dependency-analyzer
Version:        1.13.2
Release:        %autorelease
Summary:        Maven dependency analyzer
License:        Apache-2.0
URL:            https://maven.apache.org/shared/maven-dependency-analyzer/
BuildArch:      noarch
ExclusiveArch:  %{java_arches} noarch

Source0:        https://repo1.maven.org/maven2/org/apache/maven/shared/%{name}/%{version}/%{name}-%{version}-source-release.zip
# oreon url source checksums begin
%global source0_sha256 27c67ec8f81bd3bdb860f4a15d9cf785de01fef655d22f9b55d379a70408ed3d
%global source0_file maven-dependency-analyzer-1.13.2-source-release.zip
# oreon url source checksums end

%if %{with bootstrap}
BuildRequires:  javapackages-bootstrap
%else
BuildRequires:  maven-local-openjdk25
BuildRequires:  mvn(commons-io:commons-io)
BuildRequires:  mvn(javax.inject:javax.inject)
BuildRequires:  mvn(org.apache.maven.shared:maven-shared-components:pom:)
BuildRequires:  mvn(org.apache.maven:maven-artifact)
BuildRequires:  mvn(org.apache.maven:maven-core)
BuildRequires:  mvn(org.apache.maven:maven-model)
BuildRequires:  mvn(org.assertj:assertj-core)
BuildRequires:  mvn(org.eclipse.sisu:sisu-maven-plugin)
BuildRequires:  mvn(org.junit.jupiter:junit-jupiter-api)
BuildRequires:  mvn(org.ow2.asm:asm)
BuildRequires:  mvn(org.slf4j:slf4j-api)
BuildRequires:  mvn(org.slf4j:slf4j-simple)
%endif
# TODO Remove in Fedora 46
Obsoletes:      %{name}-javadoc < 1.13.2-19

%description
Analyzes the dependencies of a project for undeclared or unused artifacts.

Warning: Analysis is not done at source but bytecode level, then some cases are
not detected (constants, annotations with source-only retention, links in
javadoc) which can lead to wrong result if they are the only use of a
dependency.

%prep
# oreon verify url source checksums begin
%(f=%{_sourcedir}/maven-dependency-analyzer-1.13.2-source-release.zip; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "27c67ec8f81bd3bdb860f4a15d9cf785de01fef655d22f9b55d379a70408ed3d" || { echo "oreon: Source0 SHA256 mismatch for maven-dependency-analyzer-1.13.2-source-release.zip" >&2; exit 1; })
# oreon verify url source checksums end
%autosetup -p1

%build
%mvn_build -j

%install
%mvn_install

%files -f .mfiles
%license LICENSE NOTICE

%changelog
* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 1.13.2-1
- Prepare for Oreon 11 (RP1)
