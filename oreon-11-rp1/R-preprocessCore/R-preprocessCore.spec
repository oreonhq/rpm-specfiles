%global source0_hash 4472052371147cfbf91d223eb15f3b030d236de9b4bba6b58a205c368d53884d
Name:           R-preprocessCore
Version:        %R_rpm_version 1.72.0
Release:        1%{?dist}
Summary:        A collection of pre-processing functions
License:        LicenseRef-Callaway-LGPLv2+
URL:            %{bioc_url}
Source0:        https://bioconductor.org/packages/3.22/bioc/src/contrib/preprocessCore_1.72.0.tar.gz
Obsoletes:      %{name}-devel <= 1.72.0
# oreon:deps
BuildRequires:  R-devel
# /oreon:deps
%description
A library of core preprocessing routines

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
