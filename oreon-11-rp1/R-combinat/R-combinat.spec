%global source0_hash 1513cf6b6ed74865bfdd9f8ca58feae12b62f38965d1a32c6130bef810ca30c1
Name:           R-combinat
Version:        %R_rpm_version 0.0-8
Release:        1%{?dist}
Summary:        R routines for combinatorics
License:        GPL-2.0-only
URL:            %{cran_url}
Source0:        https://cran.r-project.org/package=combinat&version=0.0-8#/combinat_0.0-8.tar.gz
BuildArch:      noarch
# oreon:deps
BuildRequires:  R-devel
# /oreon:deps
%description
R routines for combinatorics

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -c
[ -f combinat/NAMESPACE ] || echo 'exportPattern("^[^\\.]")' > combinat/NAMESPACE

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
