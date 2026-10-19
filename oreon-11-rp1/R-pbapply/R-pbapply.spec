%global source0_hash 6a5c7110a6bf13735374d3b2e75b32ec0e0f0276ad95e928d2c802b53ff1302d
Name:           R-pbapply
Version:        %R_rpm_version 1.7-4
Release:        1%{?dist}
Summary:        Adding Progress Bar to '*apply' Functions
License:        GPL-2.0-only
URL:            %{cran_url}
Source0:        https://cran.r-project.org/package=pbapply&version=1.7-4#/pbapply_1.7-4.tar.gz
BuildArch:      noarch
# oreon:deps
BuildRequires:  R-devel
# /oreon:deps
%description
A lightweight package that adds progress bar to vectorized R functions 
('*apply'). The implementation can easily be added to functions where
showing the progress is useful (e.g. bootstrap). The type and style of
the progress bar (with percentages or remaining time) can be set through
options. Supports several parallel processing backends.

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
