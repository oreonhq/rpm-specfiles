%global source0_hash b0fcdd7fc0cdea6e80dcf1dd85ba794af0d5b4a57e26397eee3bc193272d9132

%global oreon_bootstrap %{nil}
%bcond bootstrap 0
%oreon_bootstrap
%bcond_without devel

# Recent so-version, so we do not bump accidentally.
%global nettle_so_ver 8
%global hogweed_so_ver 6

#   and HMAC is calculated there with its own tool.
%bcond_without fipshmac
%bcond_with bundle_gmp

Name:           nettle3.10
Version:        3.10.1
Release:        1%{?dist}
Summary:        Compatibility version of the Nettle library

License:        (LGPL-3.0-or-later OR GPL-2.0-or-later) AND MIT
URL:            http://www.lysator.liu.se/~nisse/nettle/
Source0:	http://www.lysator.liu.se/~nisse/archive/nettle-%{version}.tar.gz
Source1:        nettle-3.10.1.tar.gz.sig
Source2:	nettle-release-keyring.gpg
Patch:        nettle-3.10-hobble-to-configure.patch
Patch:        nettle-3.10-hobble-to-configure.patch


BuildRequires: make
BuildRequires:  gcc
BuildRequires:  gmp-devel
BuildRequires:  m4
BuildRequires:	libtool, automake, autoconf, gettext-devel
BuildRequires:  fipscheck
BuildRequires:  gnupg2
BuildRequires:  oreon-rpm-macros
Conflicts:      nettle < 4.0
Provides:       deprecated()

%package devel
Summary:        Development headers for a low-level cryptographic library
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       gmp-devel%{?_isa}
Conflicts:      nettle-devel
Provides:       deprecated()

%description
Nettle is a cryptographic library that is designed to fit easily in more
or less any context: In crypto toolkits for object-oriented languages
(C++, Python, Pike, ...), in applications like LSH or GNUPG, or even in
kernel space. This version of Nettle package contains only the libraries
from the 3.10 version and is provided for compatibility with previous
releases.

%description devel
Nettle is a cryptographic library that is designed to fit easily in more
or less any context: In crypto toolkits for object-oriented languages
(C++, Python, Pike, ...), in applications like LSH or GNUPG, or even in
kernel space.  This package contains the files needed for developing 
applications with nettle.


%prep
%oreon_sha256

%{gpgverify} --keyring='%{SOURCE2}' --signature='%{SOURCE1}' --data='%{SOURCE0}'

%autosetup -n nettle-%{version} -Tb 0 -p1


# Disable -ggdb3 which makes debugedit unhappy
sed s/ggdb3/g/ -i configure

%build

autoreconf -ifv
# For annocheck
export ASM_FLAGS="-Wa,--generate-missing-build-notes=yes"
%configure --disable-documentation --enable-shared --enable-fat \
--disable-sm3 --disable-sm4 --disable-ecc-secp192r1 --disable-ecc-secp224r1 \
%{nil}
%make_build

%define fipshmac() \
	fipshmac -d $RPM_BUILD_ROOT%{_libdir} $RPM_BUILD_ROOT%{_libdir}/%1.* \
	file=`basename $RPM_BUILD_ROOT%{_libdir}/%1.*.hmac` && \
	mv $RPM_BUILD_ROOT%{_libdir}/$file $RPM_BUILD_ROOT%{_libdir}/.$file && \
	ln -s .$file $RPM_BUILD_ROOT%{_libdir}/.%1.hmac

%define __spec_install_post \
	%{?__debug_package:%{__debug_install_post}} \
	%{__arch_install_post} \
	%{__os_install_post} \
	%fipshmac libnettle.so.%{nettle_so_ver} \
	%fipshmac libhogweed.so.%{hogweed_so_ver} \
%{nil}


%install
%make_install
make install-shared DESTDIR=$RPM_BUILD_ROOT INSTALL="install -p"
mkdir -p $RPM_BUILD_ROOT%{_infodir}
rm -f $RPM_BUILD_ROOT%{_libdir}/*.a
rm -f $RPM_BUILD_ROOT%{_infodir}/dir
rm -f $RPM_BUILD_ROOT%{_bindir}/nettle-lfib-stream
rm -f $RPM_BUILD_ROOT%{_bindir}/pkcs1-conv
rm -f $RPM_BUILD_ROOT%{_bindir}/sexp-conv
rm -f $RPM_BUILD_ROOT%{_bindir}/nettle-hash
rm -f $RPM_BUILD_ROOT%{_bindir}/nettle-pbkdf2

chmod 0755 $RPM_BUILD_ROOT%{_libdir}/libnettle.so.%{nettle_so_ver}.*
chmod 0755 $RPM_BUILD_ROOT%{_libdir}/libhogweed.so.%{hogweed_so_ver}.*


%check
make check

%files
%doc AUTHORS NEWS README
%license COPYINGv2 COPYING.LESSERv3
%{_libdir}/libnettle.so.%{nettle_so_ver}
%{_libdir}/libnettle.so.%{nettle_so_ver}.*
%{_libdir}/libhogweed.so.%{hogweed_so_ver}
%{_libdir}/libhogweed.so.%{hogweed_so_ver}.*
%{_libdir}/.libhogweed.so.*.hmac
%{_libdir}/.libnettle.so.*.hmac

%files devel
%doc descore.README
%{_includedir}/nettle
%{_libdir}/libnettle.so
%{_libdir}/libhogweed.so
%{_libdir}/pkgconfig/hogweed.pc
%{_libdir}/pkgconfig/nettle.pc

%ldconfig_scriptlets


