%global source3_hash 248fa8f3368bad3264885e0544eb7d75df95808b9c47e034f3d01e1b095c0a81
%global source2_hash 03ec235b3364abfd54c12acc67c6fdb93ce40fff4f29df48dc156960f3fd789d
%global source1_hash 802d7fc818f9efa908aae8ac401d9b207c3d6169215bf2eb8701e31e8633c7d3
%global source0_hash 2c13ab03380587e6ab05ac4d5267c238136b028fdf26e2d8d1abe93756deb35a
%global debug_package %{nil}
Name:           gnome-subtitles
Version:        1.8
Release:        1%{?dist}
Summary:        Subtitle editor for Gnome
License:        GPL-2.0-or-later AND (LicenseRef-Callaway-MPLv1.1 OR GPL-2.0-or-later OR LicenseRef-Callaway-LGPLv2+)
URL:            https://gnomesubtitles.org/
Source0:        https://downloads.sourceforge.net/%{name}/%{name}-%{version}.tar.xz
Source1:        https://gstreamer.freedesktop.org/src/gstreamer-sharp/gstreamer-sharp-1.20.3.tar.xz
Source2:        https://github.com/GLibSharp/GtkSharp/archive/3.22.2/GtkSharp-3.22.2.tar.gz
Source3:        https://github.com/GLibSharp/bindinator/archive/13cdbcdb9bd9e05666e56e7e374027fa719acda4/bindinator-13cdbcd.tar.gz
Requires:       enchant2
Requires:       gstreamer1-plugins-good-gtk
Requires:       hicolor-icon-theme
Requires:       mono-locale-extras
Provides:       bundled(gstreamer1-sharp) = 1.20.3
ExclusiveArch: %mono_arches
%global _privatelibs mono\\(gstreamer-sharp\\).*
%global __provides_exclude ^(%{_privatelibs})$
%global __requires_exclude ^(%{_privatelibs})$
# oreon:deps
BuildRequires:  desktop-file-utils
BuildRequires:  gcc
BuildRequires:  intltool
BuildRequires:  itstool
BuildRequires:  libappstream-glib
BuildRequires:  make
BuildRequires:  meson
BuildRequires:  mono-devel
BuildRequires:  mono-web
BuildRequires:  perl(XML::Parser)
BuildRequires:  pkgconfig(gst-editing-services-1.0)
BuildRequires:  pkgconfig(gstreamer-plugins-base-1.0)
BuildRequires:  pkgconfig(gstreamer-video-1.0)
BuildRequires:  pkgconfig(gstreamer-webrtc-1.0)
BuildRequires:  pkgconfig(gtk+-3.0)
BuildRequires:  pkgconfig(mono)
# /oreon:deps
%description
Gnome Subtitles is a subtitle editor for the GNOME desktop. It supports the
most common text-based subtitle formats and allows for subtitle editing,
translation and synchronization.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1
%autosetup -T -D -a 1
%autosetup -T -D -a 2
%autosetup -T -D -a 3
mv gstreamer-sharp-1.20.3 subprojects/gstreamer-sharp
mv GtkSharp-3.22.2 subprojects/gtk-sharp
mv bindinator-13cdbcdb9bd9e05666e56e7e374027fa719acda4 subprojects/bindinator

%build

%meson -Dinstall_gtk_sharp=false -Dgstreamer-sharp:tests=disabled
%meson_build
%install
%meson_install
desktop-file-validate $RPM_BUILD_ROOT%{_datadir}/applications/org.gnome.GnomeSubtitles.desktop
appstream-util validate-relax --nonet $RPM_BUILD_ROOT%{_metainfodir}/*.appdata.xml
%find_lang org.gnome.GnomeSubtitles
%oreon_autofiles main

%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
