%global source0_hash bc9ed54ef6940a6ee076f8627458fbc3cfed9b2f7bf4ef6e865be7644a51ce8f
%global _cups_serverbin %{_prefix}/lib/cups
%bcond_with mdns
Name: cups-browsed
Epoch: 1
Version: 2.1.1
Release:        1%{?dist}
Summary:        Daemon for local auto-installation of remote printers
License: Apache-2.0 WITH LLVM-exception
URL: https://github.com/OpenPrinting/cups-browsed
Source0:        https://github.com/OpenPrinting/cups-browsed/releases/download/2.1.1/cups-browsed-2.1.1.tar.gz
Patch01: 0001-Add-BrowseOptionsUpdate-configuration-directive-50.patch
Conflicts: cups-filters < 2.0
%if %{with mdns}
Recommends: avahi
Recommends: nss-mdns
%endif
Recommends: cups
Requires: cups-filesystem
Requires(post): systemd
Requires(preun): systemd
Requires(postun): systemd
# oreon:deps
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  gcc
BuildRequires:  gettext-devel
BuildRequires:  git-core
BuildRequires:  libtool
BuildRequires:  make
BuildRequires:  pkgconf-pkg-config
BuildRequires:  pkgconfig(avahi-client)
BuildRequires:  pkgconfig(avahi-glib)
BuildRequires:  pkgconfig(cups)
BuildRequires:  pkgconfig(glib-2.0)
BuildRequires:  pkgconfig(libcupsfilters)
BuildRequires:  pkgconfig(libppd)
BuildRequires:  systemd-rpm-macros
# /oreon:deps
%description
cups-browsed is a helper daemon, which automatically installs printers
locally, provides load balancing and clustering of print queues.
The daemon installs the printers based on found mDNS records and CUPS
broadcast, or by polling a remote print server.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%oreon_prep
%build

./autogen.sh
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
mkdir -p %{buildroot}%{_unitdir}
install -p -m 644 daemon/cups-browsed.service %{buildroot}%{_unitdir}
rm -f %{buildroot}%{_pkgdocdir}/INSTALL
rm -f %{buildroot}%{_pkgdocdir}/CHANGES-1.x.md
rm -f %{buildroot}%{_pkgdocdir}/{LICENSE,COPYING,NOTICE}
%oreon_autofiles main

%post

%systemd_post cups-browsed.service
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
  rm -rf /var/cache/cups/*.data /var/cache/cups/cups-browsed* &> /dev/null
  if test "x$BROWSED_ACTIVE" = "x1"
  then
    systemctl start cups-browsed
  elif test "x$CUPSD_ACTIVE" = "x1"
  then
    systemctl start cups
  fi
fi
%files -f %{oreon_filedir}/main.list

%changelog

* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 2.1.1-7
- Prepare for Oreon 11 (RP1)
