%global source0_hash bc1edb7bb16c8b299103f80a52ab8c5fc200cd07a9056578c1f672e9f5019278
Name:           R-polynom
Version:        %R_rpm_version 1.4-1
Release:        1%{?dist}
Summary:        A Class for Univariate Polynomial Manipulations
License:        GPL-2.0-only
URL:            %{cran_url}
Source0:        https://cran.r-project.org/package=polynom&version=1.4-1#/polynom_1.4-1.tar.gz
BuildArch:      noarch
# oreon:deps
BuildRequires:  R-devel
# /oreon:deps
%description
A collection of functions to implement a class for univariate polynomial
manipulations.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%oreon_prep
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
