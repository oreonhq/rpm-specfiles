%global source0_hash 5a913f960a0071cf9db05df4de03055a21a1c243b3bdbf846375537a664bcb74
Name:           R-date
Version:        %R_rpm_version 1.2-42
Release:        1%{?dist}
Summary:        Functions for Handling Dates
License:        GPL-2.0-only
URL:            %{cran_url}
Source0:        https://cran.r-project.org/package=date&version=1.2-42#/date_1.2-42.tar.gz
ExcludeArch:    %{ix86}
# oreon:deps
BuildRequires:  R-devel
# /oreon:deps
%description
Functions for handling dates.

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
