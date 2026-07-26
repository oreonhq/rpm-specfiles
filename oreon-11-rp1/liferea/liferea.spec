%global source0_hash e7bd66c44aa73d5bee27fafc854e1baed2618953f16c138f5e158bdd75a65132

Name:           liferea
Epoch:          1
Version:        1.16.7
Release:        2%{?dist}
Summary:        An RSS/RDF feed reader

License:        GPL-2.0-or-later
URL:            https://lzone.de/liferea/
Source0:        https://github.com/lwindolf/liferea/releases/download/v%{version}/liferea-%{version}.tar.bz2

# https://fedoraproject.org/wiki/Changes/EncourageI686LeafRemoval
ExcludeArch: %{ix86}

BuildRequires:  desktop-file-utils
BuildRequires:  gcc
BuildRequires:  intltool
BuildRequires:  libappstream-glib
BuildRequires:  make
BuildRequires:  pkgconfig(fribidi)
BuildRequires:  pkgconfig(glib-2.0)
BuildRequires:  pkgconfig(gobject-introspection-1.0)
BuildRequires:  pkgconfig(girepository-2.0)
BuildRequires:  pkgconfig(gsettings-desktop-schemas)
BuildRequires:  pkgconfig(gtk+-3.0)
BuildRequires:  pkgconfig(json-glib-1.0)
BuildRequires:  pkgconfig(libpeas-2)
BuildRequires:  pkgconfig(libsoup-3.0)
BuildRequires:  pkgconfig(libxml-2.0)
BuildRequires:  pkgconfig(libxslt)
BuildRequires:  pkgconfig(sqlite)
BuildRequires:  pkgconfig(webkit2gtk-4.1)
BuildRequires:  pkgconfig(webkit2gtk-web-extension-4.1)
BuildRequires:  xorg-x11-server-Xvfb

Requires:       libpeas-loader-python%{?_isa} >= 2
# gobject introspection dependencies
Recommends:     gstreamer1-plugins-base%{?_isa}
Recommends:     libappindicator-gtk3%{?_isa}
Recommends:     libnotify%{?_isa}
Recommends:     libsecret%{?_isa}

%description
Liferea (Linux Feed Reader) is an RSS/RDF feed reader.
It's intended to be a clone of the Windows-only FeedReader.
It can be used to maintain a list of subscribed feeds,
browse through their items, and show their contents.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1 -n %{name}-%{version}

%build
%configure --disable-static

xvfb-run -- %make_build

%install
%make_install

%find_lang %{name}

# Upstream sets Version to 1.1 although the 1.1 spec says to use 1.0
desktop-file-edit --set-key=Version --set-value=1.0 %{buildroot}/%{_datadir}/applications/net.sourceforge.liferea.desktop
desktop-file-validate %{buildroot}/%{_datadir}/applications/net.sourceforge.liferea.desktop

%check
appstream-util validate-relax --nonet %{buildroot}%{_datadir}/metainfo/net.sourceforge.liferea.appdata.xml

%files -f %{name}.lang
%doc AUTHORS ChangeLog
%license COPYING
%{_mandir}/man1/%{name}.1*
%lang(it) %{_mandir}/it/man1/%{name}.1*
%{_bindir}/%{name}
%{_bindir}/%{name}-add-feed
%{_libdir}/%{name}
%{_datadir}/%{name}/
%{_datadir}/metainfo/net.sourceforge.liferea.appdata.xml
%{_datadir}/applications/net.sourceforge.liferea.desktop
%{_datadir}/dbus-1/services/net.sourceforge.liferea.service
%{_datadir}/glib-2.0/schemas/net.sf.liferea.gschema.xml
%{_datadir}/GConf/gsettings/liferea.convert
%{_datadir}/icons/hicolor/16x16/apps/net.sourceforge.liferea.png
%{_datadir}/icons/hicolor/22x22/apps/net.sourceforge.liferea.png
%{_datadir}/icons/hicolor/24x24/apps/net.sourceforge.liferea.png
%{_datadir}/icons/hicolor/32x32/apps/net.sourceforge.liferea.png
%{_datadir}/icons/hicolor/48x48/apps/net.sourceforge.liferea.png
%{_datadir}/icons/hicolor/scalable/apps/net.sourceforge.liferea*.svg

%changelog
%autochangelog
