%global source0_hash 0b007d30fbb93b95a604f14848a497f57fc333a75c2e638a249972e99c01e6a4
%global gst_plugins_base_version 1.6.0
%global gtk3_version 3.19.4
%global tarball_version %(echo %{version} | tr '~' '.')
Name: totem
Epoch: 1
Version: 43.2
Release:        1%{?dist}
Summary:        Movie player for GNOME
License: LicenseRef-Callaway-GPLv2+-with-exceptions
URL: https://wiki.gnome.org/Apps/Videos
Source0:        https://download.gnome.org/sources/%{name}/43/%{name}-%{version}.tar.xz
Patch:         girepository-2.0.patch
Requires: %{name}-video-thumbnailer%{?_isa} = %{epoch}:%{version}-%{release}
Requires: libpeas-loader-python3%{?_isa}
Requires: python3-gobject
Requires: iso-codes
Requires: gstreamer1%{?_isa}
Requires: gstreamer1-plugins-base%{?_isa} >= %{gst_plugins_base_version}
Requires: gstreamer1-plugins-good%{?_isa}
Requires: gstreamer1-plugins-good-gtk%{?_isa}
%if ! 0%{?flatpak}
Requires: gvfs-fuse%{?_isa}
%endif
Requires: grilo-plugins%{?_isa}
Requires: gsettings-desktop-schemas%{?_isa}
Requires: gtk3%{?_isa} >= %{gtk3_version}
Recommends: gstreamer1-plugin-openh264%{?_isa}
Recommends: gstreamer1-plugins-bad-free%{?_isa}
Recommends: gstreamer1-plugins-ugly-free%{?_isa}
Obsoletes: totem-nautilus < 1:3.31.91
Obsoletes: totem-lirc < 1:3.33.0
# oreon:deps
BuildRequires:  /usr/bin/appstream-util
BuildRequires:  /usr/bin/desktop-file-validate
BuildRequires:  gcc-c++
BuildRequires:  gettext
BuildRequires:  gstreamer1-plugins-good
BuildRequires:  gstreamer1-plugins-good-gtk
BuildRequires:  gtk-doc
BuildRequires:  itstool
BuildRequires:  liberation-sans-fonts
BuildRequires:  meson
BuildRequires:  pkgconfig(cairo)
BuildRequires:  pkgconfig(gnome-desktop-3.0)
BuildRequires:  pkgconfig(grilo-0.3)
BuildRequires:  pkgconfig(grilo-pls-0.3)
BuildRequires:  pkgconfig(gsettings-desktop-schemas)
BuildRequires:  pkgconfig(gstreamer-1.0)
BuildRequires:  pkgconfig(gstreamer-audio-1.0)
BuildRequires:  pkgconfig(gstreamer-base-1.0)
BuildRequires:  pkgconfig(gstreamer-plugins-base-1.0)
BuildRequires:  pkgconfig(gstreamer-tag-1.0)
BuildRequires:  pkgconfig(gstreamer-video-1.0)
BuildRequires:  pkgconfig(gtk+-3.0)
BuildRequires:  pkgconfig(libhandy-1)
BuildRequires:  pkgconfig(libpeas-gtk-1.0)
BuildRequires:  pkgconfig(libportal-gtk3)
BuildRequires:  pkgconfig(pygobject-3.0)
BuildRequires:  pkgconfig(totem-plparser)
BuildRequires:  pkgconfig(x11)
BuildRequires:  python3-devel
BuildRequires:  vala
# /oreon:deps
%description
Totem is simple movie player for the GNOME desktop. It features a
simple playlist, a full-screen mode, seek and volume controls, as well as
a pretty complete keyboard navigation.

Totem is extensible through a plugin system.

%package video-thumbnailer
Summary: Totem video thumbnailer
Conflicts: totem < 1:3.38.0-4
%description video-thumbnailer
This package contains the Totem video thumbnailer.

%package devel
Summary: Plugin writer's documentation for totem
Requires: %{name}%{?_isa} = %{epoch}:%{version}-%{release}
%description devel
The %{name}-devel package contains API documentation for
developing developing plugins for %{name}.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%autosetup -p1 -n %{name}-%{tarball_version}

%build

%meson -Denable-gtk-doc=true
%meson_build -j1
%install
%meson_install
%find_lang %{name} --with-gnome
%py_byte_compile %{python3} %{buildroot}%{_libdir}/totem/plugins/
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*

%check

appstream-util validate-relax --nonet $RPM_BUILD_ROOT%{_datadir}/metainfo/org.gnome.Totem.appdata.xml
desktop-file-validate $RPM_BUILD_ROOT%{_datadir}/applications/org.gnome.Totem.desktop
%ldconfig_scriptlets
%files -f %{oreon_filedir}/main.list
%files -n totem-video-thumbnailer -f %{oreon_filedir}/totem-video-thumbnailer.list
%files -n totem-devel -f %{oreon_filedir}/totem-devel.list

%changelog

* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 43.2-1
- Prepare for Oreon 11 (RP1)
