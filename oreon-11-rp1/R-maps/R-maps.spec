%global source0_hash 3b6d4945330041280ddb3f89fbe0d7dbcf124befef94e8d77e809122d8d588b8
Name:           R-maps
Version:        %R_rpm_version 3.4.3
Release:        1%{?dist}
Summary:        Draw Geographical Maps
License:        GPL-2.0-only
URL:            %{cran_url}
Source0:        https://cran.r-project.org/package=maps&version=%{version}#/maps_%{version}.tar.gz
ExcludeArch:    %{ix86}
# oreon:deps
BuildRequires:  R-devel
# /oreon:deps
%description
Display of maps.  Projection code and larger maps are in separate packages
('mapproj' and 'mapdata').

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
