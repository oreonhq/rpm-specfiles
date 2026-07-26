%global source0_hash a2fe55bc2d90b4a848d6ff8bac361e6d1c97f899a545219cad707d17a27ff127

%global _hardened_build 1

#TODO: split nut-client so it does not require python
%global nut_uid 57
%global nut_gid 57

%global cgidir  /var/www/nut-cgi-bin
%global piddir  /run/nut
%global modeldir %{_libexecdir}/%{name}
# powerman is retired on Fedora, therefore disable it by default
%bcond_with powerman

Summary: Network UPS Tools
Name: nut
Version: 2.8.4
Release: 7%{?dist}
License: GPL-2.0-or-later AND GPL-3.0-or-later
Url: https://www.networkupstools.org/
Source: https://www.networkupstools.org/source/2.8/%{name}-%{version}.tar.gz
Source4: libs.sh
Patch2: nut-2.8.0-piddir-owner.patch

#quick fix. TODO: fix it properly
Patch9: nut-2.6.5-rmpidf.patch
Patch15: nut-c99-strdup.patch
Patch16: nut-2.8.3-rhinoname.patch

Requires(post): coreutils systemd
Requires(preun): systemd
Requires(postun): coreutils systemd
Recommends: nut-xml
Requires: group(dialout)
Requires: group(tty)

BuildRequires: asciidoc
BuildRequires: make
BuildRequires: autoconf
BuildRequires: automake
BuildRequires: augeas-libs
BuildRequires: avahi-devel
BuildRequires: cppunit-devel
BuildRequires: dbus-glib-devel
BuildRequires: desktop-file-utils
BuildRequires: elfutils-devel
BuildRequires: fontconfig-devel
BuildRequires: freeipmi-devel
BuildRequires: freetype-devel
BuildRequires: gcc
BuildRequires: gcc-c++
BuildRequires: gd-devel
BuildRequires: jq
%if 0%{?fedora} < 39
BuildRequires: libgpiod-devel
%endif
BuildRequires: libjpeg-devel
BuildRequires: libpng-devel
BuildRequires: libtool
BuildRequires: libtool-ltdl-devel
BuildRequires: libX11-devel
BuildRequires: libXpm-devel
BuildRequires: libmodbus-devel
BuildRequires: libi2c-devel
BuildRequires: neon-devel
BuildRequires: net-snmp-devel
BuildRequires: netpbm-devel
BuildRequires: nss-devel
BuildRequires: openssl-devel
BuildRequires: pkgconfig
%if %{with powerman}
BuildRequires: powerman-devel
%endif
BuildRequires: python3-devel
BuildRequires: python3-setuptools
BuildRequires: systemd-devel
BuildRequires: systemd-rpm-macros

%ifnarch s390 s390x
BuildRequires: libusb1-devel
%endif

ExcludeArch: s390 s390x

%global restart_flag %{piddir}/%{name}-restart-after-rpm-install

%description
These programs are part of a developing project to monitor the assortment
of UPSes that are found out there in the field. Many models have serial
ports of some kind that allow some form of state checking. This
capability has been harnessed where possible to allow for safe shutdowns,
live status tracking on web pages, and more.

%package client
Summary: Network UPS Tools client monitoring utilities
Requires(post): systemd
Requires(preun): systemd
Requires: group(dialout)
Requires: group(tty)

%description client
This package includes the client utilities that are required to monitor a
ups that the client host has access to, but where the UPS is physically
attached to a different computer on the network.

%package cgi
Summary: CGI utilities for the Network UPS Tools
Requires: %{name}-client = %{version}-%{release} webserver

%description cgi
This package includes CGI programs for accessing UPS status via a web
browser.

%package monitor
Summary: Network UPS Tools monitor application
BuildRequires: python3-pyqt6

%description monitor
This package contain the Python NUT-Monitor GUI application to
monitor a UPS.

%package xml
Summary: XML UPS driver for the Network UPS Tools
Requires: %{name}-client = %{version}-%{release}

%description xml
This package adds the netxml-ups driver, that allows NUT to monitor a XML
capable UPS.

%package devel
Summary: Development files for NUT Client
Requires: %{name}-client = %{version}-%{release} webserver openssl-devel

%description devel
This package contains the development header files and libraries
necessary to develop NUT client applications.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q
#patch -P 2 -p1 -b .piddir-owner
%patch -P 9 -p1 -b .rmpidf
#patch -P 15 -p1
%patch -P 16 -p2 -b .rhinoname

