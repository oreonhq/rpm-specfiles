%global source0_hash 7194743a0a41b1d8f582c071488b77f7b917be47ca5e142dd76af5d81d36f9cd

# 'without' = build with Gtk+ by default
%bcond_without gtk

%bcond_without meson

Name: audacious
Version: 4.5.1
Release: 3%{?dist}

%global tar_ver %{version}

# Minimum audacious/audacious-plugins version in inter-package dependencies.
%global aud_ver 4.4

# Audacious Generic Plugin API is defined in audacious-libs subpackage.

# approved SPDX id -- https://github.com/spdx/license-list-XML/issues/2651
License: BSD-2-Clause-pkgconf-disclaimer

Summary: Advanced audio player and music player
URL: https://audacious-media-player.org/
Group: Applications/Multimedia

Source0: https://distfiles.audacious-media-player.org/%{name}-%{tar_ver}.tar.bz2

# for /usr/bin/appstream-util
BuildRequires: libappstream-glib

BuildRequires: gcc-c++
BuildRequires: gettext
%{?with_gtk:BuildRequires: pkgconfig(gtk+-3.0) >= 3.18}
BuildRequires: pkgconfig(glib-2.0)
BuildRequires: desktop-file-utils
BuildRequires: meson
BuildRequires: make

%if 0%{?fedora} || 0%{?rhel} >= 9
BuildRequires: qt6-qtbase-devel
BuildRequires: pkgconfig(Qt6Core)
BuildRequires: pkgconfig(Qt6Gui)
BuildRequires: pkgconfig(Qt6Widgets)
BuildRequires: pkgconfig(Qt6Svg)
%else
BuildRequires: qt5-qtbase-devel
BuildRequires: pkgconfig(Qt5Core)
BuildRequires: pkgconfig(Qt5Gui)
BuildRequires: pkgconfig(Qt5Widgets)
BuildRequires: pkgconfig(Qt5Svg)
%endif

# The automatic SONAME dependency is not enough
# during version upgrades.
Requires: audacious-libs%{?_isa} = %{version}-%{release}

# For compatibility with the plugin API implemented by the player,
# a minimum version of the base plugins package is strictly required.
Requires: audacious-plugins%{?_isa} >= %{aud_ver}

# Audacious stores its own icon(s) in the hicolor tree
# and updates the icon cache.
Requires: hicolor-icon-theme
%if 0%{?fedora}
# for icons such as 'go-next', 'go-previous'
Requires: gnome-icon-theme
%endif
%if 0%{?fedora} || 0%{?rhel} >= 9
Requires: qt6-qtsvg%{?_isa}
%else
Requires: qt5-qtsvg%{?_isa}
%endif

# Skin packages can require this from xmms and all GUI compatible players
Provides: xmms-gui

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
# Provide Generic Plugin API value for plugin packages to depend on.
# As defined in /usr/include/libaudcore/plugin.h: _AUD_PLUGIN_VERSION
# This must be an exact match for plugin .so files to load.
# If multiple versions are supported, add multiple Provides below.
%global aud_plugin_api 48
%global aud_plugin_api_min 48
Provides: audacious(plugin-api)%{?_isa} = %{aud_plugin_api}
# [!] escaped macros, beware!
#Provides: audacious(plugin-api)%%{?_isa} = 46
#Provides: audacious(plugin-api)%%{?_isa} = %%{aud_plugin_api_min}

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
# temporarily was required to make Qt's MOC accessible
#rm -rf _bin
#mkdir _bin
#ln -s /usr/bin/moc-qt5 _bin/moc
#export PATH=$PATH:$(pwd)/_bin

%if %{with meson}
%meson \
%if 0%{?fedora} || 0%{?rhel} >= 9
    -Dqt=true \
%else
    -Dqt5=true \
%endif
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

%files -f %{name}.lang
%doc AUTHORS
%{_bindir}/audacious
%{_bindir}/audtool
%{_datadir}/audacious/
%{_mandir}/man[^3]/*
%{_datadir}/applications/*.desktop
%{_datadir}/icons/hicolor/*/apps/%{name}*.*
%{_datadir}/appdata/%{name}.appdata.xml

%files libs
# license file included in this subpkg
# for Fedora Licensing Guidelines change (2010-07-07)
%license COPYING
%{_libdir}/*.so.*

%files devel
%{_includedir}/audacious/
%{_includedir}/libaudcore/
%{_includedir}/libaudqt/
%{?with_gtk:%{_includedir}/libaudgui/}
%{_libdir}/*.so
%{_libdir}/pkgconfig/*.pc

%changelog
%autochangelog
