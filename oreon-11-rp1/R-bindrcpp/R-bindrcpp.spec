%global source0_hash 662dae785aee715855415f4e743281ccbf0832e426084dc2f0ca9c9c908ec9fa
Name:           R-bindrcpp
Version:        %R_rpm_version 0.2.3
Release:        1%{?dist}
Summary:        An 'Rcpp' Interface to Active Bindings
License:        MIT
URL:            %{cran_url}
Source0:        https://cran.r-project.org/package=bindrcpp&version=%{version}#/bindrcpp_%{version}.tar.gz
ExcludeArch:    %{ix86}
Obsoletes:      %{name}-devel <= 0.2.3
# oreon:deps
BuildRequires:  R-devel
# /oreon:deps
%description
Provides an easy way to fill an environment with active bindings that call
a C++ function.

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
