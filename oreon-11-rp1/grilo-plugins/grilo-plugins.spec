%global source0_hash 8e3ce74ee717c3c322d0cb0f8df26bb0914028a5d016e28055ffb49cc9a46c5e
%define release_version %(echo %{version} | awk -F. '{print $1"."$2}')
%global grilo_version 0.3.15
%global goa_version 3.17.91
Name:		grilo-plugins
Version:	0.3.18
Release:        1%{?dist}
Summary:        Plugins for the Grilo framework
License:	LicenseRef-Callaway-LGPLv2+
URL:		https://wiki.gnome.org/Projects/Grilo
Source0:        https://download.gnome.org/sources/%{name}/%{release_version}/%{name}-%{version}.tar.xz
Requires:	gnome-online-accounts%{_isa} >= %{goa_version}
Requires:	grilo%{_isa} >= %{grilo_version}
# oreon:deps
BuildRequires:  avahi-gobject-devel
BuildRequires:  gcc
BuildRequires:  gettext
BuildRequires:  git
BuildRequires:  glib2-devel
BuildRequires:  gnome-online-accounts-devel
BuildRequires:  gom-devel
BuildRequires:  gperf
BuildRequires:  grilo-devel
BuildRequires:  itstool
BuildRequires:  json-glib-devel
BuildRequires:  libarchive-devel
BuildRequires:  libgcrypt-devel
BuildRequires:  libmediaart-devel
BuildRequires:  libsoup3-devel
BuildRequires:  libxml2-devel
BuildRequires:  localsearch
BuildRequires:  lua-devel
BuildRequires:  meson
BuildRequires:  pkgconfig(tinysparql-3.0)
BuildRequires:  rest-devel
BuildRequires:  sqlite-devel
BuildRequires:  totem-pl-parser-devel
# /oreon:deps
%description
Grilo is a framework that provides access to different sources of
multimedia content, using a pluggable system.
This package contains plugins to get information from theses sources:
- Bookmarks
- Filesystem
- Flickr
- Freebox
- Gravatar
- iTunes Music Sharing
- Last.fm (for album arts)
- Local metadata (album arts and thumbnails)
- Metadata Store
- Pocket
- Podcasts
- Radio France
- Shoutcast
- The Guardian Videos
- Tracker

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%oreon_prep
%build

%meson \
    -Denable-shoutcast=no \
    -Denable-bookmarks=yes \
    -Denable-dleyna=yes \
    -Denable-dmap=yes \
    -Denable-flickr=yes \
    -Denable-filesystem=yes \
    -Denable-freebox=yes \
    -Denable-gravatar=yes \
    -Denable-lua-factory=yes \
    -Denable-metadata-store=yes \
    -Denable-tmdb=yes \
    -Denable-youtube=no \
    -Denable-tracker=no \
    -Denable-tracker3=yes
%meson_build
%install
%meson_install
%find_lang grilo-plugins --with-gnome
%oreon_autofiles main

%files -f %{oreon_filedir}/main.list

%changelog

* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 0.3.18-1
- Prepare for Oreon 11 (RP1)
