%global source0_hash 5bf884ee031fbf3f5c60bcedc0532e4b77763e924a1508f584329aae9686187c
Name:           R-svglite
Version:        %R_rpm_version 2.2.2
Release:        1%{?dist}
Summary:        An 'SVG' Graphics Device
License:        GPL-2.0-or-later AND BSL-1.0
URL:            %{cran_url}
Source0:        https://cran.r-project.org/package=svglite&version=%{version}#/svglite_%{version}.tar.gz
ExcludeArch:    %{ix86}
# oreon:deps
BuildRequires:  R-devel
BuildRequires:  libpng-devel
# /oreon:deps
%description
A graphics device for R that produces 'Scalable Vector Graphics'. 'svglite'
is a fork of the older 'RSvgDevice' package.

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
