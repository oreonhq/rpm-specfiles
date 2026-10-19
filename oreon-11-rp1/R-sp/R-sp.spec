%global source0_hash b57be793a96bec568bed5b619e62ec1f4efaf879adc0e57e486b891768148b98
Name:           R-sp
Version:        %R_rpm_version 2.2-0
Release:        1%{?dist}
Summary:        Classes and Methods for Spatial Data
License:        GPL-2.0-or-later
URL:            %{cran_url}
Source0:        https://cran.r-project.org/package=sp&version=2.2-0#/sp_2.2-0.tar.gz
ExcludeArch:    %{ix86}
Obsoletes:      %{name}-devel <= 2.2.0
# oreon:deps
BuildRequires:  R-devel
# /oreon:deps
%description
Classes and methods for spatial data; the classes document where the spatial
location information resides, for 2D or 3D data. Utility functions are
provided, e.g. for plotting data as maps, spatial selection, as well as methods
for retrieving coordinates, for subsetting, print, summary, etc.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -c
rm -f sp/tests/agg.R* sp/tests/over2.R* # whole file requires rgeos

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
