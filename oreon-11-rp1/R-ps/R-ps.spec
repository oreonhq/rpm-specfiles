%global source0_hash 6f093c0beb87684afe098b71e16593366210d5d38992a7c3740ca1075da4df7d
Name:           R-ps
Version:        %R_rpm_version 1.9.1
Release:        1%{?dist}
Summary:        List, Query, Manipulate System Processes
License:        MIT
URL:            %{cran_url}
Source0:        https://cran.r-project.org/package=ps&version=%{version}#/ps_%{version}.tar.gz
ExcludeArch:    %{ix86}
# oreon:deps
BuildRequires:  R-devel
# /oreon:deps
%description
List, query and manipulate all system processes, on 'Windows', 'Linux' and
'macOS'.

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
