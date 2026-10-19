%global source0_hash 9ec1900cc51409c2067c07c828c10be06fe3bf68d2999bb72d7d5ed325ed9bbc
%global gettext_version 0.22
%global glib2_version 2.78.3
%global gtk4_version 4.15.2
%global libadwaita_version 1.6~beta
%global libsoup_version 3.0
%global major_minor_version %(echo %{version} | cut -d "." -f 1-2)
Name:		gnome-online-accounts
Version:	3.58.1
Release:        1%{?dist}
Summary:        Single sign-on framework for GNOME
License:	LGPL-2.0-or-later AND CC-BY-SA-4.0
URL:		https://wiki.gnome.org/Projects/GnomeOnlineAccounts
Source0:        https://download.gnome.org/sources/%{name}/3.58/%{name}-%{version}.tar.xz
%if !0%{?flatpak}
%endif
Requires:	%{name}-libs%{?_isa} = %{version}-%{release}
%if !0%{?flatpak}
Requires:	gvfs-goa
Recommends:	evolution-ews-core
%endif
# oreon:deps
BuildRequires:  /usr/bin/desktop-file-validate
BuildRequires:  /usr/bin/gi-docgen
BuildRequires:  /usr/bin/xsltproc
BuildRequires:  docbook-style-xsl
BuildRequires:  gettext
BuildRequires:  meson
BuildRequires:  pkgconfig(dbus-1)
BuildRequires:  pkgconfig(gcr-4)
BuildRequires:  pkgconfig(gio-2.0)
BuildRequires:  pkgconfig(glib-2.0)
BuildRequires:  pkgconfig(gobject-2.0)
BuildRequires:  pkgconfig(gobject-introspection-1.0)
BuildRequires:  pkgconfig(gtk4)
BuildRequires:  pkgconfig(json-glib-1.0)
BuildRequires:  pkgconfig(krb5)
BuildRequires:  pkgconfig(libadwaita-1)
BuildRequires:  pkgconfig(libkeyutils)
BuildRequires:  pkgconfig(libsecret-1)
BuildRequires:  pkgconfig(libsoup-3.0)
BuildRequires:  pkgconfig(libxml-2.0)
BuildRequires:  pkgconfig(rest-1.0)
BuildRequires:  vala
# /oreon:deps
%description
GNOME Online Accounts provides interfaces so that applications and libraries
in GNOME can access the user's online accounts. It has providers for Google,
Nextcloud, Flickr, Foursquare, Microsoft Account, Microsoft Exchange, Fedora,
IMAP/SMTP and Kerberos.

%package libs
Summary:	Libraries for %{name}
Requires:	glib2%{?_isa} >= %{glib2_version}
%if !0%{?flatpak}
Requires:	gtk4%{?_isa} >= %{gtk4_version}
Requires:	libadwaita%{?_isa} >= %{libadwaita_version}
Requires:	libsoup3%{?_isa} >= %{libsoup_version}
%endif
%description libs
This package contains the libraries for GNOME Online Accounts. It is separated
from the main package to avoid build-time dependency loops.

%package devel
Summary:	Development files for %{name}
Requires:	%{name}-libs%{?_isa} = %{version}-%{release}
%description devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%oreon_prep
%build

%meson \
%if 0%{?flatpak}
  -Dgoabackend=false \
%else
  -Dfedora=true \
%endif
  %{nil}
%meson_build
%install
%meson_install
%find_lang %{name}
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*

%check

%if !0%{?flatpak}
desktop-file-validate %{buildroot}/%{_datadir}/applications/org.gnome.OnlineAccounts.OAuth2.desktop
%endif
%files -f %{oreon_filedir}/main.list
%files -n gnome-online-accounts-libs -f %{oreon_filedir}/gnome-online-accounts-libs.list
%files -n gnome-online-accounts-devel -f %{oreon_filedir}/gnome-online-accounts-devel.list

%changelog

* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 3.58.0-1
- Prepare for Oreon 11 (RP1)
