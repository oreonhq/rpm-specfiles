%global source0_hash e083efb0c1f7293a79d8fe35f90630fa34c8752d5a835cf0ea70560bf5c2ff94
Name:           R-gee
Version:        %R_rpm_version 4.13-29
Release:        1%{?dist}
Summary:        Generalized Estimation Equation Solver
License:        GPL-2.0-only
URL:            %{cran_url}
Source0:        https://cran.r-project.org/package=gee&version=4.13-29#/gee_4.13-29.tar.gz
ExcludeArch:    %{ix86}
# oreon:deps
BuildRequires:  R-devel
# /oreon:deps
%description
Generalized Estimation Equation solver.

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
