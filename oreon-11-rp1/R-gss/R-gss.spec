%global source0_hash 11c4c91caf162a4077b2c2611cedfd7fbcfeae679f4438dcb7349c90aa2e7d07
Name:           R-gss
Version:        %R_rpm_version 2.2-10
Release:        1%{?dist}
Summary:        General Smoothing Splines
License:        GPL-2.0-or-later
URL:            %{cran_url}
Source0:        https://cran.r-project.org/package=gss&version=2.2-10#/gss_2.2-10.tar.gz
ExcludeArch:    %{ix86}
# oreon:deps
BuildRequires:  R-devel
# /oreon:deps
%description
A comprehensive package for structural multivariate function estimation
using smoothing splines.

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
