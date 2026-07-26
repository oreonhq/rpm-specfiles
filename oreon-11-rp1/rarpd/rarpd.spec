%global source0_hash 4d6145d435a5d8b567b9798620f57f9b0a464078a1deba267958f168fbe776e6

Summary: The RARP daemon
Name: rarpd
Version: ss981107
Release: 70%{?dist}
# Automatically converted from old format: GPLv2+ - review is highly recommended.
License: GPL-2.0-or-later
Source: ftp://ftp.fi.netbsd.org/.m/mirrors1/ftp.inr.ac.ru/ip-routing/dhcp.bootp.rarp/rarpd-%{version}.tar.gz
Source1: rarpd.service
Source2: LICENSE
Patch0: rarpd-%{version}.patch
Patch1: rarpd-fd-leak.patch
Patch2: rarpd-sprintf.patch
Requires(post): systemd-units
Requires(preun): systemd-units
Requires(postun): systemd-units
BuildRequires: make
BuildRequires: systemd-units
BuildRequires: gcc

%description
RARP (Reverse Address Resolution Protocol) is a protocol which allows
individual devices on an IP network to get their own IP addresses from the
RARP server.  Some machines (e.g. SPARC boxes) use this protocol instead
of e.g. DHCP to query their IP addresses during network bootup.
Linux kernels up to 2.2 used to provide a kernel daemon for this service,
but since 2.3 kernels it is served by this userland daemon.

You should install rarpd if you want to set up a RARP server on your
network.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n rarpd
%patch -P0 -p1 -b .ss981107
%patch -P1 -p1 -b .fd-leak
%patch -P2 -p1 -b .sprintf

%build
%ifarch s390 s390x
export CFLAGS="$RPM_OPT_FLAGS -fPIC"
%else
export CFLAGS="$RPM_OPT_FLAGS -fpic"
%endif
export LDFLAGS="-pie -Wl,-z,relro,-z,now"
make CFLAGS="$CFLAGS"

cp %{SOURCE2} .

%install
mkdir -p ${RPM_BUILD_ROOT}%{_unitdir}
mkdir -p ${RPM_BUILD_ROOT}%{_sbindir}
mkdir -p ${RPM_BUILD_ROOT}%{_mandir}/man8

install -m 644 %{SOURCE1} ${RPM_BUILD_ROOT}%{_unitdir}/rarpd.service
install -m 755 rarpd ${RPM_BUILD_ROOT}%{_sbindir}/rarpd
install -m 644 rarpd.8 ${RPM_BUILD_ROOT}%{_mandir}/man8/rarpd.8

%post
%systemd_post rarpd.service

%preun
%systemd_preun rarpd.service

%postun
%systemd_postun_with_restart rarpd.service

%files
%doc README LICENSE
%{_sbindir}/rarpd
%{_mandir}/man8/*
%{_unitdir}/*

%changelog
%autochangelog
