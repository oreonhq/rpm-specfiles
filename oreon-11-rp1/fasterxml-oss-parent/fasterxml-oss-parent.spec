%global source0_hash 12144af57225dd8214139ae08b71bf47d1f76634fdcaf4338fa3960105601b90
%global srcname oss-parent

Name:          fasterxml-oss-parent
Version:       75
Release:       1%{?dist}
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
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | cut -d' ' -f1); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%setup -q -n %{srcname}-%{srcname}-%{version}

# Stuff unnecessary for RPM builds
%pom_remove_plugin :jacoco-maven-plugin
%pom_remove_plugin :maven-enforcer-plugin
%pom_remove_plugin :maven-javadoc-plugin
%pom_remove_plugin :maven-pmd-plugin
%pom_remove_plugin :maven-scm-plugin
%pom_remove_plugin :maven-site-plugin
%pom_remove_plugin :jdepend-maven-plugin
%pom_remove_plugin :central-publishing-maven-plugin
%pom_xpath_remove "pom:build/pom:extensions"

%build
%mvn_build

%install
%mvn_install

%files -f .mfiles
%doc README.creole
%license LICENSE NOTICE

%changelog
%autochangelog
