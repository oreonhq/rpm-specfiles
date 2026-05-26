%bcond_without bootstrap

Name:           maven-jar-plugin
Version:        3.3.0
Release:        %autorelease
Summary:        Maven JAR Plugin
License:        Apache-2.0
URL:            https://maven.apache.org/plugins/maven-jar-plugin/
BuildArch:      noarch
ExclusiveArch:  %{java_arches} noarch

Source0:        https://repo1.maven.org/maven2/org/apache/maven/plugins/%{name}/%{version}/%{name}-%{version}-source-release.zip
# oreon url source checksums begin
%global source0_sha256 87d77c76b594d5ebb6d719d5ea5ccd1249411183ff243e50d6c315c358307b4f
%global source0_file maven-jar-plugin-3.3.0-source-release.zip
# oreon url source checksums end

%if %{with bootstrap}
BuildRequires:  javapackages-bootstrap
%else
BuildRequires:  maven-local-openjdk25
BuildRequires:  mvn(junit:junit)
BuildRequires:  mvn(org.apache.maven.plugin-testing:maven-plugin-testing-harness)
BuildRequires:  mvn(org.apache.maven.plugin-tools:maven-plugin-annotations)
BuildRequires:  mvn(org.apache.maven.plugins:maven-plugin-plugin)
BuildRequires:  mvn(org.apache.maven.plugins:maven-plugins:pom:)
BuildRequires:  mvn(org.apache.maven.shared:file-management)
BuildRequires:  mvn(org.apache.maven:maven-archiver)
BuildRequires:  mvn(org.apache.maven:maven-artifact)
BuildRequires:  mvn(org.apache.maven:maven-compat)
BuildRequires:  mvn(org.apache.maven:maven-core)
BuildRequires:  mvn(org.apache.maven:maven-model)
BuildRequires:  mvn(org.apache.maven:maven-plugin-api)
BuildRequires:  mvn(org.codehaus.plexus:plexus-utils)
%endif
# TODO Remove in Fedora 46
Obsoletes:      %{name}-javadoc < 3.3.0-17

%description
Builds a Java Archive (JAR) file from the compiled
project classes and resources.

%prep
# oreon verify url source checksums begin
%(f=%{_sourcedir}/maven-jar-plugin-3.3.0-source-release.zip; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "87d77c76b594d5ebb6d719d5ea5ccd1249411183ff243e50d6c315c358307b4f" || { echo "oreon: Source0 SHA256 mismatch for maven-jar-plugin-3.3.0-source-release.zip" >&2; exit 1; })
# oreon verify url source checksums end
%autosetup -p1
# System version of maven-jar-plugin should be used, not reactor version
%pom_xpath_inject pom:pluginManagement/pom:plugins "<plugin><artifactId>maven-jar-plugin</artifactId><version>SYSTEM</version></plugin>"

%build
%mvn_build -j

%install
%mvn_install

%files -f .mfiles
%license LICENSE NOTICE

%changelog
* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 3.3.0-1
- Prepare for Oreon 11 (RP1)
