%global source0_hash 95d54c6a29b17eb11e3939a1b96b821b083a74290c95e2d2ccc8b45e0cfb3d3d

Name:           R-dbplyr
Version:        %R_rpm_version 2.5.1
Release:        %autorelease
Summary:        A 'dplyr' Back End for Databases

License:        MIT
URL:            %{cran_url}
Source:         %{cran_source}

BuildArch:      noarch
BuildRequires:  R-devel

%description
A 'dplyr' back end for databases that allows you to work with remote database
tables as if they are in-memory data frames. Basic features works with any
database that has a 'DBI' back end; more advanced features require 'SQL'
translation to be provided by the package author.

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
%R_check \--no-examples \--no-tests

%files -f %{R_files}

%changelog
%autochangelog
