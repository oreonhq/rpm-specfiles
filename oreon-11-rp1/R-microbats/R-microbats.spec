%global source0_hash 88fb9927707a9dd4ae98f12bf00ca489b586580c8d93a1c5ece1f1a8e8da50d5
Name:           R-microbats
Version:        %R_rpm_version 0.1-1
Release:        1%{?dist}
Summary:        An implementation of Bat Algorithm in R
License:        GPL-2.0-only
URL:            %{cran_url}
Source0:        https://cran.r-project.org/package=microbats&version=0.1-1#/microbats_0.1-1.tar.gz
BuildArch:      noarch
# oreon:deps
BuildRequires:  R-devel
# /oreon:deps
%description
A nature-inspired metaheuristic algorithm based on the echolocation behavior
of microbats that uses frequency tuning to optimize problems in both
continuous and discrete dimensions. This R package makes it easy to
implement the standard bat algorithm on any user-supplied function.
The algorithm was first developed by Xin-She Yang in 2010 
(<doi:10.1007/978-3-642-12538-6_6>, <doi:10.1109/CINTI.2014.7028669>.

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
