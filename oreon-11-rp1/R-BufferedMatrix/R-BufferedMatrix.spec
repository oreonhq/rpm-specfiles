%global source0_hash 5b2677cb5d33166e553479777ab026e7a0ebd74af9fa49ee9a5fe47de50d2fba
Name:           R-BufferedMatrix
Version:        %R_rpm_version 1.74.0
Release:        1%{?dist}
Summary:        A matrix data storage object method from bioconductor
License:        LicenseRef-Callaway-LGPLv2+
URL:            %{bioc_url}
Source0:        https://bioconductor.org/packages/3.22/bioc/src/contrib/BufferedMatrix_1.74.0.tar.gz
Obsoletes:      %{name}-devel <= 1.74.0
# oreon:deps
BuildRequires:  R-devel
# /oreon:deps
%description
A tabular style data object where most data is stored outside main memory.
A buffer is used to speed up access to data.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -c
sed -i -e 's/\r$//' BufferedMatrix/inst/doc/BufferedMatrix.Rnw

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
