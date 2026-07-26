%global source0_hash 403bf2106578b1f3d6ce70bc08654f7a90753f19e27b4cc170bc636307cdc78c

Summary: A high quality TV viewer
Name:    tvtime
Version: 1.0.11
Release: 1%{?dist}
# Automatically converted from old format: GPLv2+ - review is highly recommended.
License: GPL-2.0-or-later
URL:     https://tvtime.sourceforge.net
Source0: https://linuxtv.org/downloads/%{name}/%{name}-%{version}.tar.gz
Patch:   tvtime-1.0.10-honor-cflags.patch
Patch:   0003-Fix-bitwise-comparison-always-evaluates-to-false-com.patch
Patch:   0004-Fix-warning-implicit-declaration-of-function-minor-m.patch
Patch:   tvtime-1.0.10-termios_h.patch
Patch:   tvtime-1.0.11-set_fmt.patch
BuildRequires: make
BuildRequires: gcc gcc-c++
BuildRequires: alsa-lib-devel
BuildRequires: freetype-devel >= 2.0
BuildRequires: zlib-devel
BuildRequires: libpng-devel
BuildRequires: SDL-devel
BuildRequires: libxml2-devel
BuildRequires: libICE-devel
BuildRequires: libSM-devel
BuildRequires: libX11-devel
BuildRequires: libXext-devel
BuildRequires: libXinerama-devel
BuildRequires: libXtst-devel
BuildRequires: libXv-devel
BuildRequires: libXxf86vm-devel
BuildRequires: libXt-devel
BuildRequires: libXi-devel
BuildRequires: libXScrnSaver-devel
BuildRequires: libtool gettext-devel
BuildRequires: desktop-file-utils libappstream-glib
Requires: hicolor-icon-theme
ExcludeArch: s390 s390x

%description
tvtime is a high quality television application for use with video
capture cards.  tvtime processes the input from a capture card and
displays it on a computer monitor or projector.  Unlike other television
applications, tvtime focuses on high visual quality making it ideal for
videophiles.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1
autoreconf -ifv

%build
%configure --disable-dependency-tracking --disable-rpath
make %{?_smp_mflags} V=1

%install
%make_install INSTALL="install -p"
%find_lang %{name}
desktop-file-validate $RPM_BUILD_ROOT%{_datadir}/applications/%{name}.desktop
appstream-util validate-relax --nonet \
  $RPM_BUILD_ROOT%{_datadir}/appdata/%{name}.appdata.xml

%files -f %{name}.lang
%doc AUTHORS ChangeLog  NEWS README* docs/html
%license COPYING COPYING.LGPL data/COPYING*
%dir %{_sysconfdir}/tvtime/
%config(noreplace) %{_sysconfdir}/tvtime/tvtime.xml
%{_bindir}/tvtime
%{_bindir}/tvtime-command
%{_bindir}/tvtime-configure
%{_bindir}/tvtime-scanner
%{_datadir}/appdata/tvtime.appdata.xml
%{_datadir}/applications/tvtime.desktop
%{_datadir}/icons/hicolor/*/apps/tvtime.png
%{_datadir}/tvtime/
%{_mandir}/man?/*
%lang(de) %{_mandir}/de/man?/*
%lang(es) %{_mandir}/es/man?/*

%changelog
%autochangelog
