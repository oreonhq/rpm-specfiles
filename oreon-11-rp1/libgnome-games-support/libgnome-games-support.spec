%global source0_hash 0186f25c4892c86c7eac43a307fc19db696df4f19aca7f54e83c221df9d9790a

Name:           libgnome-games-support
Version:        2.0.1
Release:        3%{?dist}
Summary:        Support library for GNOME games

# Automatically converted from old format: LGPLv3+ - review is highly recommended.
License:        LGPL-3.0-or-later
URL:            https://gitlab.gnome.org/GNOME/libgnome-games-support/
Source0:        https://download.gnome.org/sources/libgnome-games-support/2.0/libgnome-games-support-%{version}.tar.xz

BuildRequires:  gcc
BuildRequires:  meson
BuildRequires:  vala
BuildRequires:  pkgconfig(glib-2.0) >= 2.40
BuildRequires:  pkgconfig(gio-2.0) >= 2.40
BuildRequires:  pkgconfig(gee-0.8)
BuildRequires:  pkgconfig(gtk4)

%description
libgnome-games-support is a small library intended for internal use
by GNOME Games, but it may be used by others.
The API will only break with the major version number.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q

%build
%meson
%meson_build

%install
%meson_install

%find_lang libgnome-games-support2

%files -f libgnome-games-support2.lang
%doc README
%license COPYING.LESSER
%{_libdir}/libgnome-games-support-2.so.4*

%files devel
%dir %{_datadir}/vala
%dir %{_datadir}/vala/vapi
%{_datadir}/vala/vapi/*.vapi
%{_includedir}/*
%{_libdir}/*.so
%{_libdir}/pkgconfig/*.pc

%changelog
%autochangelog
