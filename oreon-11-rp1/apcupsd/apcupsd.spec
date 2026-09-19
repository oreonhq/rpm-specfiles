%global source0_hash db7748559b6b4c3784f9856561ef6ac6199ef7bd019b3edcd7e0a647bf8f9867

# A change in RPM 4.15 causes the make_build macro to misbuild this package.
# See https://github.com/rpm-software-management/rpm/issues/798
%global _make_verbose %nil

Name:       apcupsd
Version:    3.14.14
Release:    41%{?dist}
Summary:    APC UPS Power Control Daemon

License:    GPL-2.0-only
URL:        http://www.apcupsd.com
Source0:    https://downloads.sourceforge.net/apcupsd/apcupsd-%version.tar.gz
Source1:    apcupsd.service
Source2:    apcupsd_shutdown
Source3:    apcupsd-httpd.conf
Source4:    apcupsd.logrotate
Source5:    apcupsd64x64.png

# fix crash in gui, rhbz#578276
Patch0:       apcupsd-3.14.9-fixgui.patch
# Halt without powering off, rhbz#1442577
Patch1:       apcupsd-3.14.4-shutdown.patch
# Fix format-security error so we can enable the checks
Patch2:       patch-format-security
Patch3:       disable_nologin.patch
# fixes "increasing NUMXFERS" bug:
# https://sourceforge.net/p/apcupsd/mailman/apcupsd-users/thread/ad9afb27-30f9-443f-a9fb-982c41ad1325%40okazoo.eu/
# https://www.reddit.com/r/homelab/comments/1c3eo9n/apcupsd_and_proxmox_frequent_battery_disconnected/
# patch source: https://sourceforge.net/p/apcupsd/mailman/message/58741334/
Patch4:       99-apcupsd-xfer-glitch.patch

BuildRequires: gcc-c++
BuildRequires: glibc-devel, gd-devel
%if %{defined fedora} || (%{defined rhel} && 0%{?rhel} > 9)
BuildRequires: libusb-compat-0.1-devel
%endif
%if (%{defined rhel} && 0%{?rhel} <= 9)
BuildRequires: libusb-devel
%endif
BuildRequires: net-snmp-devel, 
BuildRequires: gtk2-devel, GConf2-devel, desktop-file-utils
# /sbin/shutdown is required to be present when building
# Somehow in F36 systemd is installed in mock but not in koji
BuildRequires: systemd
# This is part of util-linux in Fedora, but on EL7 it's in sysvinit-tools.
BuildRequires: /usr/bin/wall
BuildRequires: make
Requires:      /bin/mail /usr/bin/wall
%{?systemd_requires}

%description
Apcupsd can be used for controlling most APC UPSes. During a
power failure, apcupsd will inform the users about the power
failure and that a shutdown may occur.  If power is not restored,
a system shutdown will follow when the battery is exausted, a
timeout (seconds) expires, or the battery runtime expires based
on internal APC calculations determined by power consumption
rates.  If the power is restored before one of the above shutdown
conditions is met, apcupsd will inform users about this fact.
Some features depend on what UPS model you have (simple or smart).

%package cgi
Summary:      Web interface for apcupsd
Requires:     apcupsd = %version-%release
Requires:     httpd

%description cgi
A CGI interface to the APC UPS monitoring daemon.

%package gui
Summary:      GUI interface for apcupsd
Requires:     apcupsd = %version-%release

%description gui
A GUI interface to the APC UPS monitoring daemon.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1

# Override the provided platform makefile
printf 'install:\n\techo skipped\n' > platforms/redhat/Makefile

%build
%configure \
        --sysconfdir="/etc/apcupsd" \
        --with-cgi-bin="/var/www/apcupsd" \
        --sbindir=%{_bindir} \
        --enable-cgi \
        --enable-pthreads \
        --enable-net \
        --enable-apcsmart \
        --enable-dumb \
        --enable-net-snmp \
        --enable-snmp \
        --enable-usb \
        --enable-modbus-usb \
        --enable-gapcmon \
        --enable-pcnet \
        --with-serial-dev= \
        --with-upstype=usb \
        --with-upscable=usb \
        --with-lock-dir=/var/lock \
        APCUPSD_MAIL=/bin/mail
%make_build

%install
mkdir -p %buildroot/var/www/apcupsd
%make_install
install -m744 platforms/apccontrol \
              %buildroot/etc/apcupsd/apccontrol

install -p -D -m0644 %SOURCE1 %buildroot/lib/systemd/system/apcupsd.service
install -p -D -m0755 %SOURCE2 %buildroot/lib/systemd/system-shutdown/apcupsd_shutdown
install -p -D -m0644 %SOURCE3 %buildroot/etc/httpd/conf.d/apcupsd.conf
install -p -D -m0644 %SOURCE4 %buildroot/etc/logrotate.d/apcupsd
install -p -D -m0644 %SOURCE5 %buildroot/usr/share/pixmaps/apcupsd64x64.png

desktop-file-install \
        --vendor="fedora" \
        --dir=%buildroot/usr/share/applications \
        --set-icon=apcupsd64x64 \
        --delete-original \
        %buildroot/usr/share/applications/gapcmon.desktop

# Cleanup for later %%doc processing
chmod -x examples/*.c
rm examples/*.in

%files
%license COPYING
%doc ChangeLog examples ReleaseNotes
%dir /etc/apcupsd
/lib/systemd/system/apcupsd.service
/lib/systemd/system-shutdown/apcupsd_shutdown
%config(noreplace) /etc/apcupsd/apcupsd.conf
%attr(0755,root,root) /etc/apcupsd/apccontrol
%config(noreplace) /etc/apcupsd/changeme
%config(noreplace) /etc/apcupsd/commfailure
%config(noreplace) /etc/apcupsd/commok
%config(noreplace) /etc/apcupsd/offbattery
%config(noreplace) /etc/apcupsd/onbattery
%config(noreplace) /etc/logrotate.d/apcupsd
/usr/share/hal/fdi/policy/20thirdparty/80-apcupsd-ups-policy.fdi
%{_bindir}/apcaccess
%{_bindir}/apctest
%{_bindir}/apcupsd
%exclude %{_bindir}/smtp

%{_mandir}/*/*

%files cgi
%config(noreplace) /etc/apcupsd/apcupsd.css
%config(noreplace) /etc/httpd/conf.d/apcupsd.conf
%config(noreplace) /etc/apcupsd/hosts.conf
%config(noreplace) /etc/apcupsd/multimon.conf
/var/www/apcupsd/

%files gui
/usr/bin/gapcmon
/usr/share/applications/*gapcmon.desktop
/usr/share/pixmaps/apcupsd.png
/usr/share/pixmaps/apcupsd64x64.png
/usr/share/pixmaps/charging.png
/usr/share/pixmaps/gapc_prefs.png
/usr/share/pixmaps/onbatt.png
/usr/share/pixmaps/online.png
/usr/share/pixmaps/unplugged.png

%post
%systemd_post apcupsd.service

%preun
%systemd_preun apcupsd.service

%postun
%systemd_postun_with_restart apcupsd.service

%changelog
%autochangelog
