%bcond_without bootstrap

Name:           maven-archiver
Version:        3.6.2
Release:        %autorelease
Summary:        Maven Archiver
License:        Apache-2.0
URL:            https://maven.apache.org/shared/maven-archiver/
BuildArch:      noarch
ExclusiveArch:  %{java_arches} noarch

Source0:        https://repo1.maven.org/maven2/org/apache/maven/%{name}/%{version}/%{name}-%{version}-source-release.zip
# oreon url source checksums begin
%global source0_sha256 7afcbc38b650dda4cd07168e792f8d5137ae630fc10ea31135735e0da04aee47
%global source0_file maven-archiver-3.6.2-source-release.zip
# oreon url source checksums end

%if %{with bootstrap}
BuildRequires:  javapackages-bootstrap
%else
BuildRequires:  maven-local-openjdk25
BuildRequires:  mvn(org.apache.maven.shared:maven-shared-components:pom:)
BuildRequires:  mvn(org.apache.maven:maven-core)
BuildRequires:  mvn(org.assertj:assertj-core)
BuildRequires:  mvn(org.codehaus.plexus:plexus-archiver)
BuildRequires:  mvn(org.codehaus.plexus:plexus-interpolation)
BuildRequires:  mvn(org.junit.jupiter:junit-jupiter-api)
BuildRequires:  mvn(org.junit.jupiter:junit-jupiter-params)
BuildRequires:  mvn(org.mockito:mockito-core)
BuildRequires:  mvn(org.slf4j:slf4j-simple)
%endif
# TODO Remove in Fedora 46
Obsoletes:      %{name}-javadoc < 3.6.2-7

%description
The Maven Archiver is used by other Maven plugins
to handle packaging

%prep
# oreon verify url source checksums begin
%(f=%{_sourcedir}/maven-archiver-3.6.2-source-release.zip; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "7afcbc38b650dda4cd07168e792f8d5137ae630fc10ea31135735e0da04aee47" || { echo "oreon: Source0 SHA256 mismatch for maven-archiver-3.6.2-source-release.zip" >&2; exit 1; })
# oreon verify url source checksums end
%autosetup -p1
%pom_remove_dep :junit-bom

%build
%mvn_build -j

%install
%mvn_install

%files -f .mfiles
%doc README.md
%license LICENSE NOTICE

%changelog
* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 3.6.2-1
- Prepare for Oreon 11 (RP1)
