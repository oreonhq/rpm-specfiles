%global source0_hash db73e62a5c536fd16b6549a61d0dd109eff4f94ac6236c52de53bde2230f81d6
Name:           R-packrat
Version:        %R_rpm_version 0.9.3
Release:        1%{?dist}
Summary:        Dependency Management System for R Projects
License:        GPL-2.0-only
URL:            %{cran_url}
Source0:        https://cran.r-project.org/package=packrat&version=%{version}#/packrat_%{version}.tar.gz
BuildArch:      noarch
# oreon:deps
BuildRequires:  R-devel
# /oreon:deps
%description
Manage the R packages your project depends on in an isolated, portable, and
reproducible way.

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
