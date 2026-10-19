%global source0_hash e54e6acdc11e6f19c691c6e069fa9d54934c37b0f4b78cd5e835ce9512866ba6
%undefine _strict_symbol_defs_build
Name:           pragha
Version:        1.3.4
Release:        1%{?dist}
Summary:        Lightweight GTK+ music manager
License:        GPL-3.0-or-later
URL:            https://github.com/pragha-music-player/pragha
Source0:        https://github.com/pragha-music-player/pragha/releases/download/v%{version}/pragha-%{version}.tar.bz2
Patch0: pragha-c99-1.patch
Patch1: pragha-c99-2.patch
Requires:       gstreamer1-plugins-base
# oreon:deps
BuildRequires:  desktop-file-utils
BuildRequires:  gcc
BuildRequires:  gettext
BuildRequires:  intltool
BuildRequires:  make
BuildRequires:  pkgconfig(gio-2.0)
BuildRequires:  pkgconfig(grilo-0.3)
BuildRequires:  pkgconfig(gstreamer-1.0)
BuildRequires:  pkgconfig(gstreamer-audio-1.0)
BuildRequires:  pkgconfig(gstreamer-base-1.0)
BuildRequires:  pkgconfig(gstreamer-interfaces-1.0)
BuildRequires:  pkgconfig(gtk+-3.0)
BuildRequires:  pkgconfig(gudev-1.0)
BuildRequires:  pkgconfig(keybinder-3.0)
BuildRequires:  pkgconfig(libcddb)
BuildRequires:  pkgconfig(libcdio)
BuildRequires:  pkgconfig(libcdio_paranoia)
BuildRequires:  pkgconfig(libclastfm)
BuildRequires:  pkgconfig(libmtp)
BuildRequires:  pkgconfig(libnotify)
BuildRequires:  pkgconfig(libpeas-1.0)
BuildRequires:  pkgconfig(libpeas-gtk-1.0)
BuildRequires:  pkgconfig(libsoup-2.4)
BuildRequires:  pkgconfig(libxfce4ui-2)
BuildRequires:  pkgconfig(sqlite3)
BuildRequires:  pkgconfig(taglib_c)
BuildRequires:  totem-pl-parser-devel
# /oreon:deps
%description
Pragha is is a lightweight GTK+ music manager that aims to be fast, bloat-free,
and light on memory consumption. It is written completely in C and GTK+.

Pragha is a fork of Consonance Music Manager, discontinued by the original
author.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1

# Hack to support grilo 0.3
sed -i -e 's/grilo-0\.2/grilo-0.3/g' configure

%build

%configure
make %{?_smp_mflags} V=1
%install
make install DESTDIR=%{buildroot} INSTALL='install -p'
desktop-file-install                                       \
  --delete-original                                        \
  --add-category=Audio                                     \
  --dir=%{buildroot}%{_datadir}/applications          \
  %{buildroot}%{_datadir}/applications/%{name}.desktop
%find_lang %{name}
rm -rf %{buildroot}%{_datadir}/doc/%{name}
find %{buildroot}%{_libdir}/pragha -name \*.ls -exec rm -f {} \;
%oreon_autofiles main

%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
