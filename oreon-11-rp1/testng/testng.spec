%global source0_hash 4aeb00ab2a24fc3fd61c70a585142e2a681e10398e4894f76dc5854e227c2639

%bcond_with bootstrap

Name:           testng
Version:        7.8.0
Release:        %autorelease
Summary:        Java-based testing framework
License:        Apache-2.0
URL:            https://testng.org/doc/
BuildArch:      noarch
ExclusiveArch:  %{java_arches} noarch

# ./generate-tarball.sh
Source0:        %{name}-%{version}.tar.gz
# Allows building with maven instead of gradle
Source1:        https://repo1.maven.org/maven2/org/testng/testng/%{version}/testng-%{version}.pom
# Remove bundled binaries to make sure we don't ship anything forbidden
Source2:        generate-tarball.sh

Patch:          0001-Avoid-accidental-javascript-in-javadoc.patch
Patch:          0002-Replace-bundled-jquery-with-CDN-link.patch

%if %{with bootstrap}
BuildRequires:  javapackages-bootstrap
%else
BuildRequires:  maven-local-openjdk25
BuildRequires:  mvn(com.beust:jcommander)
BuildRequires:  mvn(com.google.code.findbugs:jsr305)
BuildRequires:  mvn(com.google.inject:guice)
BuildRequires:  mvn(junit:junit)
BuildRequires:  mvn(org.apache.ant:ant)
BuildRequires:  mvn(org.apache.felix:maven-bundle-plugin)
%endif
# TODO Remove in Fedora 46
Obsoletes:      %{name}-javadoc < 7.8.0-20

%description
TestNG is a testing framework inspired from JUnit and NUnit but introducing
some new functionality, including flexible test configuration, and
distributed test running.  It is designed to cover unit tests as well as
functional, end-to-end, integration, etc.

%prep
%(test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; })
%autosetup -p1

cp %{SOURCE1} pom.xml


# Contains differently licensed sources
rm -r testng-test-osgi

find . -mindepth 2 -name 'src' -type d -exec cp -r -t . {} +

# remove any bundled libs, but not test resources
find ! -path '*/test/*' -name '*.jar' -print -delete
find -name '*.class' -delete

%pom_remove_dep org.webjars:jquery

%pom_remove_dep org.yaml:snakeyaml
rm src/main/java/org/testng/internal/Yaml*.java
rm src/main/java/org/testng/Converter.java

cp -p ./src/main/java/*.dtd.html ./src/main/resources/.

%mvn_file : %{name}
# jdk15 classifier is used by some other packages
%mvn_alias : :::jdk15:

%build
# Tests extend a class written in Kotlin
%mvn_build -j -f -- -Dmaven.compiler.release=11

%install
%mvn_install

%files -f .mfiles
%doc CHANGES.txt README.md
%license LICENSE.txt

%changelog
* Mon May 25 2026 Oreon Packaging Team <packaging@oreonhq.com> - 7.8.0-1
- Import
