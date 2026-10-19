%global source0_hash 8ef8c56e4d3fe55cec8de3284739ce62e7b73678c58c29549e4a8b29358ab30a
Name:           R-xfun
Version:        %R_rpm_version 0.56
Release:        1%{?dist}
Summary:        Miscellaneous Functions to Support Packages Maintained by 'Yihui Xie'
License:        MIT
URL:            %{cran_url}
Source0:        https://cran.r-project.org/package=xfun&version=%{version}#/xfun_%{version}.tar.gz
ExcludeArch:    %{ix86}
# oreon:deps
BuildRequires:  R-devel
# /oreon:deps
%description
Miscellaneous functions commonly used in other packages maintained by
'Yihui Xie'.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%oreon_prep
%build

%install
%R_install
%R_save_files
%oreon_autofiles main

%check

%R_check \--no-tests
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
