%global source0_hash 8949c1df4b933b1d324e02ce49f1834a4b73dd25fa8103579e0ed105149e080e
Name:           imv
Version:        5.0.1
Release:        1%{?dist}
Summary:        Image viewer for X11 and Wayland
License:        MIT
URL:            https://sr.ht/~exec64/imv/
%global forgeurl https://git.sr.ht/~exec64/imv
Source0:        %{forgeurl}/archive/v%{version}.tar.gz#/%{name}-%{version}.tar.gz
Patch:          %{forgeurl}/commit/5f8997ca.patch#/imv-5.0.1-Convert-LibTIFF-output-to-RGBA-byte-order.patch
# oreon:deps
BuildRequires:  /usr/bin/xxd
BuildRequires:  asciidoc
BuildRequires:  desktop-file-utils
BuildRequires:  gcc
BuildRequires:  meson
BuildRequires:  pkgconfig(cmocka)
BuildRequires:  pkgconfig(egl)
BuildRequires:  pkgconfig(gl)
BuildRequires:  pkgconfig(icu-uc)
BuildRequires:  pkgconfig(inih)
BuildRequires:  pkgconfig(libheif)
BuildRequires:  pkgconfig(libjxl)
BuildRequires:  pkgconfig(libnsbmp)
BuildRequires:  pkgconfig(libnsgif)
BuildRequires:  pkgconfig(libpng)
BuildRequires:  pkgconfig(librsvg-2.0)
BuildRequires:  pkgconfig(libtiff-4)
BuildRequires:  pkgconfig(libturbojpeg)
BuildRequires:  pkgconfig(libwebpdecoder)
BuildRequires:  pkgconfig(pangocairo)
BuildRequires:  pkgconfig(wayland-client)
BuildRequires:  pkgconfig(wayland-cursor)
BuildRequires:  pkgconfig(wayland-egl)
BuildRequires:  pkgconfig(wayland-protocols)
BuildRequires:  pkgconfig(x11)
BuildRequires:  pkgconfig(xcb)
BuildRequires:  pkgconfig(xkbcommon)
BuildRequires:  pkgconfig(xkbcommon-x11)
BuildRequires:  qoi-devel
BuildRequires:  qoi-static
# /oreon:deps
%description
imv is a command line image viewer intended for use with tiling window managers.
Features:
 - Native Wayland and X11 support
 - Support for dozens of image formats including: PNG, JPEG, animated GIFs, SVG,
    TIFF, various RAW formats, Photoshop PSD files
 - Configurable key bindings and behavior
 - Highly scriptable with IPC via imv-msg

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%global oreon_srcdir %{name}-v%{version}
%oreon_prep
%build

%meson
%meson_build
%install
%meson_install
for manfile in %{name}-wayland.1 %{name}-x11.1; do
    ln -sf %{name}.1 %{buildroot}%{_mandir}/man1/$manfile
done
%oreon_autofiles main

%check

%meson_test
desktop-file-validate \
    %{buildroot}/%{_datadir}/applications/imv.desktop \
    %{buildroot}/%{_datadir}/applications/imv-dir.desktop
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
