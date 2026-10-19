%global source0_hash 2320ebc9ef3b1a32a1e63f94a6ce2c1c34d66782221a6531e786804f681abc66
Name:           R-rappdirs
Version:        %R_rpm_version 0.3.4
Release:        1%{?dist}
Summary:        Application Directories: Determine Where to Save Data, Caches, and Logs
License:        MIT
URL:            %{cran_url}
Source0:        https://cran.r-project.org/package=rappdirs&version=%{version}#/rappdirs_%{version}.tar.gz
ExcludeArch:    %{ix86}
# oreon:deps
BuildRequires:  R-devel
# /oreon:deps
%description
An easy way to determine which directories on the users computer you should
use to save data, caches and logs. A port of Python's 'Appdirs'
(<https://github.com/ActiveState/appdirs>) to R.

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
