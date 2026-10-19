%global source0_hash 5ef98bd96b3b77eb3880474a2d904e316bb29cbd22dfa0ca85d43b04a28fba34
%global app_id  io.github.TransmissionRemoteGtk
Name:           transmission-remote-gtk
Version:        1.7.1
Release:        1%{?dist}
Summary:        GTK remote control for the Transmission BitTorrent client
License:        GPL-2.0-or-later AND GPL-2.0-only AND LicenseRef-Fedora-Public-Domain
URL:            https://github.com/transmission-remote-gtk/transmission-remote-gtk
Source0:        https://github.com/%{name}/%{name}/releases/download/%{version}/%{name}-%{version}.tar.xz
ExcludeArch:    %{ix86}
# oreon:deps
BuildRequires:  desktop-file-utils
BuildRequires:  gcc
BuildRequires:  gettext
BuildRequires:  git-core
BuildRequires:  libappstream-glib
BuildRequires:  meson
BuildRequires:  pkgconfig(ayatana-appindicator3-0.1)
BuildRequires:  pkgconfig(glib-2.0)
BuildRequires:  pkgconfig(gtk+-3.0)
BuildRequires:  pkgconfig(json-glib-1.0)
BuildRequires:  pkgconfig(libsoup-3.0)
BuildRequires:  python3-docutils
# /oreon:deps
%description
transmission-remote-gtk is a GTK client for remote management of
the Transmission BitTorrent client, using its HTTP RPC protocol.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%oreon_prep
%build

%meson
%meson_build
%install
%meson_install
%find_lang %{name}
%oreon_autofiles main

%check

desktop-file-validate %{buildroot}%{_datadir}/applications/%{app_id}.desktop
appstream-util validate-relax --nonet %{buildroot}%{_metainfodir}/%{app_id}.appdata.xml
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
