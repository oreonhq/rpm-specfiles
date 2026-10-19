%global source0_hash 2e1fafb05938e81073561ae4892dc543ef15807e375e0ea8fa75e3ab79f0281b
Name:           R-BH
Version:        %R_rpm_version 1.90.0-1
Release:        1%{?dist}
Summary:        Boost C++ Header Files for R
License:        BSL-1.0
URL:            %{cran_url}
Source0:        https://cran.r-project.org/package=BH&version=1.90.0-1#/BH_1.90.0-1.tar.gz
BuildArch:      noarch
Obsoletes:      %{name}-devel <= 1.90.0-1
# oreon:deps
BuildRequires:  R-devel
# /oreon:deps
%description
Boost provides free peer-reviewed portable C++ source libraries. A large part 
of Boost is provided as C++ template code which is resolved entirely at 
compile-time without linking. This package aims to provide the most useful 
subset of Boost libraries for template use among CRAN package. By placing 
these libraries in this package, we offer a more efficient distribution 
system for CRAN as replication of this code in the sources of other packages 
is avoided. 

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -c
# Remove spurious exec permissions
for i in `find %{packname}/inst/include/boost |grep hpp`; do chmod -x $i; done

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
