%global source0_hash f7c199b5ece6b561ea734f55532ffae8eac60f81042a40c96fe31235369ef894
Name:           R-RMariaDB
Version:        %R_rpm_version 1.3.4
Release:        1%{?dist}
Summary:        Database Interface and 'MariaDB' Driver
License:        MIT
URL:            %{cran_url}
Source0:        https://cran.r-project.org/package=RMariaDB&version=%{version}#/RMariaDB_%{version}.tar.gz
ExcludeArch:    %{ix86}
# oreon:deps
BuildRequires:  R-devel
BuildRequires:  mariadb-connector-c-devel
# /oreon:deps
%description
Implements a 'DBI'-compliant interface to 'MariaDB'
(<https://mariadb.org/>) and 'MySQL' (<https://www.mysql.com/>) databases.

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
