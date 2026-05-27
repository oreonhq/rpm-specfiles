%global source0_hash none

%bcond_with bootstrap

Name:           plexus-languages
Version:        1.2.0
Release:        %autorelease
Summary:        Plexus Languages
License:        Apache-2.0
URL:            https://github.com/codehaus-plexus/plexus-languages
BuildArch:      noarch
ExclusiveArch:  %{java_arches} noarch

# ./generate-tarball.sh
Source0:        https://github.com/codehaus-plexus/plexus-languages/archive/refs/tags/v1.2.0.tar.gz
Source1:        https://www.apache.org/licenses/LICENSE-2.0.txt
# Sources contain bundled jars that we cannot verify for licensing
Source2:        generate-tarball.sh

%if %{with bootstrap}
BuildRequires:  javapackages-bootstrap
%else
BuildRequires:  maven-local-openjdk25
BuildRequires:  mvn(com.thoughtworks.qdox:qdox)
BuildRequires:  mvn(javax.inject:javax.inject)
BuildRequires:  mvn(org.apache.maven.plugins:maven-failsafe-plugin)
BuildRequires:  mvn(org.codehaus.plexus:plexus:pom:)
BuildRequires:  mvn(org.eclipse.sisu:sisu-maven-plugin)
BuildRequires:  mvn(org.ow2.asm:asm)
%endif
# TODO Remove in Fedora 46
Obsoletes:      %{name}-javadoc < 1.2.0-15

%description
Plexus Languages is a set of Plexus components that maintain shared
language features.

%prep
%(test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; })
%autosetup -p1 -C

cp %{SOURCE1} .

%pom_remove_plugin :maven-enforcer-plugin

%build
# many tests rely on bundled test jars/classes
%mvn_build -j -f

%install
%mvn_install

%files -f .mfiles
%license LICENSE-2.0.txt

%changelog
* Mon May 25 2026 Oreon Packaging Team <packaging@oreonhq.com> - 1.2.0-1
- Import
