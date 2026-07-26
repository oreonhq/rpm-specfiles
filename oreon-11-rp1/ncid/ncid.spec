%global source0_hash cecbcae37ed110019ca617a81bfaaab9e0c89018a25b65078a306dd8227c0d90

Name:       ncid
Version:    1.18
Release:    5%{?dist}
Summary:    Network Caller ID server, client and gateways
Requires:   logrotate
# Automatically converted from old format: GPLv3+ - review is highly recommended.
License:    GPL-3.0-or-later
Url:        http://ncid.sourceforge.net
Source0:    https://sourceforge.net/projects/ncid/files/%{name}/%{version}/%{name}-%{version}-src.tar.gz

# https://fedoraproject.org/wiki/Changes/EncourageI686LeafRemoval
%if !%{defined fc40} && !%{defined fc41}
ExcludeArch:   %{ix86}
%endif

BuildRequires: make, gcc, gcc-c++
BuildRequires: libpcap-devel, pcre2-devel, libappstream-glib
BuildRequires: libphonenumber-devel, libicu-devel, protobuf-devel hidapi-devel
BuildRequires: perl-generators, perl-podlators
%{?systemd_requires}
BuildRequires: systemd

# Disable debuginfo, a stripped upstream binary is packaged.
%global debug_package %{nil}

%description
NCID is Caller ID (CID) distributed over a network to a variety of
devices and computers.  NCID includes a server, gateways, a client,
client output modules and command line tools.

The NCID server obtains the Caller ID information from a modem,
a serial or USB device and from gateways: NCID, OBI, SIP, WC, YAC and XDMF.

This package contains the server and command line tools.
The gateways are in the ncid-gateways package.
The client and default modules are in the ncid-client package.

%package gateways
Summary:    NCID (Network Caller ID) gateways
Requires:   libpcap%{?_isa} >= 1.5.0, nc, hidapi

%description gateways
NCID is Caller ID (CID) distributed over a network to a variety of
devices and computers.  NCID includes a server, gateways, a client,
client output modules and command line tools.

This package contains the NCID gateways.

%package client
Summary:    NCID (Network Caller ID) client
BuildArch:  noarch
Requires:   tcl, tk >= 8.6.8, mailx, nmap-ncat, bwidget, python3, python3-phonenumbers

%description client
The NCID client obtains the Caller ID from the NCID server and normally
displays it in a GUI window.  It can also display the Called ID in a
terminal window or, using an output module, format the output and send it
to another program.

This package contains the NCID client and output modules that are not
separate packages.

%package kpopup
Summary:    NCID kpopup module displays Caller ID info in a KDE window
BuildArch:  noarch
Requires:   %{name}-client = %{version}-%{release}
Requires:   %{name}-speak = %{version}-%{release}
Requires:   kde-baseapps, kmix

%description kpopup
The NCID kpopup module displays Caller ID information in a KDE pop-up window
and optionally speaks the number via voice synthesis.  The KDE or Gnome
desktop must be running.

%package mysql
Summary:    NCID mysql module inputs Caller ID information into a SQL database
BuildArch:  noarch
Requires:   %{name}-client = %{version}-%{release}, mysql

%description mysql
The NCID mysql module inputs NCID Caller information into a SQL database
using either MariaDB or a MySQL database.

%package mythtv
Summary:    NCID mythtv module sends Caller ID information to MythTV
BuildArch:  noarch
Requires:   %{name}-client = %{version}-%{release}
Recommends: mythtv-frontend

%description mythtv
The NCID MythTV module displays Caller ID information using mythutil

%package samba
Summary:    NCID samba module sends Caller ID information to windows machines
BuildArch:  noarch
Requires:   %{name}-client = %{version}-%{release}, samba-client

%description samba
The NCID samba module sends Caller ID information to a windows machine
as a pop-up.  This will not work if the messenger service is disabled.

%package speak
Summary:    NCID speak module speaks Caller ID information via voice synthesis
BuildArch:  noarch
Requires:   %{name}-client = %{version}-%{release}, festival

%description speak
The NCID speak module announces Caller Id information verbally, using
the Festival text-to-speech voice synthesis system.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n %{name}

%build
make %{?_smp_mflags} EXTRA_CFLAGS="$RPM_OPT_FLAGS" libdir libcdir
make %{?_smp_mflags} EXTRA_CFLAGS="$RPM_OPT_FLAGS" \
     LOCKFILE=/var/lock/lockdev/LCK.. \
     TTYPORT=/dev/ttyACM0 \
     STRIP= prefix=%{_prefix} prefix2= prefix3= package systemddir

