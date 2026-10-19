%global source0_hash f40213707b7a3be87e556f65521cef8795bd91afda13dfac8f00c3550375837d
Name:           nitrogen
Version:        1.6.1
Release:        1%{?dist}
Summary:        Background browser and setter for X windows
License:        GPL-2.0-or-later AND Zlib AND CC-BY-SA-3.0
URL:            https://github.com/l3ib/%{name}/
Source0:        https://github.com/l3ib/%{name}/releases/download/%{version}/%{name}-%{version}.tar.gz
Patch0:         appdata.patch
Patch1:         draw-background.patch
Patch2:         catch-errors.patch
Requires:       gtkmm24
# oreon:deps
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  desktop-file-utils
BuildRequires:  gcc-c++
BuildRequires:  gettext
BuildRequires:  gettext-devel
BuildRequires:  gtkmm24-devel
BuildRequires:  libappstream-glib
BuildRequires:  libpng-devel
BuildRequires:  libtool
BuildRequires:  m4
BuildRequires:  make
BuildRequires:  pkgconfig
# /oreon:deps
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
%global oreon_srcdir %{name}-%{version}
%oreon_prep
%build

autoreconf -fi
%configure --disable-dependency-tracking
make %{?_smp_mflags} CFLAGS="%{optflags} -fPIE" LDFLAGS="-lX11 -pie"
%install
make install DESTDIR=%{buildroot}
%find_lang %{name}
%oreon_autofiles main

%check

appstream-util validate-relax --nonet %{buildroot}%{_metainfodir}/%{name}.appdata.xml
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
