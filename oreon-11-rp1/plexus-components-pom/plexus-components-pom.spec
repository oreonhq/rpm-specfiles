%bcond_without bootstrap

Name:           plexus-components-pom
Version:        14.2
Release:        11%{?dist}
Summary:        Plexus Components POM
License:        Apache-2.0
URL:            https://github.com/codehaus-plexus/plexus-components
BuildArch:      noarch
ExclusiveArch:  %{java_arches} noarch

Source0:        https://github.com/codehaus-plexus/plexus-components/archive/refs/tags/plexus-components-%{version}.tar.gz
Source1:        https://www.apache.org/licenses/LICENSE-2.0.txt

%if %{with bootstrap}
BuildRequires:  javapackages-bootstrap
%else
BuildRequires:  maven-local-openjdk25
BuildRequires:  mvn(org.codehaus.plexus:plexus-component-metadata)
BuildRequires:  mvn(org.codehaus.plexus:plexus:pom:)
%endif

%description
This package provides Plexus Components parent POM used by different
Plexus packages.

%prep
%autosetup -p1
cp -p %{SOURCE1} LICENSE

%build
%mvn_build

%install
%mvn_install

%files -f .mfiles
%doc LICENSE

%changelog
* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 14.2-11
- Prepare for Oreon 11 (RP1)
