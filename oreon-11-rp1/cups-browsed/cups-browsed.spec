%global _cups_serverbin %{_prefix}/lib/cups

%if 0%{?fedora}
%bcond_without mdns
%else
%bcond_with mdns
%endif


Name: cups-browsed
Epoch: 1
Version: 2.1.1
Release: 7%{?dist}
Summary: Daemon for local auto-installation of remote printers
# the CUPS exception text is the same as LLVM exception, so using that name with
# agreement from legal team
# https://lists.fedoraproject.org/archives/list/legal@lists.fedoraproject.org/message/A7GFSD6M3GYGSI32L2FC5KB22DUAEQI3/
License: Apache-2.0 WITH LLVM-exception
URL: https://github.com/OpenPrinting/cups-browsed
Source0:        https://github.com/OpenPrinting/cups-browsed/releases/download/2.1.1/cups-browsed-2.1.1.tar.gz


# Patches
# https://github.com/OpenPrinting/cups-browsed/pull/50
Patch01: 0001-Add-BrowseOptionsUpdate-configuration-directive-50.patch
# oreon url source checksums begin
%global source0_sha256 bc9ed54ef6940a6ee076f8627458fbc3cfed9b2f7bf4ef6e865be7644a51ce8f
%global source0_file cups-browsed-2.1.1.tar.gz
# oreon url source checksums end


# remove once CentOS Stream 10 is released, cups-browsed
# was shipped in cups-filters before 2.0
Conflicts: cups-filters < 2.0

# for generating configure and Makefile scripts in autogen.h
BuildRequires: autoconf
# for generating configure and Makefile scripts in autogen.h
BuildRequires: automake
# most filter functions written in C
BuildRequires: gcc
# for generating configure and Makefile scripts in autogen.h
BuildRequires: gettext-devel
# for autosetup
BuildRequires: git-core
# for generating configure and Makefile scripts in autogen.h
BuildRequires: libtool
# uses Makefiles
BuildRequires: make
# for pkg-config in configure and in SPEC file
BuildRequires: pkgconf-pkg-config
# for looking for devices on mDNS and their sharing on mDNS
BuildRequires: pkgconfig(avahi-client)
# for polling avahi
BuildRequires: pkgconfig(avahi-glib)
# uses CUPS and IPP API
BuildRequires: pkgconfig(cups) >= 2.2.2
# uses cupsfilters API
BuildRequires: pkgconfig(libcupsfilters) >= 2.0b3
# implicitclass uses libppd
BuildRequires: pkgconfig(libppd) >= 2.0b3
# for dBUS proxy from GLib
BuildRequires: pkgconfig(glib-2.0)
# needed for systemd rpm macros in scriptlets
BuildRequires: systemd-rpm-macros

%if %{with mdns}
# Avahi has to run for mDNS support
Recommends: avahi
# if set to browse or share mDNS, we need a resolver
Recommends: nss-mdns
%endif
# only recommends cups RPM in case someone wants to use CUPS container/SNAP
# - cups-browsed has to have a cupsd daemon to send requests to
# using a weak dep will work for bootstraping as well in case the old cups-filters
# 1.x, which is CUPS dependency, will be in repos when cups-browsed
Recommends: cups

# requires cups directories
Requires: cups-filesystem

Requires(post): systemd
Requires(preun): systemd
Requires(postun): systemd


%description
cups-browsed is a helper daemon, which automatically installs printers
locally, provides load balancing and clustering of print queues.
The daemon installs the printers based on found mDNS records and CUPS
broadcast, or by polling a remote print server.


%prep
# oreon verify url source checksums begin
%(f=%{_sourcedir}/cups-browsed-2.1.1.tar.gz; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "bc9ed54ef6940a6ee076f8627458fbc3cfed9b2f7bf4ef6e865be7644a51ce8f" || { echo "oreon: Source0 SHA256 mismatch for cups-browsed-2.1.1.tar.gz" >&2; exit 1; })
# oreon verify url source checksums end
%autosetup -S git


%build
# generate configuration/compilation files
./autogen.sh

# --enable-auto-setup-driverless-only - enable autoinstalling of driverless IPP
# destinations
# --disable-saving-created-queues - don't save the queues during shutdown
# --disable-frequent-netif-update - don't update network interfaces after
# every found printer, update only on NM dBUS event
# --with-browseremoteprotocols - which protocols to use for looking for printers, default DNSSD and CUPS
# --with-remote-cups-local-queue-naming - use the name from remote server
# if polling the server for printers via BrowsePoll
%configure --enable-auto-setup-driverless-only\
  --disable-rpath\
  --disable-saving-created-queues\
  --disable-frequent-netif-update\
  --with-browseremoteprotocols=none\
  --with-remote-cups-local-queue-naming=RemoteName\
  --without-rcdir

