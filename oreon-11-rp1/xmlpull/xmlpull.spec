%global source0_hash 8066668687f3a9160caa5b6a2bbb37a046fe7eef3054f5e79378fe25e00dcfd4

Name:           xmlpull
Version:        1.2.0
Release:        14%{?dist}
Summary:        XML Pull Parsing API

# Automatically converted from old format: Public Domain - needs further work
License:        LicenseRef-Callaway-Public-Domain
URL:            https://github.com/xmlpull-xpp3/%{name}-xpp3
Source0:        %{url}/archive/%{name}-xpp3-parent-%{version}.tar.gz
BuildArch:      noarch
ExclusiveArch:  %{java_arches} noarch

BuildRequires:  maven-local-openjdk25
BuildRequires:  mvn(org.apache.felix:maven-bundle-plugin)
BuildRequires:  mvn(org.apache.maven.plugins:maven-enforcer-plugin)
BuildRequires:  mvn(org.apache.maven.plugins:maven-source-plugin)
BuildRequires:  mvn(junit:junit)

%description
XmlPull v1 API is a simple to use XML pull parsing API that was
designed for simplicity and very good performance both in constrained
environment such as defined by J2ME and on server side when used in
J2EE application servers.

%javadoc_package

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n %{name}-xpp3-%{name}-xpp3-parent-%{version}

find \( -name \*.jar -o -name \*.class \) -delete

%pom_disable_module xpp3_min

# using java 8, we need to remove the java module
rm xmlpull/src/main/java/module-info.java

%mvn_package :%{name}-xpp3-parent __noinstall

%build
%mvn_build -- -Dmaven.compiler.source=1.8 -Dmaven.compiler.target=1.8

%install
%mvn_install

%files -f .mfiles
%license %{name}/LICENSE.txt
%doc %{name}/README.adoc

%changelog
%autochangelog
