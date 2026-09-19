%global source0_hash 735adc4610af68b35cf3b8a54559ac8d79de28ac1373b0630f3def659d190f35

# Set vdr_version based on Fedora version
# Default
%global vdr_version 2.6.9

%if 0%{?fedora} == 42
%global vdr_version 2.7.4
%elif 0%{?fedora} == 43
%global vdr_version 2.7.7
%elif 0%{?fedora} >= 44
%global vdr_version 2.8.1
%endif

Name:           vdr-epg-daemon
Version:        1.3.29
Release:        12%{?dist}
Summary:        A daemon to download EPG data from internet and manage it in a mysql database
License:        GPL-1.0-or-later AND GPL-2.0-only AND LicenseRef-Callaway-BSD
URL:            https://github.com/horchi/vdr-epg-daemon
Source0:        https://github.com/horchi/vdr-epg-daemon/archive/refs/tags/%{version}.tar.gz#/%{name}-%{version}.tar.gz
# fix: Optimization flags are not honored.
Patch0:         %{name}-makefile.patch
# https://github.com/horchi/vdr-epg-daemon/commit/27a7034e7c7819ab8103fc8f8af66834d61577f9.patch
Patch1:         27a7034e7c7819ab8103fc8f8af66834d61577f9.patch

BuildRequires:  make
BuildRequires:  gcc-c++
BuildRequires:  libcurl-devel
BuildRequires:  libxslt-devel
BuildRequires:  libxml2-devel
BuildRequires:  libuuid-devel
BuildRequires:  jansson-devel
BuildRequires:  perl-generators
BuildRequires:  zlib-devel
BuildRequires:  libjpeg-turbo-devel
BuildRequires:  libmicrohttpd-devel
BuildRequires:  imlib2-devel
BuildRequires:  libxslt-devel
BuildRequires:  libxml2-devel
BuildRequires:  openssl-devel
BuildRequires:  python3-devel
BuildRequires:  mariadb-connector-c-devel
BuildRequires:  libarchive-devel
BuildRequires:  systemd-devel
BuildRequires:  systemd-units
BuildRequires:  vdr-devel >= %{vdr_version}
Requires:       mariadb-server
Requires(post):   systemd-units
Requires(preun):  systemd-units
Requires(postun): systemd-units
Requires:       vdr

%description 
epgd is part of the double team epgd+epg2vdr to effectively retrieve,
store and import epg data to vdr. It is designed to handle large amount of
data and pictures in a distributed environment with one epg-server and
many possible vdr-clients - therefore it relays on mysql. 

Though it is possible to use epgd alone with mysql it only makes sense to
use it as back-end to the vdr-plugin epg2vdr. That being said you need to
install, setup and configure mysql, epgd and epg2vdr in order to get a
working environment.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1 -n %{name}-%{version}

iconv -f iso-8859-1 -t utf-8 README > README.utf8 ; mv README.utf8 README

## Optimization flags in 'Make.config' file
sed -i \
    -e 's|PREFIX      ?= /usr/local|PREFIX       =  %{_prefix}|' \
    -e 's|PLGDEST      = $(PREFIX)/lib/epgd/plugins|PLGDEST      = %{_libdir}/epgd|' \
    -e 's|_PLGDEST     = $(DESTDIR)$(PREFIX)/lib/epgd/plugins|_PLGDEST     = $(DESTDIR)%{_libdir}/epgd|' \
    -e 's|HTTPDEST     = $(DESTDIR)/var/epgd/www|HTTPDEST     = $(DESTDIR)%{vdr_resdir}/epgd|' \
    -e 's|SYSTEMDDEST  = $(DESTDIR)/etc/systemd/system|SYSTEMDDEST  = $(DESTDIR)%{_unitdir}|' \
    -e 's|INIT_SYSTEM  = none|INIT_SYSTEM  = systemd|' \
    -e 's|INIT_AFTER   = mysql.service|INIT_AFTER   = mariadb.service|' \
    -e 's|@@OPTFLAGS | %{optflags}|' \
    Make.config

%if 0%{?without_debug}
sed -i -e 's|DEBUG = 1||' Make.config
%else
##Nothing
%endif

## Optimization flags for ../epglv
sed -i \
    -e 's|@@LIBDIR| %{_libdir}|' \
    -e 's|@@OPTFLAGS | %{optflags}|' \
    -e 's|$(PLGDIR)/$(TARGET);|$(DESTDIR)/$(PLGDIR)/$(TARGET);|' \
    -e 's|$(TARGET) $(PLGDIR);|$(TARGET) $(DESTDIR)/$(PLGDIR);|' \
    epglv/Makefile

##epglv readme file
mv epglv/README epglv/README-epglv

# Add shebang
# Add bash to beginning of file
for file in scripts/epgd-{showmerge,showtimer,conflictsof,showtimerat,showdones}; do
   sed -i '1 i\#!/bin/bash' $file
done

for file in scripts/epgh-{request,login}; do
   sed -i '1 i\#!/bin/bash' $file
done

%build
%make_build

%install
mkdir -p %{buildroot}%{_unitdir}
mkdir -p %{buildroot}%{_libdir}/mariadb/plugin
%make_install

%post
%systemd_post epgd.service
%systemd_post epghttpd.service

%preun
%systemd_preun epgd.service
%systemd_preun epghttpd.service

%postun
%systemd_postun_with_restart epgd.service
%systemd_postun_with_restart epghttpd.service

%files
%doc HISTORY* README* epglv/README* contrib/README.fedora
%license COPYING http/www/font/LICENSE.txt
%{_bindir}/epg*
%dir %{_sysconfdir}/epgd
%config(noreplace) %{_sysconfdir}/epgd/*
%{_unitdir}/epg*.service
%dir %{_libdir}/epgd
%{_libdir}/epgd/libepgd-epgdata.so
%{_libdir}/mariadb/plugin/mysqlepglv.so
%{vdr_resdir}/epgd/

%changelog
%autochangelog
