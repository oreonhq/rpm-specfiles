%global source0_hash 2ed087d6399f247d44e555b69d785b48362445c4c8c77330bbd57d282b49d3e6
Name:           R-hexbin
Version:        %R_rpm_version 1.28.5
Release:        1%{?dist}
Summary:        Hexagonal Binning Routines
License:        GPL-2.0-only
URL:            %{cran_url}
Source0:        https://cran.r-project.org/package=hexbin&version=%{version}#/hexbin_%{version}.tar.gz
ExcludeArch:    %{ix86}
# oreon:deps
BuildRequires:  R-devel
# /oreon:deps
%description
Binning and plotting functions for hexagonal bins.

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
