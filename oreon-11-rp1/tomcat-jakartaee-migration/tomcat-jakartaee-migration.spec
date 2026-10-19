%global source0_hash 9eb8bf44515ee8168e3a07a9194fb1ebba6ffe4364a7b338b39a4c3779669380
Name:           tomcat-jakartaee-migration
Version:        1.0.9
Release:        1%{?dist}
Summary:        Tomcat Migration Tool for Jakarta EE
License:        Apache-2.0
URL:            http://tomcat.apache.org/
Source0:        https://archive.apache.org/dist/tomcat/jakartaee-migration/v%{version}/source/jakartaee-migration-%{version}-src.tar.gz
Source1:        javax2jakarta
Patch0:         tomcat-jakartaee-migration-1.0.9-no-manifest-classpath.patch
BuildArch:      noarch
ExclusiveArch:  %{java_arches} noarch
# oreon:deps
BuildRequires:  ant-openjdk25
BuildRequires:  apache-commons-compress
BuildRequires:  apache-commons-io
BuildRequires:  bcel
BuildRequires:  java-25-devel
BuildRequires:  maven-local-openjdk25
BuildRequires:  mvn(junit:junit)
BuildRequires:  mvn(org.apache.maven.plugins:maven-antrun-plugin)
BuildRequires:  mvn(org.apache.maven.plugins:maven-assembly-plugin)
BuildRequires:  mvn(org.apache.maven.plugins:maven-jar-plugin)
BuildRequires:  mvn(org.apache.maven.plugins:maven-shade-plugin)
BuildRequires:  mvn(org.apache.maven.plugins:maven-source-plugin)
BuildRequires:  mvn(org.apache:apache:pom:)
# /oreon:deps
%description
The purpose of the tool is to take a web application written for Java EE 8 that runs on Apache Tomcat 9 and convert it automatically so it runs on Apache Tomcat 10 which implements Jakarta EE 9.

%package javadoc
Summary:        Javadoc for %{name}
%description javadoc
API documentation for %{name}.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%setup -q -n jakartaee-migration-%{version}
%patch 0 -p0
%pom_remove_plugin :maven-javadoc-plugin
%pom_remove_plugin org.jacoco:jacoco-maven-plugin

%build

%mvn_build 
%install
%mvn_install
%{__install} -d -m 0755 ${RPM_BUILD_ROOT}%{_bindir}
%{__install} -m 0755 %{SOURCE1} ${RPM_BUILD_ROOT}%{_bindir}
%{__install} -d -m 0755 ${RPM_BUILD_ROOT}%{_datarootdir}/licenses/%{name}-javadoc
%{__mv} ${RPM_BUILD_ROOT}%{_javadocdir}/%{name}/legal/ADDITIONAL_LICENSE_INFO ${RPM_BUILD_ROOT}%{_datarootdir}/licenses/%{name}-javadoc/
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%files -f %{oreon_filedir}/main.list
%files -n tomcat-jakartaee-migration-javadoc -f %{oreon_filedir}/tomcat-jakartaee-migration-javadoc.list

%changelog

* Mon May 25 2026 Oreon Packaging Team <packaging@oreonhq.com> - 1.0.9-9
- Import
