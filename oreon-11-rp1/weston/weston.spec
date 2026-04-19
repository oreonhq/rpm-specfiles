Name:           weston
Version:        13.0.1
Release:        10%{?dist}
Summary:        Reference Wayland compositor
License:        MIT
URL:            https://gitlab.freedesktop.org/wayland/weston
Source0:        https://gitlab.freedesktop.org/wayland/weston/-/releases/%{version}/downloads/%{name}-%{version}.tar.xz
# libdisplay-info 0.2.x (matches Weston 14 upper bound)
Patch0:         weston-libdisplay-info-0.2.patch

BuildRequires:  meson
BuildRequires:  gcc
BuildRequires:  cairo-devel
BuildRequires:  glib2-devel
BuildRequires:  lcms2-devel
BuildRequires:  libdisplay-info-devel
BuildRequires:  pkgconfig(libdisplay-info)
BuildRequires:  libdrm-devel
BuildRequires:  libevdev-devel
BuildRequires:  libinput-devel
BuildRequires:  libjpeg-devel
BuildRequires:  libpng-devel
BuildRequires:  libseat-devel
BuildRequires:  libva-devel
BuildRequires:  libwebp-devel
BuildRequires:  libXcursor-devel
BuildRequires:  pkgconfig(xcb-cursor)
BuildRequires:  libxkbcommon-devel
BuildRequires:  libxml2-devel
BuildRequires:  mesa-libEGL-devel
BuildRequires:  mesa-libgbm-devel
BuildRequires:  mtdev-devel
BuildRequires:  pam-devel
BuildRequires:  pango-devel
BuildRequires:  pixman-devel
BuildRequires:  systemd-devel
BuildRequires:  wayland-devel
BuildRequires:  wayland-protocols-devel

Requires:       xkeyboard-config
Requires:       libdisplay-info%{?_isa}
Requires:       libseat%{?_isa}

%description
Weston is the reference Wayland compositor with DRM, Wayland, and X11
backends plus demo clients.


%prep
%autosetup -p1


%build
%meson \
  -Dbackend-vnc=false \
  -Dbackend-rdp=false \
  -Dbackend-pipewire=false \
  -Dpipewire=false \
  -Dremoting=false
%meson_build


%install
%meson_install


%files
%license COPYING
%{_bindir}/*
%{_libexecdir}/weston-desktop-shell
%{_libexecdir}/weston-ivi-shell-user-interface
%{_libexecdir}/weston-keyboard
%{_libexecdir}/weston-simple-im
%{_libdir}/weston
%{_libdir}/libweston-*/*
%{_libdir}/libweston*.so*
%{_includedir}/weston
%{_includedir}/libweston-*
%{_datadir}/wayland-sessions/*
%{_datadir}/weston
%{_datadir}/libweston-*/protocols/*
%{_datadir}/pkgconfig/libweston-*-protocols.pc
%{_mandir}/man*/*
%{_libdir}/pkgconfig/libweston-*.pc
%{_libdir}/pkgconfig/weston.pc


%changelog
* Sun Apr 19 2026 Oreon Packaging Team <packaging@oreonhq.com> - 13.0.1-10
- Rebuild for libdisplay-info 0.3 SONAME

* Fri Apr 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 13.0.1-2
- Add Weston compositor reference implementation
