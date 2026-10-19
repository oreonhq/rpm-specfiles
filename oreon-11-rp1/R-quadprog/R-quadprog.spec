%global source0_hash 22128dd6b08d3516c44ff89276719ad4fe46b36b23fdd585274fa3a93e7a49cd
Name:           R-quadprog
Version:        %R_rpm_version 1.5-8
Release:        1%{?dist}
Summary:        Functions to Solve Quadratic Programming Problems
License:        GPL-2.0-or-later
URL:            %{cran_url}
Source0:        https://cran.r-project.org/package=quadprog&version=1.5-8#/quadprog_1.5-8.tar.gz
ExcludeArch:    %{ix86}
# oreon:deps
BuildRequires:  R-devel
# /oreon:deps
%description
This package contains routines and documentation for solving quadratic
programming problems.

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
