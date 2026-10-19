%global source0_hash a02093f7b57eef42c9a2d641a10899fca28f13d3e09e6e259816f8e482b60778
%global commit  e5d5465de4a4aa5804a43cefed69f0ae5c4b427c
Name:           g4music
Version:        4.6.2
Release:        1%{?dist}
Summary:        Fast fluent lightweight music player written in GTK4
License:        GPL-3.0-or-later AND GPL-2.0-or-later AND CC0-1.0
URL:            https://gitlab.gnome.org/neithern/g4music
VCS:            git:%{url}.git
Source0:        https://gitlab.gnome.org/neithern/%{name}/-/archive/v%{version}/%{name}-%{version}.tar.gz
ExcludeArch:    %{ix86}
Requires:       dbus-common
Requires:       hicolor-icon-theme
Provides:       gapless = %{version}-%{release}
Provides:       gapless%{?_isa} = %{version}-%{release}
# oreon:deps
BuildRequires:  desktop-file-utils
BuildRequires:  gcc
BuildRequires:  gettext
BuildRequires:  libappstream-glib
BuildRequires:  meson
BuildRequires:  pkgconfig(gstreamer-1.0)
BuildRequires:  pkgconfig(gstreamer-tag-1.0)
BuildRequires:  pkgconfig(gtk4)
BuildRequires:  pkgconfig(libadwaita-1)
BuildRequires:  vala
# /oreon:deps
%description
G4Music is a fast fluent lightweight music player written in GTK4, with a
beautiful and adaptive user interface.  It focuses on high performance for
large music collections.

Features:
- Supports most music file types, samba and any other remote protocol (depends
  on GIO and GStreamer).
- Fast loading and parsing thousands of music files in a few seconds, monitors
  local changes.
- Low memory usage for large music collections with album covers (embedded and
  external), no thumbnail caches to store.
- Groups and sorts by album/artist/title, shuffle list, full-text searching.
- Gaussian blurred cover as background, follows GNOME light/dark mode.
- Drag-drop from GNOME Files, showing music in Files.
- Supports audio peaks visualizer.
- Supports gapless playback.
- Supports normalizing volume with ReplayGain.
- Supports pipewire and other audio sinks.
- Supports MPRIS control.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n %{name}-v%{version}-%{commit}

%build

%meson --buildtype=release
%meson_build
%install
%meson_install
%find_lang %{name}
%oreon_autofiles main

%check

%meson_test
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
