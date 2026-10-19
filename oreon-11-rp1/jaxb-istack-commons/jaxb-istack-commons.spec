%global source0_hash c6d43fff872c91905b237fdc430ee17f5926a6c6375bd425abfbe23b01f727ad
Name:           jaxb-istack-commons
Version:        4.2.0
Release:        1%{?dist}
Summary:        iStack Common Utility Code
License:        BSD-3-Clause
URL:            https://github.com/eclipse-ee4j/jaxb-istack-commons
BuildArch:      noarch
ExclusiveArch:  %{java_arches} noarch
Source0:        https://github.com/eclipse-ee4j/jaxb-istack-commons/archive/refs/tags/4.2.0.tar.gz#/jaxb-istack-commons-4.2.0.tar.gz
# oreon:deps
BuildRequires:  maven-local-openjdk25
BuildRequires:  mvn(jakarta.activation:jakarta.activation-api)
BuildRequires:  mvn(junit:junit)
BuildRequires:  mvn(org.apache.ant:ant)
BuildRequires:  mvn(org.apache.ant:ant-junit)
BuildRequires:  mvn(org.apache.felix:maven-bundle-plugin)
BuildRequires:  mvn(org.apache.maven.plugins:maven-assembly-plugin)
BuildRequires:  mvn(org.apache.maven.plugins:maven-dependency-plugin)
BuildRequires:  mvn(org.apache.maven.plugins:maven-plugin-plugin)
BuildRequires:  mvn(org.glassfish.jaxb:codemodel)
# /oreon:deps
%description
Code shared between JAXP, JAXB, SAAJ, and JAX-WS projects.

%package maven-plugin
Summary:        istack-commons maven-plugin
%description maven-plugin
This package contains istack-commons maven-plugin.

%package runtime
Summary:        istack-commons runtime
%description runtime
This package contains istack-commons runtime.

%package test
Summary:        istack-commons test
%description test
This package contains istack-commons test.

%package tools
Summary:        istack-commons tools
%description tools
This package contains istack-commons tools.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%autosetup -p1

pushd istack-commons

%pom_remove_parent

%pom_remove_plugin :buildnumber-maven-plugin
%pom_remove_plugin :glassfish-copyright-maven-plugin
%pom_remove_plugin :maven-enforcer-plugin
%pom_remove_plugin :maven-javadoc-plugin . test tools
%pom_remove_plugin :maven-source-plugin
%pom_remove_plugin :spotbugs-maven-plugin

# Missing dependency on args4j
%pom_disable_module soimp

%pom_disable_module buildtools
%pom_disable_module import-properties-plugin

%mvn_package :istack-commons __noinstall
popd

%build

pushd istack-commons
%mvn_build -f -s -j
popd
%install
pushd istack-commons
%mvn_install
popd
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%files -f %{oreon_filedir}/main.list
%files -n jaxb-istack-commons-maven-plugin -f %{oreon_filedir}/jaxb-istack-commons-maven-plugin.list
%files -n jaxb-istack-commons-runtime -f %{oreon_filedir}/jaxb-istack-commons-runtime.list
%files -n jaxb-istack-commons-test -f %{oreon_filedir}/jaxb-istack-commons-test.list
%files -n jaxb-istack-commons-tools -f %{oreon_filedir}/jaxb-istack-commons-tools.list

%changelog

* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 4.2.0-1
- Prepare for Oreon 11 (RP1)
