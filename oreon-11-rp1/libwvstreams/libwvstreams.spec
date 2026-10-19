%global source0_hash 8403f5fbf83aa9ac0c6ce15d97fd85607488152aa84e007b7d0621b8ebc07633
Name: libwvstreams
Version: 4.6.1
Release:        49%{?dist}
Summary:        WvStreams is a network programming library written in C++
Source0:        http://wvstreams.googlecode.com/files/wvstreams-%{version}.tar.gz
Patch1: wvstreams-4.6.1-multilib.patch
Patch2: wvstreams-4.5-noxplctarget.patch
Patch3: wvstreams-4.6.1-make.patch
Patch4: wvstreams-4.6.1-statinclude.patch
Patch5: wvstreams-4.6.1-gcc.patch
Patch6: wvstreams-4.6.1-gcc47.patch
Patch7: wvstreams-4.6.1-magic.patch
Patch8: 0001-Use-explicit-cast-and-prevent-compiler-error.patch
Patch9: wvstreams-4.6.1-fix-stack-size.patch
Patch10: wvstreams-4.6.1-gcc10.patch
Patch11: wvstreams-4.6.1-openssl11.patch
URL: https://code.google.com/p/wvstreams/
License: LicenseRef-Callaway-LGPLv2+
# oreon:deps
BuildRequires:  dbus-devel
BuildRequires:  gcc-c++
BuildRequires:  libxcrypt-devel
BuildRequires:  make
BuildRequires:  openssl-devel
BuildRequires:  pkgconfig
BuildRequires:  readline-devel
BuildRequires:  zlib-devel
# /oreon:deps
%description
WvStreams aims to be an efficient, secure, and easy-to-use library for
doing network applications development.

%package devel
Summary: Development files for WvStreams
Requires: %{name} = %{version}-%{release}
%description devel
WvStreams aims to be an efficient, secure, and easy-to-use library for
doing network applications development.  This package contains the files
needed for developing applications which use WvStreams.

%package static
Summary: Static libraries files for WvStreams
%description static
WvStreams aims to be an efficient, secure, and easy-to-use library for
doing network applications development. This package contains static libraries.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n wvstreams-%{version}
%patch -P1 -p1 -b .multilib
%patch -P2 -p1 -b .xplctarget
%patch -P3 -p1 -b .make
%patch -P4 -p1 -b .statinclude
%patch -P5 -p1 -b .gcc
%patch -P6 -p1 -b .gcc47
%patch -P7 -p1 -b .magic
%patch -P8 -p1 -b .cast
%patch -P9 -p1 -b .fix-stack-size
%patch -P10 -p1 -b .gcc10
%patch -P11 -p1 -b .openssl11

%build

export CXXFLAGS="$RPM_OPT_FLAGS -fPIC -fpermissive -fno-strict-aliasing -fno-tree-dce -fno-optimize-sibling-calls"
export CFLAGS="$RPM_OPT_FLAGS -fPIC -fno-strict-aliasing"
touch configure
%configure --with-dbus=yes \
           --with-pam \
           --with-openssl \
           --without-tcl \
           --with-qt=no \
           --disable-optimization # -O2 will be turned on because of RPM_OPT_FLAFS,
make %{?_smp_mflags}
%install
make install DESTDIR=$RPM_BUILD_ROOT
chmod 755 $RPM_BUILD_ROOT%{_libdir}/*.so.*
rm -fr $RPM_BUILD_ROOT/usr/bin
pushd $RPM_BUILD_ROOT
rm -f \
   ./etc/uniconf.conf \
   .%{_bindir}/uni \
   .%{_libdir}/pkgconfig/libwvqt.pc \
   .%{_sbindir}/uniconfd \
   .%{_mandir}/man8/uni.8* \
   .%{_mandir}/man8/uniconfd.8* \
   .%{_var}/lib/uniconf/uniconfd.ini
popd
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/* usr/*/lib*.so.*

%files -f %{oreon_filedir}/main.list
%files -n libwvstreams-devel -f %{oreon_filedir}/libwvstreams-devel.list
%files -n libwvstreams-static -f %{oreon_filedir}/libwvstreams-static.list

%changelog

%autochangelog
