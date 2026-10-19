%global source0_hash 5d38f288c752bbb9cea6ff830b8388bdd65a8571fd82d8d96064586bd588cf99
Name:           R-cellranger
Version:        %R_rpm_version 1.1.0
Release:        1%{?dist}
Summary:        Translate Spreadsheet Cell Ranges to Rows and Columns
License:        MIT
URL:            %{cran_url}
Source0:        https://cran.r-project.org/package=cellranger&version=%{version}#/cellranger_%{version}.tar.gz
BuildArch:      noarch
# oreon:deps
BuildRequires:  R-devel
# /oreon:deps
%description
Helper functions to work with spreadsheets and the "A1:D10" style of cell range
specification.

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
