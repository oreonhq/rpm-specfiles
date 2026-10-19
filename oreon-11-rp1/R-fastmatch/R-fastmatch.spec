%global source0_hash 2661c01bdc2383f4a30bf940e6bc3b68f1329db5f0e837df8160eb893f748d54
Name:           R-fastmatch
Version:        %R_rpm_version 1.1-8
Release:        1%{?dist}
Summary:        Fast match() function
License:        GPL-2.0-only
URL:            %{cran_url}
Source0:        https://cran.r-project.org/package=fastmatch&version=1.1-8#/fastmatch_1.1-8.tar.gz
ExcludeArch:    %{ix86}
# oreon:deps
BuildRequires:  R-devel
# /oreon:deps
%description
Package providing a fast match() replacement for cases that require
repeated look-ups. It is slightly faster that R's built-in match()
function on first match against a table, but extremely fast on any
subsequent lookup as it keeps the hash table in memory.

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
