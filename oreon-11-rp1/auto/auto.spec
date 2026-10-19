%global source0_hash 5a34ea7fb81838c34ef4a9eab26a22f43afbb1e939b3cde7dedd3bf5171bdfb2
Name:           auto
Summary:        Collection of source code generators for Java
Version:        1.11.1
Release:        1%{?dist}
License:        Apache-2.0
URL:            https://github.com/google/auto
Source0:        https://github.com/google/auto/archive/refs/tags/auto-value-%{version}.tar.gz#/auto-value-%{version}.tar.gz
BuildArch:      noarch
ExclusiveArch:  %{java_arches} noarch
# oreon:deps
BuildRequires:  maven-local-openjdk25
BuildRequires:  mvn(com.squareup:javapoet)
BuildRequires:  mvn(org.apache.maven.plugins:maven-invoker-plugin)
# /oreon:deps
%description
The Auto sub-projects are a collection of code generators
that automate those types of tasks.

%package common
Summary:        Auto Common Utilities
Obsoletes:      %{name}-factory < %{version}-%{release}
%description common
Common utilities for creating annotation processors.

%package service
Summary:        Provider-configuration files for ServiceLoader
%description service
A configuration/meta-data generator for
java.util.ServiceLoader-style service
providers.

%package value
Summary:        Auto Value
%description value
Immutable value-type code generation for Java 1.6+.

%package value-annotations
Summary:        Auto Value Annotations
%description value-annotations
Immutable value-type code generation for Java 1.6+.

%package value-parent
Summary:        Auto Value Parent
%description value-parent
Immutable value-type code generation for Java 1.6+.

%package javadoc
Summary:        Javadoc for %{name}
%description javadoc
This package contains javadoc for %{name}.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f"  | cut -d' ' -f1); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%setup -q -n auto-auto-value-%{version}
find -name '*.class' -print -delete
find -name '*.jar' -print -delete

# remove unnecessary dependency on parent POM
%pom_remove_parent
%pom_remove_parent common
%pom_remove_parent service
%pom_remove_parent value
test -f value-parent/pom.xml && %pom_remove_parent value-parent || :

# Disable factory module due to missing dep:
# com.google.googlejavaformat:google-java-format
%pom_disable_module factory build-pom.xml
# Missing dep on com.google.gwt:gwt
%pom_disable_module src/it/functional value/pom.xml
%pom_disable_module src/it/gwtserializer value/pom.xml

# Fix deps in service module (parent already stripped above)
%pom_change_dep com.google.auto:auto-common com.google.auto:auto-common:0.10 service
%pom_remove_plugin org.apache.maven.plugins:maven-checkstyle-plugin
%pom_remove_plugin :maven-shade-plugin
%pom_remove_plugin :maven-shade-plugin value/processor

%mvn_package :build-only __noinstall

%build

%mvn_build -sf -- -f build-pom.xml
%install
%mvn_install
%oreon_autofiles auto-common usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles auto-service usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles auto-value usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles auto-value-annotations usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles auto-value-parent usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles auto-javadoc usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%files -f %{oreon_filedir}/main.list
%files -n auto-common -f %{oreon_filedir}/auto-common.list
%files -n auto-service -f %{oreon_filedir}/auto-service.list
%files -n auto-value -f %{oreon_filedir}/auto-value.list
%files -n auto-value-annotations -f %{oreon_filedir}/auto-value-annotations.list
%files -n auto-value-parent -f %{oreon_filedir}/auto-value-parent.list
%files -n auto-javadoc -f %{oreon_filedir}/auto-javadoc.list

%changelog

* Mon May 25 2026 Oreon Packaging Team <packaging@oreonhq.com> - 1.6.1-17
- Import
