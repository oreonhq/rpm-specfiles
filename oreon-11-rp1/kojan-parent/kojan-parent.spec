%global source0_hash 5b8bddbd50fa88c0a17e130cadd917cacbef018ec94ba0ddb213d58838acc977

%bcond_with bootstrap

Name:           kojan-parent
Version:        6
Release:        %autorelease
Summary:        Maven parent POM for io.kojan
License:        Apache-2.0
URL:            https://github.com/mizdebsk/kojan-parent
BuildArch:      noarch
ExclusiveArch:  %{java_arches} noarch

Source0:        https://github.com/mizdebsk/kojan-parent/archive/refs/tags/6.tar.gz#/%{name}-%{version}.tar.gz

%if %{with bootstrap}
BuildRequires:  javapackages-bootstrap
%else
BuildRequires:  maven-local-openjdk25
%endif

%description
Parent Maven POM file for io.kojan organization.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1 -C
%pom_remove_plugin :spotless-maven-plugin

%build
%mvn_build -j

%install
%mvn_install

%files -f .mfiles
%license LICENSE

%changelog
%autochangelog
