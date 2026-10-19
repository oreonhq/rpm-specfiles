%global source0_hash 1db8b51361489bb5ec4921839e4b4f8063d7c82d07f7ca97ddb4257ac47c930f
Name:           R-RODBC
Version:        %R_rpm_version 1.3-26.1
Release:        1%{?dist}
Summary:        An ODBC database interface for R
License:        GPL-2.0-only OR GPL-3.0-only
URL:            %{cran_url}
Source0:        https://cran.r-project.org/package=RODBC&version=1.3-26.1#/RODBC_1.3-26.1.tar.gz
# oreon:deps
BuildRequires:  R-devel
BuildRequires:  unixODBC-devel
# /oreon:deps
%description
An ODBC database interface for R.

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
