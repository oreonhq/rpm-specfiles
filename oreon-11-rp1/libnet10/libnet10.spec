%global source0_hash 7c7f2e8ccb47bb47072c5cd583fea5e90ab892c75889b625346b60d10464459a
Summary:        High-level API (toolkit) to construct and inject network packets
Name:		libnet10
Version:	1.0.2a
Release:        1%{?dist}
License:	BSD-2-Clause AND BSD-4-Clause-UC
URL:		http://www.packetfactory.net/libnet/
Source0:        http://www.packetfactory.net/libnet/dist/deprecated/libnet-%{version}.tar.gz
Source1:	libnet10-config.1
Patch0:		libnet10-1.0.2a-fedora.patch
Patch1:		libnet10-1.0.2a-gcc33.patch
Patch2:		libnet10-1.0.2a-c99.patch
# oreon:deps
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  gcc
BuildRequires:  libpcap-devel
BuildRequires:  libtool
BuildRequires:  make
# /oreon:deps
%description
Libnet is a high-level API (toolkit) allowing the application programmer to
construct and inject network packets. It provides a portable and simplified
interface for low-level network packet shaping, handling and injection. Libnet
hides much of the tedium of packet creation from the application programmer
such as multiplexing, buffer management, arcane packet header information,
byte-ordering, OS-dependent issues and much more. Libnet features portable
packet creation interfaces at the IP layer and link layer, as well as a host
of supplementary and complementary functionality.

This package contains an old and deprecated version of libnet. You need it
only if the software you are using hasn't been updated to work with the newer
version and the newer API.

%package devel
Summary:	Development files for the libnet library
Requires:	%{name}%{?_isa} = %{version}-%{release}
%description devel
The libnet10-devel package includes header files and libraries necessary for
developing programs which use the libnet library. Using libnet, quick and
simple packet assembly applications can be whipped up with little effort.
With a bit more time, more complex programs can be written (traceroute and
ping were easily rewritten using libnet and libpcap).

This package contains an old and deprecated version of libnet. You need it
only if the software you are using hasn't been updated to work with the newer
version and the newer API.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n Libnet-%{version}
%patch -P0 -p1 -b .fedora
%patch -P1 -p1 -b .gcc33
%patch -P2 -p1 -b .c99

# Required to apply changes from Patch0
autoreconf -i -f

%build

%configure --with-pf_packet=yes
%make_build
%install
%make_install
mkdir -p $RPM_BUILD_ROOT%{_includedir}/%{name}/
mv -f $RPM_BUILD_ROOT%{_includedir}/{libnet{,.h},%{name}}
mv -f $RPM_BUILD_ROOT%{_bindir}/libnet{,10}-config
mkdir -p $RPM_BUILD_ROOT%{_mandir}/man{1,3}/
install -p -m 644 doc/libnet.3 $RPM_BUILD_ROOT%{_mandir}/man3/%{name}.3
install -p -m 644 %{SOURCE1} $RPM_BUILD_ROOT%{_mandir}/man1/%{name}-config.1
rm -f $RPM_BUILD_ROOT%{_libdir}/%{name}.{a,la}
%ldconfig_scriptlets
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*

%files -f %{oreon_filedir}/main.list
%files -n libnet10-devel -f %{oreon_filedir}/libnet10-devel.list

%changelog

%autochangelog
