%bcond_with bootstrap

Name:           plexus-interactivity
Version:        1.3
Release:        %autorelease
Summary:        Plexus Interactivity Handler Component
License:        MIT
URL:            https://github.com/codehaus-plexus/plexus-interactivity
BuildArch:      noarch
ExclusiveArch:  %{java_arches} noarch

Source0:        https://github.com/codehaus-plexus/plexus-interactivity/archive/plexus-interactivity-1.3.tar.gz
Source1:        LICENSE.MIT
# oreon url source checksums begin
%global source0_sha256 20451c05c96785fbf9a864679b293c194a0d5ccc51d4abcd30354ab89f065d23
%global source0_file plexus-interactivity-1.3.tar.gz
# oreon url source checksums end

%if %{with bootstrap}
BuildRequires:  javapackages-bootstrap
%else
BuildRequires:  maven-local-openjdk25
BuildRequires:  mvn(com.google.inject:guice)
BuildRequires:  mvn(javax.inject:javax.inject)
BuildRequires:  mvn(org.codehaus.plexus:plexus:pom:)
BuildRequires:  mvn(org.eclipse.sisu:org.eclipse.sisu.inject)
BuildRequires:  mvn(org.eclipse.sisu:sisu-maven-plugin)
BuildRequires:  mvn(org.jline:jline-reader)
BuildRequires:  mvn(org.junit.jupiter:junit-jupiter-api)
%endif
# TODO Remove in Fedora 46
Obsoletes:      %{name}-javadoc < 1.3-5

%description
Plexus component that handles interactive user input from different
sources.

%prep
# oreon verify url source checksums begin
%(f=%{_sourcedir}/plexus-interactivity-1.3.tar.gz; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "20451c05c96785fbf9a864679b293c194a0d5ccc51d4abcd30354ab89f065d23" || { echo "oreon: Source0 SHA256 mismatch for plexus-interactivity-1.3.tar.gz" >&2; exit 1; })
# oreon verify url source checksums end
%autosetup -p1 -C
cp %{SOURCE1} .

%build
%mvn_build -j

%install
%mvn_install

%files -f .mfiles
%license LICENSE.MIT

%changelog
* Mon May 25 2026 Oreon Packaging Team <packaging@oreonhq.com> - 1.3-1
- Import
