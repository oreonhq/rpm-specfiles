%global source0_hash none

Name:           spice-parent
Version:        26
Release:        30%{?dist}
Summary:        Sonatype Spice Components
# Automatically converted from old format: ASL 2.0 - review is highly recommended.
License:        Apache-2.0
URL:            http://github.com/sonatype/oss-parents
BuildArch:      noarch
ExclusiveArch:  %{java_arches} noarch

Source0:        http://repo1.maven.org/maven2/org/sonatype/spice/%{name}/%{version}/%{name}-%{version}.pom
Source1:        http://apache.org/licenses/LICENSE-2.0.txt

Patch0:         pom.patch

BuildRequires:  maven-local-openjdk25
BuildRequires:  forge-parent

%description
Spice components and libraries are common components
used throughout the Sonatype Forge.

%prep
%(test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; })
%setup -qcT
cp -p %{SOURCE0} pom.xml
cp -p %{SOURCE1} .

#Remove plexus-javadoc
%patch -P0

%build
%mvn_build

%install
%mvn_install

%files -f .mfiles
%doc LICENSE-2.0.txt

%changelog
* Mon May 25 2026 Oreon Packaging Team <packaging@oreonhq.com> - 26-30
- Import
