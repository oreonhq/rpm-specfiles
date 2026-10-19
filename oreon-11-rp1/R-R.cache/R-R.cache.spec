%global source0_hash e265953212edd15be12cdfcc4fa8829cc0dcf3b06ab3e0aa1758108544822d21
Name:           R-R.cache
Version:        %R_rpm_version 0.17.0
Release:        1%{?dist}
Summary:        Fast and Light-Weight Caching (Memoization) of Objects and Results
License:        LGPL-2.1-or-later
URL:            %{cran_url}
Source0:        https://cran.r-project.org/package=R.cache&version=%{version}#/R.cache_%{version}.tar.gz
BuildArch:      noarch
# oreon:deps
BuildRequires:  R-devel
# /oreon:deps
%description
Memoization can be used to speed up repetitive and computational expensive
function calls.  The first time a function that implements memoization is
called the results are stored in a cache memory.  The next time the
function is called with the same set of parameters, the results are
momentarily retrieved from the cache avoiding repeating the calculations.
With this package, any R object can be cached in a key-value storage where
the key can be an arbitrary set of R objects.  The cache memory is
persistent (on the file system).

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
