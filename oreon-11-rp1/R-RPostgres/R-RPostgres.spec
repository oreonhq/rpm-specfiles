%global source0_hash 0c6c829aee387593dcf4ec0a66f2edd3b96c67d4acea19079f1dd7e4dd1768a4

Name:           R-RPostgres
Version:        %R_rpm_version 1.4.8
Release:        %autorelease
Summary:        Rcpp Interface to PostgreSQL

License:        MIT
URL:            %{cran_url}
Source:         %{cran_source}

# https://fedoraproject.org/wiki/Changes/EncourageI686LeafRemoval
ExcludeArch:    %{ix86}

BuildRequires:  R-devel
BuildRequires:  pkgconfig(libpq)

%description
Fully DBI-compliant Rcpp-backed interface to PostgreSQL
<https://www.postgresql.org/>, an open-source relational database.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -c

%generate_buildrequires
%R_buildrequires

%build

%install
%R_install
%R_save_files

%check
%R_check

%files -f %{R_files}

%changelog
%autochangelog
