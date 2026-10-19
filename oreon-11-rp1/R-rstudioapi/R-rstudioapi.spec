%global source0_hash 9649eef00381d3bde3d96928782e8792d78b9be0a2968e832728b54f5886fdbd
Name:           R-rstudioapi
Version:        %R_rpm_version 0.18.0
Release:        1%{?dist}
Summary:        Safely Access the RStudio API
License:        MIT
URL:            %{cran_url}
Source0:        https://cran.r-project.org/package=rstudioapi&version=%{version}#/rstudioapi_%{version}.tar.gz
BuildArch:      noarch
# oreon:deps
BuildRequires:  R-devel
# /oreon:deps
%description
Access the RStudio API (if available) and provide informative error
messages when it's not.

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
