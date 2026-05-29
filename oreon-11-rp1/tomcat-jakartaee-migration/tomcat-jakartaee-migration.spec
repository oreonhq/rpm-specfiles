%global source0_hash none

Name:           tomcat-jakartaee-migration
Version:        1.0.9
Release:        9%{?dist}
Summary:        Tomcat Migration Tool for Jakarta EE

License:        Apache-2.0
URL:            http://tomcat.apache.org/
Source0:        http://www.apache.org/dist/tomcat/jakartaee-migration/v1.0.9/source/jakartaee-migration-1.0.9-src.tar.gz
Source1:        javax2jakarta
# Do not generate manifest Class-Path, we rely on system-installed JARs
Patch0:         tomcat-jakartaee-migration-1.0.9-no-manifest-classpath.patch

BuildArch:      noarch
ExclusiveArch:  %{java_arches} noarch

BuildRequires:  bcel
BuildRequires:  apache-commons-compress
BuildRequires:  apache-commons-io
BuildRequires:  ant-openjdk25 
BuildRequires:  java-25-devel
	
BuildRequires:  maven-local-openjdk25
BuildRequires:  mvn(junit:junit)
BuildRequires:  mvn(org.apache:apache:pom:)
BuildRequires:  mvn(org.apache.maven.plugins:maven-antrun-plugin)
BuildRequires:  mvn(org.apache.maven.plugins:maven-shade-plugin)
BuildRequires:  mvn(org.apache.maven.plugins:maven-assembly-plugin) 
BuildRequires:  mvn(org.apache.maven.plugins:maven-jar-plugin) 
BuildRequires:  mvn(org.apache.maven.plugins:maven-source-plugin) 

%description
The purpose of the tool is to take a web application written for Java EE 8 that runs on Apache Tomcat 9 and convert it automatically so it runs on Apache Tomcat 10 which implements Jakarta EE 9.

%package javadoc
Summary:        Javadoc for %{name}
 
%description javadoc
API documentation for %{name}.

%prep
%(test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; })
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

%files -f .mfiles
%license LICENSE.txt
%doc CHANGES.md README.md
%{_bindir}/javax2jakarta
 
%files javadoc -f .mfiles-javadoc
%{_datarootdir}/licenses/%{name}-javadoc/ADDITIONAL_LICENSE_INFO
%license LICENSE.txt

%changelog
* Mon May 25 2026 Oreon Packaging Team <packaging@oreonhq.com> - 1.0.9-9
- Import
