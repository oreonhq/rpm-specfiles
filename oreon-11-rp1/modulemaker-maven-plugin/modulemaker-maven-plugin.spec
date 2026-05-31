%global source0_hash 62f6bbef4fb7c0084d455a582016b11ab839996537706c98c44367911fc56d4e

%bcond_with bootstrap

Name:           modulemaker-maven-plugin
Version:        1.11
Release:        %autorelease
Summary:        A plugin for creating module-info.class files
License:        Apache-2.0
URL:            https://github.com/raphw/modulemaker-maven-plugin
BuildArch:      noarch
ExclusiveArch:  %{java_arches} noarch

Source0:        https://github.com/raphw/modulemaker-maven-plugin/archive/refs/tags/modulemaker-maven-plugin-%{version}.tar.gz
Source1:        https://www.apache.org/licenses/LICENSE-2.0.txt

%if %{with bootstrap}
BuildRequires:  javapackages-bootstrap
%else
BuildRequires:  maven-local-openjdk25
BuildRequires:  mvn(org.apache.maven.plugin-tools:maven-plugin-annotations)
BuildRequires:  mvn(org.apache.maven.plugins:maven-plugin-plugin)
BuildRequires:  mvn(org.apache.maven.plugins:maven-source-plugin)
BuildRequires:  mvn(org.apache.maven:maven-core)
BuildRequires:  mvn(org.apache.maven:maven-plugin-api)
BuildRequires:  mvn(org.ow2.asm:asm)
BuildRequires:  mvn(org.ow2.asm:asm-commons)
%endif
# TODO Remove in Fedora 46
Obsoletes:      %{name}-javadoc < 1.11-10

%description
This plugin allows the creation of a module-info.class for projects on Java 6
to Java 8 where a module-info.java file cannot be compiled.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%autosetup -p1

cp -p %{SOURCE1} .

%pom_xpath_inject 'pom:dependency[pom:artifactId="maven-plugin-api"]' '<scope>provided</scope>'

%build
%mvn_build -j -- -Dmaven.compiler.source=1.8 -Dmaven.compiler.target=1.8

%install
%mvn_install

%files -f .mfiles
%doc README.md
%license LICENSE-2.0.txt

%changelog
* Mon May 25 2026 Oreon Packaging Team <packaging@oreonhq.com> - 1.11-1
- Import
