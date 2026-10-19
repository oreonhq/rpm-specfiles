%global source0_hash 66bed3543337535fe2cf2d3eee4165472599c14d3c5e4402f7a1ebf5112c75c9
Name:           R-rlecuyer
Version:        %R_rpm_version 0.3-8
Release:        1%{?dist}
Summary:        R interface to RNG with multiple streams
License:        GPL-2.0-or-later
URL:            %{cran_url}
Source0:        https://cran.r-project.org/package=rlecuyer&version=0.3-8#/rlecuyer_0.3-8.tar.gz
# oreon:deps
BuildRequires:  R-devel
# /oreon:deps
%description
Provides an interface to the C implementation of the random number 
generator with multiple independent streams developed by L'Ecuyer 
et al (2002). The main purpose of this package is to enable the 
use of this random number generator in parallel R applications.  

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
