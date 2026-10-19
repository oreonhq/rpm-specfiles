%global source0_hash 41379b2d5f310e6808ef047101a742a1ad31503bbd78a2fbe9b8ca7cf851f46c
Name:           janino
Version:        3.1.12
Release:        1%{?dist}
Summary:        Super-small, super-fast Java compiler
License:        BSD-3-Clause
URL:            http://janino-compiler.github.io/janino
BuildArch:      noarch
ExclusiveArch:  %{java_arches} noarch
Source0:        https://github.com/janino-compiler/janino/archive/v%{version}/%{name}-%{version}.tar.gz
Requires:       javapackages-tools
Requires:       commons-compiler = %{version}-%{release}
# oreon:deps
BuildRequires:  maven-local-openjdk25
BuildRequires:  mvn(junit:junit)
BuildRequires:  mvn(org.apache.ant:ant)
BuildRequires:  mvn(org.apache.felix:maven-bundle-plugin)
# /oreon:deps
%description
Janino is a super-small, super-fast Java compiler.

The "JANINO" implementation of the "commons-compiler" API: Super-small,
super-fast, independent from the JDK's "tools.jar".

%package -n commons-compiler
Summary:        Commons Compiler
%description -n commons-compiler
The "commons-compiler" API, including the "IExpressionEvaluator",
"IScriptEvaluator", "IClassBodyEvaluator" and "ISimpleCompiler" interfaces.

%package -n commons-compiler-jdk
Summary:        Commons Compiler JDK
%description -n commons-compiler-jdk
The "JDK" implementation of the "commons-compiler" API that uses the
JDK's Java compiler (JAVAC) in "tools.jar".

%package javadoc
Summary:        API documentation for %{name}
%description javadoc
API documentation for %{name}.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup
cd %{name}-parent
# remove maven.compiler.* properties
  %pom_xpath_remove pom:maven.compiler.executable
  %pom_xpath_remove pom:maven.compiler.fork
# remove staging maven plugin
  %pom_remove_plugin :nexus-staging-maven-plugin
# remove jarsigner plugin
  %pom_remove_plugin :maven-jarsigner-plugin
# remove javadoc plugin:
  %pom_remove_plugin :maven-javadoc-plugin
# remove source plugin:
  %pom_remove_plugin :maven-source-plugin
# disable tests module
  %pom_disable_module ../commons-compiler-tests
# don't install parent
  %mvn_package :%{name}-parent __noinstall
cd -

%build

cd %{name}-parent
  %mvn_build -s -f -- -Dmaven.compiler.source=1.8 -Dmaven.compiler.target=1.8
cd -
%install
cd %{name}-parent
  %mvn_install
  %jpackage_script org.codehaus.commons.compiler.samples.CompilerDemo "" "" %{name}/janino:%{name}/commons-compiler janinoc true
cd -
%oreon_autofiles commons-compiler usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles commons-compiler-jdk usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%files -f %{oreon_filedir}/main.list
%files -n commons-compiler -f %{oreon_filedir}/commons-compiler.list
%files -n commons-compiler-jdk -f %{oreon_filedir}/commons-compiler-jdk.list
%files -n janino-javadoc -f %{oreon_filedir}/janino-javadoc.list

%changelog

%autochangelog
