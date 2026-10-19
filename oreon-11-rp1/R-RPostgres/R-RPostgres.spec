%global source0_hash 0c6c829aee387593dcf4ec0a66f2edd3b96c67d4acea19079f1dd7e4dd1768a4
Name:           R-RPostgres
Version:        %R_rpm_version 1.4.8
Release:        1%{?dist}
Summary:        Rcpp Interface to PostgreSQL
License:        MIT
URL:            %{cran_url}
Source0:        https://cran.r-project.org/package=RPostgres&version=%{version}#/RPostgres_%{version}.tar.gz
ExcludeArch:    %{ix86}
# oreon:deps
BuildRequires:  R-devel
BuildRequires:  pkgconfig(libpq)
# /oreon:deps
%description
Fully DBI-compliant Rcpp-backed interface to PostgreSQL
<https://www.postgresql.org/>, an open-source relational database.

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
