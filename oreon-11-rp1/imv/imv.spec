%global source0_hash 8949c1df4b933b1d324e02ce49f1834a4b73dd25fa8103579e0ed105149e080e

Name:           imv
Version:        5.0.1
Release:        %autorelease
Summary:        Image viewer for X11 and Wayland

License:        MIT
URL:            https://sr.ht/~exec64/imv/
%global forgeurl https://git.sr.ht/~exec64/imv
Source:         %{forgeurl}/archive/v%{version}.tar.gz#/%{name}-%{version}.tar.gz
Patch:          %{forgeurl}/commit/5f8997ca.patch#/imv-5.0.1-Convert-LibTIFF-output-to-RGBA-byte-order.patch

BuildRequires:  /usr/bin/xxd
BuildRequires:  asciidoc
BuildRequires:  desktop-file-utils
BuildRequires:  gcc
BuildRequires:  meson
BuildRequires:  pkgconfig(cmocka)
BuildRequires:  pkgconfig(gl)
BuildRequires:  pkgconfig(icu-uc)
BuildRequires:  pkgconfig(inih)
BuildRequires:  pkgconfig(pangocairo)
BuildRequires:  pkgconfig(xkbcommon)
# wayland
BuildRequires:  pkgconfig(egl)
BuildRequires:  pkgconfig(wayland-client)
BuildRequires:  pkgconfig(wayland-cursor)
BuildRequires:  pkgconfig(wayland-egl)
BuildRequires:  pkgconfig(wayland-protocols)
# x11
BuildRequires:  pkgconfig(x11)
BuildRequires:  pkgconfig(xcb)
BuildRequires:  pkgconfig(xkbcommon-x11)
# backends
BuildRequires:  pkgconfig(libheif) >= 1.13.0
BuildRequires:  pkgconfig(libjxl)
BuildRequires:  pkgconfig(libnsbmp)
BuildRequires:  pkgconfig(libnsgif) >= 1.0.0
BuildRequires:  pkgconfig(libpng)
BuildRequires:  pkgconfig(librsvg-2.0) >= 2.44
BuildRequires:  pkgconfig(libtiff-4)
BuildRequires:  pkgconfig(libturbojpeg)
BuildRequires:  pkgconfig(libwebpdecoder)
BuildRequires:  qoi-devel
BuildRequires:  qoi-static

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

%autosetup -p1 -n %{name}-v%{version}

%build
%meson
%meson_build

%install
%meson_install
# install platform-specific manuals
for manfile in %{name}-wayland.1 %{name}-x11.1; do
    ln -sf %{name}.1 %{buildroot}%{_mandir}/man1/$manfile
done

%check
%meson_test
desktop-file-validate \
    %{buildroot}/%{_datadir}/applications/imv.desktop \
    %{buildroot}/%{_datadir}/applications/imv-dir.desktop

%files
%license LICENSE
%doc README.md
%config(noreplace) %{_sysconfdir}/%{name}_config
%{_bindir}/%{name}
%{_bindir}/%{name}-dir
%{_bindir}/%{name}-msg
%{_bindir}/%{name}-wayland
%{_bindir}/%{name}-x11
%{_datadir}/applications/%{name}.desktop
%{_datadir}/applications/%{name}-dir.desktop
%{_mandir}/man1/%{name}*
%{_mandir}/man5/%{name}*

%changelog
%autochangelog
