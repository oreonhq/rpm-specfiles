%global source0_hash cf6708a7566a80929f06575aa345fae354714159ed5fab5db14306fc5d0d2dbe
Name:           R-DBI
Version:        %R_rpm_version 1.2.3
Release:        1%{?dist}
Summary:        Database interface module for R
License:        LicenseRef-Callaway-LGPLv2+
URL:            %{cran_url}
Source0:        https://cran.r-project.org/package=DBI&version=%{version}#/DBI_%{version}.tar.gz
BuildArch:      noarch
# oreon:deps
BuildRequires:  R-devel
# /oreon:deps
%description
A database interface (DBI) definition for communication between R and
relational database management systems.

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
