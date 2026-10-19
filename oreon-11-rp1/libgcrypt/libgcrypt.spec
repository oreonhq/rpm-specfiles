%global source2_hash 6f57d0e17fefd2238bd037aebf03efa960641629dd61dd9d47f122a829f6e375
%global source1_hash 8be53f19f43ffa0297aceb520be717de539d1bdad45b5538a57fd95610b1e2db
%global source0_hash d77f68f48879510e79a2f65977ccc68981781ea0923e5bdffac2a193ea3d660e
Name: libgcrypt
Version: 1.12.4
Release:        1%{?dist}
URL: https://www.gnupg.org/
Source0:        https://www.gnupg.org/ftp/gcrypt/libgcrypt/libgcrypt-%{version}.tar.bz2
Source1:        https://www.gnupg.org/ftp/gcrypt/libgcrypt/libgcrypt-%{version}.tar.bz2.sig
Source2: https://gnupg.org/signature_key.asc
Patch1: libgcrypt-1.10.1-annobin.patch
Patch5: libgcrypt-1.11.0-marvin.patch
%global gcrylibdir %{_libdir}
%global gcrysoname libgcrypt.so.20
License: BSD-3-Clause AND (BSD-3-Clause OR GPL-2.0-only) AND GPL-2.0-or-later AND LGPL-2.1-or-later AND LGPL-2.0-or-later AND MIT-Modern-Variant
Summary:        A general-purpose cryptography library
# oreon:deps
BuildRequires:  annobin-annocheck
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  binutils
BuildRequires:  gawk
BuildRequires:  gcc
BuildRequires:  gnupg2
BuildRequires:  libgpg-error-devel
BuildRequires:  libtool
BuildRequires:  make
BuildRequires:  pkgconfig
BuildRequires:  texinfo
# /oreon:deps
%package devel
Summary: Development files for the %{name} package
Requires: libgpg-error-devel
Requires: %{name}%{?_isa} = %{version}-%{release}
Requires: pkgconfig
%description
Libgcrypt is a general purpose crypto library based on the code used
in GNU Privacy Guard.  This is a development version.

%description devel
Libgcrypt is a general purpose crypto library based on the code used
in GNU Privacy Guard.  This package contains files needed to develop
applications using libgcrypt.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%{gpgverify} --keyring='%{SOURCE2}' --signature='%{SOURCE1}' --data='%{SOURCE0}'
%setup -q
%patch 1 -p1
%patch 5 -p1

%build

export DIGESTS='crc gostr3411-94 md4 md5 rmd160 sha1 sha256 sha512 sha3 tiger whirlpool stribog blake2'
export CIPHERS='arcfour blowfish cast5 des aes twofish serpent rfc2268 seed camellia idea salsa20 gost28147 chacha20'
autoreconf -f
%configure --disable-static \
%ifarch sparc64
     --disable-asm \
%endif
     --enable-noexecstack \
     --disable-jent-support \
     --disable-O-flag-munging \
     --enable-digests="$DIGESTS" \
     --enable-ciphers="$CIPHERS" \
     --enable-marvin-workaround
sed -i -e '/^sys_lib_dlsearch_path_spec/s,/lib /usr/lib,/usr/lib /lib64 /usr/lib64 /lib,g' libtool
%make_build
%check

make check
%define libpath $RPM_BUILD_ROOT%{gcrylibdir}/%{gcrysoname}.?.?
%install
%make_install
sed -i -e 's,^libdir="/usr/lib.*"$,libdir="/usr/lib",g' $RPM_BUILD_ROOT/%{_bindir}/libgcrypt-config
sed -i -e 's,^my_host=".*"$,my_host="none",g' $RPM_BUILD_ROOT/%{_bindir}/libgcrypt-config
rm -f ${RPM_BUILD_ROOT}/%{_infodir}/dir ${RPM_BUILD_ROOT}/%{_libdir}/*.la
/sbin/ldconfig -n $RPM_BUILD_ROOT/%{_libdir}
%if "%{gcrylibdir}" != "%{_libdir}"
mkdir -p $RPM_BUILD_ROOT%{gcrylibdir}
for shlib in $RPM_BUILD_ROOT%{_libdir}/*.so* ; do
	if test -L "$shlib" ; then
		rm "$shlib"
	else
		mv "$shlib" $RPM_BUILD_ROOT%{gcrylibdir}/
	fi
done
/sbin/ldconfig -n $RPM_BUILD_ROOT/%{_lib}/
%endif
pushd $RPM_BUILD_ROOT/%{gcrylibdir}
for shlib in lib*.so.?? ; do
	target=$RPM_BUILD_ROOT/%{_libdir}/`echo "$shlib" | sed -e 's,\.so.*,,g'`.so
%if "%{gcrylibdir}" != "%{_libdir}"
	shlib=%{gcrylibdir}/$shlib
%endif
	ln -sf $shlib $target
done
popd
mkdir -p -m 755 $RPM_BUILD_ROOT/etc/gcrypt
%ldconfig_scriptlets
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*

%files -f %{oreon_filedir}/main.list
%files -n libgcrypt-devel -f %{oreon_filedir}/libgcrypt-devel.list

%changelog

%autochangelog
