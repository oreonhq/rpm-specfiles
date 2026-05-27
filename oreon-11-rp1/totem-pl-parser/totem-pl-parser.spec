%global source0_hash c0df0f68d5cf9d7da43c81c7f13f11158358368f98c22d47722f3bd04bd3ac1c

Name:		totem-pl-parser
Version:	3.26.6
Release:	14%{?dist}
Summary:	Totem Playlist Parser library

# Automatically converted from old format: LGPLv2+ - review is highly recommended.
License:	LicenseRef-Callaway-LGPLv2+
Url:		https://wiki.gnome.org/Apps/Videos
Source0:	https://download.gnome.org/sources/%{name}/3.26/%{name}-%{version}.tar.xz
Patch0: totem-pl-parser-c99.patch

BuildRequires:	glib2-devel
BuildRequires:	libxml2-devel
BuildRequires:	gobject-introspection-devel
BuildRequires:	gettext
BuildRequires:	gtk-doc
BuildRequires:	libarchive-devel
BuildRequires:	libgcrypt-devel
BuildRequires:	uchardet-devel
BuildRequires:	meson

%description
A library to parse and save playlists, as used in music and movie players.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%prep
%(test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; })
%autosetup -p1

%build
%meson -Denable-gtk-doc=true \
	-Denable-libarchive=yes \
	-Denable-libgcrypt=yes \
	-Dintrospection=true
%meson_build

%install
%meson_install

%find_lang %{name} --with-gnome

%ldconfig_scriptlets

%files -f %{name}.lang
%license COPYING.LIB
%doc AUTHORS NEWS README.md
%{_libdir}/*.so.*
%{_libdir}/girepository-1.0/*.typelib
%{_libexecdir}/totem-pl-parser/

%files devel
%{_includedir}/*
%{_libdir}/*.so
%{_libdir}/pkgconfig/*.pc
%{_datadir}/gtk-doc/html/totem-pl-parser
%dir %{_datadir}/gir-1.0
%{_datadir}/gir-1.0/*.gir

%changelog
* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 3.26.6-14
- Prepare for Oreon 11 (RP1)
