# Copyright (C) 2026 Oreon HQ
# SPDX-License-Identifier: GPL-2.0-or-later

%global source0_hash 5c1789d290bba048a6135ed1ab81b0402dd0fb528d1f1421765c42b1fc3d6289

Name:           iproute
Version:        7.3.0
Release:        1%{?dist}
Summary:        Advanced IP routing and network configuration tools
License:        GPL-2.0-or-later AND NIST-PD
URL:            https://kernel.org/pub/linux/utils/net/iproute2/
Source0:        https://kernel.org/pub/linux/utils/net/iproute2/iproute2-%{version}.tar.xz

BuildRequires:  oreon-rpm-macros
BuildRequires:  bison
BuildRequires:  elfutils-libelf-devel
BuildRequires:  flex
BuildRequires:  gcc
BuildRequires:  libbpf-devel
BuildRequires:  libcap-devel
BuildRequires:  libmnl-devel
BuildRequires:  libselinux-devel
BuildRequires:  make
BuildRequires:  pkgconfig
Requires:       psmisc
Provides:       /sbin/ip
Provides:       /sbin/ss

%description
The iproute package contains tools for configuring Linux networking,
including IP addresses, routes, links, tunnels, and network namespaces.

%package tc
Summary:        Linux traffic control utility
Requires:       %{name}%{?_isa} = %{version}-%{release}
Provides:       /sbin/tc

%description tc
The tc utility configures Linux traffic control queues, classes, filters, and
actions.

%package devel
Summary:        Development files for iproute
Requires:       %{name}%{?_isa} = %{version}-%{release}
Provides:       iproute-static = %{version}-%{release}

%description devel
Headers and the static libnetlink library provided by iproute.

%package doc
Summary:        Examples and documentation for iproute
BuildArch:      noarch

%description doc
Examples and additional documentation for iproute tools.

%prep
%oreon_sha256
%autosetup -n iproute2-%{version}

%build
%configure --color auto
printf '\nPREFIX=%s\nSBINDIR=%s\n' '%{_prefix}' '%{_sbindir}' >> config.mk
%make_build

%install
%make_install
install -Dpm0644 include/libnetlink.h %{buildroot}%{_includedir}/libnetlink.h
install -Dpm0644 lib/libnetlink.a %{buildroot}%{_libdir}/libnetlink.a
rm -rf %{buildroot}%{_docdir}

%check
make check

%files
%license COPYING
%doc README README.devel
%dir %{_sysconfdir}/iproute2
%dir %{_datadir}/iproute2
%config(noreplace) %{_datadir}/iproute2/*
%{_sysconfdir}/iproute2/*
%{_sbindir}/*
%exclude %{_sbindir}/tc
%{_mandir}/man7/*
%exclude %{_mandir}/man7/tc-*
%{_mandir}/man8/*
%exclude %{_mandir}/man8/tc*
%{_datadir}/bash-completion/completions/*

%files tc
%license COPYING
%{_sbindir}/tc
%{_libdir}/tc/
%{_mandir}/man7/tc-*
%{_mandir}/man8/tc*
%{_datadir}/bash-completion/completions/tc

%files devel
%{_includedir}/libnetlink.h
%{_includedir}/iproute2/
%{_libdir}/libnetlink.a

%files doc
%license COPYING
%doc examples

%changelog
%autochangelog
