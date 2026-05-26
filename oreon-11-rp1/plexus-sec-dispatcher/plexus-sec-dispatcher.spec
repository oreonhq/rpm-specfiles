%bcond_without bootstrap

Name:           plexus-sec-dispatcher
Version:        2.0
Release:        %autorelease
Summary:        Plexus Security Dispatcher Component
License:        Apache-2.0
URL:            https://github.com/codehaus-plexus/plexus-sec-dispatcher
BuildArch:      noarch
ExclusiveArch:  %{java_arches} noarch

Source0:        https://github.com/codehaus-plexus/plexus-sec-dispatcher/archive/plexus-sec-dispatcher-2.0/plexus-sec-dispatcher-2.0.tar.gz
Source1:        https://www.apache.org/licenses/LICENSE-2.0.txt
# oreon url source checksums begin
%global source0_sha256 21ab7548945f3d6a2cb599fe198575f11ea18841a85d5bbe3d62fa6f9183d39a
%global source0_file plexus-sec-dispatcher-2.0.tar.gz
# oreon url source checksums end

%if %{with bootstrap}
BuildRequires:  javapackages-bootstrap
%else
BuildRequires:  maven-local-openjdk25
BuildRequires:  mvn(junit:junit)
BuildRequires:  mvn(org.codehaus.modello:modello-maven-plugin)
BuildRequires:  mvn(org.codehaus.plexus:plexus-utils)
BuildRequires:  mvn(org.eclipse.sisu:sisu-maven-plugin)
BuildRequires:  mvn(org.sonatype.plexus:plexus-cipher)
%endif
# TODO Remove in Fedora 46
Obsoletes:      %{name}-javadoc < 2.0-33

%description
Plexus Security Dispatcher Component

%prep
# oreon verify url source checksums begin
%(f=%{_sourcedir}/plexus-sec-dispatcher-2.0.tar.gz; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "21ab7548945f3d6a2cb599fe198575f11ea18841a85d5bbe3d62fa6f9183d39a" || { echo "oreon: Source0 SHA256 mismatch for plexus-sec-dispatcher-2.0.tar.gz" >&2; exit 1; })
# oreon verify url source checksums end
%autosetup -p1

cp %{SOURCE1} .

%pom_remove_parent

%pom_xpath_inject 'pom:project' '<groupId>org.codehaus.plexus</groupId>'

%mvn_file : plexus/%{name}

%mvn_alias org.codehaus.plexus: org.sonatype.plexus:

%build
%mvn_build -j -- -Dmaven.compiler.source=1.8 -Dmaven.compiler.target=1.8

%install
%mvn_install

%files -f .mfiles
%license LICENSE-2.0.txt

%changelog
* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 2.0-1
- Prepare for Oreon 11 (RP1)
