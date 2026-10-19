%global source0_hash 3de1cbb889d06e5a6a945dcb921292544477ab89da95ca89f1eec2de29937afb
%bcond_with mdns
%bcond_with braille
%bcond_without cups_ppdc
%global _hardened_build 1
Summary:        OpenPrinting CUPS filters for CUPS 2.X
Name:    cups-filters
Epoch:   1
Version: 2.0.1
Release:        1%{?dist}
License: Apache-2.0 WITH LLVM-exception
URL:     https://github.com/OpenPrinting/cups-filters
Source0:        https://github.com/OpenPrinting/cups-filters/releases/download/2.0.1/cups-filters-2.0.1.tar.gz
Source1: lftocrlf.ppd
Source2: lftocrlf
Patch001: 0001-Fix-build-failure-with-GCC-15-and-std-c23.patch
Patch002: 0001-Introduce-foomatic-hash-and-reject-unauthorized-valu.patch
Patch003: foomatic-ripdie-error.patch
Patch004: foomaticrip-reject-unknown-values.patch
Patch005: 0001-rastertopclx.c-Fix-infinite-loop-caused-by-crafted-f.patch
Conflicts: cups-filters-driverless < 1:2.0.0-3
%if %{with braille}
Recommends: braille-printer-app
%endif
Requires: cups-filesystem
# oreon:deps
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  gcc
BuildRequires:  gettext-devel
BuildRequires:  git-core
BuildRequires:  libtool
BuildRequires:  make
BuildRequires:  pkgconf-pkg-config
BuildRequires:  pkgconfig(cups)
BuildRequires:  pkgconfig(libcupsfilters)
BuildRequires:  pkgconfig(libppd)
BuildRequires:  python3-cups
BuildRequires:  systemd-rpm-macros
# /oreon:deps
%description
Contains backends, filters, and other software that was
once part of the core CUPS distribution but is no longer maintained by
Apple Inc. In addition it contains additional filters developed
independently of Apple, especially filters for the PDF-centric printing
workflow introduced by OpenPrinting.

%package driverless
Summary: OpenPrinting driverless backends and drivers for CUPS 2.X
License: Apache-2.0 WITH LLVM-exception
Conflicts: cups-filters < 1:2.0.0-3
Requires: avahi
Requires: cups-ipptool
%if %{with mdns}
Recommends: nss-mdns
%endif
Requires: cups-filesystem
%description driverless
Contains backends and drivers for driverless implementation for cups-filters,
which makes driverless printers to be seen when listing printers nearby and gives
a specific generated driver for driverless printer in the local network. They are
tools for backward compatibility with applications which don't handle CUPS temporary
queues.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%autosetup -S git -N

%if 0%{?fedora} >= 43 || 0%{?rhel} >=9 || 0%{?oreon} >= 11
%autopatch
%else
%autopatch -M 3
%endif

%build

./autogen.sh
%configure --enable-driverless \
           --enable-individual-cups-filters \
           --disable-universal-cups-filter \
           --disable-mutool \
           --disable-rpath \
           --disable-silent-rules \
           --disable-static
%make_build
%install
%make_install
install -p -m 0755 %{SOURCE2} %{buildroot}%{_cups_serverbin}/filter/lftocrlf
install -p -m 0644 %{SOURCE1} %{buildroot}%{_datadir}/ppd/cupsfilters/lftocrlf.ppd
%if 0%{?fedora} >= 43 || 0%{?rhel} >=9 || 0%{?oreon} >= 11
mkdir -p %{buildroot}%{_libexecdir}/%{name}
cat > %{buildroot}%{_libexecdir}/%{name}/posttrans.sh << EOF
if grep -q -R 'FoomaticRIPCommandLine\|FoomaticRipOptionSetting' %{_sysconfdir}/cups/ppd
then
  tmpfile=\$(mktemp -p /var/tmp foomatic-scan.XXXXXXXX)
  for ppd in %{_sysconfdir}/cups/ppd/*.ppd
  do
    foomatic-hash --ppd \$ppd \$tmpfile %{_sysconfdir}/foomatic/hashes.d/hashes.upgrade || :
  done
  if test -f %{_sysconfdir}/foomatic/hashes.d/hashes.upgrade
  then
    echo "Foomatic-rip values which can inject code found - review findings in \$tmpfile. Read release notes for instructions." || :
  fi
else
  touch %{_sysconfdir}/foomatic/hashes.d/hashes.new
fi
exit 0
EOF
mkdir -p %{buildroot}%{_unitdir}
cat > %{buildroot}%{_unitdir}/foomaticrip-upgrade.service << EOF
[Unit]
Description=Allowing already installed printers for foomatic-rip
ConditionPathIsDirectory=%{_sysconfdir}/foomatic/hashes.d
ConditionDirectoryNotEmpty=!%{_sysconfdir}/foomatic/hashes.d
[Service]
Type=oneshot
ExecStart=bash -c %{_libexecdir}/%{name}/posttrans.sh
[Install]
WantedBy=multi-user.target
EOF
mkdir -p %{buildroot}%{_unitdir}/cups.service.d
cat > %{buildroot}%{_unitdir}/cups.service.d/10-foomaticrip-upgrade.conf << EOF
[Unit]
After=foomaticrip-upgrade.service
Wants=foomaticrip-upgrade.service
EOF
%endif
ln -sf %{_cups_serverbin}/filter/foomatic-rip %{buildroot}%{_bindir}/foomatic-rip
%if %{with cups_ppdc}
mkdir -p %{buildroot}%{_datadir}/cups/ppdc
mv %{buildroot}%{_datadir}/{ppdc/pcl.h,cups/ppdc/pcl.h}
mv %{buildroot}%{_datadir}/{ppdc/escp.h,cups/ppdc/escp.h}
%endif
rm -f %{buildroot}%{_pkgdocdir}/{COPYING,NOTICE,LICENSE}
rm -f %{buildroot}%{_pkgdocdir}/INSTALL
rm -f %{buildroot}%{_pkgdocdir}/CHANGES-1.x.md
%oreon_autofiles cups-filters-driverless usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%check

make check
%post

if [ $1 -gt 1 ]
then
  rm -f /var/cache/cups/ppds.dat || :
fi
%if 0%{?fedora} >= 43 || 0%{?rhel} >=9 || 0%{?oreon} >= 11
  %systemd_post foomaticrip-upgrade.service
%endif
%preun

%if 0%{?fedora} >= 43 || 0%{?rhel} >=9 || 0%{?oreon} >= 11
  %systemd_preun foomaticrip-upgrade.service
%endif
%postun

%if 0%{?fedora} >= 43 || 0%{?rhel} >=9 || 0%{?oreon} >= 11
  %systemd_postun foomaticrip-upgrade.service
%endif
%posttrans

%if 0%{?fedora} >= 43 || 0%{?rhel} >=9 || 0%{?oreon} >= 11
  %systemd_posttrans_with_reload foomaticrip-upgrade.service
%endif
if [ $1 -gt 1 ]
then
  if systemctl is-active cups &> /dev/null
  then
    systemctl restart cups || :
  fi
  %if 0%{?fedora} >= 43 || 0%{?rhel} >=9 || 0%{?oreon} >= 11
    systemctl start foomaticrip-upgrade.service || :
  %endif
fi
%files -f %{oreon_filedir}/main.list
%files -n cups-filters-driverless -f %{oreon_filedir}/cups-filters-driverless.list

%changelog

* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 2.0.1-15
- Prepare for Oreon 11 (RP1)
