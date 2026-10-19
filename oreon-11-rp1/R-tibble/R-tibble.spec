%global source0_hash fb309f8a1939021b237c7e85ff7ad6e8ff5acd57a6230d220a452094b492b28f
Name:           R-tibble
Version:        %R_rpm_version 3.3.1
Release:        1%{?dist}
Summary:        Simple Data Frames
License:        MIT
URL:            %{cran_url}
Source0:        https://cran.r-project.org/package=tibble&version=%{version}#/tibble_%{version}.tar.gz
ExcludeArch:    %{ix86}
# oreon:deps
BuildRequires:  R-devel
# /oreon:deps
%description
Provides a 'tbl_df' class (the 'tibble') with stricter checking and better
formatting than the traditional data frame.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%oreon_prep
%build

%install
%R_install
%R_save_files
%oreon_autofiles main

%check

%R_check
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
