%global source0_hash 2c3643b4218ef2008470a4b2d8feb519c217e5570d34a1ecf117e0f8d14a637e
Name:           R-RcppCCTZ
Version:        %R_rpm_version 0.2.14
Release:        1%{?dist}
Summary:        'Rcpp' Bindings for the 'CCTZ' Library
License:        GPL-2.0-or-later
URL:            %{cran_url}
Source0:        https://cran.r-project.org/package=RcppCCTZ&version=%{version}#/RcppCCTZ_%{version}.tar.gz
ExcludeArch:    %{ix86}
Requires:       cctz-devel
Obsoletes:      %{name}-devel <= 0.2.13
# oreon:deps
BuildRequires:  R-devel
BuildRequires:  cctz-devel
# /oreon:deps
%description
'Rcpp' Access to the 'CCTZ' timezone library is provided. 'CCTZ' is a C++
library for translating between absolute and civil times using the rules of a
time zone.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -c
# Remove bundled cctz.
rm -r RcppCCTZ/inst/include/cctz
rm RcppCCTZ/src/time_zone_*.{cc,h}
rm RcppCCTZ/src/{civil_time_detail,zone_info_source}.cc
echo "PKG_LIBS = -lcctz" > RcppCCTZ/src/Makevars

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
