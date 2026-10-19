%global source0_hash ece51efa4283a98b3b4b4b9317fce4928b227942115dd84452b481fd6e9d9119
Name:           R-sandwich
Version:        %R_rpm_version 3.1-1
Release:        1%{?dist}
Summary:        Robust Covariance Matrix Estimators
License:        GPL-2.0-or-later
URL:            %{cran_url}
Source0:        https://cran.r-project.org/package=sandwich&version=3.1-1#/sandwich_3.1-1.tar.gz
BuildArch:      noarch
# oreon:deps
BuildRequires:  R-devel
# /oreon:deps
%description
Model-robust standard error estimators for cross-sectional, time series
and longitudinal data.

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
