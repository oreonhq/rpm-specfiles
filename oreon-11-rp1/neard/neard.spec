%global source0_hash 129bbf69488fdb599d480356765941f111d7799495d0d64095b25e893c4d2be7

Name:          neard
Version:       0.19
Release:       8%{?dist}
Summary:       Near Field Communication (NFC) manager
# Automatically converted from old format: GPLv2 - review is highly recommended.
License:       GPL-2.0-only
URL:           https://01.org/linux-nfc/
Source0:       https://git.kernel.org/pub/scm/network/nfc/neard.git/snapshot/%{name}-%{version}.tar.gz

BuildRequires: automake autoconf libtool autoconf-archive
BuildRequires: dbus-devel
BuildRequires: gcc
BuildRequires: glib2-devel
BuildRequires: libnl3-devel
BuildRequires: make
BuildRequires: systemd

%description
neard is an NFC (Near Field Communication) daemon for managing NFC operations 
on devices running the Linux operating system. It relies on the Linux kernel NFC 
socket and generic netlink families, and is a fully modular system that can be 
extended through plug-ins.

It supports all 4 NFC tag types reading and writing, along with NFC LLCP 
(peer to peer mode) in both target and initiator modes.

%package tools
Summary: Tools for use with neard

%description tools
These are tools to use neard.

%package devel
Summary: Development package for neard
Requires: %{name}%{?_isa} = %{version}-%{release}

%description devel
Files for development with neard.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1

%build
autoreconf -vif
%configure --enable-tools
%{make_build}

%install
%{make_install}

rm -f %{buildroot}/usr/include/version.h

%check
make check %{?_smp_mflags}

%ldconfig_scriptlets

%files
%license COPYING
%{_sysconfdir}/dbus-1/system.d/org.neard.conf
%{_unitdir}/neard.service
%{_libexecdir}/nfc/neard
%{_mandir}/man5/neard.conf.5*
%{_mandir}/man8/neard.8*

%files tools
%{_bindir}/nciattach
%{_bindir}/nfctool
%{_mandir}/man1/nfctool.1*

%files devel
%doc doc/*txt
%{_includedir}/near/
%{_libdir}/pkgconfig/neard.pc

%changelog
%autochangelog
