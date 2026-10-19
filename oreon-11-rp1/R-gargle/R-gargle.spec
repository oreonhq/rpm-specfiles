%global source0_hash e4a33f23c2ad917782fff1902e23f2a4c6c333c6389f6bfe8350577ddb6af6e6
Name:           R-gargle
Version:        %R_rpm_version 1.6.0
Release:        1%{?dist}
Summary:        Utilities for Working with Google APIs
License:        MIT
URL:            %{cran_url}
Source0:        https://cran.r-project.org/package=gargle&version=%{version}#/gargle_%{version}.tar.gz
BuildArch:      noarch
# oreon:deps
BuildRequires:  R-devel
# /oreon:deps
%description
Provides utilities for working with Google APIs
<https://developers.google.com/apis-explorer>.  This includes functions and
classes for handling common credential types and for preparing, executing, and
processing HTTP requests.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -c
rm -f gargle/tests/testthat/test-secret.R # unconditional suggest

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
