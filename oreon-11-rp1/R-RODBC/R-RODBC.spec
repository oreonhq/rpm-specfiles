%global source0_hash 1db8b51361489bb5ec4921839e4b4f8063d7c82d07f7ca97ddb4257ac47c930f

Name:           R-RODBC
Version:        %R_rpm_version 1.3-26.1
Release:        %autorelease
Summary:        An ODBC database interface for R

# Automatically converted from old format: GPLv2 or GPLv3 - review is highly recommended.
License:        GPL-2.0-only OR GPL-3.0-only
URL:            %{cran_url}
Source:         %{cran_source}

BuildRequires:  R-devel
BuildRequires:  unixODBC-devel

%description
An ODBC database interface for R.

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
