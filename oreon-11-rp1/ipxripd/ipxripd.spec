%global source0_hash 9945b1dff05fd4b18904d4aa47fa71771c8e83ab270185ca21caa0b0023088f2

Summary: IPX RIP/SAP daemon - routing for IPX networks
Name: ipxripd
Version: 0.8
Release: 44%{?dist}
# Automatically converted from old format: GPLv2+ - review is highly recommended.
License: GPL-2.0-or-later
URL: ftp://ftp.ibiblio.org/pub/Linux/system/filesystems/ncpfs/
Source0: ftp://ftp.ibiblio.org/pub/Linux/system/filesystems/ncpfs/ipxripd-%{version}.tar.gz
Source1: ipxripd.init
Source2: ipxripd.service
Patch0: ipxripd-0.8-glibc2.1.patch
Patch1: ipxripd-0.7-gcc3.patch
Patch2: ipxripd-0.7-kernel2.6.patch
Patch3: ipxripd-0.8-printf.patch
Patch4: ipxripd-0.8-stdint.patch
Patch5: ipxripd-0.8-signal.patch
BuildRequires: gcc
BuildRequires: systemd-units
BuildRequires: make

Requires(post): systemd-units
Requires(preun): systemd-units
Requires(postun): systemd-units

%description
%{name} is an implementation of Novell's RIP and SAP protocols.
It automagically builds and updates IPX routing table in the Linux kernel.
%{name} can be useful to get a Linux box to act as an IPX router.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q
%patch 0 -p1
%patch 1 -p1
%patch 2 -p1
%patch 3 -p1
%patch 4 -p1
%patch 5 -p1

%build
make %{?_smp_mflags} CFLAGS="$RPM_OPT_FLAGS"

%install
rm -rf $RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT%{_sbindir}
install -m755 ipxd $RPM_BUILD_ROOT%{_sbindir}

install -d $RPM_BUILD_ROOT%{_mandir}/man8
install -d $RPM_BUILD_ROOT%{_mandir}/man5
install -p ipxd.8 $RPM_BUILD_ROOT%{_mandir}/man8
install -p ipx_ticks.5 $RPM_BUILD_ROOT%{_mandir}/man5

#install -d $RPM_BUILD_ROOT%{_initrddir}
#install -p -m755 %{SOURCE1} $RPM_BUILD_ROOT%{_initrddir}/ipxd

install -d $RPM_BUILD_ROOT%{_unitdir}
install -p -m644 %{SOURCE2} $RPM_BUILD_ROOT%{_unitdir}/ipxd.service

%post
%systemd_post ipxd.service

%preun
%systemd_preun ipxd.service

%postun
%systemd_postun_with_restart ipxd.service

%files
%doc COPYING README ipx_ticks ipxripd-*.lsm
%{_sbindir}/*
#%{_initrddir}/*
%{_unitdir}/*
%{_mandir}/*/*

%changelog
%autochangelog