%install
make install-fedora prefix=%{buildroot}/%{_prefix} \
                            prefix2=%{buildroot} \
                            prefix3=%{buildroot}
# uncomment if building a debuginfo package
# rm -f %{buildroot}/etc/ncid/*.conf.new

%check
appstream-util validate-relax --nonet %{buildroot}%{_metainfodir}/ncid.metainfo.xml

%files
%defattr(-,root,root)
%doc README VERSION doc/README-docdir
%doc doc/NCID-UserManual.md doc/NCID-API.md doc/ReleaseNotes.md doc/images
%doc man/README-mandir Fedora/README-Fedora server/README-server
%doc attic/README-attic extensions/README-extensions logrotate/README-logrotate
%doc tools/README-tools lib/README-lib udev/README-udev
%license doc/GPL.md
%{_docdir}/ncid/recordings/README-recordings
%{_docdir}/ncid/recordings/*.pvf
%{_bindir}/cidcall
%{_bindir}/cidalias
%{_bindir}/cidupdate
%{_bindir}/ncid-setup
%{_bindir}/ncidutil
%{_bindir}/ncidnumberinfo
%{_bindir}/update-cidcall
%{_prefix}/sbin/ncidd
%dir %{_libdir}/ncid
%dir %{_datadir}/ncid
%dir %{_datadir}/ncid/sys
%dir %{_datadir}/ncid/recordings
%dir %{_datadir}/ncid/extensions
%dir %{_datadir}/ncid/plugins
%{_libdir}/ncid/libcarrier.so.8.12
%{_libdir}/ncid/libcarrier.so.8
%{_libdir}/ncid/libcarrier.so
%{_datadir}/ncid/sys/ncidrotate
%{_datadir}/ncid/sys/get-areacodes-list
%{_datadir}/ncid/sys/get-fcc-list
%{_datadir}/ncid/sys/ncid-yearlog
%{_datadir}/ncid/sys/udev-action
%{_datadir}/ncid/sys/udev-name
%{_datadir}/ncid/recordings/Callback.rmd
%{_datadir}/ncid/recordings/CallingDeposit.rmd
%{_datadir}/ncid/recordings/CannotBeCompleted.rmd
%{_datadir}/ncid/recordings/DidNotGoThrough.rmd
%{_datadir}/ncid/recordings/DisconnectedNotInService.rmd
%{_datadir}/ncid/recordings/NotInService.rmd
%{_datadir}/ncid/extensions/hangup-calls
%{_datadir}/ncid/extensions/hangup-closed-skel
%{_datadir}/ncid/extensions/hangup-combo
%{_datadir}/ncid/extensions/hangup-fakenum
%{_datadir}/ncid/extensions/hangup-fcc
%{_datadir}/ncid/extensions/hangup-greylist
%{_datadir}/ncid/extensions/hangup-message-skel
%{_datadir}/ncid/extensions/hangup-nohangup
%{_datadir}/ncid/extensions/hangup-skel
%{_datadir}/ncid/extensions/hangup-postal-code
%{_datadir}/ncid/plugins/message_dialog
%{_datadir}/ncid/plugins/us_number_info
%{_datadir}/ncid/plugins/display_ncid_variables
%dir %{_sysconfdir}/ncid
%config(noreplace) %{_sysconfdir}/ncid/hangup-combo.conf
%config(noreplace) %{_sysconfdir}/ncid/postal-codes
%config(noreplace) %{_sysconfdir}/ncid/ncidd.blacklist
%config(noreplace) %{_sysconfdir}/ncid/ncidd.whitelist
%config(noreplace) %{_sysconfdir}/ncid/modem2.conf
%config(noreplace) %{_sysconfdir}/ncid/modem3.conf
%config(noreplace) %{_sysconfdir}/ncid/modem4.conf
%config(noreplace) %{_sysconfdir}/ncid/modem5.conf
%config(noreplace) %{_sysconfdir}/ncid/ncidd.conf
%config(noreplace) %{_sysconfdir}/ncid/ncidd.alias
%config(noreplace) %{_sysconfdir}/ncid/ncidrotate.conf
%config(noreplace) %{_sysconfdir}/ncid/rotatebysize.conf
%config(noreplace) %{_sysconfdir}/logrotate.d/ncid
%{_unitdir}/ncidd.service
%{_usr}/lib/udev/rules.d/*.rules
%{_mandir}/man1/cidalias.1*
%{_mandir}/man1/cidcall.1*
%{_mandir}/man1/cidupdate.1*
%{_mandir}/man1/ncidnumberinfo.1*
%{_mandir}/man1/update-cidcall.1*
%{_mandir}/man1/get-areacodes-list.1*
%{_mandir}/man1/get-fcc-list.1*
%{_mandir}/man1/hangup-calls.1*
%{_mandir}/man1/hangup-closed-skel.1*
%{_mandir}/man1/hangup-combo.1*
%{_mandir}/man1/hangup-fakenum.1*
%{_mandir}/man1/hangup-fcc.1*
%{_mandir}/man1/hangup-greylist.1*
%{_mandir}/man1/hangup-message-skel.1*
%{_mandir}/man1/hangup-nohangup.1*
%{_mandir}/man1/hangup-postal-code.1*
%{_mandir}/man1/hangup-skel.1*
%{_mandir}/man1/ncid-setup.1*
%{_mandir}/man1/ncid-yearlog.1*
%{_mandir}/man1/ncidutil.1*
%{_mandir}/man1/ncidrotate.1*
%{_mandir}/man5/ncidd.alias.5*
%{_mandir}/man5/ncidd.conf.5*
%{_mandir}/man5/ncidd.greylist.5*
%{_mandir}/man5/ncidd.blacklist.5*
%{_mandir}/man5/ncidd.whitelist.5*
%{_mandir}/man5/ncidrotate.conf.5*
%{_mandir}/man5/rotatebysize.conf.5*
%{_mandir}/man7/ncid_extensions.7*
%{_mandir}/man7/ncid_modems.7*
%{_mandir}/man7/ncid_plugins.7*
%{_mandir}/man7/ncid_recordings.7*
%{_mandir}/man7/ncid_tools.7*
%{_mandir}/man8/ncidd.8*

%files gateways
%defattr(-,root,root)
%doc README VERSION doc/GPL.md gateway/README-gateways
%{_prefix}/sbin/artech2ncid
%{_prefix}/sbin/cideasy2ncid
%{_bindir}/email2ncid
%{_bindir}/ncid2ncid
%{_bindir}/obi2ncid
%{_bindir}/rn2ncid
%{_bindir}/wc2ncid
%{_bindir}/wct
%{_bindir}/xdmf2ncid
%{_bindir}/yac2ncid
%{_prefix}/sbin/sip2ncid
%dir %{_datadir}/ncid/setup
%{_datadir}/ncid/setup/ncid-email2ncid-setup
%config(noreplace) %{_sysconfdir}/ncid/artech2ncid.conf
%config(noreplace) %{_sysconfdir}/ncid/cideasy2ncid.conf
%config(noreplace) %{_sysconfdir}/ncid/email2ncid.conf
%config(noreplace) %{_sysconfdir}/ncid/ncid2ncid.conf
%config(noreplace) %{_sysconfdir}/ncid/obi2ncid.conf
%config(noreplace) %{_sysconfdir}/ncid/rn2ncid.conf
%config(noreplace) %{_sysconfdir}/ncid/sip2ncid.conf
%config(noreplace) %{_sysconfdir}/ncid/wc2ncid.conf
%config(noreplace) %{_sysconfdir}/ncid/xdmf2ncid.conf
%config(noreplace) %{_sysconfdir}/ncid/yac2ncid.conf
%{_unitdir}/artech2ncid.service
%{_unitdir}/cideasy2ncid.service
%{_unitdir}/ncid2ncid.service
%{_unitdir}/obi2ncid.service
%{_unitdir}/rn2ncid.service
%{_unitdir}/sip2ncid.service
%{_unitdir}/wc2ncid.service
%{_unitdir}/xdmf2ncid.service
%{_unitdir}/yac2ncid.service
%{_mandir}/man1/artech2ncid.1*
%{_mandir}/man1/cideasy2ncid.1*
%{_mandir}/man1/email2ncid.1*
%{_mandir}/man1/ncid2ncid.1*
%{_mandir}/man1/obi2ncid.1*
%{_mandir}/man1/rn2ncid.1*
%{_mandir}/man1/wc2ncid.1*
%{_mandir}/man1/wct.1*
%{_mandir}/man1/xdmf2ncid.1*
%{_mandir}/man1/yac2ncid.1*
%{_mandir}/man1/ncid-email2ncid-setup.1*
%{_mandir}/man5/artech2ncid.conf.5*
%{_mandir}/man5/cideasy2ncid.conf.5*
%{_mandir}/man5/email2ncid.conf.5*
%{_mandir}/man5/ncid2ncid.conf.5*
%{_mandir}/man5/obi2ncid.conf.5*
%{_mandir}/man5/rn2ncid.conf.5*
%{_mandir}/man5/sip2ncid.conf.5*
%{_mandir}/man5/wc2ncid.conf.5*
%{_mandir}/man5/xdmf2ncid.conf.5*
%{_mandir}/man5/yac2ncid.conf.5*
%{_mandir}/man7/ncid_gateways.7*
%{_mandir}/man8/sip2ncid.8*

%files client
%defattr(-,root,root)
%doc README VERSION client/README-client modules/README-modules
%doc icons/README-icons locales/README-locales
%doc doc/GPL.md doc/README-docdir desktop/README-desktop
%{_bindir}/ncid
%{_bindir}/phonetz
%dir %{_datadir}/ncid
%dir %{_datadir}/ncid/modules
%dir %{_datadir}/ncid/images
%dir %{_datadir}/ncid/msgs
%{_datadir}/ncid/lib
%{_datadir}/ncid/icons/flags
%{_datadir}/ncid/icons/phones
%{_datadir}/ncid/modules/ncid-alert
%{_datadir}/ncid/modules/ncid-initmodem
%{_datadir}/ncid/modules/ncid-notify
%{_datadir}/ncid/modules/ncid-page
%{_datadir}/ncid/modules/ncid-skel
%{_datadir}/ncid/modules/ncid-wakeup
%{_datadir}/ncid/modules/ncid-yac
%{_datadir}/ncid/images/logo.png
%{_datadir}/ncid/msgs/de_de.msg
%{_datadir}/ncid/msgs/fr_fr.msg
%{_datadir}/ncid/msgs/ja_jp.msg
%{_datadir}/applications/ncid.desktop
%{_metainfodir}/ncid.metainfo.xml
%{_datadir}/icons/hicolor/128x128/apps/ncid.png
%{_datadir}/icons/hicolor/96x96/apps/ncid.png
%{_datadir}/icons/hicolor/72x72/apps/ncid.png
%{_datadir}/icons/hicolor/64x64/apps/ncid.png
%{_datadir}/icons/hicolor/48x48/apps/ncid.png
%{_datadir}/icons/hicolor/32x32/apps/ncid.png
%{_datadir}/icons/hicolor/24x24/apps/ncid.png
%{_datadir}/icons/hicolor/22x22/apps/ncid.png
%{_datadir}/icons/hicolor/16x16/apps/ncid.png
%dir %{_sysconfdir}/ncid
%dir %{_sysconfdir}/ncid/conf.d
%config(noreplace) %{_sysconfdir}/ncid/ncid.conf
%config(noreplace) %{_sysconfdir}/ncid/conf.d/ncid-alert.conf
%config(noreplace) %{_sysconfdir}/ncid/conf.d/ncid-notify.conf
%config(noreplace) %{_sysconfdir}/ncid/conf.d/ncid-page.conf
%config(noreplace) %{_sysconfdir}/ncid/conf.d/ncid-skel.conf
%config(noreplace) %{_sysconfdir}/ncid/conf.d/ncid-yac.conf
%{_unitdir}/ncid-initmodem.service
%{_unitdir}/ncid-notify.service
%{_unitdir}/ncid-page.service
%{_unitdir}/ncid-yac.service
%{_mandir}/man1/phonetz.1*
%{_mandir}/man1/ncid.1*
%{_mandir}/man1/ncid-alert.1*
%{_mandir}/man1/ncid-initmodem.1*
%{_mandir}/man1/ncid-notify.1*
%{_mandir}/man1/ncid-page.1*
%{_mandir}/man1/ncid-skel.1*
%{_mandir}/man1/ncid-wakeup.1*
%{_mandir}/man1/ncid-yac.1*
%{_mandir}/man5/ncid.conf.5*
%{_mandir}/man7/ncid_modules.7*

%files kpopup
%defattr(-,root,root)
%doc VERSION modules/README-modules
%{_datadir}/ncid/modules/ncid-kpopup
%config(noreplace) %{_sysconfdir}/ncid/conf.d/ncid-kpopup.conf
%{_mandir}/man1/ncid-kpopup.1*

%files mysql
%defattr(-,root,root)
%doc VERSION modules/README-modules setup/README-setup
%{_datadir}/ncid/modules/ncid-mysql
%{_datadir}/ncid/setup/ncid-mysql-setup
%config(noreplace) %{_sysconfdir}/ncid/conf.d/ncid-mysql.conf
%{_unitdir}/ncid-mysql.service
%{_mandir}/man1/ncid-mysql.1*
%{_mandir}/man8/ncid-mysql-setup.8*

%files mythtv
%defattr(-,root,root)
%doc VERSION modules/README-modules
%{_datadir}/ncid/modules/ncid-mythtv
%config(noreplace) %{_sysconfdir}/ncid/conf.d/ncid-mythtv.conf
%{_unitdir}/ncid-mythtv.service
%{_mandir}/man1/ncid-mythtv.1*

%files samba
%defattr(-,root,root)
%doc VERSION modules/README-modules
%{_datadir}/ncid/modules/ncid-samba
%config(noreplace) %{_sysconfdir}/ncid/conf.d/ncid-samba.conf
%{_unitdir}/ncid-samba.service
%{_mandir}/man1/ncid-samba.1*

%files speak
%defattr(-,root,root)
%doc VERSION modules/README-modules
%{_datadir}/ncid/modules/ncid-speak
%config(noreplace) %{_sysconfdir}/ncid/conf.d/ncid-speak.conf
%{_unitdir}/ncid-speak.service
%{_mandir}/man1/ncid-speak.1*

%post
%systemd_post ncidd.service

%post gateways
%systemd_post artech2ncid.service cideasy2ncid ncid2ncid.service obi2ncid.service rn2ncid.service sip2ncid.service wc2ncid.service xdmf2ncid.service yac2ncid.service

%post client
%systemd_post ncid-initmodem.service ncid-notify.service ncid-page.service ncid-yac.service

%post mythtv
%systemd_post ncid-mythtv.service

%post mysql
%systemd_post ncid-mysql.service

%post samba
%systemd_post ncid-samba.service

%post speak
%systemd_post ncid-speak.service

%preun
%systemd_preun ncidd.service ncid2ncid.service sip2ncid.service yac2ncid.service obi2ncid.service rn2ncid.service wc2ncid.service

%preun client
# stop all modules even from other packages
%systemd_preun ncid-alert ncid-initmodem.service ncid-mysql.service ncid-mythtv.service ncid-notify.service ncid-page.service ncid-samba.service ncid-speak.service ncid-yac.service
# stop ncid GUI client and any user started modules
if [ $1 -eq 0 ] ; then
    pkill -f 'wish.*ncid ' || true
    pkill -f 'tclsh.*ncid-' || true
fi

%preun mysql
%systemd_preun ncid-mysql.service

%preun mythtv
%systemd_preun ncid-mythtv.service

%preun samba
%systemd_preun ncid-samba.service

%preun speak
%systemd_preun ncid-speak.service

%postun
if [ $1 -ne 0 ]; then
    ### upgrade package ###
    # move any user recordings to recordings directory
    for RECORDING in %{_datadir}/ncid/*.rmd
    do
        test -f $RECORDING && mv $RECORDING %{_datadir}/ncid/recordings || :
    done

    gtk-update-icon-cache /usr/share/icons/hicolor &>/dev/null || :
fi
%systemd_postun_with_restart ncidd.service

%postun gateways
%systemd_postun_with_restart ncid2ncid.service obi2ncid.service rn2ncid.service sip2ncid.service wc2ncid.service xdmf2ncid.service yac2ncid.service

%postun client
if [ $1 -ge 1 ]; then ### upgrade package ###
    # move any modules found to the modules directory
    for MODULE in %{_datadir}/ncid/ncid-*
    do
        test -f $MODULE && mv $MODULE %{_datadir}/ncid/modules
    done
fi
# a module service could have been installed by another package
%systemd_postun_with_restart %{_datadir}/ncid/modules/ncid-*

%postun mysql
%systemd_postun_with_restart ncid-mysql.service

%postun mythtv
%systemd_postun_with_restart ncid-mythtv.service

%postun samba
%systemd_postun_with_restart ncid-samba.service

%postun speak
%systemd_postun_with_restart ncid-speak.service

%posttrans client
# Icon Cache
touch --no-create %{_datadir}/icons/hicolor &>/dev/null
gtk-update-icon-cache %{_datadir}/icons/hicolor &>/dev/null || :

%changelog
%autochangelog
