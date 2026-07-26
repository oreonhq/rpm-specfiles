%global source0_hash fdc11e74c10fc9ffe4188537e2b370c0abacca7d89021d4d303afdf7fd7476fa

Name: libart_lgpl
Version: 2.3.21
Release: 37%{?dist}
Summary: Library of graphics routines used by libgnomecanvas
URL: http://www.gnome.org/
Source0: http://download.gnome.org/sources/libart_lgpl/2.3/%{name}-%{version}.tar.bz2
#Fedora specific patch
Patch0: libart-multilib.patch
# Automatically converted from old format: LGPLv2+ - review is highly recommended.
License: LicenseRef-Callaway-LGPLv2+
BuildRequires: automake autoconf
BuildRequires: pkgconfig
BuildRequires: libtool
BuildRequires: make

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

# fix multilib issues
mv $RPM_BUILD_ROOT%{_includedir}/libart-2.0/libart_lgpl/art_config.h \
   $RPM_BUILD_ROOT%{_includedir}/libart-2.0/libart_lgpl/art_config-%{__isa_bits}.h

cat >$RPM_BUILD_ROOT%{_includedir}/libart-2.0/libart_lgpl/art_config.h <<EOF
#ifndef LIBART_MULTILIB
#define LIBART_MULTILIB

#include <bits/wordsize.h>

#if __WORDSIZE == 32
# include "art_config-32.h"
#elif __WORDSIZE == 64
# include "art_config-64.h"
#else
# error "unexpected value for __WORDSIZE macro"
#endif

#endif 
EOF

%ldconfig_scriptlets

%files
%doc AUTHORS NEWS README
%license COPYING
%{_libdir}/lib*.so.*

%files devel
%{_libdir}/lib*.so
%{_libdir}/pkgconfig/*
%{_bindir}/libart2-config
%{_includedir}/*

%changelog
%autochangelog
