%global source0_hash 18bf32e59eb764b13da3c4fa70384926d7fa584cb31d2fe7f137a570633eeec1
%global _hardened_build 1
%global nut_uid 57
%global nut_gid 57
%global cgidir  /var/www/nut-cgi-bin
%global piddir  /run/nut
%global modeldir %{_libexecdir}/%{name}
%bcond_with powerman
Summary:        Network UPS Tools
Name: nut
Version: 2.8.5
Release:        1%{?dist}
License: GPL-2.0-or-later AND GPL-3.0-or-later
Url: https://www.networkupstools.org/
Source0:        https://www.networkupstools.org/source/2.8/%{name}-%{version}.tar.gz
Source4: libs.sh
Patch2: nut-2.8.0-piddir-owner.patch
Patch9: nut-2.6.5-rmpidf.patch
Patch15: nut-c99-strdup.patch
Patch16: nut-2.8.3-rhinoname.patch
Requires(post): coreutils systemd
Requires(preun): systemd
Requires(postun): coreutils systemd
Recommends: nut-xml
Requires: group(dialout)
Requires: group(tty)
%if %{with powerman}
%endif
%ifnarch s390 s390x
%endif
ExcludeArch: s390 s390x
%global restart_flag %{piddir}/%{name}-restart-after-rpm-install
# oreon:deps
BuildRequires:  asciidoc
BuildRequires:  augeas-libs
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  avahi-devel
BuildRequires:  cppunit-devel
BuildRequires:  dbus-glib-devel
BuildRequires:  desktop-file-utils
BuildRequires:  elfutils-devel
BuildRequires:  fontconfig-devel
BuildRequires:  freeipmi-devel
BuildRequires:  freetype-devel
BuildRequires:  gcc
BuildRequires:  gcc-c++
BuildRequires:  gd-devel
BuildRequires:  jq
BuildRequires:  libX11-devel
BuildRequires:  libXpm-devel
BuildRequires:  libi2c-devel
BuildRequires:  libjpeg-devel
BuildRequires:  libmodbus-devel
BuildRequires:  libpng-devel
BuildRequires:  libtool
BuildRequires:  libtool-ltdl-devel
BuildRequires:  libusb1-devel
BuildRequires:  make
BuildRequires:  neon-devel
BuildRequires:  net-snmp-devel
BuildRequires:  netpbm-devel
BuildRequires:  nss-devel
BuildRequires:  openssl-devel
BuildRequires:  pkgconfig
BuildRequires:  python3-devel
BuildRequires:  python3-pyqt6
BuildRequires:  python3-setuptools
BuildRequires:  systemd-devel
BuildRequires:  systemd-rpm-macros
# /oreon:deps
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

autoreconf -i
export CXXFLAGS="-std=c++14 $RPM_OPT_FLAGS"
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
    --with-systemdsystemunitdir=%{_unitdir} \
    --with-systemdshutdowndir=/lib/systemd/system-shutdown \
    --with-pkgconfig-dir=%{_libdir}/pkgconfig \
    --disable-static \
    --with-udev-dir=%{_usr}/lib/udev \
    --libdir=%{_libdir} \
    --enable-docs-changelog=no
sh %{SOURCE4} >>include/config.h
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
mv %{buildroot}/%{_usr}/lib/udev/rules.d/52-nut-ipmipsu.rules %{buildroot}/%{_usr}/lib/udev/rules.d/62-nut-ipmipsu.rules
for fe in ./docs/cables/powerware.txt
do
  iconv -f iso-8859-1 -t utf-8 <$fe >$fe.new
  touch -r $fe $fe.new
  mv -f $fe.new $fe
done
mv %{buildroot}%{_mandir}/man8/rhino.8 %{buildroot}%{_mandir}/man8/nutdrv_rhino.8
install -p -D -m 644 scripts/python/module/PyNUT.py %{buildroot}%{python3_sitelib}/PyNUT.py
ln %{buildroot}%{_bindir}/{NUT-Monitor,nut-monitor}
mkdir -p %{buildroot}%{_datadir}/applications
desktop-file-install \
  --dir=%{buildroot}%{_datadir}/applications \
  %{buildroot}%{_datadir}/nut-monitor/app/nut-monitor.desktop
for res in 256x256 48x48 64x64 scalable
do
  mkdir -p %{buildroot}%{_datadir}/icons/hicolor/${res}/apps
  ln %{buildroot}%{_datadir}/nut-monitor/app/icons/${res}/nut-monitor.* \
    %{buildroot}%{_datadir}/icons/hicolor/${res}/apps/
done
touch %{buildroot}/%{piddir}/upsmon.pid
chmod 0644 %{buildroot}/%{piddir}/upsmon.pid
install -m0644 -D nut.sysusers.conf %{buildroot}%{_sysusersdir}/nut.conf
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*

%pre

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

if [ -e %restart_flag ]; then
  /bin/systemctl restart nut-monitor.service >/dev/null 2>&1 || :
  rm -f %restart_flag
else
  /bin/systemctl try-restart nut-monitor.service >/dev/null 2>&1 || :
fi
%files -f %{oreon_filedir}/main.list
%files -n nut-client -f %{oreon_filedir}/nut-client.list
%files -n nut-cgi -f %{oreon_filedir}/nut-cgi.list
%files -n nut-monitor -f %{oreon_filedir}/nut-monitor.list
%files -n nut-xml -f %{oreon_filedir}/nut-xml.list
%files -n nut-devel -f %{oreon_filedir}/nut-devel.list

%changelog

%autochangelog
