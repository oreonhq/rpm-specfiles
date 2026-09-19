%global source0_hash f7c199b5ece6b561ea734f55532ffae8eac60f81042a40c96fe31235369ef894

Name:           R-RMariaDB
Version:        %R_rpm_version 1.3.4
Release:        %autorelease
Summary:        Database Interface and 'MariaDB' Driver

License:        MIT
URL:            %{cran_url}
Source:         %{cran_source}

# https://fedoraproject.org/wiki/Changes/EncourageI686LeafRemoval
ExcludeArch:    %{ix86}

BuildRequires:  R-devel
BuildRequires:  mariadb-connector-c-devel

%description
Implements a 'DBI'-compliant interface to 'MariaDB'
(<https://mariadb.org/>) and 'MySQL' (<https://www.mysql.com/>) databases.

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
