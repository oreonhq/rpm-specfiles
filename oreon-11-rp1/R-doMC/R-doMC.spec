%global source0_hash b2186f851448251ae6af5d14b9e3e7f9221f90887e5f8de6a68c91caf16619a3
Name:           R-doMC
Version:        %R_rpm_version 1.3.8
Release:        1%{?dist}
Summary:        Foreach Parallel Adaptor for 'parallel'
License:        GPL-2.0-only
URL:            %{cran_url}
Source0:        https://cran.r-project.org/package=doMC&version=%{version}#/doMC_%{version}.tar.gz
BuildArch:      noarch
# oreon:deps
BuildRequires:  R-devel
# /oreon:deps
%description
Provides a parallel backend for the %%dopar%% function using the multicore
functionality of the parallel package.

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
