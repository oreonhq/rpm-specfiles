%global source0_hash 672bd7d10aee4606171afb864f3570b83340f6a33e2c186dc0512f7145ffdf6a
Summary:        Library of functions for manipulating TIFF format image files
Name:          libtiff
Version:       4.7.2
Release:        1%{?dist}
License:       libtiff
URL:           http://www.simplesystems.org/libtiff/
Source0:        http://download.osgeo.org/libtiff/tiff-%{version}.tar.gz
# oreon:deps
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  gcc
BuildRequires:  gcc-c++
BuildRequires:  jbigkit-devel
BuildRequires:  libjpeg-devel
BuildRequires:  liblerc-devel
BuildRequires:  libtool
BuildRequires:  libwebp-devel
BuildRequires:  libzstd-devel
BuildRequires:  make
BuildRequires:  pkgconfig
BuildRequires:  zlib-devel
# /oreon:deps
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

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
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
rm $RPM_BUILD_ROOT%{_libdir}/*.la
rm -rf $RPM_BUILD_ROOT%{_datadir}/doc/
rm -f $RPM_BUILD_ROOT%{_bindir}/tiffgt
rm -f $RPM_BUILD_ROOT%{_bindir}/sgi2tiff
rm -f $RPM_BUILD_ROOT%{_bindir}/tiffsv
rm -f $RPM_BUILD_ROOT%{_mandir}/man1/tiffgt.1
rm -f $RPM_BUILD_ROOT%{_mandir}/man1/sgi2tiff.1
rm -f $RPM_BUILD_ROOT%{_mandir}/man1/tiffsv.1
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
EOF
fi
%ldconfig_scriptlets
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/* usr/*/lib*.so.* usr/*/lib*.so.*

%check

export LD_LIBRARY_PATH=$PWD:$LD_LIBRARY_PATH
if ! make check
then
  cat test/test-suite.log
  false
fi
%files -f %{oreon_filedir}/main.list
%files -n libtiff-devel -f %{oreon_filedir}/libtiff-devel.list
%files -n libtiff-static -f %{oreon_filedir}/libtiff-static.list
%files -n libtiff-tools -f %{oreon_filedir}/libtiff-tools.list

%changelog

%autochangelog
