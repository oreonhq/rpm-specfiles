%global source0_hash af52daa03d4ffff8cde1f9fc397689d1037dd2d0b9183df89af28e6f982132bf
Name:           cambalache
Version:        1.0.3
Release:        1%{?dist}
Summary:        User interface maker
License:        LGPL-2.1-only AND GPL-2.0-only AND GPL-2.0-or-later
URL:            https://gitlab.gnome.org/jpu/cambalache
Source0:        https://gitlab.gnome.org/jpu/%{name}/-/archive/%{version}/%{name}-%{version}.tar.gz
Requires:  cambalache-data
Requires:  hicolor-icon-theme
Requires:  gobject-introspection-devel%{?_isa}
Requires:  libadwaita
Requires:  pkgconfig(casilda-1.0)
Requires:  python3-gobject-base
Requires:  python3-lxml
Requires:  gtksourceview5-devel
Requires:  webkitgtk6.0-devel
Requires:  webkit2gtk4.1-devel
# oreon:deps
BuildRequires:  desktop-file-utils
BuildRequires:  gcc
BuildRequires:  gtksourceview5-devel
BuildRequires:  libappstream-glib
BuildRequires:  meson
BuildRequires:  pkgconfig(casilda-1.0)
BuildRequires:  pkgconfig(gtk+-3.0)
BuildRequires:  pkgconfig(gtk4)
BuildRequires:  pkgconfig(libadwaita-1)
BuildRequires:  pkgconfig(libhandy-1)
BuildRequires:  pkgconfig(libxml-2.0)
BuildRequires:  pkgconfig(pygobject-3.0)
BuildRequires:  python3-devel
BuildRequires:  python3-gobject-devel
BuildRequires:  python3-lxml
BuildRequires:  python3-pytest
BuildRequires:  webkit2gtk4.1-devel
BuildRequires:  webkitgtk6.0-devel
# /oreon:deps
%description
Cambalache is a RAD tool for Gtk 4 and 3 with a clear MVC design and data model
first philosophy. This translates to a wide feature coverage with minimal/none
developer intervention for basic support.

%package data
Summary: Shared data files for Cambalache
BuildArch: noarch
%description data
Common data files used across all architectures.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%global oreon_srcdir cambalache-%{version}
%oreon_prep
%build

%meson
%meson_build
%install
%meson_install
%find_lang %{name}
%oreon_autofiles cambalache-data usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%check

desktop-file-validate %{buildroot}/%{_datadir}/applications/ar.xjuan.Cambalache.desktop
appstream-util validate-relax --nonet %{buildroot}%{_metainfodir}/ar.xjuan.Cambalache.metainfo.xml
%files -f %{oreon_filedir}/main.list
%files -n cambalache-data -f %{oreon_filedir}/cambalache-data.list

%changelog

%autochangelog
