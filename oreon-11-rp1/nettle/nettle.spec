%global source200_hash fd4829912cddd12f84181c3451cc752be224643e87fac497b69edddadc49b4f2
%global source2_hash 50561c50f40cd9746af214c995fb219bbe7f3b9c5f038b918f5df543bb3f846f
%global source1_hash b617851da180b7a7ee8cdb34e4a9269eaa9ba3c3cfc69a64d0cbcfd0ae42a4d5
%global source0_hash 3addbc00da01846b232fb3bc453538ea5468da43033f21bb345cb1e9073f5094
%global source2_key_fpr 343C2FF0FBEE5EC2EDBEF399F3599FF828C67298
%global nettle_so_ver 9
%global hogweed_so_ver 7
%global bootstrap 0
%if 0%{?bootstrap}
%global version_old 3.5.1
%global nettle_so_ver_old 7
%global hogweed_so_ver_old 5
%endif
%bcond_without fipshmac
%bcond_with bundle_gmp
Name:           nettle
Version:        4.0
Release:        1%{?dist}
Summary:        A low-level cryptographic library
License:        LGPL-3.0-or-later OR GPL-2.0-or-later
URL:            http://www.lysator.liu.se/~nisse/nettle/
Source0:        https://www.lysator.liu.se/~nisse/archive/%{name}-%{version}.tar.gz
Source1:        https://www.lysator.liu.se/~nisse/archive/%{name}-%{version}.tar.gz.sig
Source2:        https://keyserver.ubuntu.com/pks/lookup?op=get&search=0x343C2FF0FBEE5EC2EDBEF399F3599FF828C67298#/nettle-release-keyring.gpg
%if 0%{?bootstrap}
Source100:	%{name}-%{version_old}-hobbled.tar.xz
Source101:	nettle-3.5-remove-ecc-testsuite.patch
%endif
Patch:        nettle-3.8-zeroize-stack.patch
Patch:        nettle-3.10-hobble-to-configure.patch
%if %{with bundle_gmp}
Source200:	https://gmplib.org/download/gmp/gmp-6.2.1.tar.xz
Source201:	gmp-6.2.1-intel-cet.patch
Source202:	gmp-6.2.1-zeroize-allocator.patch
Source203:	gmp-6.2.1-c23.patch
%endif
%if !%{with bundle_gmp}
%endif
%if %{with fipshmac}
%endif
# oreon:deps
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  fipscheck
BuildRequires:  gcc
BuildRequires:  gettext-devel
BuildRequires:  gmp-devel
BuildRequires:  gnupg2
BuildRequires:  libtool
BuildRequires:  m4
BuildRequires:  make
# /oreon:deps
%package devel
Summary:        Development headers for a low-level cryptographic library
Requires:       %{name} = %{version}-%{release}
Requires:       gmp-devel%{?_isa}
%description
Nettle is a cryptographic library that is designed to fit easily in more
or less any context: In crypto toolkits for object-oriented languages
(C++, Python, Pike, ...), in applications like LSH or GNUPG, or even in
kernel space.

%description devel
Nettle is a cryptographic library that is designed to fit easily in more
or less any context: In crypto toolkits for object-oriented languages
(C++, Python, Pike, ...), in applications like LSH or GNUPG, or even in
kernel space.  This package contains the files needed for developing 
applications with nettle.

%prep

%(test -z "%{source2_key_fpr}" || { f="%{SOURCE2}"; test -f "$f" || { echo "oreon: missing Source2 key $f" >&2; exit 1; }; fpr=$(GNUPGHOME=$(mktemp -d); export GNUPGHOME; trap 'rm -rf "$GNUPGHOME"' EXIT; gpg --batch --with-colons --import-options show-only --import "$f" | awk -F: '/^fpr:/ {print toupper($10); exit}'); test "$fpr" = "%{source2_key_fpr}" || { echo "oreon: Source2 key fingerprint mismatch" >&2; exit 1; }; })
%autosetup -Tb 0 -p1

%{gpgverify} --keyring='%{SOURCE2}' --signature='%{SOURCE1}' --data='%{SOURCE0}'

%if %{with bundle_gmp}
mkdir -p bundled_gmp
pushd bundled_gmp
tar --strip-components=1 -xf %{SOURCE200}
patch -p1 < %{SOURCE201}
patch -p1 < %{SOURCE202}
patch -p1 < %{SOURCE203}
popd

# Prevent -lgmp appearing in the compiler command line in dependent components
sed -i '/^Libs.private:/d' hogweed.pc.in
%endif

