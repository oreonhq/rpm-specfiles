# Copyright (C) 2026 Oreon HQ
# SPDX-License-Identifier: GPL-2.0-or-later

%global source0_hash 68fa62cffb974f4275641ce14c2e2d75739251f30e00e6a0900903b247d76a03

%{!?oreon_bootstrap:%global oreon_bootstrap %{nil}}
%bcond bootstrap 0
%oreon_bootstrap
Name:     libpcap
Epoch:    14
Version:        1.10.7
Release:        1%{?dist}
Summary:  A system-independent interface for user-level packet capture
License:  ISC AND BSD-2-Clause AND BSD-3-Clause AND BSD-4-Clause-UC
URL:      https://www.tcpdump.org/

BuildRequires: make
BuildRequires: bison
BuildRequires: bluez-libs-devel
BuildRequires: flex
BuildRequires: gcc
BuildRequires: git
BuildRequires: glibc-kernheaders >= 2.2.0
#rdma-core-devel not available on arm
%ifnarch %{arm}
BuildRequires: rdma-core-devel
BuildRequires:  oreon-rpm-macros
%endif

Source0:        https://www.tcpdump.org/release/libpcap-%{version}.tar.xz
Source1:        libpcap-1.10.7.tar.xz.sig

Patch0001:        0001-man-tcpdump-and-tcpslice-have-manpages-in-man8.patch
Patch0002:        0002-pcap-config-mitigate-multilib-conflict.patch
Patch0003:        0003-pcap-linux-apparently-ctc-interfaces-on-s390-has-eth.patch

%description
Libpcap provides a portable framework for low-level network
monitoring.  Libpcap can provide network statistics collection,
security monitoring and network debugging.  Since almost every system
vendor provides a different interface for packet capture, the libpcap
authors created this system-independent API to ease in porting and to
alleviate the need for several system-dependent packet capture modules
in each application.

Install libpcap if you need to do low-level network traffic monitoring
on your network.

%package devel
Summary: Libraries and header files for the libpcap library
Requires: %{name}%{?_isa} = %{epoch}:%{version}-%{release}

%description devel
Libpcap provides a portable framework for low-level network
monitoring.  Libpcap can provide network statistics collection,
security monitoring and network debugging.  Since almost every system
vendor provides a different interface for packet capture, the libpcap
authors created this system-independent API to ease in porting and to
alleviate the need for several system-dependent packet capture modules
in each application.

This package provides the libraries, include files, and other
resources needed for developing libpcap applications.

%prep
%oreon_sha256

%autosetup -S git

#sparc needs -fPIC
%ifarch %{sparc}
sed -i -e 's|-fpic|-fPIC|g' configure
%endif

%build
export CFLAGS="$RPM_OPT_FLAGS -fno-strict-aliasing"
%ifarch %{arm}
%configure
%else
%configure --enable-rdma
%endif
%make_build

%install
%make_install
rm -f $RPM_BUILD_ROOT%{_libdir}/libpcap.a

%ldconfig_scriptlets

%files
%license LICENSE
%doc README.md CHANGES CREDITS
%{_libdir}/libpcap.so.*
%{_mandir}/man7/pcap*.7*

%files devel
%{_bindir}/pcap-config
%{_includedir}/pcap*.h
%{_includedir}/pcap
%{_libdir}/libpcap.so
%{_libdir}/pkgconfig/libpcap.pc
%{_mandir}/man1/pcap-config.1*
%{_mandir}/man3/pcap*.3*
%{_mandir}/man5/pcap*.5*

