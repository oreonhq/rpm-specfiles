%global source0_hash 3931e47ed51f592919f205ef0a9a046b6c606283d7da0bc155230bc3250456e8

%global srcname saaj-api

Name:           jakarta-saaj
Version:        3.0.2
Release:        7%{?dist}
Summary:        SOAP with Attachments API for Java
# Automatically converted from old format: BSD - review is highly recommended.
License:        LicenseRef-Callaway-BSD
URL:            https://github.com/eclipse-ee4j/saaj-api
BuildArch:      noarch
ExclusiveArch:  %{java_arches} noarch

Source0:        %{url}/archive/%{version}/%{srcname}-%{version}.tar.gz

BuildRequires:  maven-local-openjdk25
BuildRequires:  mvn(jakarta.activation:jakarta.activation-api)
BuildRequires:  mvn(org.apache.felix:maven-bundle-plugin)
BuildRequires:  mvn(org.apache.maven.plugins:maven-enforcer-plugin)
BuildRequires:  mvn(org.codehaus.mojo:build-helper-maven-plugin)
BuildRequires:  mvn(org.glassfish.build:spec-version-maven-plugin)

%description
Jakarta SOAP with Attachments defines an API enabling developers to
produce and consume messages conforming to the SOAP 1.1, SOAP 1.2, and
SOAP Attachments Feature.

%package javadoc
Summary:        API documentation for %{name}
%description javadoc
API documentation for %{name}.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n %{srcname}-%{version} -p1

pushd api
# remove unnecessary dependency on parent POM
%pom_remove_parent
# remove unnecessary maven plugins
%pom_remove_plugin :glassfish-copyright-maven-plugin
%pom_remove_plugin :spotbugs-maven-plugin
%pom_remove_plugin :buildnumber-maven-plugin
# add compatibility alias for old maven artifact coordinates
%mvn_alias jakarta.xml.soap:jakarta.xml.soap-api javax.xml.soap:saaj-api
# add compatibility symlink for old classpath
%mvn_file : %{name}/jakarta.xml.soap-api geronimo-saaj
popd

%build
pushd api
# - skip tests because metro-saaj is not packaged for fedora yet:
#   https://github.com/eclipse-ee4j/metro-saaj
%mvn_build -f
popd

%install
pushd api
%mvn_install
popd

%files -f api/.mfiles
%license LICENSE.md NOTICE.md
%doc README.md

%files javadoc -f api/.mfiles-javadoc
%license LICENSE.md NOTICE.md

%changelog
%autochangelog
