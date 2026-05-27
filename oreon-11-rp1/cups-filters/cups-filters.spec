%global source0_hash 3de1cbb889d06e5a6a945dcb921292544477ab89da95ca89f1eec2de29937afb

%if 0%{?fedora}
%bcond_without mdns
%bcond_without braille
%else
%bcond_with mdns
%bcond_with braille
%endif

# currently we use CUPS PPD compiler which will be removed
# in CUPS 3.0, then we will use PPD compiler from libppd-tools
%bcond_without cups_ppdc

# we build CUPS also with relro
%global _hardened_build 1

Summary: OpenPrinting CUPS filters for CUPS 2.X
Name:    cups-filters
Epoch:   1
Version: 2.0.1
Release: 15%{?dist}

# the CUPS exception text is the same as LLVM exception, so using that name with
# agreement from legal team
# https://lists.fedoraproject.org/archives/list/legal@lists.fedoraproject.org/message/A7GFSD6M3GYGSI32L2FC5KB22DUAEQI3/
License: Apache-2.0 WITH LLVM-exception

URL:     https://github.com/OpenPrinting/cups-filters
Source0:        https://github.com/OpenPrinting/cups-filters/releases/download/2.0.1/cups-filters-2.0.1.tar.gz
Source1: lftocrlf.ppd
Source2: lftocrlf


# Patches
# https://github.com/OpenPrinting/cups-filters/pull/618
Patch001: 0001-Fix-build-failure-with-GCC-15-and-std-c23.patch
# introducing foomatic-hash, but without rejecting values in foomatic-rip
# https://github.com/OpenPrinting/cups-filters/pull/648
Patch002: 0001-Introduce-foomatic-hash-and-reject-unauthorized-valu.patch
# make sure errors from foomatic-rip are propagated
# https://github.com/OpenPrinting/cups-filters/pull/649
Patch003: foomatic-ripdie-error.patch
# rejecting the unknown values in foomatic-rip
# https://github.com/OpenPrinting/cups-filters/pull/648
Patch004: foomaticrip-reject-unknown-values.patch
# CVE-2025-64524 fix
Patch005: 0001-rastertopclx.c-Fix-infinite-loop-caused-by-crafted-f.patch


# driverless backend/driver was moved into a separate package to
# remove avahi dependency for filters
# remove once C10S is released and F40 is EOL
Conflicts: cups-filters-driverless < 1:2.0.0-3

# autogen.sh
BuildRequires: autoconf
# autogen.sh
BuildRequires: automake
# filter binaries and backends are written in C
BuildRequires: gcc
# autogen.sh
BuildRequires: gettext-devel
# for autosetup
BuildRequires: git-core
# autogen.sh
BuildRequires: libtool
# uses make for compiling
BuildRequires: make
# we use pkgconfig to get a proper devel packages
# proper CFLAGS and LDFLAGS
BuildRequires: pkgconf-pkg-config
# uses CUPS API
BuildRequires: pkgconfig(cups) >= 2.2.2
# uses cupsfilters API
BuildRequires: pkgconfig(libcupsfilters) >= 2.0b3
# uses PPD API
BuildRequires: pkgconfig(libppd) >= 2.0b3
# Make sure we get postscriptdriver tags.
BuildRequires: python3-cups
# for systemd unit for upgrade
BuildRequires: systemd-rpm-macros

%if %{with braille}
Recommends: braille-printer-app
%endif
# needs cups dirs
Requires: cups-filesystem


%description
Contains backends, filters, and other software that was
once part of the core CUPS distribution but is no longer maintained by
Apple Inc. In addition it contains additional filters developed
independently of Apple, especially filters for the PDF-centric printing
workflow introduced by OpenPrinting.


%package driverless
Summary: OpenPrinting driverless backends and drivers for CUPS 2.X
License: Apache-2.0 WITH LLVM-exception

# backends and drivers has been moved from the main package to subpackage
# to remove the avahi/mdns dependency needed for driverless
# remove after F40 is EOL and C10S is released
Conflicts: cups-filters < 1:2.0.0-3

