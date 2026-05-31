%global source0_hash 7ca765fdae52e1995b38a7080b023ca606d8621751d9dd5bb57ba5a0f5672b48

Name:		lsvpd
Version:	1.7.15
Release:	8%{?dist}
Summary:	VPD/hardware inventory utilities for Linux

License:	GPL-2.0-or-later
URL:    https://github.com/power-ras/%{name}/releases
Source:        https://github.com/power-ras/%{name}/archive/v%{version}/%{name}-%{version}.tar.gz

BuildRequires: gcc-c++
BuildRequires: libvpd-devel >= 2.2.9
BuildRequires: sg3_utils-devel
BuildRequires: zlib-devel
BuildRequires: automake
BuildRequires: libtool
BuildRequires:	librtas-devel
BuildRequires: make

Requires(post): %{_sbindir}/vpdupdate

ExclusiveArch:	%{power64}

%description
The lsvpd package contains all of the lsvpd, lscfg and lsmcode
commands. These commands, along with a scanning program
called vpdupdate, constitute a hardware inventory
system. The lsvpd command provides Vital Product Data (VPD) about
hardware components to higher-level serviceability tools. The lscfg
command provides a more human-readable format of the VPD, as well as
some system-specific information.  lsmcode lists microcode and
firmware levels.  lsvio lists virtual devices, usually only found
on POWER PC based systems.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%autosetup -p1

%build
./bootstrap.sh
%configure
%make_build


%install
%make_install

%post
%{_sbindir}/vpdupdate &
# Ignore the vpdupdate failures and enforce a success
exit 0

%files
%{!?_licensedir:%global license %%doc}
%license COPYING
%doc README
%{_sbindir}/lsvpd
%{_sbindir}/lscfg
%{_sbindir}/lsmcode
%{_sbindir}/lsvio
%{_sbindir}/vpdupdate
%{_mandir}/man8/vpdupdate.8.gz
%{_mandir}/man8/lsvpd.8.gz
%{_mandir}/man8/lscfg.8.gz
%{_mandir}/man8/lsvio.8.gz
%{_mandir}/man8/lsmcode.8.gz
%config %{_sysconfdir}/lsvpd/scsi_templates.conf
%config %{_sysconfdir}/lsvpd/cpu_mod_conv.conf
%config %{_sysconfdir}/lsvpd/nvme_templates.conf
%dir %{_sysconfdir}/lsvpd

%changelog
* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 1.7.15-8
- Prepare for Oreon 11 (RP1)
