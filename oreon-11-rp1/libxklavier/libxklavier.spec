%global source0_hash 17a34194df5cbcd3b7bfd0f561d95d1f723aa1c87fca56bc2c209514460a9320
Summary:        High-level API for X Keyboard Extension
Name:		libxklavier
Version:	5.4
Release:        1%{?dist}
License:	LGPL-2.0-or-later
URL: http://www.freedesktop.org/wiki/Software/LibXklavier
Requires: iso-codes
Source0:        https://people.freedesktop.org/~svu/libxklavier-5.4.tar.bz2
Patch01: 0001-props-fix-the-max-lengths-for-set_name-description-s.patch
Patch02: 0002-config-use-our-name-description-setter-functions.patch
Patch03: 0003-props-validate-name-and-descriptions-for-valid-UTF-8.patch
# oreon:deps
BuildRequires:  glib2-devel
BuildRequires:  gobject-introspection-devel
BuildRequires:  iso-codes-devel
BuildRequires:  libX11-devel
BuildRequires:  libXi-devel
BuildRequires:  libxkbfile-devel
BuildRequires:  libxml2-devel
BuildRequires:  make
# /oreon:deps
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
%global oreon_srcdir libxklavier-5.4
%oreon_prep
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
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*

%files -f %{oreon_filedir}/main.list
%files -n libxklavier-devel -f %{oreon_filedir}/libxklavier-devel.list

%changelog

* Mon May 25 2026 Oreon Packaging Team <packaging@oreonhq.com> - 5.4-30
- Import
