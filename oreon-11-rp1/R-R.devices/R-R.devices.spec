%global source0_hash 4fa070d83781774e69c8ec5f4b3ffb3751f0d3f292271cdb47d76b0c012f3cf8
Name:           R-R.devices
Version:        %R_rpm_version 2.17.3
Release:        1%{?dist}
Summary:        Unified Handling of Graphics Devices
License:        LGPL-2.1-or-later
URL:            %{cran_url}
Source0:        https://cran.r-project.org/package=R.devices&version=%{version}#/R.devices_%{version}.tar.gz
BuildArch:      noarch
# oreon:deps
BuildRequires:  R-devel
# /oreon:deps
%description
Functions for creating plots and image files in a unified way regardless of
output format (EPS, PDF, PNG, SVG, TIFF, WMF, etc.). Default device options
as well as scales and aspect ratios are controlled in a uniform way across
all device types. Switching output format requires minimal changes in code.
This package is ideal for large-scale batch processing, because it will
never leave open graphics devices or incomplete image files behind, even on
errors or user interrupts.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -c
rm -f R.devices/tests/devSet.R # unconditional suggest, should be fixed

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