sed -i 's|LIBSSL_LDFLAGS|LIBSSL_LIBS|' lib/libupsclient-config.in
sed -i 's|LIBSSL_LDFLAGS|LIBSSL_LIBS|' lib/libupsclient.pc.in

# workaround for multilib conflicts - caused by patch changing modification time of scripts
find . -mtime -1 -print0 | xargs -0 touch --reference %{SOURCE0}

# fix python site packages check
sed -i 's|\(PYTHON3\?_SITE_PACKAGES=\)".*"|\1"%{python3_sitelib}"|' m4/nut_check_python.m4

# Create a sysusers.d config file
cat >nut.sysusers.conf <<EOF
u nut %{nut_uid} 'Network UPS Tools' %{_localstatedir}/lib/ups /bin/false
m nut dialout
m nut tty
EOF

%build
%if 0%{?fedora}
#--without-gpio is not enough to stop it complaining about missing library
sed -i 's|with_gpio="[^"]*"|with_gpio="no"|g' configure.ac
%endif
autoreconf -i
export CXXFLAGS="-std=c++14 $RPM_OPT_FLAGS"
# prevent assignment of default value, it would break configure's tests
export LDFLAGS="-Wl,-z,now"
%configure \
    --with-all \
%if %{without powerman}
    --without-powerman \
%endif
    --with-libltdl \
%if 0%{?el8}
    --with-nss \
%endif
    --without-wrap \
    --with-cgi \
    --with-python=%{python3} \
    --with-python3=%{python3} \
    --without-python2 \
    --datadir=%{_datadir}/%{name} \
    --with-user=%{name} \
    --with-group=dialout \
    --with-statepath=%{piddir} \
    --with-pidpath=%{piddir} \
    --with-altpidpath=%{piddir} \
    --sysconfdir=%{_sysconfdir}/ups \
    --with-cgipath=%{cgidir} \
    --with-drvpath=%{modeldir} \
%if 0%{?fedora}
    --without-gpio \
%endif
    --with-systemdsystemunitdir=%{_unitdir} \
    --with-systemdshutdowndir=/lib/systemd/system-shutdown \
    --with-pkgconfig-dir=%{_libdir}/pkgconfig \
    --disable-static \
    --with-udev-dir=%{_usr}/lib/udev \
    --libdir=%{_libdir} \
    --enable-docs-changelog=no
#    --with-doc # does not work in 2.7.1

# for rhbz#838139 check if still needed?
sh %{SOURCE4} >>include/config.h

#remove rpath
sed -i 's|^hardcode_libdir_flag_spec=.*|hardcode_libdir_flag_spec=""|g' libtool
sed -i 's|^runpath_var=LD_RUN_PATH|runpath_var=DIE_RPATH_DIE|g' libtool
%make_build LDFLAGS="%{__global_ldflags}"

%install
mkdir -p %{buildroot}%{modeldir} \
         %{buildroot}%{_sysconfdir}/udev/rules.d \
         %{buildroot}%{_sysconfdir}/ups \
         %{buildroot}%{piddir} \
         %{buildroot}%{_localstatedir}/lib/ups \
         %{buildroot}%{_libexecdir}

%make_install

#mv %{buildroot}%{_tmpfilesdir}/nut-common.tmpfiles %{buildroot}%{_tmpfilesdir}/nut-common.conf

