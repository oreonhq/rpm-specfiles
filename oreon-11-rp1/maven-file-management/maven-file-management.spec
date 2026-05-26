%bcond_with bootstrap

Name:           maven-file-management
Epoch:          1
Version:        3.1.0
Release:        %autorelease
Summary:        Maven File Management API
License:        Apache-2.0
URL:            https://maven.apache.org/shared/file-management
BuildArch:      noarch
ExclusiveArch:  %{java_arches} noarch

Source0:        https://repo1.maven.org/maven2/org/apache/maven/shared/file-management/%{version}/file-management-%{version}-source-release.zip
# oreon url source checksums begin
%global source0_sha256 34f48b425e82581a192672e1335d937e6c27a76b53f40e07ae4f0f05e0cb2701
%global source0_file file-management-3.1.0-source-release.zip
# oreon url source checksums end

%if %{with bootstrap}
BuildRequires:  javapackages-bootstrap
%else
BuildRequires:  maven-local-openjdk25
BuildRequires:  mvn(commons-io:commons-io)
BuildRequires:  mvn(junit:junit)
BuildRequires:  mvn(org.apache.maven.shared:maven-shared-components:pom:)
BuildRequires:  mvn(org.codehaus.modello:modello-maven-plugin)
BuildRequires:  mvn(org.codehaus.plexus:plexus-utils)
BuildRequires:  mvn(org.slf4j:slf4j-api)
BuildRequires:  mvn(org.slf4j:slf4j-simple)
%endif
# TODO Remove in Fedora 46
Obsoletes:      %{name}-javadoc < 1:3.1.0-19

%description
Provides a component for plugins to easily resolve project dependencies.

%prep
# oreon verify url source checksums begin
%(f=%{_sourcedir}/file-management-3.1.0-source-release.zip; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "34f48b425e82581a192672e1335d937e6c27a76b53f40e07ae4f0f05e0cb2701" || { echo "oreon: Source0 SHA256 mismatch for file-management-3.1.0-source-release.zip" >&2; exit 1; })
# oreon verify url source checksums end
%autosetup -p1 -C

%build
%mvn_build -j

%install
%mvn_install

%files -f .mfiles
%license LICENSE NOTICE

%changelog
* Mon May 25 2026 Oreon Packaging Team <packaging@oreonhq.com> - 1:3.1.0-1
- Import