%make_build


%install
%make_install

# systemd unit file
mkdir -p %{buildroot}%{_unitdir}
install -p -m 644 daemon/cups-browsed.service %{buildroot}%{_unitdir}

# remove INSTALL file
rm -f %{buildroot}%{_pkgdocdir}/INSTALL

# provided by cups-browsed dependency
rm -f %{buildroot}%{_pkgdocdir}/CHANGES-1.x.md

# license related files are already under /usr/share/licenses
rm -f %{buildroot}%{_pkgdocdir}/{LICENSE,COPYING,NOTICE}


%post
%systemd_post cups-browsed.service

# put UpdateCUPSQueuesMaxPerCall and PauseBetweenCUPSQueueUpdates into cups-browsed.conf
# for making cups-browsed work more stable for environments with many print queues
# TODO make this configurable during build
for directive in "UpdateCUPSQueuesMaxPerCall" "PauseBetweenCUPSQueueUpdates"
do
    found=`%{_bindir}/grep "^[[:blank:]]*$directive" %{_sysconfdir}/cups/cups-browsed.conf`
    if [ -z "$found" ]
    then
        if [ "x$directive" == "xUpdateCUPSQueuesMaxPerCall" ]
        then
            %{_bindir}/echo "UpdateCUPSQueuesMaxPerCall 20" >> %{_sysconfdir}/cups/cups-browsed.conf
        else
            %{_bindir}/echo "PauseBetweenCUPSQueueUpdates 5" >> %{_sysconfdir}/cups/cups-browsed.conf
        fi
    fi
done

# Set BrowseRemoteProtocols to none in light of CVE-2024-47176 when upgrading
if [ $1 -gt 1 ]
then
  if ! grep -Fxq "# added by post scriptlet" %{_sysconfdir}/cups/cups-browsed.conf && ! grep -iq "^\s*BrowseRemoteProtocols none" %{_sysconfdir}/cups/cups-browsed.conf
  then
    cp %{_sysconfdir}/cups/cups-browsed.conf %{_sysconfdir}/cups/cups-browsed.conf.rpmsave
    sed -i "s/^\s*BrowseRemoteProtocols.*/# added by post scriptlet\nBrowseRemoteProtocols none/" %{_sysconfdir}/cups/cups-browsed.conf
  fi
fi

%preun
%systemd_preun cups-browsed.service

%postun
%systemd_postun_with_restart cups-browsed.service

# remove once F41 is EOL
%posttrans
if ls -lah /var/cache/cups/cups-browsed* &> /dev/null
then
  BROWSED_ACTIVE="0"
  CUPSD_ACTIVE="0"

  if systemctl is-active cups-browsed &> /dev/null
  then
    BROWSED_ACTIVE="1"
    CUPSD_ACTIVE="1"
  elif systemctl is-active cups &> /dev/null
  then
    CUPSD_ACTIVE="1"
  fi

  if test "x$CUPSD_ACTIVE" = "x1"
  then
    systemctl stop cups
  fi
  
  # RHEL-46785 - clean up recorded options to make the fix work
  rm -rf /var/cache/cups/*.data /var/cache/cups/cups-browsed* &> /dev/null
  
  if test "x$BROWSED_ACTIVE" = "x1"
  then
    systemctl start cups-browsed
  elif test "x$CUPSD_ACTIVE" = "x1"
  then
    systemctl start cups
  fi
fi


%files
%license COPYING LICENSE NOTICE
%doc ABOUT-NLS AUTHORS CHANGES.md CONTRIBUTING.md DEVELOPING.md README.md
# implicitclass backend must be run as root
# https://github.com/OpenPrinting/cups-filters/issues/183#issuecomment-570196216
%attr(0744,root,root) %{_cups_serverbin}/backend/implicitclass
# 2123809 - rpm -Va reports changes due %%post scriptlet (remove the verify part once we remove
# cups-browsed.conf update from %%post scriptlet)
%config(noreplace) %verify(not size filedigest mtime) %{_sysconfdir}/cups/cups-browsed.conf
%{_mandir}/man5/cups-browsed.conf.5.gz
%{_mandir}/man8/cups-browsed.8.gz
%{_sbindir}/cups-browsed
%{_unitdir}/cups-browsed.service


%changelog
* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 2.1.1-7
- Prepare for Oreon 11 (RP1)
