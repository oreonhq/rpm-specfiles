%global source0_hash 13fa9990565ef917902f777cfce091ab60adb8a114a9f6cca274dfc5c0aae661
%bcond_without check
%if 0%{?rhel} || (0%{?oreon} >= 11)
%bcond_without bundled_rust_deps
%else
%bcond_with bundled_rust_deps
%endif
%global tarball_version %(echo %{version} | tr '~' '.')
Name:           loupe
Version:        51.0
Release:        1%{?dist}
Summary:        Image viewer
License:        %{shrink:
    GPL-3.0-or-later AND
    BSD-3-Clause AND
    ISC AND
    MIT AND
    Unicode-3.0 AND
    Unicode-DFS-2016 AND
    (Apache-2.0 OR MIT) AND
    (Apache-2.0 WITH LLVM-exception OR Apache-2.0 OR MIT) AND
    (BSD-2-Clause OR Apache-2.0 OR MIT) AND
    (MIT OR Zlib OR Apache-2.0) AND
    (MPL-2.0 OR LGPL-2.1-or-later) AND
    (Unlicense OR MIT)
}
URL:            https://gitlab.gnome.org/GNOME/loupe
Source0:        https://download.gnome.org/sources/%{name}/51/%{name}-%{version}.tar.xz
ExcludeArch:    %{ix86}
%if 0%{?rhel} || (0%{?oreon} >= 11)
%else
%endif
%if %{with bundled_rust_deps}
%endif
Requires:       dbus
Requires:       glycin-loaders >= 1.1
Requires:       hicolor-icon-theme
# oreon:deps
BuildRequires:  /usr/bin/appstream-util
BuildRequires:  /usr/bin/desktop-file-validate
BuildRequires:  cargo
BuildRequires:  cargo-rpm-macros
BuildRequires:  itstool
BuildRequires:  meson
BuildRequires:  rustc
# /oreon:deps
%description
An image viewer application written with GTK 4, Libadwaita and Rust.

Features:

- Fast GPU accelerated image rendering with tiled rendering for SVGs
- Extendable and sandboxed (expect SVG) image decoding
- Support for more than 15 image formats by default
- Extensive support for touchpad and touchscreen gestures
- Accessible presentation of the most important metadata
- Sleek but powerful interface developed in conjunction with GNOME Human
  Interface Guidelines

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%if %{with bundled_rust_deps}
%autosetup -n loupe-%{tarball_version} -p1
cargo vendor --versioned-dirs
%else
%autosetup -n loupe-%{tarball_version} -p1
sed -i -e '/Cargo.lock/d' meson.build
%endif
%if %{without bundled_rust_deps}
%oreon_vendor_cargo
%build

%meson
%meson_build
%cargo_license_summary
%{cargo_license} > LICENSE.dependencies
%if %{with bundled_rust_deps}
%cargo_vendor_manifest
%endif
%install
%meson_install
%find_lang loupe --with-gnome
%oreon_autofiles main
%if %{with check}
%check

%meson_test
appstream-util validate-relax --nonet $RPM_BUILD_ROOT%{_metainfodir}/org.gnome.Loupe.metainfo.xml
desktop-file-validate $RPM_BUILD_ROOT%{_datadir}/applications/org.gnome.Loupe.desktop
%endif
%files -f %{oreon_filedir}/main.list

%changelog

* Mon May 25 2026 Oreon Packaging Team <packaging@oreonhq.com> - 50.0-1
- Import
%endif