%if 0%{?bootstrap}
mkdir -p bootstrap_ver
pushd bootstrap_ver
tar --strip-components=1 -xf %{SOURCE100}
patch -p1 < %{SOURCE101}

# Disable -ggdb3 which makes debugedit unhappy
sed s/ggdb3/g/ -i configure
sed 's/ecc-192.c//g' -i Makefile.in
sed 's/ecc-224.c//g' -i Makefile.in
popd
%endif

# Disable -ggdb3 which makes debugedit unhappy
sed s/ggdb3/g/ -i configure

%build

%if %{with bundle_gmp}
pushd bundled_gmp
autoreconf -ifv
%configure --disable-cxx --disable-shared --enable-fat --with-pic
%make_build
popd
%endif
autoreconf -ifv
export ASM_FLAGS="-Wa,--generate-missing-build-notes=yes"
%configure --enable-shared --enable-fat \
--disable-sm3 --disable-sm4 --disable-ecc-secp192r1 --disable-ecc-secp224r1 \
%if %{with bundle_gmp}
--with-include-path=$PWD/bundled_gmp --with-lib-path=$PWD/bundled_gmp/.libs \
%endif
%{nil}
%make_build
%if 0%{?bootstrap}
pushd bootstrap_ver
autoconf
%configure --with-tests
%make_build
popd
%endif
%if %{with fipshmac}
%define fipshmac() \
	fipshmac -d $RPM_BUILD_ROOT%{_libdir} $RPM_BUILD_ROOT%{_libdir}/%1.* \
	file=`basename $RPM_BUILD_ROOT%{_libdir}/%1.*.hmac` && \
	mv $RPM_BUILD_ROOT%{_libdir}/$file $RPM_BUILD_ROOT%{_libdir}/.$file && \
	ln -s .$file $RPM_BUILD_ROOT%{_libdir}/.%1.hmac
%if 0%{?bootstrap}
%define bootstrap_fips 1
%endif
%define __spec_install_post \
	%{?__debug_package:%{__debug_install_post}} \
	%{__arch_install_post} \
	%{__os_install_post} \
	%fipshmac libnettle.so.%{nettle_so_ver} \
	%fipshmac libhogweed.so.%{hogweed_so_ver} \
	%{?bootstrap_fips:%fipshmac libnettle.so.%{nettle_so_ver_old}} \
	%{?bootstrap_fips:%fipshmac libhogweed.so.%{hogweed_so_ver_old}} \
%{nil}
%endif
%install
%if 0%{?bootstrap}
make -C bootstrap_ver install-shared-nettle DESTDIR=$RPM_BUILD_ROOT INSTALL="install -p"
make -C bootstrap_ver install-shared-hogweed DESTDIR=$RPM_BUILD_ROOT INSTALL="install -p"
chmod 0755 $RPM_BUILD_ROOT%{_libdir}/libnettle.so.%{nettle_so_ver_old}.*
chmod 0755 $RPM_BUILD_ROOT%{_libdir}/libhogweed.so.%{hogweed_so_ver_old}.*
%endif
%make_install
make install-shared DESTDIR=$RPM_BUILD_ROOT INSTALL="install -p"
mkdir -p $RPM_BUILD_ROOT%{_infodir}
install -p -m 644 nettle.info $RPM_BUILD_ROOT%{_infodir}/
rm -f $RPM_BUILD_ROOT%{_libdir}/*.a
rm -f $RPM_BUILD_ROOT%{_infodir}/dir
rm -f $RPM_BUILD_ROOT%{_bindir}/nettle-lfib-stream
rm -f $RPM_BUILD_ROOT%{_bindir}/pkcs1-conv
rm -f $RPM_BUILD_ROOT%{_bindir}/sexp-conv
rm -f $RPM_BUILD_ROOT%{_bindir}/nettle-hash
rm -f $RPM_BUILD_ROOT%{_bindir}/nettle-pbkdf2
chmod 0755 $RPM_BUILD_ROOT%{_libdir}/libnettle.so.%{nettle_so_ver}.*
chmod 0755 $RPM_BUILD_ROOT%{_libdir}/libhogweed.so.%{hogweed_so_ver}.*
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*

%check

make check
%files -f %{oreon_filedir}/main.list
%files -n nettle-devel -f %{oreon_filedir}/nettle-devel.list

%changelog

* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 3.10.1-1
- Prepare for Oreon 11 (RP1)
