%global source0_hash 6d856d8a364bcdc499a0bf38bfd283b7c743d08f0b288174fba7dbf0a04b688d
Name:           R-base64enc
Version:        %R_rpm_version 0.1-3
Release:        1%{?dist}
Summary:        Tools for base64 encoding
License:        GPL-2.0-only OR GPL-3.0-only
URL:            %{cran_url}
Source0:        https://cran.r-project.org/package=base64enc&version=0.1-3#/base64enc_0.1-3.tar.gz
ExcludeArch:    %{ix86}
# oreon:deps
BuildRequires:  R-devel
# /oreon:deps
%description
This package provides tools for handling base64 encoding. It is more
flexible than the orphaned base64 package.

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
