%global source0_hash 4bdf9c0481a83037da1d0fa26d2c2c6a80cb736458fd18fde14acaf7924874c6
%global geoclue2_version 2.6.0
%global gtk4_version 4.5
%global libadwaita_version 1.5
%global tarball_version %(echo %{version} | tr '~' '.')
%global major_version %(echo %{tarball_version} | cut -d "." -f 1)
Name:           gnome-clocks
Version:        51.0
Release:        1%{?dist}
Summary:        Clock application designed for GNOME 3
License:        GPL-2.0-or-later AND CC-BY-SA-3.0 AND CC0-1.0
URL:            https://wiki.gnome.org/Apps/Clocks
Source0:        https://download.gnome.org/sources/%{name}/51/%{name}-%{version}.tar.xz
Requires:       geoclue2-libs%{?_isa} >= %{geoclue2_version}
Requires:       gtk4%{?_isa} >= %{gtk4_version}
Requires:       libadwaita%{?_isa} >= %{libadwaita_version}
# oreon:deps
BuildRequires:  /usr/bin/oggenc
BuildRequires:  desktop-file-utils
BuildRequires:  gettext
BuildRequires:  itstool
BuildRequires:  libappstream-glib
BuildRequires:  meson
BuildRequires:  pkgconfig(geocode-glib-2.0)
BuildRequires:  pkgconfig(glib-2.0)
BuildRequires:  pkgconfig(gnome-desktop-4)
BuildRequires:  pkgconfig(gobject-2.0)
BuildRequires:  pkgconfig(gsound)
BuildRequires:  pkgconfig(gtk4)
BuildRequires:  pkgconfig(gweather4)
BuildRequires:  pkgconfig(libadwaita-1)
BuildRequires:  pkgconfig(libgeoclue-2.0)
BuildRequires:  vala
# /oreon:deps
%description
Clock application designed for GNOME 3

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
# check for human errors
if [ `echo "%{version}" | grep -cE "\.alpha|\.beta|\.rc"` = "1" ]; then echo "Error: Use tilde in Version field in front of alpha/beta/rc; checked '%{version}'" 1>&2; exit 1; fi

%autosetup -p1 -n %{name}-%{tarball_version}

%build

%meson
%meson_build
%install
%meson_install
%find_lang gnome-clocks --with-gnome
%oreon_autofiles main

%check

desktop-file-validate $RPM_BUILD_ROOT%{_datadir}/applications/org.gnome.clocks.desktop
%files -f %{oreon_filedir}/main.list

%changelog

* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 50.0-1
- Prepare for Oreon 11 (RP1)
