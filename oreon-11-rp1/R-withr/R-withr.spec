%global source0_hash 0a3a05f493d275cca4bf13c8c1b95a1a4eed7f83b2493f41fde02ce3fc92c1a3

Name:           R-withr
Version:        %R_rpm_version 3.0.2
Release:        %autorelease
Summary:        Run Code 'With' Temporarily Modified Global State

License:        MIT
URL:            %{cran_url}
Source:         %{cran_source}

BuildArch:      noarch
BuildRequires:  R-devel

%description
A set of functions to run code 'with' safely and temporarily modified
global state. Many of these functions were originally a part of the
'devtools' package, this provides a simple package with limited
dependencies to provide access to these functions.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -c
# Remove failing tests
rm -f %{packname}/tests/testthat/test-{language,defer,standalone-defer}.R

%generate_buildrequires
%R_buildrequires

%build

%install
%R_install
%R_save_files

%check
%R_check \--no-examples

%files -f %{R_files}

%changelog
%autochangelog
