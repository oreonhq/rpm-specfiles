Name:     libpcap
Epoch:    14
Version:  1.10.6
Release:  2%{?dist}
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
Source0:  https://www.tcpdump.org/release/%{name}-%{version}.tar.xz
Source1:  https://www.tcpdump.org/release/%{name}-%{version}.tar.xz.sig

Patch0001:      0001-man-tcpdump-and-tcpslice-have-manpages-in-man8.patch
Patch0002:      0002-pcap-config-mitigate-multilib-conflict.patch
Patch0003:      0003-pcap-linux-apparently-ctc-interfaces-on-s390-has-eth.patch
# oreon url source checksums begin
%global source0_sha256 ec97d1206bdd19cb6bdd043eaa9f0037aa732262ec68e070fd7c7b5f834d5dfc
%global source0_file libpcap-1.10.6.tar.xz
# oreon url source checksums end

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
# oreon verify url source checksums begin
%(f=%{_sourcedir}/libpcap-1.10.6.tar.xz; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "ec97d1206bdd19cb6bdd043eaa9f0037aa732262ec68e070fd7c7b5f834d5dfc" || { echo "oreon: Source0 SHA256 mismatch for libpcap-1.10.6.tar.xz" >&2; exit 1; })
# oreon verify url source checksums end
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

%changelog
* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 1.10.6-2
- Prepare for Oreon 11 (RP1)
