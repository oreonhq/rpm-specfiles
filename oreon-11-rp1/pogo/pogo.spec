%global source0_hash 884f1d3f4f8a9a0688bc55c1bc83f5c8dbbaf12cf95826d29b8cdebd50f50f2d
Name:		pogo
Version:	1.0.1
Release:        1%{?dist}
Summary:        Probably the simplest and fastest audio player for Linux
Summary(de):	Möglicherweise der einfachste und schnellste Audioplayer für Linux
License:	GPL-2.0-or-later
URL:		https://github.com/jendrikseipp/pogo
Source0:        https://github.com/jendrikseipp/%{name}/archive/%{name}-%{version}.tar.gz
BuildArch:	noarch
Requires:	python3-dbus
Requires:	python3-mutagen
Requires:	python3-pillow
Requires:	python3-inotify
Requires:	python3-gobject
Requires:	python3-gstreamer1
Obsoletes: pogo < %{version}
Obsoletes: pogo-zeitgeist < %{version}
# oreon:deps
BuildRequires:  desktop-file-utils
BuildRequires:  intltool
BuildRequires:  libappstream-glib
BuildRequires:  make
BuildRequires:  python3-devel
# /oreon:deps
%description
Pogo's elementary-inspired design uses the screen-space very efficiently. It is
especially well-suited for people who organize their music by albums on the
harddrive. The main interface components are a directory tree and a playlist
that groups albums in an innovative way.
Pogo is a fork of Decibel Audio Player.

%description -l de
Das Elementary-inspirierte Design von Pogo nutzt den Platz auf dem Bildschirm
effizient. Es richtet sich speziell an Benutzer, die Ihre Musik nach Alben
auf der Festplatte verwalten. Die Hauptkomponenten der Benutzeroberfläche
sind ein Ordnerbaum und eine Wiedergabeliste, die Alben auf innovative
Weise gruppiert.
Pogo ist ein Fork des Decibel Audio Players.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%oreon_prep
%build

%install
%make_install
%find_lang %{name}
desktop-file-validate $RPM_BUILD_ROOT/%{_datadir}/applications/%{name}.desktop
install -D -p -m644 %{name}.appdata.xml %{buildroot}/%{_datadir}/appdata/%{name}.appdata.xml
appstream-util validate-relax --nonet %{buildroot}/%{_datadir}/appdata/*.appdata.xml
%oreon_autofiles main

%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