# finding device via driverless depends on running avahi-daemon
Requires: avahi
# ippfind is used in driverless backend, not needed classic PPD based print queue
Requires: cups-ipptool
# cups-browsed needs systemd-resolved or nss-mdns for resolving .local addresses of remote print queues
# let's not require a specific package and let the user decide what he wants to use.
# just recommend nss-mdns for Fedora for now to have working default, but
# don't hardwire it for resolved users
%if %{with mdns}
Recommends: nss-mdns
%endif

# needs cups dirs
Requires: cups-filesystem


%description driverless
Contains backends and drivers for driverless implementation for cups-filters,
which makes driverless printers to be seen when listing printers nearby and gives
a specific generated driver for driverless printer in the local network. They are
tools for backward compatibility with applications which don't handle CUPS temporary
queues.


%prep
%(test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; })
%autosetup -S git -N

%if 0%{?fedora} >= 43 || 0%{?rhel} >=9
%autopatch
%else
%autopatch -M 3
%endif


%build
# work-around Rpath
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

# 2229776 - Add textonly driver back, but as lftocrlf
install -p -m 0755 %{SOURCE2} %{buildroot}%{_cups_serverbin}/filter/lftocrlf
install -p -m 0644 %{SOURCE1} %{buildroot}%{_datadir}/ppd/cupsfilters/lftocrlf.ppd

# remove this once F43 is EOL
%if 0%{?fedora} >= 43 || 0%{?rhel} >=9

mkdir -p %{buildroot}%{_libexecdir}/%{name}

cat > %{buildroot}%{_libexecdir}/%{name}/posttrans.sh << EOF
#!/usr/bin/bash

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


# LSB3.2 requires /usr/bin/foomatic-rip,
# create it temporarily as a relative symlink
# we may use symlink to universal filter, but LSB is about guaranteed compatibility set
# among distibutions, so rather have the strict foomatic-rip filter...
ln -sf %{_cups_serverbin}/filter/foomatic-rip %{buildroot}%{_bindir}/foomatic-rip

%if %{with cups_ppdc}
mkdir -p %{buildroot}%{_datadir}/cups/ppdc
mv %{buildroot}%{_datadir}/{ppdc/pcl.h,cups/ppdc/pcl.h}
mv %{buildroot}%{_datadir}/{ppdc/escp.h,cups/ppdc/escp.h}
%endif

# remove license files which are in %%pkgdocdir
rm -f %{buildroot}%{_pkgdocdir}/{COPYING,NOTICE,LICENSE}

# remove INSTALL since it is unnecessary
rm -f %{buildroot}%{_pkgdocdir}/INSTALL

# remove CHANGES-1.x.md, since it is carried by a dependency
rm -f %{buildroot}%{_pkgdocdir}/CHANGES-1.x.md


%check
make check


%post
# remove PPD cache to make bz#2351389 fix work right away
# remove after F43 EOL
if [ $1 -gt 1 ]
then
  rm -f /var/cache/cups/ppds.dat || :
fi

%if 0%{?fedora} >= 43 || 0%{?rhel} >=9
  %systemd_post foomaticrip-upgrade.service
%endif


%preun
%if 0%{?fedora} >= 43 || 0%{?rhel} >=9
  %systemd_preun foomaticrip-upgrade.service
%endif


%postun
%if 0%{?fedora} >= 43 || 0%{?rhel} >=9
  %systemd_postun foomaticrip-upgrade.service
%endif


%posttrans
%if 0%{?fedora} >= 43 || 0%{?rhel} >=9
  %systemd_posttrans_with_reload foomaticrip-upgrade.service
%endif

if [ $1 -gt 1 ]
then
  # since we moved to individual filters, we have to restart cups
  # to load new conversion tables if it is running
  # remove by F43 EOL and C11S release
  if systemctl is-active cups &> /dev/null
  then
    systemctl restart cups || :
  fi

  %if 0%{?fedora} >= 43 || 0%{?rhel} >=9
    systemctl start foomaticrip-upgrade.service || :
  %endif
fi


