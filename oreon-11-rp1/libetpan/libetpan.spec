%global source0_hash 87bacdc62661a2a7aa5fe9f1f28d2f7c7a53256633ac5129903916c59f80c4c2
Name:           libetpan
Version:        1.10.1
Release:        1%{?dist}
Summary:        Portable, efficient middle-ware for different kinds of mail access
License:        BSD-3-Clause AND BSD-3-Clause-Attribution AND BSD-4-Clause
URL:            http://www.etpan.org/
Source0:        https://github.com/dinhviethoa/%{name}/archive/%{version}/%{name}-%{version}.tar.gz
Patch10:        libetpan-1.9.2-cryptopolicy.patch
Patch101:       libetpan-1.9.4-0001-Detect-extra-data-after-STARTTLS-response-and-exit-3.patch
Patch102:       libetpan-1.9.4-0002-Detect-extra-data-after-STARTTLS-responses-in-SMTP-a.patch
Patch103:       libetpan-1.9.4-mailbox_data_status-info_list-invalid-free.patch
Patch104:       libetpan-configure-c99.patch
Patch105:		libetpan-pr447-fix-poll-logical-op.patch
# oreon:deps
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  cyrus-sasl-devel
BuildRequires:  gcc-c++
BuildRequires:  gnutls-devel
BuildRequires:  libdb-devel
BuildRequires:  liblockfile-devel
BuildRequires:  libtool
BuildRequires:  make
BuildRequires:  zlib-devel
# /oreon:deps
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

%configure \
    --disable-static \
    --with-gnutls=yes \
    --with-openssl=no \
    %{nil}
%make_build
cd doc
make doc
%install
%make_install
rm -rf $RPM_BUILD_ROOT%{_libdir}/libetpan.{,l}a
iconv -f iso8859-1 -t utf-8 ChangeLog > ChangeLog.conv && mv -f ChangeLog.conv ChangeLog
%ldconfig_scriptlets
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*

%files -f %{oreon_filedir}/main.list
%files -n libetpan-devel -f %{oreon_filedir}/libetpan-devel.list

%changelog

%autochangelog
