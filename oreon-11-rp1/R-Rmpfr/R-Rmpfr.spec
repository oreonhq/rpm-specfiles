%global source0_hash d9f6caa4511afbf1465fee5edd2ae56869e496229dabd9f6e1a7e122e55ed5b4
Name:           R-Rmpfr
Version:        %R_rpm_version 1.1-2
Release:        1%{?dist}
Summary:        R MPFR - Multiple Precision Floating-Point Reliable
License:        GPL-2.0-or-later
URL:            %{cran_url}
Source0:        https://cran.r-project.org/package=Rmpfr&version=1.1-2#/Rmpfr_1.1-2.tar.gz
ExcludeArch:    %{ix86}
# oreon:deps
BuildRequires:  R-devel
BuildRequires:  gmp-devel
BuildRequires:  mpfr-devel
# /oreon:deps
%description
Arithmetic (via S4 classes and methods) for arbitrary precision floating
point numbers, including transcendental ("special") functions.  To this
end, the package interfaces to the 'LGPL' licensed 'MPFR' (Multiple
Precision Floating-Point Reliable) Library which itself is based on the
'GMP' (GNU Multiple Precision) Library.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -c
rm -f Rmpfr/tests/special-*.R # unconditional suggest, should be fixed

%build

%install
%R_install
%R_save_files
%oreon_autofiles main

%check

%R_check \--no-examples
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
