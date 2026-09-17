%global source0_hash aeea5986a596dd953e2997421a25e45923928c6286c4c8c36e5ef63ca1c2a75a

Name:           lv2-mdala-plugins
Version:        1.2.10
Release:        10%{?dist}
Summary:        A collection of LV2 plugins ported from the MDA VST plugins

# BSD for waflib
# Automatically converted from old format: GPLv3+ and BSD - review is highly recommended.
License:        GPL-3.0-or-later AND LicenseRef-Callaway-BSD
URL:            https://drobilla.net
Source0:        https://download.drobilla.net/mda-lv2-%{version}.tar.xz

BuildRequires:  gcc-c++
BuildRequires:  lv2-devel
BuildRequires:  meson
Requires:       lv2

%description
A collection of LV2 plugins including delay, tube distortion, compressor,
LPF, HPF, phaser, reverb, and utilities, all featuring GUIs.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n mda-lv2-%{version}

%build
# tests require lv2lint
%meson -Dtests=disabled
%meson_build

%install
%meson_install

%files
%doc NEWS README.md
%license LICENSES/CC0-1.0.txt LICENSES/GPL-2.0-or-later.txt LICENSES/MIT.txt
%{_libdir}/lv2/mda.lv2/

%changelog
%autochangelog
