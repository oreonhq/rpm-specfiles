%global source0_hash 08199520c6590e19307b5e6cbfa79fbdbe0ea6ecb690957f31222d4bf8d3792d
Name:           R-mockr
Version:        %R_rpm_version 0.2.2
Release:        1%{?dist}
Summary:        Mocking in R
License:        MIT
URL:            %{cran_url}
Source0:        https://cran.r-project.org/package=mockr&version=%{version}#/mockr_%{version}.tar.gz
BuildArch:      noarch
# oreon:deps
BuildRequires:  R-devel
# /oreon:deps
%description
Provides a means to mock a package function, i.e., temporarily substitute
it for testing. Designed as a drop-in replacement for
'testthat::with_mock()', which may break in R 3.4.0 and later.

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
