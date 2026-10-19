%global source0_hash 1973c7732f1f9f0a4c0ccf2c1ce462c7c25060b25643ea90f9b98f53a813faec
Name:           dante
Version:        1.4.4
Release:        1%{?dist}
Summary:        A free SOCKS v4/v5 client implementation
License:        BSD-Inferno-Nettverk
URL:            https://www.inet.no/%{name}
Source0:        https://www.inet.no/%{name}/files/%{name}-%{version}.tar.gz
Source1:        sockd.service
Patch0:         dante-1.4.3-HAVE_SENDBUF_IOCTL.patch
# oreon:deps
BuildRequires:  autoconf
BuildRequires:  bison
BuildRequires:  cyrus-sasl-devel
BuildRequires:  flex
BuildRequires:  gcc
BuildRequires:  krb5-devel
BuildRequires:  libtool
BuildRequires:  libxcrypt-devel
BuildRequires:  miniupnpc-devel
BuildRequires:  pam-devel
BuildRequires:  systemd
BuildRequires:  systemd-rpm-macros
# /oreon:deps
%description
Dante is a free implementation of the SOCKS proxy protocol, version 4,
and version 5 (rfc1928). It can be used as a firewall between
networks. It is being developed by Inferno Nettverk A/S, a Norwegian
consulting company. Commercial support is available.

This package contains the dynamic libraries required to "socksify"
existing applications, allowing them to automatically use the SOCKS
protocol.

%package server
Summary:        A free SOCKS v4/v5 server implementation
Requires:       %{name}%{?_isa} = %{version}-%{release}
%description server
This package contains "sockd", the SOCKS proxy daemon and its
documentation.  This is the server part of the Dante SOCKS proxy
package and allows SOCKS clients to connect through it to the external
network.

%package devel
Summary:        Development libraries for SOCKS
Requires:       %{name}%{?_isa} = %{version}-%{release}
%description devel
Additional libraries required to compile programs that use SOCKS.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%oreon_prep
%build

for file in CREDITS NEWS doc/socksify.1; do
  iconv -f ISO-8859-1 -t UTF-8 -o $file.new $file && \
  touch -r $file $file.new && \
  mv $file.new $file
done
DANTELIBC=`find /%{_lib}/ -maxdepth 1 -iname "libc.so.*"`
echo >> acinclude.m4
sed -i -e 's!AM_CONFIG_HEADER!AC_CONFIG_HEADERS!' configure.ac
autoreconf --force --install --verbose
%configure \
  --libdir=${exec_prefix}%{_libdir}/dante \
  --disable-static \
  --without-glibc-secure \
  --enable-preload \
  --enable-clientdl \
  --enable-serverdl \
  --enable-drt-fallback \
  --enable-shared \
  --with-libc=$DANTELIBC
sed -i -e 's! -shared ! -Wl,--as-needed\0!g' libtool
%make_build
%install
%make_install
rm Makefile* SPECS/Makefile*
rm INSTALL
mkdir -p %{buildroot}/%{_sysconfdir} %{buildroot}/%{_unitdir}
install -m 644 example/socks.conf %{buildroot}/%{_sysconfdir}
install -m 644 example/sockd.conf %{buildroot}/%{_sysconfdir}
install -m 644 %{SOURCE1} %{buildroot}/%{_unitdir}/sockd.service
%oreon_autofiles dante-server usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles dante-devel usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*

%post server

%systemd_post sockd.service
%preun server

%systemd_preun sockd.service
%postun server

%systemd_postun sockd.service
%files -f %{oreon_filedir}/main.list
%files -n dante-server -f %{oreon_filedir}/dante-server.list
%files -n dante-devel -f %{oreon_filedir}/dante-devel.list

%changelog

%autochangelog
