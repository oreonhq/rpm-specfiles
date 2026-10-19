%global source0_hash b32fa402cc282488a4061a12619308342df1a9d5145a412078014850f2fe6b50
Name:           R-RcppDate
Version:        %R_rpm_version 0.0.6
Release:        1%{?dist}
Summary:        'date' C++ Header Library for Date and Time Functionality
License:        GPL-2.0-or-later
URL:            %{cran_url}
Source0:        https://cran.r-project.org/package=RcppDate&version=%{version}#/RcppDate_%{version}.tar.gz
BuildArch:      noarch
Obsoletes:      %{name}-devel <= 0.0.6
Provides:       bundled(date)
# oreon:deps
BuildRequires:  R-devel
# /oreon:deps
%description
A header-only C++ library is provided with support for dates, time zones,
ISO weeks, Julian dates, and Islamic dates. 'date' offers extensive date
and time functionality for the C++11, C++14 and C++17 standards and was
written by Howard Hinnant and released under the MIT license. A slightly
modified version has been accepted (along with 'tz.h') as part of C++20.
This package regroups all header files from the upstream repository by
Howard Hinnant so that other R packages can use them in their C++ code. At
present, few of the types have explicit 'Rcpp' wrappers though these may be
added as needed.

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
