%global source0_hash 16efc5f13f4b78919c9d51c07acf62c051e0e3830ae3cc32c596f8daf569c3cb
Name:           R-profmem
Version:        %R_rpm_version 0.7.0
Release:        1%{?dist}
Summary:        Simple Memory Profiling for R
License:        LGPL-2.1-or-later
URL:            %{cran_url}
Source0:        https://cran.r-project.org/package=profmem&version=%{version}#/profmem_%{version}.tar.gz
BuildArch:      noarch
# oreon:deps
BuildRequires:  R-devel
# /oreon:deps
%description
A simple and light-weight API for memory profiling of R expressions.  The
profiling is built on top of R's built-in memory profiler
('utils::Rprofmem()'), which records every memory allocation done by R (also
native code).

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
