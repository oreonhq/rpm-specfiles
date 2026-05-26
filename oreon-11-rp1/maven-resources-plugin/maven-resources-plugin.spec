%bcond_without bootstrap

Name:           maven-resources-plugin
Version:        3.3.1
Release:        %autorelease
Summary:        Maven Resources Plugin
License:        Apache-2.0
URL:            https://maven.apache.org/plugins/maven-resources-plugin
BuildArch:      noarch
ExclusiveArch:  %{java_arches} noarch

Source0:        https://repo1.maven.org/maven2/org/apache/maven/plugins/%{name}/%{version}/%{name}-%{version}-source-release.zip
# oreon url source checksums begin
%global source0_sha256 84e8c90032551b79c392596cf7231ff6ce9403c5644d6433c51029ac506f944d
%global source0_file maven-resources-plugin-3.3.1-source-release.zip
# oreon url source checksums end

%if %{with bootstrap}
BuildRequires:  javapackages-bootstrap
%else
BuildRequires:  maven-local-openjdk25
BuildRequires:  mvn(commons-io:commons-io)
BuildRequires:  mvn(junit:junit)
BuildRequires:  mvn(org.apache.commons:commons-lang3)
BuildRequires:  mvn(org.apache.maven.plugin-testing:maven-plugin-testing-harness)
BuildRequires:  mvn(org.apache.maven.plugin-tools:maven-plugin-annotations)
BuildRequires:  mvn(org.apache.maven.plugins:maven-plugin-plugin)
BuildRequires:  mvn(org.apache.maven.plugins:maven-plugins:pom:)
BuildRequires:  mvn(org.apache.maven.resolver:maven-resolver-api)
BuildRequires:  mvn(org.apache.maven.shared:maven-filtering)
BuildRequires:  mvn(org.apache.maven:maven-compat)
BuildRequires:  mvn(org.apache.maven:maven-core)
BuildRequires:  mvn(org.apache.maven:maven-model)
BuildRequires:  mvn(org.apache.maven:maven-plugin-api)
BuildRequires:  mvn(org.apache.maven:maven-settings)
BuildRequires:  mvn(org.codehaus.plexus:plexus-interpolation)
BuildRequires:  mvn(org.codehaus.plexus:plexus-utils)
BuildRequires:  mvn(org.eclipse.sisu:org.eclipse.sisu.plexus)
%endif
# TODO Remove in Fedora 46
Obsoletes:      %{name}-javadoc < 3.3.1-18

%description
The Resources Plugin handles the copying of project resources
to the output directory.

%prep
# oreon verify url source checksums begin
%(f=%{_sourcedir}/maven-resources-plugin-3.3.1-source-release.zip; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "84e8c90032551b79c392596cf7231ff6ce9403c5644d6433c51029ac506f944d" || { echo "oreon: Source0 SHA256 mismatch for maven-resources-plugin-3.3.1-source-release.zip" >&2; exit 1; })
# oreon verify url source checksums end
%autosetup -p1

%build
%mvn_build -j

%install
%mvn_install

%files -f .mfiles
%license LICENSE NOTICE

%changelog
* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 3.3.1-1
- Prepare for Oreon 11 (RP1)
