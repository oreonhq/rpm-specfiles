%global source0_hash f76c36a46e801ebd6e1f53d06987f148e70c1a4b288da5aba0dce1b3c7b2bf0f

Name:           lsvpd
Version:        1.7.17
Release:        1%{?dist}
Summary:        VPD/hardware inventory utilities for Linux
License:        GPL-2.0-or-later
URL:            https://github.com/power-ras/lsvpd/releases
Source0:        https://github.com/power-ras/lsvpd/archive/v%{version}/lsvpd-%{version}.tar.gz

Patch10: lsvpd-add-FRU-number-for-Spyre-cards.patch

BuildRequires: gcc-c++
BuildRequires: libvpd-devel >= 2.2.9
BuildRequires: sg3_utils-devel
BuildRequires: zlib-devel
BuildRequires: automake
BuildRequires: libtool
BuildRequires: librtas-devel
BuildRequires: make
BuildRequires: systemd-rpm-macros
Requires: systemd
Requires(post): %{_sbindir}/vpdupdate

ExclusiveArch:  %{power64}

%description
The lsvpd package contains all of the lsvpd, lscfg and lsmcode
commands. These commands, along with a scanning program
called vpdupdate, constitute a hardware inventory
system.

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
systemctl -q enable vpdupdate.service >/dev/null 2>&1 || :
systemctl daemon-reload >/dev/null 2>&1 || :
%{_sbindir}/vpdupdate &
exit 0

%preun
systemctl -q disable vpdupdate.service >/dev/null 2>&1 || :
systemctl daemon-reload >/dev/null 2>&1 || :

%files
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
%{_unitdir}/vpdupdate.service

%changelog
* Mon Jun 09 2026 Oreon Packaging Team <packaging@oreonhq.com> - 1.7.17-1
- import for oreon 11 iso
