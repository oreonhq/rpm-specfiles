%global source0_hash 805d483dc58c041f1616267abeb39cecaaf7271a34e90668a5439383bf9a0d58
Name:           R-biglm
Version:        %R_rpm_version 0.9-3
Release:        1%{?dist}
Summary:        Bounded memory linear and generalized linear models
License:        GPL-1.0-or-later
URL:            %{cran_url}
Source0:        https://cran.r-project.org/package=biglm&version=0.9-3#/biglm_0.9-3.tar.gz
# oreon:deps
BuildRequires:  R-devel
# /oreon:deps
%description
Regression for data too large to fit in memory.

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
