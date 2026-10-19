%global source0_hash f212a6d812d27b7d766d2b017ae0828f55b460e923161648ec46671c3477346f
Name:           R-bindr
Version:        %R_rpm_version 0.1.3
Release:        1%{?dist}
Summary:        Parametrized Active Bindings
License:        MIT
URL:            %{cran_url}
Source0:        https://cran.r-project.org/package=bindr&version=%{version}#/bindr_%{version}.tar.gz
BuildArch:      noarch
# oreon:deps
BuildRequires:  R-devel
# /oreon:deps
%description
Provides a simple interface for creating active bindings where the bound
function accepts additional arguments.

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
