%global source0_hash 1de46b83b7038a293e612775197b7ffe47bd079cd2385aa7c65e98171bbd3605
Name:           R-forcats
Version:        %R_rpm_version 1.0.1
Release:        1%{?dist}
Summary:        Tools for Working with Categorical Variables (Factors)
License:        MIT
URL:            %{cran_url}
Source0:        https://cran.r-project.org/package=forcats&version=%{version}#/forcats_%{version}.tar.gz
BuildArch:      noarch
# oreon:deps
BuildRequires:  R-devel
# /oreon:deps
%description
Helpers for reordering factor levels (including moving specified levels to
front, ordering by first appearance, reversing, and randomly shuffling),
and tools for modifying factor levels (including collapsing rare levels
into other, 'anonymising', and manually 'recoding').

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%oreon_prep
%build

%install
%R_install
%R_save_files
%oreon_autofiles main

%check

%R_check \--no-examples
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
