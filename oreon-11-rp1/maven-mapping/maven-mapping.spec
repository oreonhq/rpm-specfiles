%global source0_hash 853af6b2e388dedc064ef5091c890812d4cf894e37d088b1c0666a6f62467fd5

%bcond_with bootstrap

Name:           maven-mapping
Version:        3.0.0
Release:        %autorelease
Summary:        Apache Maven Mapping
License:        Apache-2.0
URL:            https://maven.apache.org/shared/maven-mapping/
BuildArch:      noarch
ExclusiveArch:  %{java_arches} noarch

Source0:        https://repo.maven.apache.org/maven2/org/apache/maven/shared/%{name}/%{version}/%{name}-%{version}-source-release.zip

%if %{with bootstrap}
BuildRequires:  javapackages-bootstrap
%else
BuildRequires:  maven-local-openjdk25
BuildRequires:  mvn(junit:junit)
BuildRequires:  mvn(org.apache.maven.plugin-testing:maven-plugin-testing-harness)
BuildRequires:  mvn(org.apache.maven.shared:maven-shared-components:pom:)
BuildRequires:  mvn(org.apache.maven:maven-core)
BuildRequires:  mvn(org.codehaus.plexus:plexus-interpolation)
%endif

# TODO Remove in Fedora 46
Obsoletes:      %{name}-javadoc < 3.0.0-46

%description
Maven shared component that implements file name mapping.

%prep
%(test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; })
%autosetup -p1
%pom_xpath_set "pom:project/pom:properties/pom:maven.compiler.target" "8" pom.xml
%pom_xpath_set "pom:project/pom:properties/pom:maven.compiler.source" "8" pom.xml

%build
%mvn_build -j

%install
%mvn_install

%files -f .mfiles
%license LICENSE NOTICE

%changelog
* Mon May 25 2026 Oreon Packaging Team <packaging@oreonhq.com> - 3.0.0-1
- Import
