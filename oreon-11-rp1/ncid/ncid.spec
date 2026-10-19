%global source0_hash cecbcae37ed110019ca617a81bfaaab9e0c89018a25b65078a306dd8227c0d90
Name:       ncid
Version:    1.18
Release:        1%{?dist}
Summary:        Network Caller ID server, client and gateways
Requires:   logrotate
License:    GPL-3.0-or-later
Url:        http://ncid.sourceforge.net
Source0:        https://sourceforge.net/projects/ncid/files/%{name}/%{version}/%{name}-%{version}-src.tar.gz
%if !%{defined fc40} && !%{defined fc41}
ExcludeArch:   %{ix86}
%endif
%{?systemd_requires}
%global debug_package %{nil}
# oreon:deps
BuildRequires:  gcc
BuildRequires:  gcc-c++
BuildRequires:  hidapi-devel
BuildRequires:  libappstream-glib
BuildRequires:  libicu-devel
BuildRequires:  libpcap-devel
BuildRequires:  libphonenumber-devel
BuildRequires:  make
BuildRequires:  pcre2-devel
BuildRequires:  perl-generators
BuildRequires:  perl-podlators
BuildRequires:  protobuf-devel
BuildRequires:  systemd
# /oreon:deps
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
%global oreon_srcdir %{name}
%oreon_prep
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
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%check

appstream-util validate-relax --nonet %{buildroot}%{_metainfodir}/ncid.metainfo.xml
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

%systemd_preun ncid-alert ncid-initmodem.service ncid-mysql.service ncid-mythtv.service ncid-notify.service ncid-page.service ncid-samba.service ncid-speak.service ncid-yac.service
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
    for MODULE in %{_datadir}/ncid/ncid-*
    do
        test -f $MODULE && mv $MODULE %{_datadir}/ncid/modules
    done
fi
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

touch --no-create %{_datadir}/icons/hicolor &>/dev/null
gtk-update-icon-cache %{_datadir}/icons/hicolor &>/dev/null || :
%files -f %{oreon_filedir}/main.list
%files -n ncid-gateways -f %{oreon_filedir}/ncid-gateways.list
%files -n ncid-client -f %{oreon_filedir}/ncid-client.list
%files -n ncid-kpopup -f %{oreon_filedir}/ncid-kpopup.list
%files -n ncid-mysql -f %{oreon_filedir}/ncid-mysql.list
%files -n ncid-mythtv -f %{oreon_filedir}/ncid-mythtv.list
%files -n ncid-samba -f %{oreon_filedir}/ncid-samba.list
%files -n ncid-speak -f %{oreon_filedir}/ncid-speak.list

%changelog

%autochangelog
