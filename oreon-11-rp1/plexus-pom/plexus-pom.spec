%global source0_hash 6ca0d8dc0ad0211146c55d7805a3ab6531f91cf76e9dcc4312ec63dc507eac47

%bcond_without bootstrap

Name:           plexus-pom
Version:        27
Release:        %autorelease
Summary:        Root Plexus Projects POM
License:        Apache-2.0
URL:            https://github.com/codehaus-plexus/plexus-pom
BuildArch:      noarch
ExclusiveArch:  %{java_arches} noarch

Source0:        https://github.com/codehaus-plexus/plexus-pom/archive/plexus-%{version}.tar.gz#/plexus-pom-18.tar.gz
Source1:        https://www.apache.org/licenses/LICENSE-2.0.txt

%if %{with bootstrap}
BuildRequires:  javapackages-bootstrap
%else
BuildRequires:  maven-local-openjdk25
%endif

%description
The Plexus project provides a full software stack for creating and
executing software projects. This package provides parent POM for
Plexus packages.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%setup -q -n plexus-pom-plexus-18
%autosetup -p1 -n plexus-pom-plexus-18
cp -p %{SOURCE1} LICENSE

%pom_remove_dep org.junit:junit-bom
%pom_remove_plugin :maven-site-plugin
%pom_remove_plugin :maven-enforcer-plugin
%pom_remove_plugin :taglist-maven-plugin
%pom_remove_plugin :spotless-maven-plugin

%build
%mvn_build -j

%install
%mvn_install

%files -f .mfiles
%license LICENSE

%changelog
* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 18-1
- Prepare for Oreon 11 (RP1)
