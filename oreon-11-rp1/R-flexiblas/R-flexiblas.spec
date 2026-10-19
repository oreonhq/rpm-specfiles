%global source0_hash 31902d98c782180f2db72efa9aa2252dacbceee85c65a333d3fecaa800de1cd8
Name:           R-flexiblas
Version:        %R_rpm_version 3.4.0
Release:        1%{?dist}
Summary:        FlexiBLAS API Interface for R
License:        LGPL-3.0-or-later
URL:            %{cran_url}
Source0:        https://cran.r-project.org/package=flexiblas&version=%{version}#/flexiblas_%{version}.tar.gz
# oreon:deps
BuildRequires:  R-devel
BuildRequires:  flexiblas-devel
# /oreon:deps
%description
Provides functions to switch the BLAS/LAPACK optimized backend and
change the number of threads without leaving the R session, which needs
to be linked against the FlexiBLAS wrapper library
<https://www.mpi-magdeburg.mpg.de/projects/flexiblas>.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -c
# use system-provided headers and libraries
rm -f flexiblas/src/flexiblas*
sed -i 's/"flexiblas_api.h"/<flexiblas_api.h>/' flexiblas/src/wrapper.c
%global pkg_flags export PKG_LIBS=$(pkg-config --libs flexiblas_api) \\\
                  export PKG_CFLAGS=$(pkg-config --cflags flexiblas_api)

%build

%install
%{pkg_flags}
%R_install
%R_save_files
%oreon_autofiles main

%check

%{pkg_flags}
%R_check
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
