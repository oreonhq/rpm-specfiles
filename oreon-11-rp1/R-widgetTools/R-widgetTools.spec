%global source0_hash dceed7d3efac665aaf35783d1ceb128b93ca175ce5e905a55cd966fee5c4d55c
Name:           R-widgetTools
Version:        %R_rpm_version 1.88.0
Release:        1%{?dist}
Summary:        Bioconductor tools to support tcltk widgets
License:        LicenseRef-Callaway-LGPLv2+
URL:            %{bioc_url}
Source0:        https://bioconductor.org/packages/3.22/bioc/src/contrib/widgetTools_1.88.0.tar.gz
BuildArch:      noarch
# oreon:deps
BuildRequires:  R-devel
# /oreon:deps
%description
This package contains tools to support the construction of tcltk widgets.
This library is part of the bioconductor (bioconductor.org) project

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
