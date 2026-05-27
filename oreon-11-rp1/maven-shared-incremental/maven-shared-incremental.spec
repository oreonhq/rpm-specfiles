%global source0_hash none

%bcond_with bootstrap

Name:           maven-shared-incremental
Version:        1.1
Release:        %autorelease
Summary:        Maven Incremental Build support utilities
License:        Apache-2.0
URL:            https://maven.apache.org/shared/maven-shared-incremental/
BuildArch:      noarch
ExclusiveArch:  %{java_arches} noarch

Source0:        http://repo1.maven.org/maven2/org/apache/maven/shared/%{name}/%{version}/%{name}-%{version}-source-release.zip

# From upstream commit 1b5c81a7
Patch:          0001-MSHARED-1374-Upgrade-parent-pom-to-41.patch

%if %{with bootstrap}
BuildRequires:  javapackages-bootstrap
%else
BuildRequires:  maven-local-openjdk25
BuildRequires:  mvn(org.apache.maven.shared:maven-shared-components:pom:)
BuildRequires:  mvn(org.apache.maven.shared:maven-shared-utils)
BuildRequires:  mvn(org.apache.maven:maven-core)
BuildRequires:  mvn(org.apache.maven:maven-plugin-api)
BuildRequires:  mvn(org.codehaus.plexus:plexus-component-annotations)
BuildRequires:  mvn(org.codehaus.plexus:plexus-component-metadata)
%endif
# TODO Remove in Fedora 46
Obsoletes:      %{name}-javadoc < 1.1-53

%description
Various utility classes and plexus components for supporting
incremental build functionality in maven plugins.

%prep
%(test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; })
%autosetup -p1 -C
%pom_remove_dep :plexus-component-api

%build
%mvn_build -j

%install
%mvn_install

%files -f .mfiles
%license LICENSE NOTICE

%changelog
* Mon May 25 2026 Oreon Packaging Team <packaging@oreonhq.com> - 1.1-1
- Import
