%global source0_hash f40213707b7a3be87e556f65521cef8795bd91afda13dfac8f00c3550375837d

Name:           nitrogen
Version:        1.6.1
Release:        %autorelease
Summary:        Background browser and setter for X windows

# Code is GPLv2+ and zlib, icons are CC-BY-SA as described in COPYING
# SPDX
License:        GPL-2.0-or-later AND Zlib AND CC-BY-SA-3.0
URL:            https://github.com/l3ib/%{name}/
Source:         https://github.com/l3ib/%{name}/releases/download/%{version}/%{name}-%{version}.tar.gz
Patch0:         appdata.patch
Patch1:         draw-background.patch
Patch2:         catch-errors.patch
BuildRequires: make
BuildRequires:  gtkmm24-devel
BuildRequires:  libpng-devel
BuildRequires:  gettext
BuildRequires:  pkgconfig
BuildRequires:  desktop-file-utils
BuildRequires:  libappstream-glib
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  m4
BuildRequires:  libtool
BuildRequires:  gettext-devel
BuildRequires:  gcc-c++
Requires:       gtkmm24

%description
A background browser and setter for X windows that can be used in two
modes: browser and recall. It features Multihead and Xinerama awareness,
a recall mode to be used in start up scripts, uses the freedesktop.org
standard for thumbnails, can set the GNOME background, command line set
modes for use in scripts, inotify monitoring of browse directory, lazy
loading of thumbnails to conserve memory and an 'automatic' set mode
which determines the best mode to set an image based on its size.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1 -n %{name}-%{version}

%build
autoreconf -fi

%configure --disable-dependency-tracking
# -lX11 is missing (DSO: https://fedoraproject.org/wiki/UnderstandingDSOLinkChange)
make %{?_smp_mflags} CFLAGS="%{optflags} -fPIE" LDFLAGS="-lX11 -pie"

%install
make install DESTDIR=%{buildroot}
%find_lang %{name}

%check
appstream-util validate-relax --nonet %{buildroot}%{_metainfodir}/%{name}.appdata.xml

%files -f %{name}.lang
%doc COPYING NEWS README AUTHORS ChangeLog
%{_bindir}/%{name}
%{_metainfodir}/%{name}.appdata.xml
%{_datadir}/icons/hicolor/16x16/actions/wallpaper-*.png
%{_datadir}/icons/hicolor/16x16/devices/video-display.png
%{_datadir}/icons/hicolor/16x16/mimetypes/image-x-generic.png
%{_datadir}/applications/%{name}.desktop
%{_datadir}/icons/hicolor/*/apps/%{name}.png
%{_mandir}/man1/%{name}.1*

%changelog
%autochangelog
