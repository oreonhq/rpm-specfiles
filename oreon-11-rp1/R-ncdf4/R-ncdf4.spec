%global source0_hash 6cba9907b093bf48e0239a903c64938a57d142e4fd5364eb1ee5e5eb97d959e0
Name:           R-ncdf4
Version:        %R_rpm_version 1.24
Release:        1%{?dist}
Summary:        Interface to Unidata netCDF (Version 4 or Earlier) Format Data Files
License:        GPL-3.0-or-later
URL:            %{cran_url}
Source0:        https://cran.r-project.org/package=ncdf4&version=%{version}#/ncdf4_%{version}.tar.gz
ExcludeArch:    %{ix86}
# oreon:deps
BuildRequires:  R-devel
BuildRequires:  chrpath
BuildRequires:  netcdf-devel
# /oreon:deps
%description
Provides a high-level R interface to data files written using Unidata's netCDF
library (version 4 or earlier), which are binary data files that are portable
across platforms and include metadata information in addition to the data sets.
Using this package, netCDF files (either version 4 or "classic" version 3) can
be opened and data sets read in easily. It is also easy to create new netCDF
dimensions, variables, and files, in either version 3 or 4 format, and
manipulate existing netCDF files.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -c
# Remove license about bundled (but not on Fedora) HDF5.
rm ncdf4/inst/HDF5_COPYING

%build

%install
%R_install
%R_save_files
chrpath -d %{buildroot}%{_R_libdir}/ncdf4/libs/ncdf4.so
%oreon_autofiles main

%check

%R_check
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
