%global source0_hash d85c0b5514ab9578d16032e703c33f197feaed1a424c834ebfcbf0ad46ae46b4
Name:           R-timechange
Version:        %R_rpm_version 0.3.0
Release:        1%{?dist}
Summary:        Efficient Updating of Date-Times
License:        GPL-3.0-or-later AND Apache-2.0
URL:            %{cran_url}
Source0:        https://cran.r-project.org/package=timechange&version=%{version}#/timechange_%{version}.tar.gz
ExcludeArch:    %{ix86}
# oreon:deps
BuildRequires:  R-devel
# /oreon:deps
%description
Efficient routines for manipulation of date-time objects while accounting
for time-zones and daylight saving times. The package includes utilities
for updating of date-time components (year, month, day etc.), modification
of time-zones, rounding of date-times, period addition and subtraction etc.

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
