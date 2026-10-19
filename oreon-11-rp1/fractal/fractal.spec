%global source0_hash f66e5a06521cdb2999d25acf6ecfdc23ffff3b98b77e19a853c8c19748e92ad2
%global tarball_version %%(echo %{version} | tr '~' '.')
%global __brp_mangle_shebangs_exclude_from /usr/src/debug/.*\.rs
%global rustflags_debuginfo 1
Name:           fractal
Version:        14.1
Release:        1%{?dist}
Summary:        Matrix group messaging app
License:        GPL-3.0-or-later AND (Apache-2.0 OR MIT) AND BSD-3-Clause AND (0BSD OR MIT OR Apache-2.0) AND Apache-2.0 AND (Apache-2.0 OR BSL-1.0) AND (Apache-2.0 OR ISC OR MIT) AND (Apache-2.0 OR MIT) AND Apache-2.0 WITH LLVM-exception AND (Apache-2.0 WITH LLVM-exception OR Apache-2.0 OR MIT) AND BSD-2-Clause AND (BSD-2-Clause OR Apache-2.0 OR MIT) AND BSD-3-Clause AND (CC0-1.0 OR Apache-2.0) AND (CC0-1.0 OR MIT-0 OR Apache-2.0) AND MIT AND (MIT OR Apache-2.0) AND (MIT OR Apache-2.0 OR BSD-1-Clause) AND (MIT OR Apache-2.0 OR NCSA) AND (MIT OR Apache-2.0 OR Zlib) AND (MIT OR Zlib OR Apache-2.0) AND MPL-2.0 AND MPL-2.0+ AND (Unlicense OR MIT) AND Zlib AND (Zlib OR Apache-2.0 OR MIT)
URL:            https://gitlab.gnome.org/World/fractal
Source0:        https://gitlab.gnome.org/World/%{name}/-/archive/%{version}/%{name}-%{version}.tar.bz2
Source1:        fractal-%{version}-vendor.tar.bz2
Patch0:          cargo-vendor.patch
ExcludeArch:    %{ix86}
Requires:       glycin-loaders%{?_isa}
Requires:       gstreamer1-plugin-gtk4%{?_isa}
# oreon:deps
BuildRequires:  /usr/bin/appstream-util
BuildRequires:  /usr/bin/desktop-file-validate
BuildRequires:  blueprint-compiler
BuildRequires:  cargo
BuildRequires:  cargo-rpm-macros
BuildRequires:  clang-devel
BuildRequires:  grass-compiler
BuildRequires:  llvm-devel
BuildRequires:  meson
BuildRequires:  pkgconfig(gio-2.0)
BuildRequires:  pkgconfig(glib-2.0)
BuildRequires:  pkgconfig(gstreamer-1.0)
BuildRequires:  pkgconfig(gstreamer-base-1.0)
BuildRequires:  pkgconfig(gstreamer-pbutils-1.0)
BuildRequires:  pkgconfig(gstreamer-play-1.0)
BuildRequires:  pkgconfig(gstreamer-video-1.0)
BuildRequires:  pkgconfig(gtk4)
BuildRequires:  pkgconfig(gtksourceview-5)
BuildRequires:  pkgconfig(lcms2)
BuildRequires:  pkgconfig(libadwaita-1)
BuildRequires:  pkgconfig(libpipewire-0.3)
BuildRequires:  pkgconfig(libseccomp)
BuildRequires:  pkgconfig(libwebp)
BuildRequires:  pkgconfig(openssl)
BuildRequires:  pkgconfig(shumate-1.0)
BuildRequires:  pkgconfig(sqlite3)
BuildRequires:  pkgconfig(xdg-desktop-portal)
BuildRequires:  rustc
# /oreon:deps
%description
Fractal is a Matrix messaging app for GNOME written in Rust. Its interface is
optimized for collaboration in large groups, such as free software projects.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%autosetup -n fractal-%{tarball_version} -p1 -a1
sed -i -e '/\(gtk_update_icon_cache\|glib_compile_schemas\|update_desktop_database\)/s/true/false/' meson.build
%oreon_vendor_cargo
%build

%meson
%meson_build
%cargo_license_summary
%{cargo_license} > LICENSE.dependencies
%cargo_vendor_manifest
sed 's/\(.*\) (.*#\(.*\))/\1+git\2/' -i cargo-vendor.txt
%install
%meson_install
%find_lang fractal
%oreon_autofiles main

%check

appstream-util validate-relax --nonet $RPM_BUILD_ROOT%{_datadir}/metainfo/*.metainfo.xml
desktop-file-validate $RPM_BUILD_ROOT%{_datadir}/applications/*.desktop
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
