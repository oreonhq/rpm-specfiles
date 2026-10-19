%global source0_hash afad151302817ddf098b5e416e7ac7f2d5eea567a3b80bb90bd3c62afd13b9a1
%global tarball_version %%(echo %{version} | tr '~' '.')
Name:		geary
Version:	46.0
Release:        9%{?dist}
Summary:        A lightweight email program designed around conversations
License:	LGPL-2.1-or-later AND CC-BY-3.0 AND CC-BY-SA-3.0 AND LicenseRef-Callaway-Public-Domain
URL:		https://wiki.gnome.org/Apps/Geary
Source0:        https://download.gnome.org/sources/%{name}/46/%{name}-%{version}.tar.xz
Requires:	hicolor-icon-theme
Recommends:	gnome-keyring
# oreon:deps
BuildRequires:  desktop-file-utils
BuildRequires:  fakechroot
BuildRequires:  gettext
BuildRequires:  itstool
BuildRequires:  libstemmer-devel
BuildRequires:  meson
BuildRequires:  pkgconfig(appstream-glib)
BuildRequires:  pkgconfig(cairo)
BuildRequires:  pkgconfig(enchant-2)
BuildRequires:  pkgconfig(folks)
BuildRequires:  pkgconfig(gck-1)
BuildRequires:  pkgconfig(gcr-3)
BuildRequires:  pkgconfig(gdk-3.0)
BuildRequires:  pkgconfig(gee-0.8)
BuildRequires:  pkgconfig(gio-2.0)
BuildRequires:  pkgconfig(glib-2.0)
BuildRequires:  pkgconfig(gmime-3.0)
BuildRequires:  pkgconfig(goa-1.0)
BuildRequires:  pkgconfig(gsound)
BuildRequires:  pkgconfig(gspell-1)
BuildRequires:  pkgconfig(gthread-2.0)
BuildRequires:  pkgconfig(gtk+-3.0)
BuildRequires:  pkgconfig(icu-uc)
BuildRequires:  pkgconfig(iso-codes)
BuildRequires:  pkgconfig(javascriptcoregtk-4.1)
BuildRequires:  pkgconfig(json-glib-1.0)
BuildRequires:  pkgconfig(libhandy-1)
BuildRequires:  pkgconfig(libpeas-1.0)
BuildRequires:  pkgconfig(libsecret-1)
BuildRequires:  pkgconfig(libsoup-3.0)
BuildRequires:  pkgconfig(libunwind)
BuildRequires:  pkgconfig(libunwind-generic)
BuildRequires:  pkgconfig(libxml-2.0)
BuildRequires:  pkgconfig(libytnef)
BuildRequires:  pkgconfig(sqlite3)
BuildRequires:  pkgconfig(webkit2gtk-4.1)
BuildRequires:  pkgconfig(webkit2gtk-web-extension-4.1)
BuildRequires:  python3
BuildRequires:  symlinks
BuildRequires:  vala
BuildRequires:  valadoc
# /oreon:deps
%description
Geary is a new email reader for GNOME designed to let you read your
email quickly and effortlessly. Its interface is based on
conversations, so you can easily read an entire discussion without
having to click from message to message. Geary is still in early
development and has limited features today, but we're planning to add
drag-and-drop attachments, lightning-fast searching, multiple account
support and much more. Eventually we'd like Geary to have an
extensible plugin architecture so that developers will be able to add
all kinds of nifty features in a modular way.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1 -n %{name}-%{tarball_version}

%build

%meson -Dprofile=release
%meson_build
%install
%meson_install
desktop-file-validate \
  %{buildroot}%{_datadir}/applications/org.gnome.Geary.desktop \
  %{buildroot}%{_datadir}/applications/geary-autostart.desktop
pushd %{buildroot}
fakechroot -- symlinks -C -cvr %{_datadir}/help
popd
%find_lang %{name} --with-gnome
%oreon_autofiles main

%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
