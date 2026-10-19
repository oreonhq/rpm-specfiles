%global source0_hash 46c39607d3f256e40174c9c81fb476280291c1bcd894d99f9789a3a3d52ca2d7
Name:           R-lpSolve
Version:        %R_rpm_version 5.6.23
Release:        1%{?dist}
Summary:        Interface to Lp_solve to Solve Linear/Integer Programs
License:        LGPL-2.0-or-later
URL:            %{cran_url}
Source0:        https://cran.r-project.org/package=lpSolve&version=%{version}#/lpSolve_%{version}.tar.gz
Patch:          0001-Use-R-provided-BLAS-routines.patch
ExcludeArch:    %{ix86}
# oreon:deps
BuildRequires:  R-devel
# /oreon:deps
%description
Lp_solve is freely available (under LGPL 2) software for solving linear,
integer and mixed integer programs. In this implementation we supply a
"wrapper" function in C and some R functions that solve general
linear/integer problems, assignment problems, and transportation problems.
This version calls lp_solve version 5.5.

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
