%global source0_hash none

%bcond_with bootstrap
%global upstream_version %(echo %{version} | tr '~' '-')

Name:           hamcrest
Version:        3.0
Release:        %autorelease
Summary:        Library of matchers for building test expressions
License:        BSD-3-Clause
URL:            https://github.com/hamcrest/JavaHamcrest
BuildArch:      noarch
ExclusiveArch:  %{java_arches} noarch

Source0:        https://github.com/hamcrest/JavaHamcrest/archive/v%{version}.tar.gz#/hamcrest-%{version}.tar.gz
Source1:        https://repo1.maven.org/maven2/org/hamcrest/hamcrest/%{version}/hamcrest-%{version}.pom

%if %{with bootstrap}
BuildRequires:  javapackages-bootstrap
%else
BuildRequires:  maven-local-openjdk25
BuildRequires:  mvn(junit:junit)
%endif
# TODO Remove in Fedora 46
Obsoletes:      %{name}-javadoc < 3.0-7

%description
Provides a library of matcher objects (also known as constraints or predicates)
allowing 'match' rules to be defined declaratively, to be used in other
frameworks. Typical scenarios include testing frameworks, mocking libraries and
UI validation rules.

%prep
%(test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; })
%autosetup -p1

pushd hamcrest
cp -p %{SOURCE1} pom.xml
%pom_add_dep junit:junit::test
%pom_xpath_inject pom:project '
<build>
  <plugins>
    <plugin>
      <groupId>org.apache.maven.plugins</groupId>
      <artifactId>maven-compiler-plugin</artifactId>
      <version>any</version>
      <configuration>
        <source>1.8</source>
        <target>1.8</target>
      </configuration>
    </plugin>
    <plugin>
      <groupId>org.apache.maven.plugins</groupId>
      <artifactId>maven-jar-plugin</artifactId>
      <version>any</version>
      <configuration>
        <archive>
          <manifestEntries>
            <Automatic-Module-Name>org.hamcrest</Automatic-Module-Name>
          </manifestEntries>
        </archive>
      </configuration>
    </plugin>
  </plugins>
</build>'

%mvn_alias org.hamcrest:hamcrest org.hamcrest:hamcrest-all
%mvn_alias org.hamcrest:hamcrest org.hamcrest:hamcrest-core
%mvn_alias org.hamcrest:hamcrest org.hamcrest:hamcrest-library

%build
pushd hamcrest
%mvn_build -j
popd

%install
pushd hamcrest
%mvn_install
popd

%files -f hamcrest/.mfiles
%doc README.md
%license LICENSE

%changelog
* Mon May 25 2026 Oreon Packaging Team <packaging@oreonhq.com> - 3.0-1
- Import
