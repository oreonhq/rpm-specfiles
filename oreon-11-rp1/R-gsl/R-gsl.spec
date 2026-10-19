%global source0_hash 56dec6105a882c7d976765b879d0832b436f0371c174e34a3e37bc390c56ed80
Name:           R-gsl
Version:        %R_rpm_version 2.1-9
Release:        1%{?dist}
Summary:        Wrapper for the Gnu Scientific Library
License:        GPL-3.0-only
URL:            %{cran_url}
Source0:        https://cran.r-project.org/package=gsl&version=2.1-9#/gsl_2.1-9.tar.gz
ExcludeArch:    %{ix86}
# oreon:deps
BuildRequires:  R-devel
BuildRequires:  gsl-devel
# /oreon:deps
%description
An R wrapper for some of the functionality of the Gnu Scientific Library.

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
