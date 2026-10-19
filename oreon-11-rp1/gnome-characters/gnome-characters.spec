%global source0_hash 8b90e9d7fcff43622ed34677f0029cd74b440185f1639af48c439f63bebadc31
%global appname org.gnome.Characters
%global gjs_version 1.50
%global gtk4_version 4.6
%global libadwaita_version 1.5~alpha
%global tarball_version %(echo %{version} | tr '~' '.')
%global major_version %(echo %{tarball_version} | cut -d "." -f 1)
Name:		gnome-characters
Version:	51.0
Release:        1%{?dist}
Summary:        Character map application for GNOME
License:	BSD-3-Clause AND GPL-2.0-or-later
URL:		https://wiki.gnome.org/Design/Apps/CharacterMap
Source0:        https://download.gnome.org/sources/%{name}/51/%{name}-%{version}.tar.xz
Requires:	gjs >= %{gjs_version}
Requires:	gnome-desktop4%{_isa}
Requires:	gtk4%{_isa} >= %{gtk4_version}
Requires:	libadwaita%{?_isa} >= %{libadwaita_version}
# oreon:deps
BuildRequires:  desktop-file-utils
BuildRequires:  gettext
BuildRequires:  gobject-introspection-devel
BuildRequires:  libappstream-glib
BuildRequires:  libunistring-devel
BuildRequires:  meson
BuildRequires:  pkgconfig(gjs-1.0)
BuildRequires:  pkgconfig(gtk4)
BuildRequires:  pkgconfig(libadwaita-1)
# /oreon:deps
%description
Characters is a simple utility application to find and insert unusual
characters.

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
%find_lang %{appname}
%oreon_autofiles main

%check

desktop-file-validate $RPM_BUILD_ROOT/%{_datadir}/applications/%{appname}.desktop
%files -f %{oreon_filedir}/main.list

%changelog

* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 50.0-1
- Prepare for Oreon 11 (RP1)
