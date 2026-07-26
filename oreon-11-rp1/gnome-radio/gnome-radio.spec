%global source0_hash a31f17be199bc3fa2cec9124a9b8fbb232eac40fd07797e0314549f355617b83

Name:           gnome-radio
Version:        73.0
Release:        %autorelease
Summary:        GNOME Radio
 
License:        GPL-3.0-or-later
URL:            http://gnomeradio.org
Source0:        http://www.gnomeradio.org/src/%{name}-%{version}.tar.xz

BuildRequires:  autoconf
BuildRequires:  automake
# BuildRequires:  desktop-file-utils
BuildRequires:  gcc
BuildRequires:  gtk-doc
BuildRequires:  intltool
BuildRequires:  itstool
# BuildRequires:  libappstream-glib
BuildRequires:  pkgconfig(champlain-gtk-0.12) >= 0.12.10
BuildRequires:  pkgconfig(geoclue-2.0) >= 1.0
BuildRequires:  pkgconfig(geocode-glib-2.0) >= 1.0
BuildRequires:  pkgconfig(glib-2.0) >= 2.40
BuildRequires:  pkgconfig(gstreamer-1.0) >= 1.0
BuildRequires:  pkgconfig(gstreamer-player-1.0) >= 1.0
BuildRequires:  pkgconfig(gstreamer-tag-1.0) >= 1.0
BuildRequires:  pkgconfig(gstreamer-video-1.0) >= 1.0
BuildRequires:  pkgconfig(gtk+-3.0) >= 3.22.30
BuildRequires:  pkgconfig(libgeoclue-2.0) >= 1.0
BuildRequires:  make
# Requires:       hicolor-icon-theme

%description
GNOME Radio is a free network radio software for the GNOME desktop.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup

%build
%configure
%make_build

%install
%make_install

%files
%{_bindir}/gnome-internet-radio-locator
%{_bindir}/gnome-radio
%{_bindir}/gtk-internet-radio-locator
%{_bindir}/gtk-radio
%{_bindir}/org.gnome.Radio
%{_bindir}/radio-icy
%{_datadir}/applications/gnome-radio.desktop
%{_datadir}/applications/gtk-radio.desktop
%{_datadir}/applications/org.gnome.Radio.desktop
%{_datadir}/gnome-radio/doc/AAMOT.txt.xz
%{_datadir}/gnome-radio/doc/Aamot-2020.txt.xz
%{_datadir}/gnome-radio/gnome-radio-48.0.dtd
%{_datadir}/gnome-radio/gnome-radio.xml
%{_datadir}/gnome-radio/org.gnome.Radio.dtd
%{_datadir}/gnome-radio/org.gnome.Radio.xml
%{_datadir}/gtk-internet-radio-locator/internet-radio-locator-48.0.dtd
%{_datadir}/gtk-internet-radio-locator/internet-radio-locator.xml
%{_datadir}/gtk-radio/gtk-radio-550.3.dtd
%{_datadir}/gtk-radio/gtk-radio.xml
%{_datadir}/icons/hicolor/scalable/apps/gnome-radio.svg
%{_datadir}/icons/hicolor/scalable/apps/gtk-radio.svg
%{_datadir}/icons/hicolor/scalable/apps/org.gnome.Radio.svg
%{_datadir}/locale/ca/LC_MESSAGES/gnome-radio.mo
%{_datadir}/locale/cs/LC_MESSAGES/gnome-radio.mo
%{_datadir}/locale/da/LC_MESSAGES/gnome-radio.mo
%{_datadir}/locale/de/LC_MESSAGES/gnome-radio.mo
%{_datadir}/locale/el/LC_MESSAGES/gnome-radio.mo
%{_datadir}/locale/es/LC_MESSAGES/gnome-radio.mo
%{_datadir}/locale/eu/LC_MESSAGES/gnome-radio.mo
%{_datadir}/locale/fr/LC_MESSAGES/gnome-radio.mo
%{_datadir}/locale/fur/LC_MESSAGES/gnome-radio.mo
%{_datadir}/locale/hi/LC_MESSAGES/gnome-radio.mo
%{_datadir}/locale/hr/LC_MESSAGES/gnome-radio.mo
%{_datadir}/locale/hu/LC_MESSAGES/gnome-radio.mo
%{_datadir}/locale/id/LC_MESSAGES/gnome-radio.mo
%{_datadir}/locale/is/LC_MESSAGES/gnome-radio.mo
%{_datadir}/locale/ka/LC_MESSAGES/gnome-radio.mo
%{_datadir}/locale/nb/LC_MESSAGES/gnome-radio.mo
%{_datadir}/locale/nl/LC_MESSAGES/gnome-radio.mo
%{_datadir}/locale/oc/LC_MESSAGES/gnome-radio.mo
%{_datadir}/locale/pl/LC_MESSAGES/gnome-radio.mo
%{_datadir}/locale/pt_BR/LC_MESSAGES/gnome-radio.mo
%{_datadir}/locale/ro/LC_MESSAGES/gnome-radio.mo
%{_datadir}/locale/ru/LC_MESSAGES/gnome-radio.mo
%{_datadir}/locale/sk/LC_MESSAGES/gnome-radio.mo
%{_datadir}/locale/sl/LC_MESSAGES/gnome-radio.mo
%{_datadir}/locale/sr/LC_MESSAGES/gnome-radio.mo
%{_datadir}/locale/sv/LC_MESSAGES/gnome-radio.mo
%{_datadir}/locale/tr/LC_MESSAGES/gnome-radio.mo
%{_datadir}/locale/uk/LC_MESSAGES/gnome-radio.mo
%{_datadir}/locale/zh_CN/LC_MESSAGES/gnome-radio.mo
%{_datadir}/man/man1/gnome-radio.1.gz
%{_datadir}/metainfo/gnome-radio.appdata.xml
%{_datadir}/metainfo/gtk-radio.appdata.xml
%{_datadir}/metainfo/org.gnome.Radio.appdata.xml
%doc README AUTHORS

%changelog
%autochangelog
