%global source0_hash 864b7ee223d622d41214c6aacc7d68d8984090a8e1e823c729983d33624646c1
Name:           R-lubridate
Version:        %R_rpm_version 1.9.4
Release:        1%{?dist}
Summary:        Make dealing with dates a little easier
License:        GPL-2.0-or-later
URL:            %{cran_url}
Source0:        https://cran.r-project.org/package=lubridate&version=%{version}#/lubridate_%{version}.tar.gz
ExcludeArch:    %{ix86}
# oreon:deps
BuildRequires:  R-devel
# /oreon:deps
%description
Functions to work with date-times and time-spans: fast and user friendly
parsing of date-time data, extraction and updating of components of a date-time
(years, months, days, hours, minutes, and seconds), algebraic manipulation on
date-time and time-span objects. The 'lubridate' package has a consistent and
memorable syntax that makes working with dates easy and fun.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -c
rm -f lubridate/inst/cctz.sh # dev stuff
rm -f lubridate/tests/testthat/test-vctrs.R # unconditional suggest, should be fixed

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
