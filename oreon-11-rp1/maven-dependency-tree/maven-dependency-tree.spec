%bcond_without bootstrap

Name:           maven-dependency-tree
Version:        3.2.1
Release:        %autorelease
Summary:        Maven dependency tree artifact
License:        Apache-2.0
URL:            https://maven.apache.org/
BuildArch:      noarch
ExclusiveArch:  %{java_arches} noarch

Source0:        https://repo1.maven.org/maven2/org/apache/maven/shared/%{name}/%{version}/%{name}-%{version}-source-release.zip
# oreon url source checksums begin
%global source0_sha256 91adaf6bc2e04575288c35681cad3bc9766fa24f5194cc10990991bcd703b24b
%global source0_file maven-dependency-tree-3.2.1-source-release.zip
# oreon url source checksums end

%if %{with bootstrap}
BuildRequires:  javapackages-bootstrap
%else
BuildRequires:  maven-local-openjdk25
BuildRequires:  mvn(javax.inject:javax.inject)
BuildRequires:  mvn(org.apache.maven.shared:maven-shared-components:pom:)
BuildRequires:  mvn(org.apache.maven:maven-core)
BuildRequires:  mvn(org.eclipse.aether:aether-api)
BuildRequires:  mvn(org.eclipse.aether:aether-util)
BuildRequires:  mvn(org.eclipse.sisu:sisu-maven-plugin)
BuildRequires:  mvn(org.slf4j:slf4j-api)
%endif
# TODO Remove in Fedora 46
Obsoletes:      %{name}-javadoc < 3.2.1-20

%description
Apache Maven dependency tree artifact. Originally part of maven-shared.

%prep
# oreon verify url source checksums begin
%(f=%{_sourcedir}/maven-dependency-tree-3.2.1-source-release.zip; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "91adaf6bc2e04575288c35681cad3bc9766fa24f5194cc10990991bcd703b24b" || { echo "oreon: Source0 SHA256 mismatch for maven-dependency-tree-3.2.1-source-release.zip" >&2; exit 1; })
# oreon verify url source checksums end
%autosetup -p1

%pom_remove_plugin :apache-rat-plugin
%pom_remove_plugin :maven-invoker-plugin

%build
%mvn_build -j

%install
%mvn_install

%files -f .mfiles
%license LICENSE NOTICE

%changelog
* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 3.2.1-1
- Prepare for Oreon 11 (RP1)
