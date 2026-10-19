%global source0_hash 169e97ba0bbfbcdf4a80534322751f87a04370310c40e27f04aac6525d45903c
Name:           R-tidyselect
Version:        %R_rpm_version 1.2.1
Release:        1%{?dist}
Summary:        Select from a Set of Strings
License:        MIT
URL:            %{cran_url}
Source0:        https://cran.r-project.org/package=tidyselect&version=%{version}#/tidyselect_%{version}.tar.gz
BuildArch:      noarch
# oreon:deps
BuildRequires:  R-devel
# /oreon:deps
%description
A backend for the selecting functions of the 'tidyverse'. It makes it easy
to implement select-like functions in your own packages in a way that is
consistent with other 'tidyverse' interfaces for selection.

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
