Name:           weston
Version:        13.0.1
Release:        2%{?dist}
Summary:        Reference Wayland compositor
License:        MIT
URL:            https://gitlab.freedesktop.org/wayland/weston
Source0:        https://gitlab.freedesktop.org/wayland/weston/-/releases/%{version}/downloads/%{name}-%{version}.tar.xz

BuildRequires:  meson
BuildRequires:  gcc
BuildRequires:  cairo-devel
BuildRequires:  glib2-devel
BuildRequires:  lcms2-devel
BuildRequires:  libdisplay-info-devel
BuildRequires:  libdrm-devel
BuildRequires:  libevdev-devel
BuildRequires:  libinput-devel
BuildRequires:  libjpeg-devel
BuildRequires:  libpng-devel
BuildRequires:  libseat-devel
BuildRequires:  libva-devel
BuildRequires:  libwebp-devel
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

%description
Weston is the reference Wayland compositor with DRM, Wayland, and X11
backends plus demo clients.


%prep
%autosetup -p1


%build
%meson \
  -Dbackend-vnc=false \
  -Dbackend-rdp=false \
  -Dpipewire=false \
  -Dtests=false
%meson_build


%install
%meson_install


%files
%license COPYING
%{_bindir}/*
%{_libdir}/weston
%{_libdir}/libweston-*/*
%{_libdir}/libweston*.so*
%{_includedir}/weston
%{_includedir}/libweston-*
%{_datadir}/wayland-sessions/*
%{_datadir}/weston
%{_mandir}/man*/*
%{_libdir}/pkgconfig/libweston-*.pc


%changelog
* Fri Apr 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 13.0.1-2
- Add Weston compositor reference implementation
