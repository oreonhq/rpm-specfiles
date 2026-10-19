%global source0_hash a9f22335ea39039de25bb27bccd5ff1ffb2b743579b31d150b6b91c9ea81d0b8
Name:           R-brio
Version:        %R_rpm_version 1.1.5
Release:        1%{?dist}
Summary:        Basic R Input Output
License:        MIT
URL:            %{cran_url}
Source0:        https://cran.r-project.org/package=brio&version=%{version}#/brio_%{version}.tar.gz
ExcludeArch:    %{ix86}
# oreon:deps
BuildRequires:  R-devel
# /oreon:deps
%description
Functions to handle basic input output, these functions always read and write
UTF-8 (8-bit Unicode Transformation Format) files and provide more explicit
control over line endings.

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
