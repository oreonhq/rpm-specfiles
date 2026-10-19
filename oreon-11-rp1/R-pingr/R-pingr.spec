%global source0_hash 218ba664f38b68d8c5c2c934122a114b191b6c7303c13397f4bebc25a2735f94
Name:           R-pingr
Version:        %R_rpm_version 2.0.5
Release:        1%{?dist}
Summary:        Check if a Remote Computer is Up
License:        MIT
URL:            %{cran_url}
Source0:        https://cran.r-project.org/package=pingr&version=%{version}#/pingr_%{version}.tar.gz
ExcludeArch:    %{ix86}
# oreon:deps
BuildRequires:  R-devel
# /oreon:deps
%description
Check if a remote computer is up. It can either just call the system ping
command, or check a specified TCP port.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%oreon_prep
%build

%install
%R_install
%R_save_files
%oreon_autofiles main

%check

%R_check \--no-examples
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
