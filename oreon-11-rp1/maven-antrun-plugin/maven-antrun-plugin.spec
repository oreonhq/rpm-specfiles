%bcond_without bootstrap

Name:           maven-antrun-plugin
Version:        3.1.0
Release:        %autorelease
Summary:        Maven AntRun Plugin
License:        Apache-2.0
URL:            https://maven.apache.org/plugins/maven-antrun-plugin/
BuildArch:      noarch
ExclusiveArch:  %{java_arches} noarch

Source0:        https://repo1.maven.org/maven2/org/apache/maven/plugins/%{name}/%{version}/%{name}-%{version}-source-release.zip
# oreon url source checksums begin
%global source0_sha256 76773effbb33efdc28d91219e473b2142dac2da40686dd123d7d4d785dc81942
%global source0_file maven-antrun-plugin-3.1.0-source-release.zip
# oreon url source checksums end

%if %{with bootstrap}
BuildRequires:  javapackages-bootstrap
%else
BuildRequires:  maven-local-openjdk25
BuildRequires:  mvn(org.apache.ant:ant)
BuildRequires:  mvn(org.apache.maven.plugin-tools:maven-plugin-annotations)
BuildRequires:  mvn(org.apache.maven.plugins:maven-plugin-plugin)
BuildRequires:  mvn(org.apache.maven.plugins:maven-plugins:pom:)
BuildRequires:  mvn(org.apache.maven:maven-artifact)
BuildRequires:  mvn(org.apache.maven:maven-core)
BuildRequires:  mvn(org.apache.maven:maven-plugin-api)
BuildRequires:  mvn(org.codehaus.modello:modello-maven-plugin)
BuildRequires:  mvn(org.codehaus.plexus:plexus-utils)
BuildRequires:  mvn(org.junit.jupiter:junit-jupiter-engine)
BuildRequires:  mvn(org.xmlunit:xmlunit-core)
BuildRequires:  mvn(org.xmlunit:xmlunit-matchers)
%endif
# TODO Remove in Fedora 46
Obsoletes:      %{name}-javadoc < 3.1.0-23

%description
This plugin provides the ability to run Ant tasks from within Maven.
It is even possible to embed Ant scripts in the POM.

%prep
# oreon verify url source checksums begin
%(f=%{_sourcedir}/maven-antrun-plugin-3.1.0-source-release.zip; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "76773effbb33efdc28d91219e473b2142dac2da40686dd123d7d4d785dc81942" || { echo "oreon: Source0 SHA256 mismatch for maven-antrun-plugin-3.1.0-source-release.zip" >&2; exit 1; })
# oreon verify url source checksums end
%autosetup -p1

%build
%mvn_build -j

%install
%mvn_install

%files -f .mfiles
%license LICENSE NOTICE

%changelog
* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 3.1.0-1
- Prepare for Oreon 11 (RP1)
