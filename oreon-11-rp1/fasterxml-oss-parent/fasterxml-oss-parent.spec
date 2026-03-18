%global srcname oss-parent

Name:          fasterxml-oss-parent
Version:       62
Release:       6%{?dist}
Summary:       FasterXML parent pom
License:       Apache-2.0

URL:           https://github.com/FasterXML/oss-parent
Source0:       %{url}/archive/%{srcname}-%{version}.tar.gz

%if 0%{?rhel} || 0%{?fedora} && 0%{?fedora} <= 42
BuildRequires: maven-local
%else
BuildRequires: maven-local-openjdk25
%endif

BuildRequires: mvn(org.apache.felix:maven-bundle-plugin)
BuildRequires: mvn(org.codehaus.mojo:build-helper-maven-plugin)

BuildArch:     noarch
%if 0%{?fedora} || 0%{?rhel} >= 10
ExclusiveArch:  %{java_arches} noarch
%endif

%description
FasterXML is the business behind the Woodstox streaming XML parser,
Jackson streaming JSON parser, the Aalto non-blocking XML parser, and
a growing family of utility libraries and extensions.

FasterXML offers consulting services for adoption, performance tuning,
and extension.

This package contains the parent pom file for FasterXML.com projects.

%prep
%setup -q -n %{srcname}-%{srcname}-%{version}

# Stuff unnecessary for RPM builds
%pom_remove_plugin :jacoco-maven-plugin
%pom_remove_plugin :maven-enforcer-plugin
%pom_remove_plugin :maven-javadoc-plugin
%pom_remove_plugin :maven-pmd-plugin
%pom_remove_plugin :maven-scm-plugin
%pom_remove_plugin :maven-site-plugin
%pom_remove_plugin :jdepend-maven-plugin
%pom_xpath_remove "pom:build/pom:extensions"

%build
%mvn_build

%install
%mvn_install

%files -f .mfiles
%doc README.creole
%license LICENSE NOTICE

%changelog
* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 62-6
- Prepare for Oreon 11 (RP1)
