%global source0_hash 8403f5fbf83aa9ac0c6ce15d97fd85607488152aa84e007b7d0621b8ebc07633

Name: libwvstreams
Version: 4.6.1
Release: 49%{?dist}
Summary: WvStreams is a network programming library written in C++
Source: http://wvstreams.googlecode.com/files/wvstreams-%{version}.tar.gz
#fixed multilib issue (bug #192717)
Patch1: wvstreams-4.6.1-multilib.patch
#install-xplc target was missing
Patch2: wvstreams-4.5-noxplctarget.patch
#Fix parallel build (#226061)
Patch3: wvstreams-4.6.1-make.patch
#sys/stat.h is missing some files in rawhide build
Patch4: wvstreams-4.6.1-statinclude.patch
#const X509V3_EXT_METHOD * -> X509V3_EXT_METHOD * conversion not allowed
#by rawhide gcc
Patch5: wvstreams-4.6.1-gcc.patch
# fix missing unistd.h header for gcc 4.7
Patch6: wvstreams-4.6.1-gcc47.patch
Patch7: wvstreams-4.6.1-magic.patch
Patch8: 0001-Use-explicit-cast-and-prevent-compiler-error.patch
Patch9: wvstreams-4.6.1-fix-stack-size.patch
Patch10: wvstreams-4.6.1-gcc10.patch
# patch was taken from debian
Patch11: wvstreams-4.6.1-openssl11.patch
URL: https://code.google.com/p/wvstreams/
BuildRequires: gcc-c++
BuildRequires: openssl-devel, pkgconfig, zlib-devel, readline-devel, dbus-devel
BuildRequires: make
BuildRequires: libxcrypt-devel
# Automatically converted from old format: LGPLv2+ - review is highly recommended.
License: LicenseRef-Callaway-LGPLv2+

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

#  --without-PACKAGE       do not use PACKAGE (same as --with-PACKAGE=no)
#  --with-dbus             DBUS
#  --with-openssl          OpenSSL >= 0.9.7 (required)
#  --with-pam              PAM
#  --with-tcl              Tcl
#  --with-qt               Qt
#  --with-zlib             zlib (required)
touch configure
%configure --with-dbus=yes \
           --with-pam \
           --with-openssl \
           --without-tcl \
           --with-qt=no \
           --disable-optimization # -O2 will be turned on because of RPM_OPT_FLAFS,
                                  # but it won't be appended at the end of CFLAGS

#upstream is working with .a lib, so hardcoding path to libdbus-1.so to prevent build failures
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

%files
%doc LICENSE README
%{_libdir}/*.so.*

%files devel
%{_includedir}/wvstreams
%{_libdir}/*.so
%{_libdir}/valgrind/*.supp
%{_libdir}/pkgconfig/*.pc

%files static
%{_libdir}/*.a

%ldconfig_scriptlets

%changelog
%autochangelog
