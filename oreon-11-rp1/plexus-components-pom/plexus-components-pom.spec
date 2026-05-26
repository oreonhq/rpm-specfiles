%bcond_with bootstrap

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
# oreon url source checksums begin
%global source0_sha256 ecadd0e8873a553d7d6b23647b920fd20ef7fe4509cf86048a599573290634c6
%global source0_file plexus-components-14.2.tar.gz
# oreon url source checksums end

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
# oreon verify url source checksums begin
%(f=%{_sourcedir}/plexus-components-14.2.tar.gz; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "ecadd0e8873a553d7d6b23647b920fd20ef7fe4509cf86048a599573290634c6" || { echo "oreon: Source0 SHA256 mismatch for plexus-components-14.2.tar.gz" >&2; exit 1; })
# oreon verify url source checksums end
%autosetup -p1 -C
cp -p %{SOURCE1} LICENSE

%build
%mvn_build

%install
%mvn_install

%files -f .mfiles
%doc LICENSE

%changelog
* Mon May 25 2026 Oreon Packaging Team <packaging@oreonhq.com> - 14.2-11
- Import
