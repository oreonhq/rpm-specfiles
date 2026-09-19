%global source0_hash 6c07f527417f7562074f99012da4d11eb4dbafd33f49e66b442ccd6e3b8cfd20

Name: libchipcard
Summary: A library for easy access to smart cards (chipcards)
Version: 5.1.6
Release: 13%{?dist}
# Download is PHP form at http://www.aquamaniac.de/sites/download/packages.php
Source0: https://www.aquamaniac.de/rdm/attachments/download/382/libchipcard-%{version}.tar.gz
Source1: https://www.aquamaniac.de/rdm/attachments/download/381/libchipcard-%{version}.tar.gz.asc
# Keyfile obtained from https://keyserver.ubuntu.com/pks/lookup?op=get&search=0xe9899d784a977416
Source2: keyfile.asc
License: LGPL-2.0-only and GPL-2.0-or-later and LGPL-2.1-or-later
# Most LGPL 2
# LGPL 2.1+: src/lib/version.h
# GPLv2+: src/tools/cardcommander/cardcommander.cpp, src/tools/kvkcard/main.c, src/tools/memcard/main.c
URL: https://www.aquamaniac.de/rdm/projects/libchipcard

BuildRequires: gcc-c++
BuildRequires: gwenhywfar-devel
BuildRequires: libsysfs-devel
BuildRequires: pcsc-lite-devel
BuildRequires: zlib-devel
BuildRequires: gnupg2

%description 
Libchipcard allows easy access to smart cards. It provides basic access
to memory and processor cards and has special support for German medical
cards, German "GeldKarte" and FinTS (homebanking, formerly known as HBCI) 
cards (both type 0 and type 1).
It accesses the readers via CTAPI or IFD interfaces and has successfully
been tested with Towitoko, Kobil, SCM, Orga, Omnikey and Reiner-SCT readers.
This package contains the chipcard-daemon needed to access card readers.

%package devel
Summary: Development headers for libchipcard
Requires: %{name}%{?_isa} = %{version}-%{release}
Requires: gwenhywfar-devel

%description devel
This package contains chipcard-config and header files for writing
drivers, services or even your own chipcard daemon for LibChipCard.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n %{name}-%{version}

%{gpgverify} --keyring='%{SOURCE2}' --signature='%{SOURCE1}' --data='%{SOURCE0}'

%build

%configure \
  --disable-static

%make_build

%install

%make_install

rm -fv %{buildroot}%{_libdir}/lib*.la

pushd tutorials
make clean
rm -rf .deps
rm -f Makefile*
popd

%ldconfig_scriptlets

%files
%doc README ChangeLog
%license COPYING
%{_libdir}/libchipcard.so.6*
%{_libdir}/gwenhywfar/plugins/79/
%{_datadir}/chipcard
%{_bindir}/cardcommander
%{_bindir}/chipcard*
%{_bindir}/geldkarte
%{_bindir}/kvkcard
%{_bindir}/memcard
%{_bindir}/usbtan-test
%{_bindir}/zkacard-tool
%{_sysconfdir}/chipcard/

%files devel
%doc doc/ tutorials
%{_libdir}/libchipcard.so
%{_includedir}/libchipcard5/
%{_libdir}/pkgconfig/libchipcard-client.pc
%{_libdir}/pkgconfig/libchipcard-server.pc
%{_datadir}/aclocal/chipcard.m4

%changelog
%autochangelog