rm -rf %{buildroot}%{_prefix}/html
rm -f %{buildroot}%{_libdir}/*.la
rm -rf docs/man
rm -rf %{buildroot}%{_datadir}/nut/solaris-init
find docs/ -name 'Makefile*' -delete

pushd conf;
%make_install
for file in %{buildroot}%{_sysconfdir}/ups/*.sample
do
   mv $file %{buildroot}%{_sysconfdir}/ups/`basename $file .sample`
done
popd

#fix collision with virtualbox
#mv %{buildroot}/%{_usr}/lib/udev/rules.d/52-nut-usbups.rules %{buildroot}/%{_usr}/lib/udev/rules.d/62-nut-usbups.rules
mv %{buildroot}/%{_usr}/lib/udev/rules.d/52-nut-ipmipsu.rules %{buildroot}/%{_usr}/lib/udev/rules.d/62-nut-ipmipsu.rules

# fix encoding
for fe in ./docs/cables/powerware.txt
do
  iconv -f iso-8859-1 -t utf-8 <$fe >$fe.new
  touch -r $fe $fe.new
  mv -f $fe.new $fe
done

# rename rhino to nutdrv_rhino to prevent file conflict (rhbz#2367057)
mv %{buildroot}%{_mandir}/man8/rhino.8 %{buildroot}%{_mandir}/man8/nutdrv_rhino.8

# install PyNUT
install -p -D -m 644 scripts/python/module/PyNUT.py %{buildroot}%{python3_sitelib}/PyNUT.py
# add lowercase name
ln %{buildroot}%{_bindir}/{NUT-Monitor,nut-monitor}
# install desktop file
mkdir -p %{buildroot}%{_datadir}/applications
desktop-file-install \
  --dir=%{buildroot}%{_datadir}/applications \
  %{buildroot}%{_datadir}/nut-monitor/app/nut-monitor.desktop
# install icons
for res in 256x256 48x48 64x64 scalable
do
  mkdir -p %{buildroot}%{_datadir}/icons/hicolor/${res}/apps
  ln %{buildroot}%{_datadir}/nut-monitor/app/icons/${res}/nut-monitor.* \
    %{buildroot}%{_datadir}/icons/hicolor/${res}/apps/
done

# Setup permissions for pid file
touch %{buildroot}/%{piddir}/upsmon.pid
chmod 0644 %{buildroot}/%{piddir}/upsmon.pid

install -m0644 -D nut.sysusers.conf %{buildroot}%{_sysusersdir}/nut.conf

%pre
# do not let upsmon run during upgrade rhbz#916472
# phase 1: stop upsmon before upsd changes
if [ "$1" = "2" ]; then
  rm -f %restart_flag
  /bin/systemctl is-active nut-monitor.service >/dev/null 2>&1 && touch %restart_flag || :
  /bin/systemctl stop nut-monitor.service >/dev/null 2>&1 || :
fi

%post
%systemd_post nut-driver-enumerator.path nut-driver-enumerator.service nut-driver.target nut-server.service nut.target

%preun
%systemd_preun nut-driver-enumerator.path nut-driver-enumerator.service nut-driver.target nut-server.service nut.target

%postun
%systemd_postun_with_restart nut-driver.target nut-server.service

%post client
%systemd_post nut-monitor.service nut.target

%preun client
%systemd_preun nut-monitor.service nut.target

%postun client
%systemd_postun_with_restart nut-monitor.service

%posttrans
# phase 2: start upsmon again
if [ -e %restart_flag ]; then
  /bin/systemctl restart nut-monitor.service >/dev/null 2>&1 || :
  rm -f %restart_flag
else
  # maybe we did not stop it - if we reinstalled just nut-client
  /bin/systemctl try-restart nut-monitor.service >/dev/null 2>&1 || :
fi

%files
%license COPYING LICENSE-GPL2 LICENSE-GPL3
%doc ChangeLog AUTHORS MAINTAINERS README docs INSTALL NEWS
%config(noreplace) %attr(640,root,nut) %{_sysconfdir}/ups/ups.conf
%config(noreplace) %attr(640,root,nut) %{_sysconfdir}/ups/upsd.conf
%config(noreplace) %attr(640,root,nut) %{_sysconfdir}/ups/upsd.users
%attr(644,root,root) %{_usr}/lib/udev/rules.d/62-nut-usbups.rules
%attr(644,root,root) %{_usr}/lib/udev/rules.d/62-nut-ipmipsu.rules
%{modeldir}/
# dummy-ups requires libupsclient
%exclude %{modeldir}/dummy-ups
%exclude %{modeldir}/netxml-ups
%{_unitdir}/nut-driver-enumerator.path
%{_unitdir}/nut-driver-enumerator.service
%{_unitdir}/nut-driver-enumerator-daemon-activator.path
%{_unitdir}/nut-driver-enumerator-daemon-activator.service
%{_unitdir}/nut-driver-enumerator-daemon.service
%{_unitdir}/nut-driver@.service
%{_unitdir}/nut-driver.target
%{_unitdir}/nut-server.service
%{_unitdir}/nut.target
%{_presetdir}/nut-systemd.preset
%{_unitdir}/enphase-monitor@.service
%{_unitdir}/nut-logger.service
%{_unitdir}/nut-udev-settle.service
%{_sbindir}/upsd
%{_bindir}/nutconf
%{_bindir}/nut-scanner
%{_sbindir}/upsdrvctl
%{_sbindir}/upsdrvsvcctl
%{_libdir}/libnutscan.so.*
%{_libdir}/libnutconf.so.*
%{_libexecdir}/nut-driver-enumerator.sh
%{_libexecdir}/sockdebug
%{_libexecdir}/enphase-monitor
%{_datadir}/augeas/lenses/dist/nut*
%{_datadir}/augeas/lenses/dist/tests/test_nut.aug
%{_datadir}/%{name}/cmdvartab
%{_datadir}/%{name}/driver.list
%{_mandir}/man5/ups.conf.5.gz
%{_mandir}/man5/upsd.conf.5.gz
%{_mandir}/man5/upsd.users.5.gz

%{_mandir}/man8/nutconf.8.gz

%{_mandir}/man8/adelsystem_cbi.8.gz
%{_mandir}/man8/apc_modbus.8.gz

%{_mandir}/man8/al175.8.gz
%{_mandir}/man8/apcsmart.8.gz
%{_mandir}/man8/apcsmart-old.8.gz
%{_mandir}/man8/apcupsd-ups.8.gz
%{_mandir}/man8/asem.8.gz
%{_mandir}/man8/bcmxcp.8*
%{_mandir}/man8/bcmxcp_usb.8.gz
%{_mandir}/man8/belkin.8.gz
%{_mandir}/man8/bestfcom.8.gz
%{_mandir}/man8/belkinunv.8.gz
%{_mandir}/man8/bestfortress.8.gz
%{_mandir}/man8/bestups.8.gz
%{_mandir}/man8/bestuferrups.8.gz
%{_mandir}/man8/bicker_ser.8.gz
%{_mandir}/man8/blazer_ser.8.gz
%{_mandir}/man8/blazer_usb.8.gz
%{_mandir}/man8/clone.8.gz
%{_mandir}/man8/clone-outlet.8.gz
%{_mandir}/man8/dummy-ups.8.gz
%{_mandir}/man8/everups.8.gz
%{_mandir}/man8/etapro.8.gz
%{_mandir}/man8/failover.8.gz
%{_mandir}/man8/gamatronic.8.gz
%{_mandir}/man8/generic_modbus.8.gz
%{_mandir}/man8/genericups.8.gz
%if 0%{?fedora} < 39
%{_mandir}/man8/generic_gpio.8.gz
%endif
%{_mandir}/man8/hwmon_ina219.8.gz
%{_mandir}/man8/huawei-ups2000.8.gz
%{_mandir}/man8/isbmex.8.gz
%{_mandir}/man8/ivtscd.8.gz
%{_mandir}/man8/liebert.8.gz
%{_mandir}/man8/liebert-esp2.8.gz
%{_mandir}/man8/liebert-gxe.8.gz
%{_mandir}/man8/masterguard.8.gz
%{_mandir}/man8/metasys.8.gz
%{_mandir}/man8/microdowell.8.gz
%{_mandir}/man8/microsol-apc.8.gz
%{_mandir}/man8/mge-utalk.8.gz
%{_mandir}/man8/mge-shut.8.gz
%{_mandir}/man8/nhs_ser.8.gz
%{_mandir}/man8/nutupsdrv.8.gz
%{_mandir}/man8/nutdrv_atcl_usb.8.gz
%{_mandir}/man8/nutdrv_hashx.8.gz
%{_mandir}/man8/nutdrv_siemens_sitop.8.gz
%{_mandir}/man8/nut-driver-enumerator.8.gz
%{_mandir}/man8/nut-ipmipsu.8.gz
%{_mandir}/man8/nut-recorder.8.gz
%{_mandir}/man8/nut-scanner.8.gz
%{_mandir}/man8/nutdrv_qx.8.gz
%{_mandir}/man8/oneac.8.gz
%{_mandir}/man8/optiups.8.gz
%{_mandir}/man8/phoenixcontact_modbus.8.gz
%{_mandir}/man8/pijuice.8.gz
%{_mandir}/man8/powercom.8.gz
%if %{with powerman}
%{_mandir}/man8/powerman-pdu.8.gz
%endif
%{_mandir}/man8/powerpanel.8.gz
%{_mandir}/man8/powervar_cx_ser.8.gz
%{_mandir}/man8/powervar_cx_usb.8.gz
%{_mandir}/man8/nutdrv_rhino.8.gz
%{_mandir}/man8/richcomm_usb.8.gz
%{_mandir}/man8/riello_ser.8.gz
%{_mandir}/man8/riello_usb.8.gz
%{_mandir}/man8/safenet.8.gz
%{_mandir}/man8/sms_ser.8.gz
%{_mandir}/man8/snmp-ups.8.gz
%{_mandir}/man8/solis.8*
%{_mandir}/man8/sockdebug.8.gz
%{_mandir}/man8/socomec_jbus.8.gz
%{_mandir}/man8/tripplite.8.gz
%{_mandir}/man8/tripplite_usb.8.gz
%{_mandir}/man8/tripplitesu.8.gz
%{_mandir}/man8/upscode2.8*
%{_mandir}/man8/upsd.8.gz
%{_mandir}/man8/upsdrvctl.8.gz
%{_mandir}/man8/upsdrvsvcctl.8.gz
%{_mandir}/man8/usbhid-ups.8.gz
%{_mandir}/man8/victronups.8.gz
%{_mandir}/man8/ve-direct.8.gz
%{_sysusersdir}/nut.conf

%files client
%license COPYING LICENSE-GPL2 LICENSE-GPL3
%dir %{_sysconfdir}/ups
%config(noreplace) %attr(640,root,nut) %{_sysconfdir}/ups/nut.conf
%config(noreplace) %attr(640,root,nut) %{_sysconfdir}/ups/upsmon.conf
%config(noreplace) %attr(640,root,nut) %{_sysconfdir}/ups/upssched.conf
%{_tmpfilesdir}/nut-common-tmpfiles.conf
%dir %attr(750,nut,nut) %{_localstatedir}/lib/ups
# upsmon.pid is written as root, so root needs access for now
%dir %attr(770,root,dialout) %{piddir}
%attr(644,nut,nut) %verify(not size mtime md5) /run/%{name}/upsmon.pid
%{_bindir}/upsc
%{_bindir}/upscmd
%{_bindir}/upslog
%{_bindir}/upsrw
%{_sbindir}/upsmon
%{_sbindir}/upssched
%{_bindir}/upssched-cmd
# dummy-ups requires libupsclient
%{modeldir}/dummy-ups
%{_unitdir}/nut-monitor.service
# nut-monitor.service also needs nut.target
%{_unitdir}/nut.target
/lib/systemd/system-shutdown/nutshutdown
%{_libdir}/libupsclient.so.*
%{_libdir}/libnutclient.so.*
%{_libdir}/libnutclientstub.so.*
%{_mandir}/man5/nut.conf.5.gz
%{_mandir}/man5/upsmon.conf.5.gz
%{_mandir}/man5/upssched.conf.5.gz
%{_mandir}/man7/nut.7.gz
%{_mandir}/man8/upsc.8.gz
%{_mandir}/man8/upscmd.8.gz
%{_mandir}/man8/upslog.8.gz
%{_mandir}/man8/upsrw.8.gz
%{_mandir}/man8/upsmon.8.gz
%{_mandir}/man8/upssched.8.gz
%{_datadir}/nut
%{_sysusersdir}/nut.conf

%files monitor
%{_bindir}/nut-monitor
%{_bindir}/NUT-Monitor
%{_datadir}/applications/nut-monitor.desktop
%{_datadir}/icons/hicolor/*/apps/nut-monitor.png
%{_datadir}/icons/hicolor/scalable/apps/nut-monitor.svg
%{_datadir}/nut-monitor/
%{_mandir}/man8/NUT-Monitor*.8.gz
%pycached %{python3_sitelib}/PyNUT.py
%pycached %{python3_sitelib}/test_nutclient.py

