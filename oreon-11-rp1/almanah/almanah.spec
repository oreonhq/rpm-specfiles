%global source0_hash 0f2c16e8692885fd25ad7dccc3f51ac2b4b887624e68e7ea1f64ae9479319452

Name:		almanah
Version:	0.12.4
Release:	5%{?dist}
Summary:	Application for keeping an encrypted diary

License:	GPL-3.0-or-later
URL:		https://wiki.gnome.org/Apps/Almanah_Diary
Source0:	https://download.gnome.org/sources/almanah/0.12/almanah-%{version}.tar.xz

BuildRequires:	appstream
BuildRequires:	gcc
BuildRequires:	gettext
BuildRequires:	gpgme-devel
BuildRequires:	desktop-file-utils
BuildRequires:	meson
BuildRequires:	pkgconfig(cryptui-0.0)
BuildRequires:	pkgconfig(gtk+-3.0)
BuildRequires:	pkgconfig(gcr-4)
BuildRequires:	pkgconfig(gtkspell3-3.0)
BuildRequires:	pkgconfig(gtksourceview-4)
BuildRequires:	pkgconfig(libecal-2.0) >= 3.45.1
BuildRequires:	pkgconfig(libedataserver-1.2) >= 3.45.1
BuildRequires:	pkgconfig(sqlite3)

%description
Almanah Diary is a small application to ease the management of an encrypted
personal diary. It's got good editing abilities, including text formatting
and printing. Evolution tasks and appointments will be listed to ease the
creation of diary entries related to them. At the same time, you can create
diary entries using multiple events.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1 -S gendiff

%build
%meson
%meson_build

%install
%meson_install

%find_lang %{name}

%files -f %{name}.lang
%license COPYING
%doc AUTHORS NEWS.md README.md
%{_bindir}/%{name}
%{_datadir}/icons/hicolor/*/apps/org.gnome.Almanah.png
%{_datadir}/icons/hicolor/scalable/actions/org.gnome.Almanah-tags-symbolic.svg
%{_datadir}/icons/hicolor/scalable/apps/org.gnome.Almanah-symbolic.svg
%{_datadir}/applications/org.gnome.Almanah.desktop
%{_datadir}/metainfo/org.gnome.Almanah.metainfo.xml
%{_datadir}/glib-2.0/schemas/org.gnome.%{name}.gschema.xml

%changelog
%autochangelog
