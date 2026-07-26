%global source0_hash 88b30feace372c4a61e6adb2534791c0cfba6123ebcca7f59bbb76580d4a6915

Name:		can-utils
Version:	2025.01
Release:	5%{?dist}
Summary:	SocketCAN user space utilities and tools

# most utilities are dual-licensed but some are GPLv2 only
# Automatically converted from old format: GPLv2 and (GPLv2 or BSD) - review is highly recommended.
License:	GPL-2.0-only AND (GPL-2.0-only OR LicenseRef-Callaway-BSD)
URL:		https://github.com/linux-can/can-utils
Source0:	%{url}/archive/v%{version}.tar.gz#/%{name}-%{version}.tar.gz

BuildRequires:	cmake
BuildRequires:	gcc
BuildRequires:	glibc-devel

%description
CAN is a message-based network protocol designed for vehicles originally
created by Robert Bosch GmbH. SocketCAN is a set of open source CAN
drivers and a networking stack contributed by Volkswagen Research to
the Linux kernel.

This package contains some user space utilities for Linux SocketCAN subsystem.

%package devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description devel
Development file for %{name}.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1

%build
%cmake -DCMAKE_INSTALL_LIBDIR=%{_libdir}
%cmake_build

# Extract the dual license from one of the sources
head -39 asc2log.c | tail -37 | cut -c4- > COPYING

%install
%cmake_install

%files
%license COPYING
%doc README.md
%{_bindir}/asc2log
%{_bindir}/bcmserver
%{_bindir}/can-calc-bit-timing
%{_bindir}/canbusload
%{_bindir}/candump
%{_bindir}/canfdtest
%{_bindir}/cangen
%{_bindir}/cangw
%{_bindir}/canlogserver
%{_bindir}/canplayer
%{_bindir}/cansend
%{_bindir}/cansequence
%{_bindir}/cansniffer
%{_bindir}/isotpdump
%{_bindir}/isotpperf
%{_bindir}/isotprecv
%{_bindir}/isotpsend
%{_bindir}/isotpserver
%{_bindir}/isotpsniffer
%{_bindir}/isotptun
%{_bindir}/j1939acd
%{_bindir}/j1939cat
%{_bindir}/j1939spy
%{_bindir}/j1939sr
%{_bindir}/j1939-timedate-cli
%{_bindir}/j1939-timedate-srv
%{_bindir}/log2asc
%{_bindir}/log2long
%{_bindir}/mcp251xfd-dump
%{_bindir}/slcan_attach
%{_bindir}/slcand
%{_bindir}/slcanpty
%{_bindir}/testj1939

%files devel
%{_bindir}/isobusfs-cli
%{_bindir}/isobusfs-srv
%{_includedir}/isobusfs*
%{_libdir}/libisobusfs*.so

%changelog
%autochangelog
