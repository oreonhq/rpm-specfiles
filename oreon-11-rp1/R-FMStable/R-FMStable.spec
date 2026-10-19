%global source0_hash 2a391061dc2d2e89f6639aada07e839fdf950c0b20e27566219bb89befb4e93a
Name:           R-FMStable
Version:        %R_rpm_version 0.1-4
Release:        1%{?dist}
Summary:        Finite Moment Stable Distributions
License:        GPL-3.0-only
URL:            %{cran_url}
Source0:        https://cran.r-project.org/package=FMStable&version=0.1-4#/FMStable_0.1-4.tar.gz
ExcludeArch:    %{ix86}
# oreon:deps
BuildRequires:  R-devel
# /oreon:deps
%description
This package implements some basic procedures for dealing with log
maximally skew stable distributions, which are also called finite moment
log stable distributions.

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
