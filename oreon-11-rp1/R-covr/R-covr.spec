%global source0_hash 20d3a98c1d751c68115e0dacd9ac46d83a112bbadf1f46da7c9672afee7e8986
Name:           R-covr
Version:        %R_rpm_version 3.6.5
Release:        1%{?dist}
Summary:        Test Coverage for Packages
License:        MIT
URL:            %{cran_url}
Source0:        https://cran.r-project.org/package=covr&version=%{version}#/covr_%{version}.tar.gz
ExcludeArch:    %{ix86}
Provides:       bundled(xstatic-bootstrap-common) = 3.3.5
Provides:       bundled(js-highlight) = 6.2
# oreon:deps
BuildRequires:  R-devel
# /oreon:deps
%description
Track and report code coverage for your package and (optionally) upload the
results to a coverage service like 'Codecov' <https://codecov.io> or
'Coveralls' <https://coveralls.io>. Code coverage is a measure of the amount of
code being exercised by a set of tests. It is an indirect measure of test
quality and completeness. This package is compatible with any testing
methodology or framework and tracks coverage of both R code and compiled
C/C++/FORTRAN code.

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
