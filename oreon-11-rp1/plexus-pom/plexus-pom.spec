%bcond_without bootstrap

Name:           plexus-pom
Version:        18
Release:        %autorelease
Summary:        Root Plexus Projects POM
License:        Apache-2.0
URL:            https://github.com/codehaus-plexus/plexus-pom
BuildArch:      noarch
ExclusiveArch:  %{java_arches} noarch

Source0:        https://github.com/codehaus-plexus/plexus-pom/archive/plexus-%{version}.tar.gz
Source1:        https://www.apache.org/licenses/LICENSE-2.0.txt
# oreon url source checksums begin
%global source0_sha256 09c20b62d3bc85413581b15867e20d1a9513a8ef67b6eee53948077c67795f38
%global source0_file plexus-18.tar.gz
# oreon url source checksums end

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
# oreon verify url source checksums begin
%(f=%{_sourcedir}/plexus-18.tar.gz; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "09c20b62d3bc85413581b15867e20d1a9513a8ef67b6eee53948077c67795f38" || { echo "oreon: Source0 SHA256 mismatch for plexus-18.tar.gz" >&2; exit 1; })
# oreon verify url source checksums end
%autosetup -p1
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
