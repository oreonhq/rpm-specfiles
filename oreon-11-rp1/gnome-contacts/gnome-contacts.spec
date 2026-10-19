%global source0_hash c8b60752f65a966e0a2c0cbf7c1e1607ee3b4a49318b50b19bdad2ab7fc6706d
%global gtk4_version 4.15.3
%global tarball_version %%(echo %{version} | tr '~' '.')
Name:           gnome-contacts
Version:        51.0
Release:        1%{?dist}
Summary:        Contacts manager for GNOME
%global tarball_version %%(echo %{version} | tr '~' '.')
%global major_version %%(cut -d "." -f 1 <<<%{tarball_version})
License:        GPL-2.0-or-later AND CC0-1.0 AND CC-BY-SA-4.0
URL:            https://apps.gnome.org/Contacts
Source0:        https://download.gnome.org/sources/%{name}/51/%{name}-%{version}.tar.xz
Requires:       gtk4%{?_isa} >= %{gtk4_version}
Requires:       hicolor-icon-theme
Requires:       gstreamer1-plugin-gtk4
Requires:       pipewire-gstreamer
# oreon:deps
BuildRequires:  /usr/bin/appstreamcli
BuildRequires:  /usr/bin/xsltproc
BuildRequires:  blueprint-compiler
BuildRequires:  desktop-file-utils
BuildRequires:  docbook-dtds
BuildRequires:  docbook-style-xsl
BuildRequires:  gettext
BuildRequires:  meson
BuildRequires:  pkgconfig(folks)
BuildRequires:  pkgconfig(folks-eds)
BuildRequires:  pkgconfig(gee-0.8)
BuildRequires:  pkgconfig(glycin-gtk4-2)
BuildRequires:  pkgconfig(goa-1.0)
BuildRequires:  pkgconfig(gobject-introspection-1.0)
BuildRequires:  pkgconfig(gstreamer-1.0)
BuildRequires:  pkgconfig(gtk4)
BuildRequires:  pkgconfig(libadwaita-1)
BuildRequires:  pkgconfig(libportal-gtk4)
BuildRequires:  pkgconfig(libqrencode)
BuildRequires:  vala
# /oreon:deps
%description
%{name} is a standalone contacts manager for GNOME desktop.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1 -n %{name}-%{tarball_version}

%build

%meson
%meson_build
%install
%meson_install
appstreamcli metainfo-to-news %{buildroot}/%{_metainfodir}/org.gnome.Contacts.metainfo.xml NEWS
%find_lang %{name}
%oreon_autofiles main

%check

appstreamcli validate --no-net %{buildroot}/%{_metainfodir}/org.gnome.Contacts.metainfo.xml
desktop-file-validate %{buildroot}/%{_datadir}/applications/org.gnome.Contacts.desktop
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
