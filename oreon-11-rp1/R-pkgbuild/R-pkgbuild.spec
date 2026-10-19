%global source0_hash 2e4259202ce90fc452f31ff36cfe14ff21a38e9fd71c3015e25018b9079924cb
Name:           R-pkgbuild
Version:        %R_rpm_version 1.4.8
Release:        1%{?dist}
Summary:        Find Tools Needed to Build R Packages
License:        MIT
URL:            %{cran_url}
Source0:        https://cran.r-project.org/package=pkgbuild&version=%{version}#/pkgbuild_%{version}.tar.gz
BuildArch:      noarch
# oreon:deps
BuildRequires:  R-devel
# /oreon:deps
%description
Provides functions used to build R packages. Locates compilers needed to
build R packages on various platforms and ensures the PATH is configured
appropriately so R can use them.

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
