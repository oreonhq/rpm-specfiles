%global source0_hash 98f3d77713a2e3a10fcb09c365c92fa96ab84bf157e59bd3f4d4d274ce0496e8

%global tarball_version %%(echo %{version} | tr '~' '_')

Name:           sfwbar
Version:        1.0~beta16.1
Release:        %autorelease
Summary:        S* Floating Window Bar

# Icons are from yr.no and are licensed under MIT license
License:        GPL-3.0-only AND MIT
URL:            https://github.com/LBCrion/sfwbar
Source0:        %{url}/archive/v%{tarball_version}/%{name}-%{tarball_version}.tar.gz

BuildRequires:  gcc
BuildRequires:  make
BuildRequires:  meson
BuildRequires:  python3-docutils
BuildRequires:  pkgconfig(alsa)
BuildRequires:  pkgconfig(gio-2.0)
BuildRequires:  pkgconfig(gio-unix-2.0)
BuildRequires:  pkgconfig(glib-2.0)
BuildRequires:  pkgconfig(gmodule-2.0)
BuildRequires:  pkgconfig(gtk-layer-shell-0)
BuildRequires:  pkgconfig(gtk+-3.0)
BuildRequires:  pkgconfig(json-c)
BuildRequires:  pkgconfig(libmpdclient)
BuildRequires:  pkgconfig(libpulse-mainloop-glib)
BuildRequires:  pkgconfig(libpulse)
BuildRequires:  pkgconfig(wayland-client)
BuildRequires:  pkgconfig(wayland-protocols) >= 1.17
BuildRequires:  pkgconfig(xkbregistry)

Requires:       hicolor-icon-theme

%description
SFWBar (S* Floating Window Bar) is a flexible taskbar application for wayland
compositors, designed with a stacking layout in mind. Originally developed for
Sway, SFWBar will work with any wayland compositor supporting layer shell
protocol, the taskbar and window switcher functionality shall work with any
compositor supporting foreign toplevel protocol, but the pager, and window
placement functionality require sway (or at least i3 IPC support).

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1 -n %{name}-%{tarball_version}

%build
%meson
%meson_build

%install
%meson_install

%files
%doc README.md doc/ChangeLog
%license LICENSE
# Icons license file:
# %%{_datadir}/%%{name}/icons/weather/LICENSE
%{_bindir}/%{name}
%{_datadir}/%{name}/
%{_datadir}/icons/hicolor/scalable/*/*.svg
%{_libdir}/%{name}/
%{_mandir}/man1/*.1*

%changelog
%autochangelog
