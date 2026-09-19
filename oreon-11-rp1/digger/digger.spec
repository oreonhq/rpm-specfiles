%global source0_hash 5d47bd3634a2a15237158db51b9bb8b06952493c3b502de30f35bd3d83a422a6

Name:           digger
Version:        2.6.1
Release:        %autorelease
Summary:        Advanced DNS Lookup Tool

License:        GPL-3.0-or-later
URL:            https://github.com/tobagin/digger
Source0:        %{url}/archive/refs/tags/v%{version}/%{name}-%{version}.tar.gz

BuildRequires:  blueprint-compiler
BuildRequires:  desktop-file-utils
BuildRequires:  meson
BuildRequires:  vala
BuildRequires:  libappstream-glib
BuildRequires:  pkgconfig(gee-0.8)
BuildRequires:  pkgconfig(gio-2.0)
BuildRequires:  pkgconfig(gtk4) >= 4.6.0
BuildRequires:  pkgconfig(json-glib-1.0)
BuildRequires:  pkgconfig(libadwaita-1) >= 1.0
BuildRequires:  pkgconfig(libsoup-3.0)

Requires:       hicolor-icon-theme
Requires:       glib2
Requires:       %{_bindir}/dig

%description
A powerful and modern DNS lookup tool built with Vala, GTK4, and libadwaita.
Digger provides an intuitive interface for performing DNS queries with
advanced features including batch lookups, server comparison, DNSSEC validation,
and DNS-over-HTTPS support.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup

%build
%meson
%meson_build

%install
%meson_install

%check
desktop-file-validate %{buildroot}%{_datadir}/applications/io.github.tobagin.digger.desktop
appstream-util validate-relax --nonet %{buildroot}%{_metainfodir}/*.metainfo.xml

%files
%license LICENSE
%doc README.md
%{_bindir}/digger-vala
%{_datadir}/applications/io.github.tobagin.digger.desktop
%{_datadir}/%{name}/
%{_datadir}/glib-2.0/schemas/io.github.tobagin.digger.gschema.xml
%{_datadir}/icons/hicolor/scalable/apps/io.github.tobagin.digger*.svg
%{_metainfodir}/io.github.tobagin.digger.metainfo.xml

%changelog
%autochangelog
