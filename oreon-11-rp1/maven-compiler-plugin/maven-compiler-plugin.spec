%bcond_with bootstrap

Name:           maven-compiler-plugin
Version:        3.12.1
Release:        %autorelease
Summary:        Maven Compiler Plugin
License:        Apache-2.0
URL:            https://maven.apache.org/plugins/maven-compiler-plugin
BuildArch:      noarch
ExclusiveArch:  %{java_arches} noarch

Source0:        https://archive.apache.org/dist/maven/plugins/%{name}-%{version}-source-release.zip
# oreon url source checksums begin
%global source0_sha256 5d1fd38ee713684b991d6551b4fc305b12ef51731e8498bf1b40668e4e24c0e6
%global source0_file maven-compiler-plugin-3.12.1-source-release.zip
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
BuildRequires:  mvn(org.apache.maven.shared:maven-shared-incremental)
BuildRequires:  mvn(org.apache.maven.shared:maven-shared-utils)
BuildRequires:  mvn(org.apache.maven:maven-artifact)
BuildRequires:  mvn(org.apache.maven:maven-compat)
BuildRequires:  mvn(org.apache.maven:maven-core)
BuildRequires:  mvn(org.apache.maven:maven-plugin-api)
BuildRequires:  mvn(org.codehaus.plexus:plexus-compiler-api)
BuildRequires:  mvn(org.codehaus.plexus:plexus-compiler-javac)
BuildRequires:  mvn(org.codehaus.plexus:plexus-compiler-manager)
BuildRequires:  mvn(org.codehaus.plexus:plexus-java)
BuildRequires:  mvn(org.codehaus.plexus:plexus-utils)
BuildRequires:  mvn(org.codehaus.plexus:plexus-xml)
BuildRequires:  mvn(org.eclipse.sisu:sisu-maven-plugin)
BuildRequires:  mvn(org.mockito:mockito-core)
%endif
# TODO Remove in Fedora 46
Obsoletes:      %{name}-javadoc < 3.12.1-13

%description
The Compiler Plugin is used to compile the sources of your project.

%prep
# oreon verify url source checksums begin
%(f=%{_sourcedir}/maven-compiler-plugin-3.12.1-source-release.zip; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "5d1fd38ee713684b991d6551b4fc305b12ef51731e8498bf1b40668e4e24c0e6" || { echo "oreon: Source0 SHA256 mismatch for maven-compiler-plugin-3.12.1-source-release.zip" >&2; exit 1; })
# oreon verify url source checksums end
%autosetup -p1 -C

# Replace path to junit in a test case with the system wide .jar
sed -i 's|localRepository,\ "junit/junit/3.8.1/junit-3.8.1.jar"|"%(find-jar junit || find-jar javapackages-bootstrap/junit)"|' src/test/java/org/apache/maven/plugin/compiler/CompilerMojoTestCase.java

%build
# JAVA_HOME must be exported because unit tests make use of it for locating javac executable
export JAVA_HOME=%{java_home}
%mvn_build -j

%install
%mvn_install

%files -f .mfiles
%license LICENSE NOTICE

%changelog
* Mon May 25 2026 Oreon Packaging Team <packaging@oreonhq.com> - 3.12.1-1
- Import
