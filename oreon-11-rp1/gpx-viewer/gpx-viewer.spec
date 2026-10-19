%global source0_hash 956acfaf870ac436300cd9953dece630df7fd7dff8e4ae2577a6002884466f80
Name:           gpx-viewer
Version:        0.4.0
Release:        1%{?dist}
Summary:        A simple gpx viewer
License:        GPL-2.0-or-later
URL:            https://edge.launchpad.net/gpx-viewer
Source0:        http://edge.launchpad.net/gpx-viewer/trunk/0.4.0/+download/%{name}-%{version}.tar.gz
Patch0:         gpx-viewer-0.4.0-gtk3-bugfix.patch
Requires:       hicolor-icon-theme
Requires:       shared-mime-info
# oreon:deps
BuildRequires:  desktop-file-utils
BuildRequires:  gcc
BuildRequires:  gtk2-devel
BuildRequires:  intltool
BuildRequires:  libchamplain-devel
BuildRequires:  libchamplain-gtk-devel
BuildRequires:  libgdl-devel
BuildRequires:  libxml2-devel
BuildRequires:  make
BuildRequires:  unique-devel
BuildRequires:  vala-devel
# /oreon:deps
%description
GPX Viewer is a simple tool to visualize tracks and waypoints
stored in a gpx file.

It has the following features:
- Show multiple GPX files
- Height map
- Show waypoints and multiple tracks per gpx file
- Highlight selected track
- Show speed vs time graph
- Show distance, duration, average, moving average, max speed,
  moving time and gps points
- Zooming
- Smoothing of speed graph
- Playback of track
- Highlighting points in speed graph on map

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q
%patch -P0 -p0 -b.gtk3-bugfix

%build

%configure --disable-database-updates
make %{?_smp_mflags}
%install
make install DESTDIR=%{buildroot} INSTALL="install -p"
desktop-file-validate %{buildroot}%{_datadir}/applications/%{name}.desktop
%find_lang %{name}
%oreon_autofiles main

%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
