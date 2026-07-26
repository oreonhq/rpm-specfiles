%global source0_hash fa351c3cf981843729f76b2a712582922bf17c37a6b62b69fc0fea5c56dda91c

%global appid com.github.hugolabe.Wike

Name:           wike
Version:        3.2.0
Release:        %autorelease
Summary:        Wikipedia Reader for the GNOME Desktop

License:        GPL-3.0-or-later
URL:            https://hugolabe.github.io/Wike
Source0:        https://github.com/hugolabe/wike/archive/%{version}/%{name}-%{version}.tar.gz

BuildArch:      noarch

BuildRequires:  python3-devel
BuildRequires:  meson
BuildRequires:  gettext
BuildRequires:  glib2-devel
BuildRequires:  desktop-file-utils
BuildRequires:  libappstream-glib
BuildRequires:  gtk-update-icon-cache

Requires:       hicolor-icon-theme
Requires:       python3-gobject
Requires:       gtk4
Requires:       libadwaita
Requires:       webkitgtk6.0
Requires:       libsoup
Requires:       pango

%description
Wike is a Wikipedia reader for the GNOME Desktop. Provides access to all the
content of this online encyclopedia in a native application, with a simpler and
distraction-free view of articles.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n Wike-%{version}

%build
%meson
%meson_build

%install
%meson_install
%find_lang %{name}

%check
appstream-util validate-relax --nonet %{buildroot}/%{_metainfodir}/%{appid}.metainfo.xml
desktop-file-validate %{buildroot}/%{_datadir}/applications/%{appid}.desktop

%files -f %{name}.lang
%license COPYING
%doc README.md
%{_bindir}/%{name}
%{_datadir}/%{name}
%{_datadir}/applications/%{appid}.desktop
%{_datadir}/icons/hicolor/*/apps/*
%{_datadir}/glib-2.0/schemas/%{appid}.gschema.xml
%{_metainfodir}/%{appid}.metainfo.xml
%dir %{_datadir}/dbus-1
%dir %{_datadir}/dbus-1/services
%{_datadir}/dbus-1/services/%{appid}.service
%{_datadir}/dbus-1/services/%{appid}.SearchProvider.service
%dir %{_datadir}/gnome-shell
%dir %{_datadir}/gnome-shell/search-providers
%{_datadir}/gnome-shell/search-providers/%{appid}.SearchProvider.ini

%changelog
%autochangelog
