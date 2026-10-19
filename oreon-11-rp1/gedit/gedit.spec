%global source0_hash c2d064001b95196f046a6f9705245e3a02dc427265f4e24af9bd2d5f3cb619ee
%global amtk_version 5.9
%global glib2_version 2.76
%global gtk3_version 3.22
%global gtksourceview_version 299.6
%global libpeas_version 1.14.1
%global gspell_version 1.0
%global tepl_version 6.14
%global __provides_exclude_from ^%{_libdir}/gedit/plugins/
%global api_version %%(ver=%{version}; echo ${ver%%.*})
%global tarball_version %%(ver=%{version}; echo ${ver//~/.})
%global libgd_commit 3cccf99234288a6121b3945a25cd4ec3b7445c74
Name:		gedit
Epoch:		2
Version:	50.0
Release:        1%{?dist}
Summary:        Text editor for the GNOME desktop
License:	GPL-3.0-or-later AND LGPL-3.0-or-later
URL:		https://gedit-text-editor.org/
Source0:        https://gitlab.gnome.org/World/gedit/%{name}/-/archive/%{version}/%{name}-%{version}.tar.bz2
Provides: bundled(libgd) = %{libgd_commit}
Requires: glib2%{?_isa} >= %{glib2_version}
Requires: gspell%{?_isa} >= %{gspell_version}
Requires: gtk3%{?_isa} >= %{gtk3_version}
Requires: libgedit-gtksourceview%{?_isa} >= %{gtksourceview_version}
Requires: libgedit-tepl%{?_isa} >= %{tepl_version}
Requires: python3-gobject
Requires: gsettings-desktop-schemas
Obsoletes: gedit-collaboration < 3.6.1-6
Obsoletes: gedit-plugin-zeitgeist < 3.35.90
Obsoletes: gedit-plugin-commander < 43.0
Obsoletes: gedit-plugin-findinfiles < 43.0
Obsoletes: gedit-plugin-translate < 43.0
Obsoletes: gedit-plugin-colorschemer < 45.0
Obsoletes: gedit-plugin-synctex < 45.0
Obsoletes: gedit-plugin-git < 48.0
Obsoletes: gedit-plugin-textsize < 48.0
Obsoletes: gedit-color-schemes < 0-18
Obsoletes: gedit-control-your-tabs < 0.5.2
Obsoletes: gedit-latex < 48.0
Obsoletes: gedit-plugin-bracketcompletion < 48.2
Obsoletes: gedit-plugin-charmap < 48.2
Obsoletes: gedit-plugin-codecomment < 48.2
Obsoletes: gedit-plugin-colorpicker < 48.2
Obsoletes: gedit-plugin-joinlines < 48.2
Obsoletes: gedit-plugin-multiedit < 48.2
Obsoletes: gedit-plugin-sessionsaver < 48.2
Obsoletes: gedit-plugin-terminal < 48.2
# oreon:deps
BuildRequires:  /usr/bin/appstream-util
BuildRequires:  desktop-file-utils
BuildRequires:  gettext
BuildRequires:  gtk-doc
BuildRequires:  itstool
BuildRequires:  meson
BuildRequires:  pkgconfig(glib-2.0)
BuildRequires:  pkgconfig(gobject-introspection-1.0)
BuildRequires:  pkgconfig(gsettings-desktop-schemas)
BuildRequires:  pkgconfig(gspell-1)
BuildRequires:  pkgconfig(gtk+-3.0)
BuildRequires:  pkgconfig(libgedit-amtk-5)
BuildRequires:  pkgconfig(libgedit-gtksourceview-300)
BuildRequires:  pkgconfig(libgedit-tepl-6)
BuildRequires:  pkgconfig(libpeas-gtk-1.0)
BuildRequires:  which
BuildRequires:  yelp-tools
# /oreon:deps
%description
gedit is a small, but powerful text editor designed specifically for
the GNOME desktop. It has most standard text editor functions and fully
supports international text in Unicode. Advanced features include syntax
highlighting and automatic indentation of source code, printing and editing
of multiple documents in one window.

gedit is extensible through a plugin system, which currently includes
support for spell checking, comparing files, viewing CVS ChangeLogs, and
adjusting indentation levels. Further plugins can be found in the
gedit-plugins package.

%package devel
Summary: Support for developing plugins for the gedit text editor
Requires: %{name}%{?_isa} = %{epoch}:%{version}-%{release}
%description devel
gedit is a small, but powerful text editor for the GNOME desktop.
This package allows you to develop plugins that add new functionality
to gedit.

Install gedit-devel if you want to write plugins for gedit.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%autosetup -p1 -n %{name}-%{tarball_version}
tar --strip-components=1 -xf %{S:1} -C subprojects/libgd

%build

%meson -Dgtk_doc=true
%define __ninja_common_opts -v
%meson_build
%install
%meson_install
%find_lang %{name} --with-gnome
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*

%check

appstream-util validate-relax --nonet %{buildroot}%{_metainfodir}/org.gnome.gedit.metainfo.xml
desktop-file-validate %{buildroot}%{_datadir}/applications/org.gnome.gedit.desktop
%files -f %{oreon_filedir}/main.list
%files -n gedit-devel -f %{oreon_filedir}/gedit-devel.list

%changelog

* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 49.0-1
- Prepare for Oreon 11 (RP1)
