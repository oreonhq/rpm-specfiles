%global source0_hash b3bb91dbc67a1cc34080eae960d330626cc76585f80360524b5fceb08febf363
Name:           R-purrr
Version:        %R_rpm_version 1.2.1
Release:        1%{?dist}
Summary:        Functional Programming Tools
License:        MIT
URL:            %{cran_url}
Source0:        https://cran.r-project.org/package=purrr&version=%{version}#/purrr_%{version}.tar.gz
ExcludeArch:    %{ix86}
# oreon:deps
BuildRequires:  R-devel
# /oreon:deps
%description
A complete and consistent functional programming toolkit for R.

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
