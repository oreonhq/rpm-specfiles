%global source0_hash 8f2090433e60e90d9c4d0326970c845a3cb471951657cd9355d3dbca4040b873
Name:           lv2-mdala-plugins
Version:        1.2.12
Release:        1%{?dist}
Summary:        A collection of LV2 plugins ported from the MDA VST plugins
License:        GPL-3.0-or-later AND LicenseRef-Callaway-BSD
URL:            https://drobilla.net
Source0:        https://download.drobilla.net/mda-lv2-%{version}.tar.xz
Requires:       lv2
# oreon:deps
BuildRequires:  gcc-c++
BuildRequires:  lv2-devel
BuildRequires:  meson
# /oreon:deps
%description
A collection of LV2 plugins including delay, tube distortion, compressor,
LPF, HPF, phaser, reverb, and utilities, all featuring GUIs.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%global oreon_srcdir mda-lv2-%{version}
%oreon_prep
%build

%meson -Dtests=disabled
%meson_build
%install
%meson_install
%oreon_autofiles main

%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
