# Copyright (C) 2026 Oreon HQ
# SPDX-License-Identifier: GPL-2.0-or-later

%global source0_hash 7ce33c2492221a0436f96a8500215e9f3e3dcb5fd26a757cd415e7a843babd5e

%{!?oreon_bootstrap:%global oreon_bootstrap %{nil}}
%bcond bootstrap 0
%oreon_bootstrap
Name: libgcrypt
Version:        1.12.2
Release:        1%{?dist}
URL: https://www.gnupg.org/
Source0:        https://www.gnupg.org/ftp/gcrypt/libgcrypt/libgcrypt-%{version}.tar.bz2
Source1:        libgcrypt-1.12.2.tar.bz2.sig
Source2:        signature_key.asc
# Pass the annobin flags to the libgcrypt.so (#2016349)
Patch1:        libgcrypt-1.10.1-annobin.patch
# https://gitlab.com/redhat-crypto/libgcrypt/libgcrypt-mirror/-/merge_requests/19/
Patch5:        libgcrypt-1.11.0-marvin.patch

%global gcrylibdir %{_libdir}
%global gcrysoname libgcrypt.so.20

License: BSD-3-Clause AND (BSD-3-Clause OR GPL-2.0-only) AND GPL-2.0-or-later AND LGPL-2.1-or-later AND LGPL-2.0-or-later AND MIT-Modern-Variant
Summary: A general-purpose cryptography library
BuildRequires: gcc
BuildRequires: gawk, libgpg-error-devel >= 1.56, pkgconfig
# This is needed only when patching the .texi doc.
BuildRequires: texinfo
BuildRequires: autoconf, automake, libtool
BuildRequires: make
BuildRequires: gnupg2
BuildRequires: annobin-annocheck binutils
BuildRequires: gdb
BuildRequires:  oreon-rpm-macros

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
%oreon_sha256

%oreon_gpgverify --key %{SOURCE2} --sig %{SOURCE1} --data %{SOURCE0}
%setup -q
%patch 1 -p1
%patch 5 -p1

%build
specdir=$PWD/oreon-specs
wrapdir=$PWD/oreon-cc
mkdir -p "$specdir" "$wrapdir"
plugindir=$(/usr/bin/gcc -print-file-name=plugin)
plugin=
for cand in "$plugindir/gcc-annobin.so" "$plugindir/annobin.so"; do
  if [ -e "$cand" ]; then
    plugin=$cand
    break
  fi
done
if [ -n "$plugin" ]; then
  printf '%s\n' '*cc1_options:' "+ -fplugin=$plugin" > "$specdir/annobin-cc1"
else
  cp -L %{_rpmconfigdir}/oreon/oreon-annobin-cc1 "$specdir/annobin-cc1"
fi
cp -L %{_rpmconfigdir}/oreon/oreon-hardened-cc1 "$specdir/hardened-cc1"
cp -L %{_rpmconfigdir}/oreon/oreon-hardened-ld "$specdir/hardened-ld"
cp -L %{_rpmconfigdir}/oreon/oreon-hardened-ld-errors "$specdir/hardened-ld-errors"
cat > "$wrapdir/ccwrap.py" << 'PY'
import os, sys
specdir = os.environ["OREON_SPECDIR"]
rpm = os.environ["OREON_RPMCONFIG"]
repl = {
    rpm + "/redhat/redhat-hardened-cc1": specdir + "/hardened-cc1",
    rpm + "/oreon/oreon-annobin-cc1": specdir + "/annobin-cc1",
    rpm + "/redhat/redhat-hardened-ld": specdir + "/hardened-ld",
    rpm + "/redhat/redhat-hardened-ld-errors": specdir + "/hardened-ld-errors",
}
args = []
for a in sys.argv[1:]:
    if a.startswith("-specs="):
        path = a[len("-specs="):]
        if "annobin-cc1" in path:
            path = specdir + "/annobin-cc1"
        else:
            path = repl.get(path, path)
        if "/redhat/" in path and not os.path.exists(path):
            continue
        a = "-specs=" + path
    elif a == "-fplugin=annobin" or a.startswith("-fplugin=annobin"):
        plug = os.environ.get("OREON_ANNOBIN")
        if plug:
            a = "-fplugin=" + plug
    args.append(a)
