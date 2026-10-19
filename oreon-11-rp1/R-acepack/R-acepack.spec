%global source0_hash 653093e308f0dea5ec2719985a01aff700d5795074b3f5239b34632bf45ebadf
Name:           R-acepack
Version:        %R_rpm_version 1.6.3
Release:        1%{?dist}
Summary:        ACE and AVAS methods for choosing regression transformations
License:        LicenseRef-Callaway-Public-Domain AND LicenseRef-Callaway-MIT
URL:            %{cran_url}
Source0:        https://cran.r-project.org/package=acepack&version=%{version}#/acepack_%{version}.tar.gz
ExcludeArch:    %{ix86}
# oreon:deps
BuildRequires:  R-devel
# /oreon:deps
%description
ACE and AVAS (additivity and variance stabilization) are used to estimate 
transformations for regression.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -c
mkdir -p acepack/inst
cp %{SOURCE1} acepack/inst/NOTICE.txt

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
