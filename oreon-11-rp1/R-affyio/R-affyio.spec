%global source0_hash 14c3baf864a3604eb4c2348350168dcc87c20fbb55079d531163aaa97becdde2
Name:           R-affyio
Version:        %R_rpm_version 1.80.0
Release:        1%{?dist}
Summary:        Tools for parsing Affymetrix data files
License:        LicenseRef-Callaway-LGPLv2+
URL:            %{bioc_url}
Source0:        https://bioconductor.org/packages/3.22/bioc/src/contrib/affyio_1.80.0.tar.gz
# oreon:deps
BuildRequires:  R-devel
# /oreon:deps
%description
Routines for parsing Affymetrix data files based upon file format 
information. Primary focus is on accessing the CEL and CDF file formats.

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
