%global source0_hash d92a5e1d9baacc9e363c24b9398a7fe67531bf04e6d6f01aadea09afefd40d7f

%global srcname jax-ws-api

Name:           jakarta-xml-ws
Version:        4.0.0
Release:        12%{?dist}
Summary:        Jakarta XML Web Services API
# spec and enterprise-ws-spec is under EPL-2.0 but it is not shipped
# Automatically converted from old format: BSD - review is highly recommended.
License:        LicenseRef-Callaway-BSD

URL:            https://github.com/eclipse-ee4j/jax-ws-api
Source0:        %{url}/archive/%{version}/%{srcname}-%{version}.tar.gz

BuildArch:      noarch
ExclusiveArch:  %{java_arches} noarch

BuildRequires:  maven-local-openjdk25
BuildRequires:  mvn(jakarta.xml.bind:jakarta.xml.bind-api)
BuildRequires:  mvn(jakarta.xml.soap:jakarta.xml.soap-api)
BuildRequires:  mvn(org.apache.felix:maven-bundle-plugin)
BuildRequires:  mvn(org.codehaus.mojo:build-helper-maven-plugin)
BuildRequires:  mvn(org.glassfish.build:spec-version-maven-plugin)

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

%files -f api/.mfiles
%license LICENSE.md NOTICE.md

%files javadoc -f api/.mfiles-javadoc

%changelog
%autochangelog
