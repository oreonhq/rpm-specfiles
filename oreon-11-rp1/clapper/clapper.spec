%global source0_hash 344c0f20e540a63c6fb44cdd5de88c168ed145bb66c1307e79b2b08124780118
Name:           clapper
Version:        0.10.0
Release:        1%{?dist}
Summary:        Modern media player powered by GStreamer and GTK4
License:        GPL-3.0-or-later AND LGPL-2.1-or-later
URL:            https://github.com/Rafostar/clapper
Source0:        https://github.com/Rafostar/%{name}/archive/%{version}/%{name}-%{version}.tar.gz
Requires:       hicolor-icon-theme
# oreon:deps
BuildRequires:  desktop-file-utils
BuildRequires:  gcc
BuildRequires:  gettext
BuildRequires:  gi-docgen
BuildRequires:  gobject-introspection-devel
BuildRequires:  graphviz
BuildRequires:  libappstream-glib
BuildRequires:  meson
BuildRequires:  pkgconfig(gio-2.0)
BuildRequires:  pkgconfig(gio-unix-2.0)
BuildRequires:  pkgconfig(glib-2.0)
BuildRequires:  pkgconfig(gmodule-2.0)
BuildRequires:  pkgconfig(gobject-2.0)
BuildRequires:  pkgconfig(gstreamer-1.0)
BuildRequires:  pkgconfig(gstreamer-audio-1.0)
BuildRequires:  pkgconfig(gstreamer-base-1.0)
BuildRequires:  pkgconfig(gstreamer-pbutils-1.0)
BuildRequires:  pkgconfig(gstreamer-tag-1.0)
BuildRequires:  pkgconfig(gstreamer-video-1.0)
BuildRequires:  pkgconfig(gtk4)
BuildRequires:  pkgconfig(libadwaita-1)
BuildRequires:  pkgconfig(libcgraph)
BuildRequires:  pkgconfig(libgvc)
BuildRequires:  pkgconfig(libpeas-2)
BuildRequires:  pkgconfig(libsoup-3.0)
BuildRequires:  pkgconfig(microdns)
BuildRequires:  vala
# /oreon:deps
%description
Clapper is a modern media player designed for simplicity and ease of
use. Powered by GStreamer and built for the GNOME desktop environment
using GTK4 toolkit, it has a clean and stylish interface that lets you
focus on enjoying your favorite videos.

%package        devel
Summary:        Header files and libraries for Clapper development
Requires:       %{name}%{_isa} = %{version}-%{release}
%description    devel
The clapper-devel package contains header files and libraries needed to
develop programs that use Clapper.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%oreon_prep
%build

%meson
%meson_build
%install
%meson_install
%find_lang clapper-app
%find_lang clapper-gtk
%oreon_autofiles clapper-devel usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*

%check

appstream-util validate-relax --nonet %{buildroot}%{_metainfodir}/*.xml
desktop-file-validate %{buildroot}%{_datadir}/applications/*.desktop
%files -f %{oreon_filedir}/main.list
%files -n clapper-devel -f %{oreon_filedir}/clapper-devel.list

%changelog

%autochangelog
