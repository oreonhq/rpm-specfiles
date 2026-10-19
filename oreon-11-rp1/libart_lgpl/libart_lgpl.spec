%global source0_hash fdc11e74c10fc9ffe4188537e2b370c0abacca7d89021d4d303afdf7fd7476fa
Name: libart_lgpl
Version: 2.3.21
Release:        37%{?dist}
Summary:        Library of graphics routines used by libgnomecanvas
URL: http://www.gnome.org/
Source0:        http://download.gnome.org/sources/libart_lgpl/2.3/%{name}-%{version}.tar.bz2
Patch0: libart-multilib.patch
License: LicenseRef-Callaway-LGPLv2+
# oreon:deps
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  libtool
BuildRequires:  make
BuildRequires:  pkgconfig
# /oreon:deps
%description
Graphics routines used by the GnomeCanvas widget and some other 
applications. libart renders vector paths and the like.

%package devel
Summary: Libraries and headers for libart_lgpl
Requires: %{name} = %{version}-%{release}
%description devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q
%patch -P0 -p1 -b .multilib

%build

libtoolize
autoreconf -i
%configure --disable-static
make %{?_smp_mflags}
%install
make install DESTDIR=$RPM_BUILD_ROOT INSTALL="install -p"
find $RPM_BUILD_ROOT -name '*.la' -exec rm -f {} ';'
mv $RPM_BUILD_ROOT%{_includedir}/libart-2.0/libart_lgpl/art_config.h \
   $RPM_BUILD_ROOT%{_includedir}/libart-2.0/libart_lgpl/art_config-%{__isa_bits}.h
cat >$RPM_BUILD_ROOT%{_includedir}/libart-2.0/libart_lgpl/art_config.h <<EOF
EOF
%ldconfig_scriptlets
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*

%files -f %{oreon_filedir}/main.list
%files -n libart_lgpl-devel -f %{oreon_filedir}/libart_lgpl-devel.list

%changelog

%autochangelog
