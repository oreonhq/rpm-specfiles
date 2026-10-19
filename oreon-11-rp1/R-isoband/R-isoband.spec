%global source0_hash fe8d3d58ca75bbee32f389152ac0058818f3f76f09c9867949531de7abc424ac
Name:           R-isoband
Version:        %R_rpm_version 0.3.0
Release:        1%{?dist}
Summary:        Generate Isolines and Isobands from Regularly Spaced Elevation Grids
License:        MIT
URL:            %{cran_url}
Source0:        https://cran.r-project.org/package=isoband&version=%{version}#/isoband_%{version}.tar.gz
ExcludeArch:    %{ix86}
# oreon:deps
BuildRequires:  R-devel
# /oreon:deps
%description
A fast C++ implementation to generate contour lines (isolines) and contour
polygons (isobands) from regularly spaced grids containing elevation data.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%oreon_prep
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
