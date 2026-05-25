%bcond_with     groovy
Name:           maven-script-interpreter
Version:        1.3
Release:        15%{?dist}
Summary:        Maven Script Interpreter
# Automatically converted from old format: ASL 2.0 - review is highly recommended.
License:        Apache-2.0
URL:            https://maven.apache.org/shared/maven-script-interpreter/
Source0:        https://dlcdn.apache.org/maven/shared/%{name}-%{version}-source-release.zip


BuildArch:      noarch
ExclusiveArch:  %{java_arches} noarch

BuildRequires:  maven-local-openjdk25
BuildRequires:  mvn(junit:junit)
BuildRequires:  mvn(org.apache.ant:ant)
BuildRequires:  mvn(org.apache.maven:maven-plugin-api)
BuildRequires:  mvn(org.apache.maven.shared:maven-shared-components:pom:)
BuildRequires:  mvn(org.apache.maven.shared:maven-shared-utils)
BuildRequires:  mvn(org.beanshell:bsh)
%if %{with groovy}
BuildRequires:  mvn(org.codehaus.groovy:groovy)
%endif
BuildRequires:  mvn(org.codehaus.plexus:plexus-component-annotations)
BuildRequires:  mvn(org.codehaus.plexus:plexus-component-metadata)


%description
This component provides some utilities to interpret/execute some scripts for
various implementations: Groovy or BeanShell.


%package javadoc
Summary:        Javadoc for %{name}

%description javadoc
API documentation for %{name}.


%prep
%setup -q

%if %{without groovy}
%pom_remove_dep :groovy
rm src/main/java/org/apache/maven/shared/scriptinterpreter/GroovyScriptInterpreter.java
rm src/test/java/org/apache/maven/shared/scriptinterpreter/GroovyScriptInterpreterTest.java
rm src/test/java/org/apache/maven/shared/scriptinterpreter/ScriptRunnerTest.java
sed -i /GroovyScriptInterpreter/d src/main/java/org/apache/maven/shared/scriptinterpreter/ScriptRunner.java
%endif

%pom_xpath_set "pom:project/pom:properties/pom:javaVersion" "8" pom.xml

%build
%mvn_build

%install
%mvn_install

%files -f .mfiles
%doc DEPENDENCIES LICENSE NOTICE

%files javadoc -f .mfiles-javadoc
%doc LICENSE NOTICE


%changelog
* Mon May 25 2026 Oreon Packaging Team <packaging@oreonhq.com> - 1.3-15
- Import
