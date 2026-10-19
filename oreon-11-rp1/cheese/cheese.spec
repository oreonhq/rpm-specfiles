%global source0_hash 5f2185c4c99e54ddf2b8baf60c82819950e54952e132e8639875f3edcbf8f68e
%global tarball_version %(echo %{version} | tr '~' '.')
Name:           cheese
Epoch:          2
Version:        44.1
Release:        1%{?dist}
Summary:        Application for taking pictures and movies from a webcam
License:        GPL-2.0-or-later
URL:            https://wiki.gnome.org/Apps/Cheese
Source0:        https://download.gnome.org/sources/%{name}/44/%{name}-%{version}.tar.xz
Patch0: cheese-c99.patch
Patch1: 73.patch
ExcludeArch:    %{ix86}
Requires: %{name}-libs%{?_isa} = %{epoch}:%{version}-%{release}
Requires: gstreamer1-plugins-good%{?_isa}
Requires: gstreamer1-plugins-bad-free%{?_isa}
Requires: gnome-video-effects
# oreon:deps
BuildRequires:  /usr/bin/appstream-util
BuildRequires:  /usr/bin/xsltproc
BuildRequires:  desktop-file-utils
BuildRequires:  docbook-dtds
BuildRequires:  docbook-style-xsl
BuildRequires:  gcc
BuildRequires:  gettext
BuildRequires:  gtk-doc
BuildRequires:  itstool
BuildRequires:  libXtst-devel
BuildRequires:  meson
BuildRequires:  pkgconfig(clutter-1.0)
BuildRequires:  pkgconfig(clutter-gst-3.0)
BuildRequires:  pkgconfig(clutter-gtk-1.0)
BuildRequires:  pkgconfig(gdk-pixbuf-2.0)
BuildRequires:  pkgconfig(gio-2.0)
BuildRequires:  pkgconfig(glib-2.0)
BuildRequires:  pkgconfig(gnome-desktop-3.0)
BuildRequires:  pkgconfig(gobject-introspection-1.0)
BuildRequires:  pkgconfig(gstreamer-pbutils-1.0)
BuildRequires:  pkgconfig(gstreamer-plugins-bad-1.0)
BuildRequires:  pkgconfig(gtk+-3.0)
BuildRequires:  pkgconfig(libcanberra-gtk3)
BuildRequires:  pkgconfig(x11)
BuildRequires:  vala
# /oreon:deps
%description
Cheese is a Photobooth-inspired GNOME application for taking pictures and
videos from a webcam. It can also apply fancy graphical effects.

%package libs
Summary:        Webcam display and capture widgets
License:        GPL-2.0-or-later
Obsoletes: cheese-camera-service < 2:3.25.90
%description libs
This package contains libraries needed for applications that
want to display a webcam in their interface.

%package libs-devel
Summary:        Development files for %{name}-libs
License:        GPL-2.0-or-later
Requires:       %{name}-libs%{?_isa} = %{epoch}:%{version}-%{release}
%description libs-devel
This package contains the libraries and header files that are needed
for writing applications that require a webcam display widget.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%autosetup -p1 -n %{name}-%{tarball_version}
# Trigger recompilation of all Vala sources.
find -name '*.vala' -exec touch {} \;

%build

%meson -Dtests=false
%meson_build
%install
%meson_install
%find_lang %{name} --with-gnome
%oreon_autofiles cheese-libs usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles cheese-libs-devel usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*

%check

desktop-file-validate %{buildroot}%{_datadir}/applications/org.gnome.Cheese.desktop
%meson_test
%files -f %{oreon_filedir}/main.list
%files -n cheese-libs -f %{oreon_filedir}/cheese-libs.list
%files -n cheese-libs-devel -f %{oreon_filedir}/cheese-libs-devel.list

%changelog

* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 44.1-1
- Prepare for Oreon 11 (RP1)
