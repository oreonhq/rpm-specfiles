%global source0_hash 5e98cea9bd958860d90003d37037172a95ed8b699133e8f1e6033147aaefed73

%global branch 0.12

Name:    kmplayer
Summary: A simple front-end for MPlayer/FFMpeg/Phonon
Version: 0.12.0b
Release: 17%{?dist}
# The documentation is GFDL.
# The files under src/moz-sdk are MPLv1.1 or GPLv2+ or LGPLv2+
# except src/moz-sdk/npruntime.h is BSD.
# The other source files carry GPL and LGPL licenses
# For instance:
# src/kmplayer.h is GPLv2+
# src/kmplayer_asx.cpp is LGPLv2
# src/kmplayer_atom.h is LGPLv2+
# and each of the other source files carry one of the above 3 licenses. So
#License: GFDL and (MPLv1.1 or GPLv2+ or LGPLv2+) and BSD and GPLv2+ and LGPLv2 and LGPLv2+
# Automatically converted from old format: GFDL and GPLv2+ - review is highly recommended.
License: LicenseRef-Callaway-GFDL AND GPL-2.0-or-later
URL:     https://kmplayer.kde.org
Source0: https://download.kde.org/stable/kmplayer/%{branch}/kmplayer-%{version}.tar.bz2

## upstream patches

BuildRequires: kf5-kdelibs4support-devel 
BuildRequires: kf5-kmediaplayer-devel
BuildRequires: desktop-file-utils
BuildRequires: kf5-kwidgetsaddons-devel
BuildRequires: gettext
BuildRequires: extra-cmake-modules
BuildRequires: xcb-util-devel
BuildRequires: kf5-kcoreaddons-devel
BuildRequires: phonon-qt5-devel
BuildRequires: qt5-qtbase-devel
BuildRequires: qt5-qtsvg-devel
BuildRequires: qt5-qtx11extras-devel
BuildRequires: xcb-util-wm-devel
BuildRequires: xcb-util-cursor-devel
BuildRequires: xcb-util-image-devel
BuildRequires: xcb-util-keysyms-devel
BuildRequires: xcb-util-renderutil-devel
BuildRequires: libxcb-devel
BuildRequires: cmake-data
BuildRequires: kf5-kxmlgui-devel
BuildRequires: kf5-kglobalaccel-devel
BuildRequires: qt5-qtspeech-devel
BuildRequires: polkit-qt5-1-devel

%description
KMPlayer, a simple front-end for MPlayer/FFMpeg/Phonon.
It can play DVD/VCD movies, from file or URL and from a video device.
KMPlayer can embed inside Konqueror. Which means if you click
on a movie file, the movie is played inside Konqueror.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n %{name}-%{version}

#Set Phonon as default
sed -i  "s:Show Toolbar=true:Show Toolbar=true\nurlsource=phonon:g" src/kmplayerrc
#Fix building issue
sed -i 's:Q_PLUGIN_METADATA(IID "org.kde.KPluginFactory" FILE ""):Q_PLUGIN_METADATA(IID "org.kde.KPluginFactory" ""):g' src/kmplayer_part.h
#Fix desktop entry
sed -i "s:Exec=kmplayer -caption %c %i %U:Exec=kmplayer %U:g" src/kmplayer.desktop

%build
%{cmake}
%cmake_build

%install
%cmake_install
%find_lang %{name}

%files -f %{name}.lang
%doc AUTHORS ChangeLog COPYING* README TODO
%{_bindir}/*
%{_datadir}/icons/hicolor/*/*/*
%{_libdir}/qt5/plugins/kmplayerpart.so
%{_libdir}/libkdeinit5_kmplayer.so
%{_libdir}/libkmplayercommon.so
%{_sysconfdir}/xdg/kmplayerrc
%{_docdir}/HTML/*
%{_datadir}/%{name}/*
%{_datadir}/applications/kmplayer.desktop
%{_datadir}/kxmlgui5/%{name}/*
%{_datadir}/kservices5/*.desktop

%changelog
%autochangelog
