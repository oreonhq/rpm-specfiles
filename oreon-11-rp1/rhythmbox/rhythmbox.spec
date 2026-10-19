%global source0_hash 8ee7d1714481956023b464264ebe0bd50217d4b472b1c5b3a6254ff8da924093
%global gtk3_version 3.20.0
%global libdmapsharing_version 3.9.11
%global libsecret_version 0.18
%global __provides_exclude_from ^%{_libdir}/%{name}/plugins/.*/.*\\.so.*$
Name:    rhythmbox
Version: 3.5.1
Release:        1%{?dist}
Summary:        Music Management Application
License: LicenseRef-Callaway-GPLv2+-with-exceptions AND GFDL-1.1-no-invariants-or-later
URL:     https://wiki.gnome.org/Apps/Rhythmbox
Source0:        https://download.gnome.org/sources/%{name}/3.5/%{name}-%{version}.tar.xz
ExcludeArch:    s390 s390x
Requires: gtk3%{?_isa} >= %{gtk3_version}
Requires: libdmapsharing4%{?_isa} >= %{libdmapsharing_version}
Requires: libpeas-loader-python3%{?_isa}
Requires: libsecret%{?_isa} >= %{libsecret_version}
Requires: media-player-info
Requires: python3-gobject
Requires: python3-mako
Requires: gstreamer1-plugins-good
Suggests: zeitgeist-libs%{?_isa}
Obsoletes: rhythmbox-upnp < %{version}-%{release}
Provides: rhythmbox-upnp = %{version}-%{release}
Obsoletes: rhythmbox-lirc < %{version}-%{release}
Provides: rhythmbox-lirc = %{version}-%{release}
# oreon:deps
BuildRequires:  /usr/bin/desktop-file-validate
BuildRequires:  gettext
BuildRequires:  intltool
BuildRequires:  itstool
BuildRequires:  kernel-headers
BuildRequires:  meson
BuildRequires:  pkgconfig(gobject-introspection-1.0)
BuildRequires:  pkgconfig(grilo-0.3)
BuildRequires:  pkgconfig(gstreamer-1.0)
BuildRequires:  pkgconfig(gstreamer-pbutils-1.0)
BuildRequires:  pkgconfig(gtk+-3.0)
BuildRequires:  pkgconfig(gudev-1.0)
BuildRequires:  pkgconfig(json-glib-1.0)
BuildRequires:  pkgconfig(libbrasero-media3)
BuildRequires:  pkgconfig(libdmapsharing-4.0)
BuildRequires:  pkgconfig(libmtp)
BuildRequires:  pkgconfig(libnotify)
BuildRequires:  pkgconfig(libpeas-gtk-1.0)
BuildRequires:  pkgconfig(libsecret-1)
BuildRequires:  pkgconfig(libsoup-3.0)
BuildRequires:  pkgconfig(libxml-2.0)
BuildRequires:  pkgconfig(pygobject-3.0)
BuildRequires:  pkgconfig(tdb)
BuildRequires:  pkgconfig(totem-plparser)
BuildRequires:  python3-devel
BuildRequires:  vala
BuildRequires:  yelp-tools
# /oreon:deps
%description
Rhythmbox is an integrated music management application based on the powerful
GStreamer media framework. It has a number of features, including an easy to
use music browser, searching and sorting, comprehensive audio format support
through GStreamer, Internet Radio support, playlists and more.

Rhythmbox is extensible through a plugin system.

%package devel
Summary: Development files for Rhythmbox plugins
Requires: %{name}%{?_isa} = %{version}-%{release}
%description devel
This package contains the development files necessary to create
a Rhythmbox plugin.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%oreon_prep
%build

%meson \
    -Ddaap=enabled \
    -Dlirc=disabled
%meson_build
%install
%meson_install
%py_byte_compile %{__python3} %{buildroot}%{_libdir}/rhythmbox
%find_lang %name --with-gnome
rm -rf %{buildroot}%{_libdir}/rhythmbox/plugins/*/*.h
rm -rf %{buildroot}%{_libdir}/rhythmbox/plugins/context
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*

%check

desktop-file-validate %{buildroot}/%{_datadir}/applications/org.gnome.Rhythmbox3*.desktop
%ldconfig_scriptlets
%files -f %{oreon_filedir}/main.list
%files -n rhythmbox-devel -f %{oreon_filedir}/rhythmbox-devel.list

%changelog

* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 3.4.9-1
- Prepare for Oreon 11 (RP1)
