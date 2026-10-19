%global source0_hash 62a5a609267eca7f6e3ce52ef6f42d5618d2961e3b4ddc227c6a5859026965d9
%bcond_without gtk
%bcond_without meson
Name: audacious
Version: 4.6.1
Release:        1%{?dist}
%global tar_ver %{version}
%global aud_ver 4.4
License: BSD-2-Clause-pkgconf-disclaimer
Summary:        Advanced audio player and music player
URL: https://audacious-media-player.org/
Group: Applications/Multimedia
Source0:        https://distfiles.%{name}-media-player.org/%{name}-%{version}.tar.bz2
%{?with_gtk:BuildRequires: pkgconfig(gtk+-3.0) >= 3.18}
Requires: audacious-libs%{?_isa} = %{version}-%{release}
Requires: audacious-plugins%{?_isa} >= %{aud_ver}
Requires: hicolor-icon-theme
Requires: qt5-qtsvg%{?_isa}
Provides: xmms-gui
# oreon:deps
BuildRequires:  desktop-file-utils
BuildRequires:  gcc-c++
BuildRequires:  gettext
BuildRequires:  libappstream-glib
BuildRequires:  make
BuildRequires:  meson
BuildRequires:  pkgconfig(Qt6Core)
BuildRequires:  pkgconfig(Qt6Gui)
BuildRequires:  pkgconfig(Qt6Svg)
BuildRequires:  pkgconfig(Qt6Widgets)
BuildRequires:  pkgconfig(glib-2.0)
BuildRequires:  pkgconfig(gtk+-3.0)
BuildRequires:  qt6-qtbase-devel
# /oreon:deps
%description
Audacious is an open source audio player and music player.

A descendant of XMMS, Audacious plays your music how you want it, without
stealing away your computer’s resources from other tasks. Drag and drop
folders and individual song files, search for artists and albums in your
entire music library, or create and edit your own custom playlists. Listen
to CDs or stream music from the Internet. Tweak the sound with the
graphical equalizer or change the dynamic range with audio effects. Enjoy
the modern Qt-themed interface or change things up with Winamp Classic
skins. Use the plugins included with Audacious to fetch lyrics for your
music, display a VU meter, and more.

An alternative GTK3-based user interface can still be chosen, too.

%package libs
Summary: Library files for the Audacious audio player
Group: System Environment/Libraries
%global aud_plugin_api 48
%global aud_plugin_api_min 48
Provides: audacious(plugin-api)%{?_isa} = %{aud_plugin_api}
%description libs
Library files for the Audacious audio player.

%package devel
Summary: Development files for the Audacious audio player
Group: Development/Libraries
Requires: %{name}-libs%{?_isa} = %{version}-%{release}
Requires: pkgconfig(glib-2.0)
%{?with_gtk:Requires: pkgconfig(gtk+-3.0)}
%description devel
Files needed when building software for the Audacious audio player.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1 -n %{name}-%{tar_ver}

# Verify the value of the audacious(plugin-api) Provides.
api=$(grep '[ ]*#define[ ]*_AUD_PLUGIN_VERSION[ ]\+' src/libaudcore/plugin.h | sed 's!.*_AUD_PLUGIN_VERSION[ ]*\([0-9]\+\).*!\1!')
[ "${api}" == "%{aud_plugin_api}" ] || exit -1
api_min=$(grep '[ ]*#define[ ]*_AUD_PLUGIN_VERSION_MIN' src/libaudcore/plugin.h | sed 's!.*_AUD_PLUGIN_VERSION_MIN[ ]*\([0-9]\+\).*!\1!')
[ "${api_min}" == "%{aud_plugin_api_min}" ] || exit -1

%if %{without meson}
sed -i '\,^.SILENT:,d' buildsys.mk.in
sed -i 's!MAKE} -s!MAKE} !' buildsys.mk.in
%endif

%build

%if %{with meson}
%meson \
    -Dqt5=true \
    -Dgtk=%{?with_gtk:true}%{!?with_gtk:false} \
    -Dlibarchive=false \
    -Dbuildstamp="Fedora package"
%meson_build
%else
%configure  \
    %{?with_gtk:--enable-gtk} \
    %{!?with_gtk:--disable-gtk} \
    --disable-libarchive \
    --with-buildstamp="Fedora package"  \
    --disable-silent-rules \
    --disable-rpath \
    --disable-dependency-tracking
make %{?_smp_mflags}
%endif
%install
%if %{with meson}
%meson_install
%else
%make_install INSTALL="install -p"
%endif
find ${RPM_BUILD_ROOT} -type f -name "*.la" -exec rm -f {} ';'
%find_lang %{name}
desktop-file-install  \
    --dir ${RPM_BUILD_ROOT}%{_datadir}/applications  \
    ${RPM_BUILD_ROOT}%{_datadir}/applications/audacious.desktop
install -D -m0644 contrib/%{name}.appdata.xml ${RPM_BUILD_ROOT}%{_datadir}/appdata/%{name}.appdata.xml
appstream-util validate-relax --nonet ${RPM_BUILD_ROOT}%{_datadir}/appdata/%{name}.appdata.xml
%ldconfig_scriptlets libs
%oreon_autofiles audacious-libs usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles audacious-devel usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*

%files -f %{oreon_filedir}/main.list
%files -n audacious-libs -f %{oreon_filedir}/audacious-libs.list
%files -n audacious-devel -f %{oreon_filedir}/audacious-devel.list

%changelog

%autochangelog
