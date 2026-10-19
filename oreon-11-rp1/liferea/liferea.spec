%global source0_hash e7bd66c44aa73d5bee27fafc854e1baed2618953f16c138f5e158bdd75a65132
Name:           liferea
Epoch:          1
Version:        2.0.1
Release:        1%{?dist}
Summary:        An RSS/RDF feed reader
License:        GPL-2.0-or-later
URL:            https://lzone.de/liferea/
Source0:        https://github.com/lwindolf/liferea/releases/download/v%{version}/liferea-%{version}.tar.bz2
ExcludeArch: %{ix86}
Requires:       libpeas-loader-python%{?_isa} >= 2
Recommends:     gstreamer1-plugins-base%{?_isa}
Recommends:     libappindicator-gtk3%{?_isa}
Recommends:     libnotify%{?_isa}
Recommends:     libsecret%{?_isa}
# oreon:deps
BuildRequires:  desktop-file-utils
BuildRequires:  gcc
BuildRequires:  intltool
BuildRequires:  libappstream-glib
BuildRequires:  make
BuildRequires:  pkgconfig(fribidi)
BuildRequires:  pkgconfig(girepository-2.0)
BuildRequires:  pkgconfig(glib-2.0)
BuildRequires:  pkgconfig(gobject-introspection-1.0)
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
# /oreon:deps
%description
Liferea (Linux Feed Reader) is an RSS/RDF feed reader.
It's intended to be a clone of the Windows-only FeedReader.
It can be used to maintain a list of subscribed feeds,
browse through their items, and show their contents.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%global oreon_srcdir %{name}-%{version}
%oreon_prep
%build

%configure --disable-static
xvfb-run -- %make_build
%install
%make_install
%find_lang %{name}
desktop-file-edit --set-key=Version --set-value=1.0 %{buildroot}/%{_datadir}/applications/net.sourceforge.liferea.desktop
desktop-file-validate %{buildroot}/%{_datadir}/applications/net.sourceforge.liferea.desktop
%oreon_autofiles main

%check

appstream-util validate-relax --nonet %{buildroot}%{_datadir}/metainfo/net.sourceforge.liferea.appdata.xml
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
