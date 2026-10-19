%global source0_hash 8e4e1f5530967d11390b70a72cd9208e64bb78ffb25a6819091cb851122fdb3b
Name:           R-Bessel
Version:        %R_rpm_version 0.7-0
Release:        1%{?dist}
Summary:        Computations and Approximations for Bessel Functions
License:        GPL-2.0-or-later
URL:            %{cran_url}
Source0:        https://cran.r-project.org/package=Bessel&version=0.7-0#/Bessel_0.7-0.tar.gz
ExcludeArch:    %{ix86}
# oreon:deps
BuildRequires:  R-devel
# /oreon:deps
%description
Computations for Bessel function for complex, real and partly 'mpfr'
(arbitrary precision) numbers; notably interfacing TOMS 644;
approximations for large arguments, experiments, etc.

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
