%global source0_hash 17795ff63ca767a48df95d2f4c774400c6098102dce9ffcb5db2596a6d9b68e0
Name:           R-BiocGenerics
Version:        %R_rpm_version 0.56.0
Release:        1%{?dist}
Summary:        Generic functions for Bioconductor
License:        Artistic-2.0
URL:            %{bioc_url}
Source0:        https://bioconductor.org/packages/3.22/bioc/src/contrib/BiocGenerics_0.56.0.tar.gz
BuildArch:      noarch
# oreon:deps
BuildRequires:  R-devel
# /oreon:deps
%description
S4 generic functions needed by many other Bioconductor packages.

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
