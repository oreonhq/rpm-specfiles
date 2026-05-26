# oreon source sha256 begin
# URL sources: global sourceN_sha256 = 64-char hex from sha256sum. Omit a sourceN_sha256 line to skip verify for that source.
%global source0_sha256 02d186e71967646803b9316b17ce7ac5a858a4690f4afe9e4af2a2f9e73b2bb3
%global oreon_verify_sources \
%{?source0_sha256:%(test -z "%{source0_sha256}" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_sha256}" || { echo "oreon: Source0 sha256 mismatch" >&2; exit 1; }; })}
%(true)
# oreon source sha256 end

%bcond_without bootstrap

Name:           moditect
Version:        1.1.0
Release:        %autorelease
Summary:        Tooling for the Java Module System
License:        Apache-2.0
URL:            https://github.com/moditect/moditect
BuildArch:      noarch
ExclusiveArch:  %{java_arches} noarch

Source0:        https://github.com/moditect/moditect/archive/1.1.0/moditect-1.1.0.tar.gz

%if %{with bootstrap}
BuildRequires:  javapackages-bootstrap
%else
BuildRequires:  maven-local-openjdk25
BuildRequires:  mvn(com.beust:jcommander)
BuildRequires:  mvn(com.github.javaparser:javaparser-core)
BuildRequires:  mvn(junit:junit)
BuildRequires:  mvn(org.apache.maven.plugin-tools:maven-plugin-annotations)
BuildRequires:  mvn(org.apache.maven.plugins:maven-plugin-plugin)
BuildRequires:  mvn(org.apache.maven:maven-core)
BuildRequires:  mvn(org.apache.maven:maven-plugin-api)
BuildRequires:  mvn(org.assertj:assertj-core)
BuildRequires:  mvn(org.eclipse.aether:aether-util)
BuildRequires:  mvn(org.ow2.asm:asm)
%endif
# TODO Remove in Fedora 46
Obsoletes:      %{name}-javadoc < 1.1.0-12

%description
The ModiTect project aims at providing productivity tools for working with the
Java module system ("Jigsaw"). Currently the following tasks are supported:
* Generating module-info.java descriptors for given artifacts (Maven
  dependencies or local JAR files)
* Adding module descriptors to your project's JAR as well as existing JAR files
  (dependencies)
* Creating module runtime images

Compared to authoring module descriptors by hand, using ModiTect saves you work
by defining dependence clauses based on your project's dependencies, describing
exported and opened packages with patterns (instead of listing all packages
separately), auto-detecting service usages and more. You also can use ModiTect
to add a module descriptor to your project JAR while staying on Java 8 with your
own build.

%prep
%oreon_verify_sources
%autosetup -p1

%pom_remove_parent parent
%pom_xpath_inject 'pom:project' '<groupId>org.moditect</groupId>' parent

# Missing dependencies in each submodule of integration tests
%pom_disable_module integrationtest

%pom_remove_plugin com.mycila:license-maven-plugin parent
%pom_remove_plugin -r :maven-shade-plugin

%pom_remove_dep -r com.google.testing.compile:compile-testing
rm core/src/test/java/org/moditect/test/AddModuleInfoTest.java
# Test fails with early-access versions of Java
rm core/src/test/java/org/moditect/internal/parser/JavaVersionHelperTest.java

%build
%mvn_build -j -- -Dproject.build.sourceEncoding=UTF-8

%install
%mvn_install

%files -f .mfiles
%license LICENSE.txt
%doc README.md

%changelog
* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 1.1.0-1
- Prepare for Oreon 11 (RP1)
