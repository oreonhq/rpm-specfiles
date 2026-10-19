%global source0_hash 16d8be64fed9932f0438c05e6ad2ff733da10542577a7f6ec6e13c4f81dbdb0e
%global namedreltag .Final
%global namedversion %{version}%{?namedreltag}
%global alphatag r12
Name:          scannotation
Version:       1.0.3
Release:        1%{?dist}
Summary:        A Java annotation scanner
License:       Apache-2.0
URL:           http://scannotation.sourceforge.net
Source0:        %{name}-%{version}%{namedreltag}.tar.xz
Source1:       License.txt
BuildArch:     noarch
ExclusiveArch:  %{java_arches} noarch
# oreon:deps
BuildRequires:  maven-local-openjdk25
BuildRequires:  mvn(javassist:javassist)
BuildRequires:  mvn(javax.servlet:javax.servlet-api)
BuildRequires:  mvn(junit:junit)
# /oreon:deps
%description
Scannotation is a Java library that creates an annotation database 
from a set of .class files.This database is really just a set of maps that index
what annotations are used and what classes are using them. Why do you need this? 
What if you are an annotation framework like an EJB 3.0 container and you want 
to automatically scan your classpath for EJB annotations so that you know what 
to deploy? Scannotation gives you apis that allow you to find archives in your 
classpath or WAR (web application) that you want to scan, then automatically 
scans them without loading each and every class within those archives

%package javadoc
Summary:       Javadoc for %{name}
%description javadoc
This package contains the API documentation for %{name}.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n %{name}-%{namedversion}

%pom_disable_module titan-test-jar
%pom_remove_dep :titan-cruise %{name}

# Force use servlet 3.1 apis
%pom_change_dep :servlet-api javax.servlet:javax.servlet-api:3.1.0 %{name}

# remove maven-compiler-plugin configurations that are broken with Java 11
%pom_xpath_remove -r 'pom:plugin[pom:artifactId="maven-compiler-plugin"]/pom:configuration'

cp -p %SOURCE1 .

%mvn_file org.%{name}:%{name} %{name}

%build

%mvn_build -- -Dproject.build.sourceEncoding=UTF-8 -Dmaven.compiler.source=1.8 -Dmaven.compiler.target=1.8
%install
%mvn_install
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%files -f %{oreon_filedir}/main.list
%files -n scannotation-javadoc -f %{oreon_filedir}/scannotation-javadoc.list

%changelog

%autochangelog
