%global source5_hash 7675353b10f78fd85a41eeb46827dac2a17c9087d3c2c4cff2c69c024e1a666a
%global source4_hash 3232c2f1efcf97ab6bbeba1faf8e994948900c7c076cab3232581e9cfeadf96a
%global source3_hash 4747158a2e69115a8a08fe2a3c9943b3d7d589e0ae104dda61ffcc1d05014a00
%global source2_hash 19b565ab4c4f9eaf6d2bbab18a94c1220c78315590bdce0ff085878537cd710b
%global source1_hash dd85577a39ae898bc40b56af6d1e16233f5f59fe2131bb709fa89e699dd4737a
%global source0_hash 36740021795d4153994679809448a94dad97131ae1535ba194c964227769126a
%global commit d0cc618721a8b450997f44626c9d937245dc1b9a
%global link_bin nmap
%global link_man ncman
Summary:        OpenBSD netcat to read and write data across connections using TCP or UDP
Name:            netcat
Version:         1.237
Release:        1%{?dist}
License:         BSD-3-Clause AND BSD-2-Clause
URL:             https://man.openbsd.org/nc.1
Source0:        https://raw.githubusercontent.com/openbsd/src/%{commit}/usr.bin/nc/%{name}.c
Source1:         https://raw.githubusercontent.com/openbsd/src/%{commit}/usr.bin/nc/nc.1
Source2:         https://raw.githubusercontent.com/openbsd/src/%{commit}/usr.bin/nc/atomicio.c
Source3:         https://raw.githubusercontent.com/openbsd/src/%{commit}/usr.bin/nc/atomicio.h
Source4:         https://raw.githubusercontent.com/openbsd/src/%{commit}/usr.bin/nc/socks.c
Source5:         https://raw.githubusercontent.com/openbsd/src/%{commit}/usr.bin/nc/Makefile
Patch0:          https://salsa.debian.org/debian/netcat-openbsd/-/raw/3dd21269220dd746eaf4e64a17b7257eba47c2c2/debian/patches/port-to-linux-with-libbsd.patch
Requires(post):  %{?el8:/usr/sbin/}alternatives
Requires(preun): %{?el8:/usr/sbin/}alternatives
# oreon:deps
BuildRequires:  gcc
BuildRequires:  libbsd-devel
BuildRequires:  libretls-devel
BuildRequires:  make
# /oreon:deps
%description
The OpenBSD nc (or netcat) utility can be used for just about anything involving
TCP, UDP, or UNIX-domain sockets. It can open TCP connections, send UDP packets,
listen on arbitrary TCP and UDP ports, do port scanning, and deal with both IPv4
and IPv6. Unlike telnet(1), nc scripts nicely, and separates error messages onto
standard error instead of sending them to standard output, as telnet(1) might do
with some.

%prep

%setup -q -T -c
cp -pf %{SOURCE0} %{SOURCE1} %{SOURCE2} %{SOURCE3} %{SOURCE4} %{SOURCE5} .
%patch -P0 -p1 -b .port-to-linux-with-libbsd
sed -e '1i #define unveil(path, permissions) 0' \
    -e '1i #define pledge(request, paths) 0' \
    -e '1i #ifndef IPTOS_DSCP_VA\n#define IPTOS_DSCP_VA 0xb0\n#endif' \
    -i netcat.c
sed -e 's/^\(LIBS ?= .*\)/\1 -ltls/' -i Makefile

# https://fedoraproject.org/wiki/Changes/dropingOfCertPemFile
%if 0%{?fedora} >= 43 || 0%{?rhel} >= 11 || 0%{?oreon} >= 11
sed -e 's/\(^[[:space:]]*Rflag =\) tls_default_ca_cert_file();/\1 NULL;/' \
    -i netcat.c
%endif

%build

%make_build CFLAGS="$RPM_OPT_FLAGS" LDFLAGS="$RPM_LD_FLAGS"
%install
install -D -p -m 0755 nc $RPM_BUILD_ROOT%{_bindir}/%{name}
install -D -p -m 0644 nc.1 $RPM_BUILD_ROOT%{_mandir}/man1/%{name}.1
touch $RPM_BUILD_ROOT%{_bindir}/nc
touch $RPM_BUILD_ROOT%{_mandir}/man1/nc.1.gz
%oreon_autofiles main

%post

alternatives --install %{_bindir}/nc %{link_bin} %{_bindir}/%{name} 10 \
  --slave %{_mandir}/man1/nc.1.gz %{link_man} %{_mandir}/man1/%{name}.1.gz
%preun

if [ $1 -eq 0 ]; then
  alternatives --remove %{link_bin} %{_bindir}/%{name}
fi
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
