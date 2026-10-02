%global source0_hash 8a9190e7ed4e1af28da7759d1b0d17a8f0d1e92eb5dac8abafb31db7cf3d6c00

%bcond_without bootstrap

Name:           maven-dependency-plugin
Version:        3.11.0
Release:        %autorelease
Summary:        Plugin to manipulate, copy and unpack local and remote artifacts
License:        Apache-2.0
URL:            https://maven.apache.org/plugins/%{name}
BuildArch:      noarch
ExclusiveArch:  %{java_arches} noarch

Source0:        https://repo1.maven.org/maven2/org/apache/maven/plugins/%{name}/%{version}/%{name}-%{version}-source-release.zip


%if %{with bootstrap}
BuildRequires:  javapackages-bootstrap
%else
BuildRequires:  maven-local-openjdk25
BuildRequires:  mvn(commons-collections:commons-collections)
BuildRequires:  mvn(org.apache.maven.plugin-tools:maven-plugin-annotations)
BuildRequires:  mvn(org.apache.maven.plugins:maven-plugin-plugin)
BuildRequires:  mvn(org.apache.maven.plugins:maven-plugins:pom:)
BuildRequires:  mvn(org.apache.maven.shared:maven-artifact-transfer)
BuildRequires:  mvn(org.apache.maven.shared:maven-common-artifact-filters)
BuildRequires:  mvn(org.apache.maven.shared:maven-dependency-analyzer)
BuildRequires:  mvn(org.apache.maven.shared:maven-dependency-tree)
BuildRequires:  mvn(org.apache.maven.shared:maven-shared-utils)
BuildRequires:  mvn(org.apache.maven:maven-aether-provider)
BuildRequires:  mvn(org.apache.maven:maven-artifact)
BuildRequires:  mvn(org.apache.maven:maven-core)
BuildRequires:  mvn(org.apache.maven:maven-model)
BuildRequires:  mvn(org.apache.maven:maven-plugin-api)
BuildRequires:  mvn(org.apache.maven:maven-repository-metadata)
BuildRequires:  mvn(org.apache.maven:maven-settings)
BuildRequires:  mvn(org.codehaus.plexus:plexus-archiver)
BuildRequires:  mvn(org.codehaus.plexus:plexus-io)
BuildRequires:  mvn(org.codehaus.plexus:plexus-utils)
BuildRequires:  mvn(org.eclipse.aether:aether-api)
BuildRequires:  mvn(org.eclipse.aether:aether-util)
BuildRequires:  mvn(org.eclipse.sisu:sisu-maven-plugin)
BuildRequires:  mvn(org.sonatype.plexus:plexus-build-api)
%endif
# TODO Remove in Fedora 46
Obsoletes:      %{name}-javadoc < 3.11.0-16

%description
The dependency plugin provides the capability to manipulate
artifacts. It can copy and/or unpack artifacts from local or remote
repositories to a specified location.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%autosetup -p1
find src -name '*.java' -exec sed -i 's/\r//' {} +

%pom_remove_dep :maven-reporting-impl

%pom_remove_dep :jetty-server
%pom_remove_dep :jetty-util
%pom_remove_dep :jetty-security

%pom_remove_dep org.apache.maven.doxia:doxia-sink-api
%pom_remove_dep org.apache.maven.reporting:maven-reporting-api
%pom_remove_dep org.codehaus.plexus:plexus-i18n


# Tests which require eclipse
rm src/test/java/org/apache/maven/plugins/dependency/TestGetMojo.java
rm -r src/test/java/org/apache/maven/plugins/dependency/fromDependencies
rm -r src/test/java/org/apache/maven/plugins/dependency/fromConfiguration
rm src/test/java/org/apache/maven/plugins/dependency/utils/translators/TestClassifierTypeTranslator.java

# Requires org.apache.maven.reporting
rm src/main/java/org/apache/maven/plugins/dependency/analyze/AnalyzeReport{,Renderer}.java
sed -i '/doSpecialTest( "analyze-report" );/d' src/test/java/org/apache/maven/plugins/dependency/TestSkip.java

%build
%mvn_build -j -f

%install
%mvn_install

%files -f .mfiles
%license LICENSE NOTICE

%changelog
%autochangelog
