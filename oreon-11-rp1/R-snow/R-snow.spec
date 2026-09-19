%global source0_hash 84587f46f222a96f3e2fde10ad6ec6ddbd878f4e917cd926d632f61a87db13c9

Name:           R-snow
Version:        %R_rpm_version 0.4-4
Release:        %autorelease
Summary:        Simple Network of Workstations

# Automatically converted from old format: GPLv2+ - review is highly recommended.
License:        GPL-2.0-or-later
URL:            %{cran_url}
Source:         %{cran_source}

BuildArch:      noarch
BuildRequires:  R-devel

%description
Support for simple parallel computing in R.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -c
chmod -x snow/inst/RMPInode.R
rm -rf snow/inst/*.bat # do not need on Linux

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
