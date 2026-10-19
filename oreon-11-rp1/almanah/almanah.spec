%global source0_hash 0f2c16e8692885fd25ad7dccc3f51ac2b4b887624e68e7ea1f64ae9479319452
Name:		almanah
Version:	0.12.4
Release:        1%{?dist}
Summary:        Application for keeping an encrypted diary
License:	GPL-3.0-or-later
URL:		https://wiki.gnome.org/Apps/Almanah_Diary
Source0:        https://download.gnome.org/sources/almanah/0.12/almanah-%{version}.tar.xz
# oreon:deps
BuildRequires:  appstream
BuildRequires:  desktop-file-utils
BuildRequires:  gcc
BuildRequires:  gettext
BuildRequires:  gpgme-devel
BuildRequires:  meson
BuildRequires:  pkgconfig(cryptui-0.0)
BuildRequires:  pkgconfig(gcr-4)
BuildRequires:  pkgconfig(gtk+-3.0)
BuildRequires:  pkgconfig(gtksourceview-4)
BuildRequires:  pkgconfig(gtkspell3-3.0)
BuildRequires:  pkgconfig(libecal-2.0)
BuildRequires:  pkgconfig(libedataserver-1.2)
BuildRequires:  pkgconfig(sqlite3)
# /oreon:deps
%description
Almanah Diary is a small application to ease the management of an encrypted
personal diary. It's got good editing abilities, including text formatting
and printing. Evolution tasks and appointments will be listed to ease the
creation of diary entries related to them. At the same time, you can create
diary entries using multiple events.

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

%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
