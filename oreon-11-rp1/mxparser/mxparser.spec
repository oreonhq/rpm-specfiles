%global source0_hash 65ff0685a991ee8c1ffe36da0afdf767e607b20cccdf36825b1231751b80dfc0
Name:           mxparser
Version:        1.2.3
Release:        1%{?dist}
Summary:        Parser of xpp3_min 1.1.7 with merged changes of the Plexus fork
License:        xpp
URL:            https://github.com/x-stream/%{name}
BuildArch:      noarch
ExclusiveArch:  %{java_arches} noarch
Source0:        https://github.com/x-stream/%{name}/archive/v-%{version}/%{name}-%{version}.tar.gz
# oreon:deps
BuildRequires:  maven-local-openjdk25
BuildRequires:  mvn(junit:junit)
BuildRequires:  mvn(org.apache.felix:maven-bundle-plugin)
BuildRequires:  mvn(org.apache.maven.plugins:maven-antrun-plugin)
BuildRequires:  mvn(org.codehaus.mojo:build-helper-maven-plugin)
BuildRequires:  mvn(xmlpull:xmlpull)
# /oreon:deps
%description
MXParser is a fork of xpp3_min 1.1.7 containing only the parser with merged
changes of the Plexus fork. It is an implementation of the XMLPULL V1 API
(parser only).

%{?javadoc_package}

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n %{name}-v-%{version}

%pom_remove_plugin :maven-changes-plugin .
%pom_remove_plugin :maven-javadoc-plugin .
%pom_remove_plugin :maven-source-plugin .

%pom_xpath_set 'pom:project/pom:properties/pom:version.java.source' 1.8
%pom_xpath_set 'pom:project/pom:properties/pom:version.java.target' 1.8
%pom_xpath_set 'pom:project/pom:properties/pom:version.java.test.source' 1.8
%pom_xpath_set 'pom:project/pom:properties/pom:version.java.test.target' 1.8

%build

%mvn_build -- -Dmaven.compiler.source=1.8 -Dmaven.compiler.target=1.8
%install
%mvn_install
%oreon_autofiles main

%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
