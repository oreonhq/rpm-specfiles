%global source0_hash db7748559b6b4c3784f9856561ef6ac6199ef7bd019b3edcd7e0a647bf8f9867
%global _make_verbose %nil
Name:       apcupsd
Version:    3.14.14
Release:        1%{?dist}
Summary:        APC UPS Power Control Daemon
License:    GPL-2.0-only
URL:        http://www.apcupsd.com
Source0:        https://downloads.sourceforge.net/%{name}/%{name}-%{version}.tar.gz
Source1:    apcupsd.service
Source2:    apcupsd_shutdown
Source3:    apcupsd-httpd.conf
Source4:    apcupsd.logrotate
Source5:    apcupsd64x64.png
Patch0:       apcupsd-3.14.9-fixgui.patch
Patch1:       apcupsd-3.14.4-shutdown.patch
Patch2:       patch-format-security
Patch3:       disable_nologin.patch
Patch4:       99-apcupsd-xfer-glitch.patch
Requires:      /bin/mail /usr/bin/wall
%{?systemd_requires}
# oreon:deps
BuildRequires:  /usr/bin/wall
BuildRequires:  GConf2-devel
BuildRequires:  desktop-file-utils
BuildRequires:  gcc-c++
BuildRequires:  gd-devel
BuildRequires:  glibc-devel
BuildRequires:  gtk2-devel
BuildRequires:  libusb-compat-0.1-devel
BuildRequires:  make
BuildRequires:  net-snmp-devel
BuildRequires:  systemd
# /oreon:deps
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
chmod -x examples/*.c
rm examples/*.in
%oreon_autofiles apcupsd-cgi usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles apcupsd-gui usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%post

%systemd_post apcupsd.service
%preun

%systemd_preun apcupsd.service
%postun

%systemd_postun_with_restart apcupsd.service
%files -f %{oreon_filedir}/main.list
%files -n apcupsd-cgi -f %{oreon_filedir}/apcupsd-cgi.list
%files -n apcupsd-gui -f %{oreon_filedir}/apcupsd-gui.list

%changelog

%autochangelog
