%global source0_hash 657c58da899ff5f0391468004c8e5013c92333b1703934dee52c3155909252ed
%global srcname jax-ws-api
Name:           jakarta-xml-ws
Version:        4.0.3
Release:        1%{?dist}
Summary:        Jakarta XML Web Services API
License:        LicenseRef-Callaway-BSD
URL:            https://github.com/eclipse-ee4j/jax-ws-api
Source0:        https://github.com/eclipse-ee4j/%{srcname}/archive/%{version}/%{srcname}-%{version}.tar.gz
BuildArch:      noarch
ExclusiveArch:  %{java_arches} noarch
# oreon:deps
BuildRequires:  maven-local-openjdk25
BuildRequires:  mvn(jakarta.xml.bind:jakarta.xml.bind-api)
BuildRequires:  mvn(jakarta.xml.soap:jakarta.xml.soap-api)
BuildRequires:  mvn(org.apache.felix:maven-bundle-plugin)
BuildRequires:  mvn(org.codehaus.mojo:build-helper-maven-plugin)
BuildRequires:  mvn(org.glassfish.build:spec-version-maven-plugin)
# /oreon:deps
%description
Jakarta XML Web Services defines a means for implementing XML-Based Web
Services based on Jakarta SOAP with Attachments and Jakarta Web Services
Metadata.

%package javadoc
Summary:        Javadocs for %{name}
%description javadoc
This package contains the API documentation for %{name}.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n %{srcname}-%{version}

cd api
# remove unnecessary dependency on parent POM
  %pom_remove_parent
# remove unnecessary maven plugin
  %pom_remove_plugin :glassfish-copyright-maven-plugin
  %pom_remove_plugin :buildnumber-maven-plugin
cd -

%build

cd api
  %mvn_build
cd -
%install
cd api
  %mvn_install
cd -
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%files -f %{oreon_filedir}/main.list
%files -n jakarta-xml-ws-javadoc -f %{oreon_filedir}/jakarta-xml-ws-javadoc.list

%changelog

%autochangelog
