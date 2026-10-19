%global source0_hash 530a7435640e86c34db16bcc4c8a38b5046ac79512a86e7b97f66a9d57813cbc
Name:           R-Biobase
Version:        %R_rpm_version 2.70.0
Release:        1%{?dist}
Summary:        Base functions for Bioconductor
License:        Artistic-2.0
URL:            %{bioc_url}
Source0:        https://bioconductor.org/packages/3.22/bioc/src/contrib/Biobase_2.70.0.tar.gz
# oreon:deps
BuildRequires:  R-devel
# /oreon:deps
%description
Base functions for Bioconductor (bioconductor.org). Biobase provides
functions that are needed by many other Bioconductor packages or which
replace R functions.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%oreon_prep
%build

%install
%R_install
%R_save_files
%oreon_autofiles main

%check

%R_check \--no-tests
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
