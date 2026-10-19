%global source0_hash a534a225bfd08dc6ad61480f177eda97fadc3fc8fd66f23ad6cb327dcf68661e
Name:           R-webutils
Version:        %R_rpm_version 1.2.2
Release:        1%{?dist}
Summary:        Utility Functions for Developing Web Applications
License:        MIT
URL:            %{cran_url}
Source0:        https://cran.r-project.org/package=webutils&version=%{version}#/webutils_%{version}.tar.gz
ExcludeArch:    %{ix86}
# oreon:deps
BuildRequires:  R-devel
# /oreon:deps
%description
Parses http request data in application/json, multipart/form-data, or
application/x-www-form-urlencoded format. Includes example of hosting and
parsing html form data in R using either 'httpuv' or 'Rhttpd'.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -c
rm -f webutils/tests/testthat/test-echo.R # unconditional suggest, should be fixed

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