%files
%license COPYING LICENSE NOTICE
%doc AUTHORS ABOUT-NLS CHANGES.md CONTRIBUTING.md DEVELOPING.md README.md
%{_bindir}/foomatic-hash
%{_bindir}/foomatic-rip
%attr(0744,root,root) %{_cups_serverbin}/backend/beh
# all backends needs to be run only as root because of kerberos
%attr(0744,root,root) %{_cups_serverbin}/backend/parallel
# Serial backend needs to run as root (bug #212577#c4).
%attr(0744,root,root) %{_cups_serverbin}/backend/serial
%attr(0755,root,root) %{_cups_serverbin}/filter/bannertopdf
%attr(0755,root,root) %{_cups_serverbin}/filter/commandtoescpx
%attr(0755,root,root) %{_cups_serverbin}/filter/commandtopclx
%attr(0755,root,root) %{_cups_serverbin}/filter/foomatic-rip
%attr(0755,root,root) %{_cups_serverbin}/filter/gstopdf
%attr(0755,root,root) %{_cups_serverbin}/filter/gstopxl
%attr(0755,root,root) %{_cups_serverbin}/filter/gstoraster
%attr(0755,root,root) %{_cups_serverbin}/filter/imagetopdf
%attr(0755,root,root) %{_cups_serverbin}/filter/imagetops
%attr(0755,root,root) %{_cups_serverbin}/filter/imagetoraster
# 2229776 - Add textonly driver back, but as lftocrlf
%attr(0755,root,root) %{_cups_serverbin}/filter/lftocrlf
%attr(0755,root,root) %{_cups_serverbin}/filter/pclmtoraster
%attr(0755,root,root) %{_cups_serverbin}/filter/pdftopdf
%attr(0755,root,root) %{_cups_serverbin}/filter/pdftops
%attr(0755,root,root) %{_cups_serverbin}/filter/pdftoraster
%attr(0755,root,root) %{_cups_serverbin}/filter/pwgtopclm
%attr(0755,root,root) %{_cups_serverbin}/filter/pwgtopdf
%attr(0755,root,root) %{_cups_serverbin}/filter/pwgtoraster
%attr(0755,root,root) %{_cups_serverbin}/filter/rastertoescpx
%attr(0755,root,root) %{_cups_serverbin}/filter/rastertopclx
%attr(0755,root,root) %{_cups_serverbin}/filter/rastertops
%attr(0755,root,root) %{_cups_serverbin}/filter/texttopdf
%attr(0755,root,root) %{_cups_serverbin}/filter/texttops
%attr(0755,root,root) %{_cups_serverbin}/filter/texttotext
%{_datadir}/cups/drv/cupsfilters.drv
%{_datadir}/cups/mime/cupsfilters.types
%{_datadir}/cups/mime/cupsfilters.convs
%{_datadir}/cups/mime/cupsfilters-ghostscript.convs
%{_datadir}/cups/mime/cupsfilters-individual.convs
%{_datadir}/cups/mime/cupsfilters-poppler.convs
%dir %{_datadir}/foomatic
%dir %{_datadir}/foomatic/hashes.d
%{_datadir}/ppd/cupsfilters
%if %{with cups_ppdc}
# escp.h and pcl.h are required during runtime, because
# CUPS PPD compiler (ppdc) uses them for generating drivers
# per request from cupsfilters.drv file
%{_datadir}/cups/ppdc/escp.h
%{_datadir}/cups/ppdc/pcl.h
%else
%dir %{_datadir}/ppdc
%{_datadir}/ppdc/escp.h
%{_datadir}/ppdc/pcl.h
%endif
%{_mandir}/man1/foomatic-hash.1.gz
%{_mandir}/man1/foomatic-rip.1.gz
%config(noreplace) %{_sysconfdir}/foomatic
%if 0%{?fedora} >= 43 || 0%{?rhel} >=9
%dir %{_libexecdir}/%{name}
%attr(0744,root,root) %{_libexecdir}/%{name}/posttrans.sh
%ghost %attr(0644,root,root) %{_sysconfdir}/foomatic/hashes.d/hashes.new
%dir %{_unitdir}/cups.service.d
%{_unitdir}/cups.service.d/10-foomaticrip-upgrade.conf
%{_unitdir}/foomaticrip-upgrade.service
%endif

%files driverless
%license COPYING LICENSE NOTICE
%{_bindir}/driverless
%{_bindir}/driverless-fax
%{_cups_serverbin}/backend/driverless
%{_cups_serverbin}/backend/driverless-fax
%{_cups_serverbin}/driver/driverless
%{_cups_serverbin}/driver/driverless-fax
%{_mandir}/man1/driverless.1.gz


%changelog
* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 2.0.1-15
- Prepare for Oreon 11 (RP1)
