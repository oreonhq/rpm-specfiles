%global source0_hash 50f0f94e8de44a3ca457156943068d694ca88474a94dbf6d85fa369f7e8ec1ae

Name:           exec-maven-plugin
Version:        3.6.3
Release:        %autorelease
Summary:        Exec Maven Plugin

License:        Apache-2.0
URL:            https://www.mojohaus.org/exec-maven-plugin/
Source0:        https://repo1.maven.org/maven2/org/codehaus/mojo/exec-maven-plugin/3.6.3/exec-maven-plugin-3.6.3-source-release.zip

BuildArch:      noarch
ExclusiveArch:  %{java_arches} noarch

BuildRequires:  maven-local-openjdk25
BuildRequires:  maven-artifact-transfer
BuildRequires:  maven-dependency-plugin
BuildRequires:  mvn(org.mockito:mockito-junit-jupiter)
BuildRequires:  mvn(org.apache.commons:commons-exec)
BuildRequires:  mvn(org.apache.maven:maven-artifact)
BuildRequires:  mvn(org.apache.maven:maven-compat)
BuildRequires:  mvn(org.apache.maven:maven-core)
BuildRequires:  mvn(org.apache.maven:maven-model)
BuildRequires:  mvn(org.apache.maven:maven-plugin-api)
BuildRequires:  mvn(org.apache.maven.plugins:maven-plugin-plugin)
BuildRequires:  mvn(org.apache.maven.plugin-tools:maven-plugin-annotations)
BuildRequires:  mvn(org.codehaus.mojo:mojo-parent:pom:)
BuildRequires:  mvn(org.codehaus.plexus:plexus-component-annotations)
BuildRequires:  mvn(org.codehaus.plexus:plexus-component-metadata)
BuildRequires:  mvn(org.codehaus.plexus:plexus-utils)

%description
A plugin to allow execution of system and Java programs.

%javadoc_package

%prep
%(test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; })
%setup -q -n exec-maven-plugin-%{version}

find . -name *.jar -delete

%pom_remove_plugin :animal-sniffer-maven-plugin

#Drop test part. sonatype-aerther not available
%pom_remove_dep :mockito-core
%pom_remove_dep :maven-plugin-testing-harness
%pom_remove_dep :slf4j-simple

%pom_remove_plugin :sisu-maven-plugin
%pom_remove_plugin :maven-dependency-plugin
%pom_remove_plugin :maven-toolchains-plugin

rm -rf src/test/

%build
%mvn_build

%install
%mvn_install

%files -f .mfiles
%license LICENSE.txt
%dir %{_javadir}/%{name}

%changelog
* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 3.6.3-1
- Prepare for Oreon 11 (RP1)
