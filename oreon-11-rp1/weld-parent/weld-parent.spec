%global source0_hash e013b6525b10994fb9be6c3559d5b7e32c7d12df7bfb38d03c5cda729a1836e9

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
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
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
* Mon May 25 2026 Oreon Packaging Team <packaging@oreonhq.com> - 46-13
- Import
