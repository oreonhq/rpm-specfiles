%global source0_hash 582134953ffc75cd517e5f3449e8d2562f31986dd9c6f8c3b3d0af3df17bf4cb

%bcond_with bootstrap

Name:           jakarta-inject1.0
Version:        1.0.5
Release:        %autorelease
Summary:        Jakarta Dependency Injection
License:        Apache-2.0
URL:            https://jakarta.ee/specifications/dependency-injection/1.0/
BuildArch:      noarch
ExclusiveArch:  %{java_arches} noarch

Source0:        https://github.com/jakartaee/inject/archive/%{version}.tar.gz

%if %{with bootstrap}
BuildRequires:  javapackages-bootstrap
%else
BuildRequires:  maven-local-openjdk25
BuildRequires:  mvn(org.apache.felix:maven-bundle-plugin)
%endif
# TODO Remove in Fedora 46
Obsoletes:      %{name}-javadoc < 1.0.5-8
# Remove in Fedora 45
Obsoletes:      atinject < 1.0.5-14
Provides:       atinject = %{version}-%{release}

%description
Jakarta Dependency Injection specifies a means for obtaining objects
in such a way as to maximize reusability, testability and
maintainability compared to traditional approaches such as
constructors, factories, and service locators (e.g., JNDI).
This process, known as dependency injection, is beneficial
to most nontrivial applications.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1 -C

%pom_remove_parent
%pom_xpath_set pom:project/pom:groupId javax.inject
%pom_xpath_set pom:project/pom:artifactId javax.inject
%pom_remove_plugin :maven-javadoc-plugin
%pom_remove_plugin :moditect-maven-plugin

%mvn_file : jakarta-inject1.0 atinject

%build
%mvn_build -j

%install
%mvn_install

%files -f .mfiles
%license LICENSE.txt NOTICE.md

%changelog
%autochangelog
