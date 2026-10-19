%global source1_hash daa90b6b3424c562e12fa72375f4ccefdc21d74e70a51c230ad39b848fd72199
%global source0_hash 9237f5bae9dcf3a91823d9963ec43b7c0e2e3374ef2ad57d92c8cd39530f4723
Name:     libpcap
Epoch:    14
Version:  1.11.0
Release:        1%{?dist}
Summary:        A system-independent interface for user-level packet capture
License:  ISC AND BSD-2-Clause AND BSD-3-Clause AND BSD-4-Clause-UC
URL:      https://www.tcpdump.org/
Source0:        https://www.tcpdump.org/release/%{name}-%{version}.tar.xz
Source1:        https://www.tcpdump.org/release/%{name}-%{version}.tar.xz.sig
Patch0001:      0001-man-tcpdump-and-tcpslice-have-manpages-in-man8.patch
Patch0002:      0002-pcap-config-mitigate-multilib-conflict.patch
Patch0003:      0003-pcap-linux-apparently-ctc-interfaces-on-s390-has-eth.patch
# oreon:deps
BuildRequires:  bison
BuildRequires:  bluez-libs-devel
BuildRequires:  flex
BuildRequires:  gcc
BuildRequires:  git
BuildRequires:  glibc-kernheaders
BuildRequires:  make
# /oreon:deps
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

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%autosetup -S git

#sparc needs -fPIC
%ifarch %{sparc}
sed -i -e 's|-fpic|-fPIC|g' configure
%endif

%build

export CFLAGS="$RPM_OPT_FLAGS -fno-strict-aliasing"
%configure --disable-rdma
%make_build
%install
%make_install
rm -f $RPM_BUILD_ROOT%{_libdir}/libpcap.a
%ldconfig_scriptlets
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*

%files -f %{oreon_filedir}/main.list
%files -n libpcap-devel -f %{oreon_filedir}/libpcap-devel.list

%changelog

%autochangelog