os.execv(os.environ["OREON_REAL_CC"], [os.environ["OREON_REAL_CC"], *args])
PY
for pair in "gcc:/usr/bin/gcc" "cc:/usr/bin/gcc" "g++:/usr/bin/g++" "c++:/usr/bin/c++"; do
  name=${pair%%:*}
  real=${pair#*:}
  cat > "$wrapdir/$name" << EOF
#!/bin/sh
export OREON_SPECDIR="$specdir"
export OREON_RPMCONFIG="%{_rpmconfigdir}"
export OREON_ANNOBIN="$plugin"
export OREON_REAL_CC=$real
exec /usr/bin/python3 "$wrapdir/ccwrap.py" "\$@"
EOF
  chmod +x "$wrapdir/$name"
done
export PATH="$wrapdir:$PATH"
export CC="$wrapdir/gcc"
export CXX="$wrapdir/g++"
# should be all algorithms except SM3 and SM4, aria
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

# Disabled now due to failing in F44
# https://github.com/rpminspect/rpminspect/issues/1546
# export PROFILE=%{?dist}
# annocheck --ignore-unknown --verbose --profile=${PROFILE:1} %{libpath}

%install
%make_install

# Change /usr/lib64 back to /usr/lib.  This saves us from having to patch the
# script to "know" that -L/usr/lib64 should be suppressed, and also removes
# a file conflict between 32- and 64-bit versions of this package.
# Also replace my_host with none.
sed -i -e 's,^libdir="/usr/lib.*"$,libdir="/usr/lib",g' $RPM_BUILD_ROOT/%{_bindir}/libgcrypt-config
sed -i -e 's,^my_host=".*"$,my_host="none",g' $RPM_BUILD_ROOT/%{_bindir}/libgcrypt-config

rm -f ${RPM_BUILD_ROOT}/%{_infodir}/dir ${RPM_BUILD_ROOT}/%{_libdir}/*.la
/sbin/ldconfig -n $RPM_BUILD_ROOT/%{_libdir}

%if "%{gcrylibdir}" != "%{_libdir}"
# Relocate the shared libraries to %{gcrylibdir}.
mkdir -p $RPM_BUILD_ROOT%{gcrylibdir}
for shlib in $RPM_BUILD_ROOT%{_libdir}/*.so* ; do
	if test -L "$shlib" ; then
		rm "$shlib"
	else
		mv "$shlib" $RPM_BUILD_ROOT%{gcrylibdir}/
	fi
done

# Add soname symlink.
/sbin/ldconfig -n $RPM_BUILD_ROOT/%{_lib}/
%endif

# Overwrite development symlinks.
pushd $RPM_BUILD_ROOT/%{gcrylibdir}
for shlib in lib*.so.?? ; do
	target=$RPM_BUILD_ROOT/%{_libdir}/`echo "$shlib" | sed -e 's,\.so.*,,g'`.so
%if "%{gcrylibdir}" != "%{_libdir}"
	shlib=%{gcrylibdir}/$shlib
%endif
	ln -sf $shlib $target
done
popd

# Create /etc/gcrypt (hardwired, not dependent on the configure invocation) so
# that _someone_ owns it.
mkdir -p -m 755 $RPM_BUILD_ROOT/etc/gcrypt

%ldconfig_scriptlets

%files
%dir /etc/gcrypt
%{gcrylibdir}/libgcrypt.so.*.*
%{gcrylibdir}/%{gcrysoname}
%license COPYING.LIB
%doc AUTHORS NEWS THANKS

%files devel
%{_bindir}/%{name}-config
%{_bindir}/dumpsexp
%{_bindir}/hmac256
%{_bindir}/mpicalc
%{_includedir}/*
%{_libdir}/*.so
%{_libdir}/pkgconfig/libgcrypt.pc
%{_datadir}/aclocal/*
%{_mandir}/man1/*

%{_infodir}/gcrypt.info*
%license COPYING