%files cgi
%config(noreplace) %attr(644,root,root) %{_sysconfdir}/ups/hosts.conf
%config(noreplace) %attr(600,nut,root) %{_sysconfdir}/ups/upsset.conf
%config(noreplace) %attr(644,root,root) %{_sysconfdir}/ups/upsstats.html
%config(noreplace) %attr(644,root,root) %{_sysconfdir}/ups/upsstats-single.html
%{cgidir}/
%{_mandir}/man5/hosts.conf.5.gz
%{_mandir}/man5/upsstats.html.5.gz
%{_mandir}/man5/upsset.conf.5.gz
%{_mandir}/man8/upsimage.cgi.8.gz
%{_mandir}/man8/upsstats.cgi.8.gz
%{_mandir}/man8/upsset.cgi.8.gz

%files xml
%{modeldir}/netxml-ups
%doc %{_mandir}/man8/netxml-ups.8.gz

%files devel
%{_includedir}/*
%{_mandir}/man3/upscli*
%{_mandir}/man3/nutscan*
%{_mandir}/man3/nutclient*
%{_mandir}/man3/libnutclient*
%{_libdir}/libupsclient.so
%{_libdir}/libnutclient.so
%{_libdir}/libnutclientstub.so
%{_libdir}/libnutconf.so
%{_libdir}/libnutscan.so
%{_libdir}/pkgconfig/libupsclient.pc
%{_libdir}/pkgconfig/libnutclient.pc
%{_libdir}/pkgconfig/libnutconf.pc
%{_libdir}/pkgconfig/libnutclientstub.pc
%{_libdir}/pkgconfig/libnutscan.pc

%changelog
%autochangelog
