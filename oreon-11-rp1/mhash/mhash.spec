%global source0_hash 56521c52a9033779154432d0ae47ad7198914785265e1f570cee21ab248dfef0

# http://sourceforge.net/projects/mhash
# As of 2007-08-18 11:03, this project is no longer under active development.

Summary: Thread-safe hash algorithms library
Name: mhash
Version: 0.9.9.9
Release: 36%{?dist}
URL: http://mhash.sourceforge.net/
License: LGPL-2.1-or-later
Source: http://downloads.sourceforge.net/mhash/mhash-%{version}.tar.bz2
Patch2: mhash-0.9.9.9-align.patch
Patch3: mhash-0.9.9.9-force64bit-tiger.patch
# Taken from Gentoo: 
# http://mirror.its.uidaho.edu/pub/gentoo-portage/app-crypt/mhash/files/mhash-0.9.9-fix-snefru-segfault.patch
Patch4: mhash-0.9.9.9-fix-snefru-segfault.patch
# Taken from Gentoo:
# http://mirror.its.uidaho.edu/pub/gentoo-portage/app-crypt/mhash/files/mhash-0.9.9-fix-mem-leak.patch
Patch5: mhash-0.9.9.9-fix-mem-leak.patch
# Taken from Gentoo:
# http://mirror.its.uidaho.edu/pub/gentoo-portage/app-crypt/mhash/files/mhash-0.9.9-fix-whirlpool-segfault.patch
Patch6: mhash-0.9.9.9-fix-whirlpool-segfault.patch
# Taken from Gentoo:
# http://mirror.its.uidaho.edu/pub/gentoo-portage/app-crypt/mhash/files/mhash-0.9.9-autotools-namespace-stomping.patch
Patch7: mhash-0.9.9.9-autotools-namespace-stomping.patch
# Taken from openpkg:
# http://www.mail-archive.com/openpkg-cvs@openpkg.org/msg26353.html
Patch8: mhash-0.9.9.9-maxint.patch
# Taken from Jitesh Shah
# http://ftp.uk.linux.org/pub/armlinux/fedora/diffs-f11/mhash/0001-Alignment-fixes.patch
Patch9: mhash-0.9.9.9-alignment.patch
# Fix keygen_test
Patch10: mhash-0.9.9.9-keygen_test_fix.patch
# Fix mhash_test
# Credit to Hanno Böck back in 2015.
Patch11: mhash-0.9.9-no-free-before-use.patch
# Taken from Gentoo:
# https://gitweb.gentoo.org/repo/gentoo.git/tree/app-crypt/mhash/files/mhash-0.9.9.9-cast-temp-64bit.patch
Patch12: mhash-0.9.9.9-cast-temp-64bit.patch

BuildRequires: make
BuildRequires:  gcc
BuildRequires: autoconf, automake
Provides: libmhash = %{version}-%{release}

%description
Mhash is a free library which provides a uniform interface to a
large number of hash algorithms.

These algorithms can be used to compute checksums, message digests,
and other signatures. The HMAC support implements the basics for
message authentication, following RFC 2104. In the later versions
some key generation algorithms, which use hash algorithms, have been
added. Currently, the library supports the algorithms: ADLER32, GOST,
HAVAL256, HAVAL224, HAVAL192, HAVAL160, HAVAL128, MD5, MD4, MD2,
RIPEMD128/160/256/320, TIGER, TIGER160, TIGER128, SHA1/224/256/384/512,
Whirlpool, SNEFRU128/256, CRC32B and CRC32 checksums.

%package -n %{name}-devel
Summary: Header files and libraries for developing apps which use mhash
Requires: %{name} = %{version}-%{release}
Provides: libmhash-devel = %{version}-%{release}

%description -n %{name}-devel
This package contains the header files and libraries needed to
develop programs that use the mhash library.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q
%patch -P2 -p1 -b .alignment
%patch -P3 -p1 -b .force64bit-tiger
%patch -P4 -p1 -b .fix-snefru-segfault
%patch -P5 -p1 -b .fix-mem-leak
%patch -P6 -p1 -b .fix-whirlpool-segfault
%patch -P7 -p1 -b .fix-autotool-stomping
%patch -P8 -p1 -b .maxint
%patch -P9 -p1 -b .alignment2
%patch -P10 -p1 -b .fix
%patch -P11 -p1 -b .nofree
%patch -P12 -p1 -b .cast-temp-64bit
autoconf

%build
export CFLAGS="$CFLAGS -std=gnu17"
%configure --enable-shared %{?_with_static: --enable-static} %{!?_with_static: --disable-static}

# If this exits, the multiarch patch needs an update.
grep 'define SIZEOF_' include/mutils/mhash_config.h && exit 1

make %{?_smp_mflags}

%install
rm -rf $RPM_BUILD_ROOT
make DESTDIR=${RPM_BUILD_ROOT} install

# Eliminate some autoheader definitions which should not enter a public API.
# There are more which wait for a fix upstream.
sed -i 's!\(#define \(PACKAGE\|VERSION \).*\)!/* \1 */!g' ${RPM_BUILD_ROOT}%{_includedir}/mutils/mhash_config.h

%check
make check

%ldconfig_scriptlets -n %{name}

%files -n %{name}
%doc AUTHORS COPYING NEWS README THANKS TODO
%{_libdir}/*.so.*

%files -n %{name}-devel
%doc ChangeLog ./doc/*.c ./doc/skid2-authentication
%{_includedir}/*.h
%{_includedir}/mutils/
%{?_with_static: %{_libdir}/*.a}
%{_libdir}/*.so
%exclude %{_libdir}/*.la
%{_mandir}/man3/*

%changelog
%autochangelog
