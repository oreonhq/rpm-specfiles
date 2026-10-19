%global source0_hash 9c1917e4a61f7febb787849ce36ce717fce706c346880b991d056d54dadbcacc
%global tarball_version %(echo %{version} | tr '~' '.')
Name:           seahorse
Version:        47.0.1
Release:        1%{?dist}
Summary:        A GNOME application for managing encryption keys
License:        GPL-2.0-or-later AND LGPL-2.0-or-later AND CC-BY-SA-3.0
URL:            https://wiki.gnome.org/Apps/Seahorse
Source0:        https://download.gnome.org/sources/%{name}/47/%{name}-%{version}.tar.xz
Patch1:         seahorse-47.0.1-allow-build-with-gpgme2.patch
Requires:       pinentry-gui
# oreon:deps
BuildRequires:  /usr/bin/appstream-util
BuildRequires:  /usr/bin/xsltproc
BuildRequires:  desktop-file-utils
BuildRequires:  docbook-style-xsl
BuildRequires:  gettext
BuildRequires:  gnupg2
BuildRequires:  gpgme-devel
BuildRequires:  itstool
BuildRequires:  libSM-devel
BuildRequires:  meson
BuildRequires:  openldap-devel
BuildRequires:  openssh-clients
BuildRequires:  pkgconfig(avahi-client)
BuildRequires:  pkgconfig(avahi-glib)
BuildRequires:  pkgconfig(gck-1)
BuildRequires:  pkgconfig(gcr-3)
BuildRequires:  pkgconfig(gio-2.0)
BuildRequires:  pkgconfig(gtk+-3.0)
BuildRequires:  pkgconfig(libhandy-1)
BuildRequires:  pkgconfig(libsecret-unstable)
BuildRequires:  pkgconfig(libsoup-3.0)
BuildRequires:  pkgconfig(pwquality)
BuildRequires:  vala
# /oreon:deps
%description
Seahorse is a graphical interface for managing and using encryption keys.
It also integrates with nautilus, gedit and other places for encryption
operations.  It is a keyring manager.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%autosetup -p1 -n %{name}-%{tarball_version}

%build

%meson -Dmanpage=true
%meson_build
%install
%meson_install
%find_lang seahorse --with-gnome --all-name
%oreon_autofiles main

%check

appstream-util validate-relax --nonet $RPM_BUILD_ROOT/%{_metainfodir}/org.gnome.seahorse.Application.appdata.xml
desktop-file-validate ${RPM_BUILD_ROOT}%{_datadir}/applications/org.gnome.seahorse.Application.desktop
%files -f %{oreon_filedir}/main.list

%changelog

* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 47.0.1-1
- Prepare for Oreon 11 (RP1)
