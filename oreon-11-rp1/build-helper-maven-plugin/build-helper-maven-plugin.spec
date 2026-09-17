%global source0_hash 9f79c0c19597b832e7a7a3dcf4252f1808405dffde96b6ae34cf936df160c525

%bcond_without bootstrap

Name:           build-helper-maven-plugin
Version:        3.6.1
Release:        %autorelease
Summary:        Build Helper Maven Plugin
License:        MIT
URL:            https://www.mojohaus.org/build-helper-maven-plugin/
BuildArch:      noarch
ExclusiveArch:  %{java_arches} noarch

Source0:        https://repo1.maven.org/maven2/org/codehaus/mojo/build-helper-maven-plugin/%{version}/build-helper-maven-plugin-%{version}-source-release.zip

%if %{with bootstrap}
BuildRequires:  javapackages-bootstrap
%else
BuildRequires:  maven-local-openjdk25
BuildRequires:  mvn(junit:junit)
BuildRequires:  mvn(org.apache.maven.plugin-tools:maven-plugin-annotations)
BuildRequires:  mvn(org.apache.maven.plugins:maven-plugin-plugin)
BuildRequires:  mvn(org.apache.maven.shared:file-management)
BuildRequires:  mvn(org.apache.maven:maven-core)
BuildRequires:  mvn(org.apache.maven:maven-plugin-api)
BuildRequires:  mvn(org.codehaus.mojo:mojo-parent:pom:)
BuildRequires:  mvn(org.codehaus.plexus:plexus-utils)
BuildRequires:  mvn(org.junit.jupiter:junit-jupiter)
BuildRequires:  mvn(org.slf4j:slf4j-api)
BuildRequires:  mvn(org.slf4j:slf4j-simple)
%endif
# TODO Remove in Fedora 46
Obsoletes:      %{name}-javadoc < 3.6.0-10

%description
This plugin contains various small independent goals to assist with
Maven build lifecycle.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%autosetup -p1

%pom_add_dep junit:junit::test

rm src/main/java/org/codehaus/mojo/buildhelper/BeanshellPropertyMojo.java
%pom_remove_dep :bsh

%pom_remove_plugin :maven-invoker-plugin

%build
%mvn_build -j

%install
%mvn_install

%files -f .mfiles
%license LICENSE.txt
%doc README.md

%changelog
* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 3.6.1-1
- Prepare for Oreon 11 (RP1)
