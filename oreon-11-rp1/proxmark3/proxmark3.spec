%global source0_hash 5d727313d912d8d758365d3528fbf8af7463e5deec23a9bef79f1fab4fd0c66d
Name:		proxmark3
Version:	4.23346
Release:        1%{?dist}
Summary:        The Swiss Army Knife of RFID Research - RRG/Iceman repo
License:	GPL-3.0-or-later
URL:		https://github.com/RfidResearchGroup/proxmark3
Source0:        https://github.com/RfidResearchGroup/proxmark3/archive/refs/tags/v%{version}.tar.gz
Requires:	bzip2-libs, readline, python3, bluez, qt5-qtbase, gd
ExcludeArch:	ppc64le s390x i686
# oreon:deps
BuildRequires:  arm-none-eabi-gcc
BuildRequires:  arm-none-eabi-newlib
BuildRequires:  bluez-libs-devel
BuildRequires:  bzip2-devel
BuildRequires:  g++
BuildRequires:  gcc
BuildRequires:  gd
BuildRequires:  gd-devel
BuildRequires:  jansson-devel
BuildRequires:  libatomic
BuildRequires:  lz4-devel
BuildRequires:  make
BuildRequires:  openssl-devel
BuildRequires:  python3-devel
BuildRequires:  qt5-qtbase-devel
BuildRequires:  readline-devel
# /oreon:deps
%description
The Swiss Army Knife of RFID Research - RRG/Iceman repo

%define __strip /bin/true

%prep
%oreon_prep
%build

export CFLAGS="%{optflags}"
make %{?_smp_mflags} V=1 clean
make %{?_smp_mflags} V=1
rm -rf %{buildroot}/doc/datasheets/
rm -rf %{buildroot}/doc/original_proxmark3/
%install
chmod -x ./client/luascripts/examples/example_cmdline.lua
chmod -x ./client/cmdscripts/rdv4_init_extflash.cmd
chmod -x ./client/pyscripts/xorcheck.py
chmod -x ./client/cmdscripts/example.cmd
sed -i 's|^TOOLS_PATH \?= \?None|TOOLS_PATH="/usr/share/proxmark3/"|' ./client/pyscripts/pm3_resources.py
sed -i 's|^DICTS_PATH \?= \?None|DICTS_PATH="/usr/share/proxmark3/dictionaries"|' ./client/pyscripts/pm3_resources.py
make %{?_smp_mflags} V=1 install PREFIX=%{buildroot}/usr UDEV_PREFIX=%{buildroot}/etc/udev/rules.d/
chmod -x %{buildroot}/usr/share/proxmark3/firmware/fullimage.elf
chmod -x %{buildroot}/usr/share/proxmark3/firmware/bootrom.elf
rm -rf %{buildroot}%{_datadir}/doc/proxmark3
%oreon_autofiles main

%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
