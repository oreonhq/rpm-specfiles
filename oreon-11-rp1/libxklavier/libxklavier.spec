%global source0_hash 17a34194df5cbcd3b7bfd0f561d95d1f723aa1c87fca56bc2c209514460a9320

Summary:	High-level API for X Keyboard Extension
Name:		libxklavier
Version:	5.4
Release: 	30%{?dist}
License:	LGPL-2.0-or-later
URL: http://www.freedesktop.org/wiki/Software/LibXklavier
BuildRequires: make
BuildRequires: libxml2-devel
BuildRequires: libxkbfile-devel
BuildRequires: libX11-devel
BuildRequires: libXi-devel
BuildRequires: libxml2-devel
BuildRequires: glib2-devel >= 2.6.0
BuildRequires: iso-codes-devel
BuildRequires: gobject-introspection-devel
Requires: iso-codes
#Source: http://download.gnome.org/sources/libxklavier/5.3/%%{name}-%%{version}.tar.xz
Source: http://people.freedesktop.org/~svu/libxklavier-5.4.tar.bz2

Patch01: 0001-props-fix-the-max-lengths-for-set_name-description-s.patch
Patch02: 0002-config-use-our-name-description-setter-functions.patch
Patch03: 0003-props-validate-name-and-descriptions-for-valid-UTF-8.patch

%description
libxklavier is a library providing a high-level API for the X Keyboard
Extension (XKB). This library is intended to support XFree86 and other
commercial X servers. It is useful for creating XKB-related software
(layout indicators etc).

%package devel
Summary: Development files for libxklavier
Requires: %{name} = %{version}-%{release}
Requires: libxml2-devel

%description devel
This package contains libraries, header files and developer documentation
needed to develop libxklavier applications.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%autosetup -p1 -n libxklavier-5.4

%build
%configure \
  --disable-static \
  --with-xkb-base='%{_datadir}/X11/xkb' \
  --with-xkb-bin-base='%{_bindir}'

make V=1 %{?_smp_mflags}


%install
make install DESTDIR=$RPM_BUILD_ROOT

rm -f $RPM_BUILD_ROOT%{_libdir}/*.{a,la}

%ldconfig_post

%ldconfig_postun

%files
%doc AUTHORS NEWS README COPYING.LIB
%{_libdir}/libxklavier.so.16*
%dir %{_libdir}/girepository-1.0
%{_libdir}/girepository-1.0/Xkl-1.0.typelib

%files devel
%{_libdir}/pkgconfig/libxklavier.pc
%{_libdir}/libxklavier.so
%{_includedir}/libxklavier/
%{_datadir}/gtk-doc
%dir %{_datadir}/gir-1.0
%{_datadir}/gir-1.0/Xkl-1.0.gir

%changelog
* Mon May 25 2026 Oreon Packaging Team <packaging@oreonhq.com> - 5.4-30
- Import
