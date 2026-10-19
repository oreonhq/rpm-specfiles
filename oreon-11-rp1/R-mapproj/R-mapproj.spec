%global source0_hash 1210b12d17c9884935a49e8aa5b6963fe1ef67e74d9f7081ffdeb2a6d71d6077
Name:           R-mapproj
Version:        %R_rpm_version 1.2.12
Release:        1%{?dist}
Summary:        Map Projections
License:        LPL-1.02
URL:            %{cran_url}
Source0:        https://cran.r-project.org/package=mapproj&version=%{version}#/mapproj_%{version}.tar.gz
ExcludeArch:    %{ix86}
# oreon:deps
BuildRequires:  R-devel
# /oreon:deps
%description
Converts latitude/longitude into projected coordinates.

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
