%global source0_hash 0ead5acd0153e5073b3c24e8e782982a4eab3aaa768ba17700d796fb13b68cef
Name:           R-reshape2
Version:        %R_rpm_version 1.4.5
Release:        1%{?dist}
Summary:        Flexibly Reshape Data: A Reboot of the Reshape Package
License:        MIT
URL:            %{cran_url}
Source0:        https://cran.r-project.org/package=reshape2&version=%{version}#/reshape2_%{version}.tar.gz
ExcludeArch:    %{ix86}
# oreon:deps
BuildRequires:  R-devel
# /oreon:deps
%description
Flexibly restructure and aggregate data using just two functions: melt and
'dcast' (or 'acast').

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
