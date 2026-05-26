# oreon source sha256 begin
# URL sources: global sourceN_sha256 = 64-char hex from sha256sum. Omit a sourceN_sha256 line to skip verify for that source.
%global source0_sha256 f698d94f3103da8ca7438d84e0344e453fe0ba3b7486e04c5bf7a9a3fabe9b69
%global oreon_verify_sources \
%{?source0_sha256:%(test -z "%{source0_sha256}" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_sha256}" || { echo "oreon: Source0 sha256 mismatch" >&2; exit 1; }; })}
%(true)
# oreon source sha256 end

Summary:       Library of functions for manipulating TIFF format image files
Name:          libtiff
Version:       4.7.1
Release:       2%{?dist}
License:       libtiff
URL:           http://www.simplesystems.org/libtiff/

Source:        http://download.osgeo.org/libtiff/tiff-%{version}.tar.gz

BuildRequires: gcc, gcc-c++
BuildRequires: zlib-devel libjpeg-devel jbigkit-devel libzstd-devel libwebp-devel liblerc-devel
BuildRequires: libtool automake autoconf pkgconfig
%if 0%{?fedora} == 40
# Add old libtiff to work with packages not built with new libtiff.so.6
BuildRequires: libtiff
%endif
BuildRequires: make

%description
The libtiff package contains a library of functions for manipulating
TIFF (Tagged Image File Format) image format files.  TIFF is a widely
used file format for bitmapped images.  TIFF files usually end in the
.tif extension and they are often quite large.

The libtiff package should be installed if you need to manipulate TIFF
format image files.

%package devel
Summary:       Development tools for programs which will use the libtiff library
Requires:      %{name}%{?_isa} = %{version}-%{release}
Requires:      pkgconfig

%description devel
This package contains the header files and documentation necessary for
developing programs which will manipulate TIFF format image files
using the libtiff library.

If you need to develop programs which will manipulate TIFF format
image files, you should install this package.  You'll also need to
install the libtiff package.

%package static
Summary:     Static TIFF image format file library
Requires:    %{name}-devel%{?_isa} = %{version}-%{release}

%description static
The libtiff-static package contains the statically linkable version of libtiff.
Linking to static libraries is discouraged for most applications, but it is
necessary for some boot packages.

%package tools
Summary:    Command-line utility programs for manipulating TIFF files
Requires:   %{name}%{?_isa} = %{version}-%{release}

%description tools
This package contains command-line programs for manipulating TIFF format
image files using the libtiff library.

%prep
%oreon_verify_sources
%autosetup -n tiff-%{version} -N

# Use build system's libtool.m4, not the one in the package.
rm -f libtool.m4

libtoolize --force  --copy
aclocal -I . -I m4
automake --add-missing --copy
autoconf
autoheader

%build
export CFLAGS="%{optflags} -fno-strict-aliasing"
%configure --enable-ld-version-script --enable-tools-unsupported
%make_build

%install
%make_install

# remove what we didn't want installed
rm $RPM_BUILD_ROOT%{_libdir}/*.la
rm -rf $RPM_BUILD_ROOT%{_datadir}/doc/

# no libGL dependency, please
rm -f $RPM_BUILD_ROOT%{_bindir}/tiffgt

# no sgi2tiff or tiffsv, either
rm -f $RPM_BUILD_ROOT%{_bindir}/sgi2tiff
rm -f $RPM_BUILD_ROOT%{_bindir}/tiffsv

rm -f $RPM_BUILD_ROOT%{_mandir}/man1/tiffgt.1
rm -f $RPM_BUILD_ROOT%{_mandir}/man1/sgi2tiff.1
rm -f $RPM_BUILD_ROOT%{_mandir}/man1/tiffsv.1

# multilib header hack
# we only apply this to known Red Hat multilib arches, per bug #233091
case `uname -m` in
  i?86 | ppc | s390 | sparc )
    wordsize="32"
    ;;
  x86_64 | ppc64 | s390x | sparc64 )
    wordsize="64"
    ;;
  *)
    wordsize=""
    ;;
esac

if test -n "$wordsize"
then
  mv $RPM_BUILD_ROOT%{_includedir}/tiffconf.h \
     $RPM_BUILD_ROOT%{_includedir}/tiffconf-$wordsize.h

  cat >$RPM_BUILD_ROOT%{_includedir}/tiffconf.h <<EOF
#ifndef TIFFCONF_H_MULTILIB
#define TIFFCONF_H_MULTILIB

#include <bits/wordsize.h>

#if __WORDSIZE == 32
# include "tiffconf-32.h"
#elif __WORDSIZE == 64
# include "tiffconf-64.h"
#else
# error "unexpected value for __WORDSIZE macro"
#endif

#endif
EOF

fi

%if 0%{?fedora} == 40
# Copy old soname %{_libdir}/libtiff.so.5
# Copy old soname %{_libdir}/libtiffxx.so.5
cp %{_libdir}/libtiff.so.5* $RPM_BUILD_ROOT%{_libdir}
cp %{_libdir}/libtiffxx.so.5* $RPM_BUILD_ROOT%{_libdir}
%endif

%ldconfig_scriptlets

%check
export LD_LIBRARY_PATH=$PWD:$LD_LIBRARY_PATH
if ! make check
then
  cat test/test-suite.log
  false
fi

%files
%license LICENSE.md
%doc README.md RELEASE-DATE VERSION
%{_libdir}/libtiff.so.*
%{_libdir}/libtiffxx.so.*

%files devel
%doc TODO ChangeLog
%{_includedir}/*
%{_libdir}/libtiff.so
%{_libdir}/libtiffxx.so
%{_libdir}/pkgconfig/libtiff*.pc
%{_mandir}/man3/*

%files static
%{_libdir}/*.a

%files tools
%{_bindir}/*
%{_mandir}/man1/*

%changelog
* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 4.7.1-2
- Prepare for Oreon 11 (RP1)
