%global source0_hash 004651c18aef50c9f7ebde3c399da168ec465b04f3515fe6c3ebe0a321678518
%bcond_with     groovy
Name:           maven-script-interpreter
Version:        1.9
Release:        1%{?dist}
Summary:        Maven Script Interpreter
License:        Apache-2.0
URL:            https://maven.apache.org/shared/maven-script-interpreter/
Source0:        https://archive.apache.org/dist/maven/shared/%{name}-%{version}-source-release.zip
BuildArch:      noarch
ExclusiveArch:  %{java_arches} noarch
%if %{with groovy}
%endif
# oreon:deps
BuildRequires:  maven-local-openjdk25
BuildRequires:  mvn(junit:junit)
BuildRequires:  mvn(org.apache.ant:ant)
BuildRequires:  mvn(org.apache.maven.shared:maven-shared-components:pom:)
BuildRequires:  mvn(org.apache.maven.shared:maven-shared-utils)
BuildRequires:  mvn(org.apache.maven:maven-plugin-api)
BuildRequires:  mvn(org.beanshell:bsh)
BuildRequires:  mvn(org.codehaus.plexus:plexus-component-annotations)
BuildRequires:  mvn(org.codehaus.plexus:plexus-component-metadata)
# /oreon:deps
%description
This component provides some utilities to interpret/execute some scripts for
various implementations: Groovy or BeanShell.

%package javadoc
Summary:        Javadoc for %{name}
%description javadoc
API documentation for %{name}.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%setup -q

%if %{without groovy}
%pom_remove_dep :groovy
rm src/main/java/org/apache/maven/shared/scriptinterpreter/GroovyScriptInterpreter.java
rm src/test/java/org/apache/maven/shared/scriptinterpreter/GroovyScriptInterpreterTest.java
rm src/test/java/org/apache/maven/shared/scriptinterpreter/ScriptRunnerTest.java
sed -i /GroovyScriptInterpreter/d src/main/java/org/apache/maven/shared/scriptinterpreter/ScriptRunner.java
%endif

%build

%mvn_build
%install
%mvn_install
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%files -f %{oreon_filedir}/main.list
%files -n maven-script-interpreter-javadoc -f %{oreon_filedir}/maven-script-interpreter-javadoc.list

%changelog

%autochangelog
