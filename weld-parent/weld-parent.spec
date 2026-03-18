Name:           weld-parent
Version:        46
Release:        13%{?dist}
Summary:        Parent POM for Weld
# Automatically converted from old format: ASL 2.0 - review is highly recommended.
License:        Apache-2.0

URL:            http://weld.cdi-spec.org
Source0:        https://github.com/weld/parent/archive/%{version}/%{name}-%{version}.tar.gz

BuildArch:      noarch
ExclusiveArch:  %{java_arches} noarch

BuildRequires:  maven-local-openjdk25
BuildRequires:  mvn(org.codehaus.mojo:build-helper-maven-plugin)

%description
Parent POM for Weld

%prep
%setup -q -n parent-%{version}

%pom_remove_plugin :buildnumber-maven-plugin
%pom_remove_plugin :maven-enforcer-plugin
%pom_remove_plugin :maven-remote-resources-plugin
%pom_remove_plugin :maven-source-plugin

%pom_remove_dep :maven-scm-api


%build
%mvn_build

%install
%mvn_install

%files -f .mfiles

%changelog
* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 46-13
- Prepare for Oreon 11 (RP1)
