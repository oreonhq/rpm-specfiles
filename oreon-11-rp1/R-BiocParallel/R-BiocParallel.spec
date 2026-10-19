%global source0_hash 3b2069e6b5aeb9c2e0586c110527dc2557240f4a447b67b8061931ee0b9a23c2
Name:           R-BiocParallel
Version:        %R_rpm_version 1.44.0
Release:        1%{?dist}
Summary:        Bioconductor facilities for parallel evaluation
License:        GPL-2.0-only OR GPL-3.0-only
URL:            %{bioc_url}
Source0:        https://bioconductor.org/packages/3.22/bioc/src/contrib/BiocParallel_1.44.0.tar.gz
# oreon:deps
BuildRequires:  R-devel
# /oreon:deps
%description
This package provides modified versions and novel implementation of functions
for parallel evaluation, tailored to use with Bioconductor objects.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%oreon_prep
%build

%install
%R_install
%R_save_files
%oreon_autofiles main

%check

%R_check \--no-examples \--no-tests
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
