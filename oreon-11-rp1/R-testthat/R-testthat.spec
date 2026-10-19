%global source0_hash 5d2e2fa2c3dcb523afb6898c02be9544c24c1c7e0789149c436fef768a409808
Name:           R-testthat
Version:        %R_rpm_version 3.3.2
Release:        1%{?dist}
Summary:        Unit Testing for R
License:        MIT
URL:            %{cran_url}
Source0:        https://cran.r-project.org/package=testthat&version=%{version}#/testthat_%{version}.tar.gz
ExcludeArch:    %{ix86}
# oreon:deps
BuildRequires:  R-devel
# /oreon:deps
%description
A unit testing system designed to be fun, flexible, and easy to set up.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -c
rm -f testthat/tests/testthat/test-expect-known.R # unconditional suggest, should be fixed

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
