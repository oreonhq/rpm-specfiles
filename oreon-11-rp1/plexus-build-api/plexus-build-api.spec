%global source0_hash 47aae8f94b6fffd3ea0816eca79094541a28fbf35a9d0ac1fd6459196b30ee1b

%bcond_with bootstrap

Name:           plexus-build-api
Version:        1.2.0
Release:        %autorelease
Summary:        Plexus Build API
License:        Apache-2.0
URL:            https://github.com/codehaus-plexus/plexus-build-api
BuildArch:      noarch
ExclusiveArch:  %{java_arches} noarch

Source0:        https://github.com/codehaus-plexus/plexus-build-api/archive/refs/tags/plexus-build-api-%{version}.tar.gz
Source1:        http://www.apache.org/licenses/LICENSE-2.0.txt

%if %{with bootstrap}
BuildRequires:  javapackages-bootstrap
%else
BuildRequires:  maven-local-openjdk25
BuildRequires:  mvn(javax.inject:javax.inject)
BuildRequires:  mvn(org.codehaus.plexus:plexus-utils)
BuildRequires:  mvn(org.codehaus.plexus:plexus:pom:)
BuildRequires:  mvn(org.eclipse.sisu:org.eclipse.sisu.plexus)
BuildRequires:  mvn(org.eclipse.sisu:sisu-maven-plugin)
BuildRequires:  mvn(org.slf4j:slf4j-api)
BuildRequires:  mvn(org.sonatype.plexus:plexus-build-api)
%endif
# TODO Remove in Fedora 46
Obsoletes:      %{name}-javadoc < 1.2.0-17

%description
Plexus Build API

%prep
%(test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; })
%autosetup -p1
cp -p %{SOURCE1} .

%mvn_file : plexus/%{name}

# Install plexus-build-api-tests as well
%mvn_package :

%build
%mvn_build -j

%install
%mvn_install

%files -f .mfiles
%license LICENSE-2.0.txt

%changelog
* Mon May 25 2026 Oreon Packaging Team <packaging@oreonhq.com> - 1.2.0-1
- Import
