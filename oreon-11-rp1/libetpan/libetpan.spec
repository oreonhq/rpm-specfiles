%global source0_hash 82ec8ea11d239c9967dbd1717cac09c8330a558e025b3e4dc6a7594e80d13bb1

Name:           libetpan
Version:        1.9.4
Release:        19%{?dist}
Summary:        Portable, efficient middle-ware for different kinds of mail access

# src/bsd/getopt.c BSD-4-Clause (not used)
# src/data-types/timeutils.c BSD-3-Clause-Attribution AND BSD-4-Clause
# SPDX confirmed
License:        BSD-3-Clause AND BSD-3-Clause-Attribution AND BSD-4-Clause
URL:            http://www.etpan.org/
Source0:        https://github.com/dinhviethoa/%{name}/archive/%{version}/%{name}-%{version}.tar.gz
# system crypto policy (see rhbz#1179310)
Patch10:        libetpan-1.9.2-cryptopolicy.patch
# Upstream patches
#
# CVE-2020-15953
# https://github.com/dinhvh/libetpan/issues/386
# Detect extra data after STARTTLS response and exit
# https://github.com/dinhvh/libetpan/pull/387
Patch101:       libetpan-1.9.4-0001-Detect-extra-data-after-STARTTLS-response-and-exit-3.patch
# Detect extra data after STARTTLS responses in SMTP and POP3 and exit
# https://github.com/dinhvh/libetpan/pull/388
Patch102:       libetpan-1.9.4-0002-Detect-extra-data-after-STARTTLS-responses-in-SMTP-a.patch
# https://github.com/dinhvh/libetpan/issues/420
Patch103:       libetpan-1.9.4-mailbox_data_status-info_list-invalid-free.patch
# https://github.com/dinhvh/libetpan/pull/423
Patch104:       libetpan-configure-c99.patch
# https://github.com/dinhvh/libetpan/pull/447
Patch105:		libetpan-pr447-fix-poll-logical-op.patch

BuildRequires:  gcc-c++
BuildRequires:  liblockfile-devel
BuildRequires:  libdb-devel < 5.4
BuildRequires:  cyrus-sasl-devel
BuildRequires:  gnutls-devel
BuildRequires:  libtool
BuildRequires:  zlib-devel
BuildRequires:  autoconf automake
BuildRequires:  make
# disabled by default in configure.ac accidentally
# https://github.com/dinhviethoa/libetpan/issues/221
# libcurl and libexpat not needed by Claws Mail:
# http://lists.claws-mail.org/pipermail/users/2016-January/015665.html
#BuildRequires:  libcurl-devel expat-devel

%description
The purpose of this mail library is to provide a portable, efficient middle-ware
for different kinds of mail access. When using the drivers interface, the
interface is the same for all kinds of mail access, remote and local mailboxes.

%package        devel
Summary:        Development package for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    devel
The %{name}-devel package contains the files needed for development
with %{name}.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q

#%patch0 -b .libetpan-config-script
sed -i.flags libetpan.pc.in \
    -e 's|-letpan@LIBSUFFIX@.*$|-letpan@LIBSUFFIX@|'
%patch -P10 -p1 -b .crypto-policy
%patch -P101 -p1 -b .CVE-2020-15953-1
%patch -P102 -p1 -b .CVE-2020-15953-2
%patch -P103 -p1 -b .CVE-2022-4121.tmp
%patch -P104 -p1 -b .c99
%patch -P105 -p1 -b .logical_op

# 2013-08-05 F20 development, bz 992070: The configure scripts adds some
# extra libs to the GnuTLS link options, which cause rebuilds to fail, since
# gnutls-devel no longer pulls in libgcrypt-devel libgpg-error-devel
# [The alternative fix is to BR those packages, of course.]
grep 'GNUTLSLIB="-lgnutls -lgcrypt -lgpg-error -lz"' configure.ac || exit -1
sed -i '\@GNUTLSLIB=@s!-lgcrypt -lgpg-error -lz!!g' configure.ac

env NOCONFIGURE=1 ./autogen.sh
cp -p %{_bindir}/libtool .

%build
#%global optflags %(echo %{optflags} | sed 's/-g /-g -Wno-format-truncation /')
# Use poll instead of select on F40 and above (bug 2283446)
%configure \
    --disable-static \
    --with-gnutls=yes \
    --with-openssl=no \
%if 0%{?fedora} >= 41
    --with-poll=yes \
%endif
    %{nil}

%make_build

cd doc
make doc

%install
%make_install

rm -rf $RPM_BUILD_ROOT%{_libdir}/libetpan.{,l}a

iconv -f iso8859-1 -t utf-8 ChangeLog > ChangeLog.conv && mv -f ChangeLog.conv ChangeLog

%ldconfig_scriptlets

%files
%license COPYRIGHT
%doc ChangeLog NEWS
%{_libdir}/%{name}.so.20
%{_libdir}/%{name}.so.20.*

%files devel
%doc doc/API.html doc/README.html doc/DOCUMENTATION
%{_libdir}/pkgconfig/%{name}.pc
%{_includedir}/libetpan/
%{_includedir}/libetpan.h
%{_libdir}/%{name}.so

%changelog
%autochangelog
