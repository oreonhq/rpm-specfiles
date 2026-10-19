%global source0_hash c92e5604e1e149e00f49fd236c6ab8cd09d96106eb14479f7839e6996bf95e4e
Name:           R-wesanderson
Version:        %R_rpm_version 0.3.7
Release:        1%{?dist}
Summary:        Wes Anderson Palette Generator
License:        MIT
URL:            %{cran_url}
Source0:        https://cran.r-project.org/package=wesanderson&version=%{version}#/wesanderson_%{version}.tar.gz
BuildArch:      noarch
# oreon:deps
BuildRequires:  R-devel
# /oreon:deps
%description
Palettes generated mostly from 'Wes Anderson' movies.

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
