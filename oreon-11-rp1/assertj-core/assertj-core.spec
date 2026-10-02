%global source0_hash 61c6b1871b10cd7c2d768a58f3853cb78ae0be586824ef47a1db174f44a0c3e1

%bcond_with bootstrap

Name:           assertj-core
Version:        3.27.7
Release:        %autorelease
Summary:        Library of assertions similar to fest-assert
License:        Apache-2.0
URL:            https://joel-costigliola.github.io/assertj/
BuildArch:      noarch
ExclusiveArch:  %{java_arches} noarch

Source0:        https://github.com/joel-costigliola/assertj-core/archive/assertj-build-%{version}.tar.gz#/assertj-core-%{version}.tar.gz

%if %{with bootstrap}
BuildRequires:  javapackages-bootstrap
%else
BuildRequires:  maven-local-openjdk25
BuildRequires:  mvn(junit:junit)
BuildRequires:  mvn(net.bytebuddy:byte-buddy)
BuildRequires:  mvn(org.hamcrest:hamcrest)
BuildRequires:  mvn(org.junit.jupiter:junit-jupiter-api)
BuildRequires:  mvn(org.opentest4j:opentest4j)
%endif
# TODO Remove in Fedora 46
Obsoletes:      %{name}-javadoc < 3.27.7-8

%description
A rich and intuitive set of strongly-typed assertions to use for unit testing
(either with JUnit or TestNG).

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%autosetup -p1 -n assertj-assertj-build-%{version}

%pom_remove_plugin -r :license-maven-plugin
%pom_remove_plugin -r :flatten-maven-plugin
%pom_remove_dep -r :mockito-bom
%pom_remove_dep -r :junit-bom

%pom_disable_module assertj-core-kotlin assertj-tests/assertj-integration-tests
%pom_disable_module assertj-core-groovy assertj-tests/assertj-integration-tests

%pom_xpath_inject pom:plugins '
<plugin>
  <groupId>org.apache.maven.plugins</groupId>
  <artifactId>maven-jar-plugin</artifactId>
  <version>any</version>
  <configuration>
    <archive>
      <manifestEntries>
        <Multi-Release>true</Multi-Release>
      </manifestEntries>
    </archive>
  </configuration>
</plugin>' assertj-core

%build
%mvn_build -j -f -- -Dproject.build.sourceEncoding=UTF-8

%install
%mvn_install

%files -f .mfiles
%doc README.md CONTRIBUTING.md
%license LICENSE.txt

%changelog
%autochangelog
