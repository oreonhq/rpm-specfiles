%global source0_hash 02c536f8f6af55b132210a50b1e9694a3549806bf97c49e0fe03595945aab254
Name:           R-expm
Version:        %R_rpm_version 1.0-0
Release:        1%{?dist}
Summary:        Computation of the matrix exponential and related quantities
License:        GPL-2.0-or-later
URL:            %{cran_url}
Source0:        https://cran.r-project.org/package=expm&version=1.0-0#/expm_1.0-0.tar.gz
# oreon:deps
BuildRequires:  R-devel
# /oreon:deps
%description
Efficient calculation of the exponential of a matrix. The package
contains an R interface and a C API that package authors can use.

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
