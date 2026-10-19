%global source0_hash ab302f27a1ab734e98cff13a6f49cb28e39f1ec63fe9f55b16b3485c1c8b2649
Name:           R-RSQLite
Version:        %R_rpm_version 2.4.5
Release:        1%{?dist}
Summary:        SQLite database interface for R
License:        LicenseRef-Callaway-LGPLv2+
URL:            %{cran_url}
Source0:        https://cran.r-project.org/package=RSQLite&version=%{version}#/RSQLite_%{version}.tar.gz
ExcludeArch:    %{ix86}
# oreon:deps
BuildRequires:  R-devel
BuildRequires:  sqlite-devel
# /oreon:deps
%description
A SQLite database interface definition for communication between R and SQLite
databases.

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
