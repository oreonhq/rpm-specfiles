%global source0_hash a31f17be199bc3fa2cec9124a9b8fbb232eac40fd07797e0314549f355617b83
Name:           gnome-radio
Version:        73.0
Release:        1%{?dist}
Summary:        GNOME Radio
License:        GPL-3.0-or-later
URL:            http://gnomeradio.org
Source0:        http://www.gnomeradio.org/src/%{name}-%{version}.tar.xz
# oreon:deps
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  gcc
BuildRequires:  gtk-doc
BuildRequires:  intltool
BuildRequires:  itstool
BuildRequires:  make
BuildRequires:  pkgconfig(champlain-gtk-0.12)
BuildRequires:  pkgconfig(geoclue-2.0)
BuildRequires:  pkgconfig(geocode-glib-2.0)
BuildRequires:  pkgconfig(glib-2.0)
BuildRequires:  pkgconfig(gstreamer-1.0)
BuildRequires:  pkgconfig(gstreamer-player-1.0)
BuildRequires:  pkgconfig(gstreamer-tag-1.0)
BuildRequires:  pkgconfig(gstreamer-video-1.0)
BuildRequires:  pkgconfig(gtk+-3.0)
BuildRequires:  pkgconfig(libgeoclue-2.0)
# /oreon:deps
%description
GNOME Radio is a free network radio software for the GNOME desktop.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%oreon_prep
%build

%configure
%make_build
%install
%make_install
%oreon_autofiles main

%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
