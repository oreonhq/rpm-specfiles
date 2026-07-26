%global source0_hash 13a1ceef025d430b47ae76f3271d4a36bfa6304949331711fd36f9d9a95049ed

Name:          reflections
Version:       0.9.12
Release:       22%{?dist}
Summary:       Java run-time meta-data analysis
License:       WTFPL
URL:           https://github.com/ronmamo/reflections
BuildArch:     noarch
ExclusiveArch:  %{java_arches} noarch

Source0:       %{url}/archive/%{version}/%{name}-%{version}.tar.gz

BuildRequires:  maven-local-openjdk25
BuildRequires:  mvn(com.google.code.gson:gson)
BuildRequires:  mvn(javax.servlet:javax.servlet-api)
BuildRequires:  mvn(junit:junit)
BuildRequires:  mvn(org.dom4j:dom4j)
BuildRequires:  mvn(org.javassist:javassist)

%description
A Java run-time meta-data analysis, in the spirit of Scannotations

Reflections scans your class-path, indexes the meta-data, allows you
to query it on run-time and may save and collect that information
for many modules within your project.

Using Reflections you can query your meta-data such as:
* get all sub types of some type
* get all types/methods/fields annotated with some annotation,
  w/o annotation parameters matching
* get all resources matching matching a regular expression

%{?javadoc_package}

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup

find -type f '(' -name '*.jar' -o -name '*.class' ')' -not -path './src/test/*' -print -delete

%pom_xpath_inject 'pom:plugin[pom:artifactId = "maven-compiler-plugin"]' '<version>3.8.1</version>'

%build
%mvn_build -- -Dmaven.compiler.source=1.8 -Dmaven.compiler.target=1.8 -Dproject.build.sourceEncoding=UTF-8

%install
%mvn_install

%files -f .mfiles
%doc README.md
%license COPYING.txt

%changelog
%autochangelog
