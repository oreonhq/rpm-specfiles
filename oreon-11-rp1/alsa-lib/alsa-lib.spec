# Copyright (C) 2026 Oreon HQ
# SPDX-License-Identifier: GPL-2.0-or-later

%global source0_hash f740db7f488255944ffd4428416ee3390a96742856916433df468c281436480e

%{!?oreon_bootstrap:%global oreon_bootstrap %{nil}}
%bcond bootstrap 0
%oreon_bootstrap

%global version_alsa_lib 1.2.16.1
%global version_alsa_ucm 1.2.16.1
%global version_alsa_tplg 1.2.5

%global sysmodprobedir %{_prefix}/lib/modprobe.d

Name:           alsa-lib
Version:        %{version_alsa_lib}
Release:        1%{?dist}
Summary:        The Advanced Linux Sound Architecture (ALSA) library
License:        LGPL-2.1-or-later
URL:            https://www.alsa-project.org/

Source0:        https://www.alsa-project.org/files/pub/lib/%{name}-%{version}.tar.bz2
Source1:        https://www.alsa-project.org/files/pub/lib/alsa-ucm-conf-%{version_alsa_ucm}.tar.bz2
Source2:        https://www.alsa-project.org/files/pub/lib/alsa-topology-conf-%{version_alsa_tplg}.tar.bz2
Source3:        %{name}-%{version}.tar.bz2.sig
Source4:        alsa-ucm-conf-%{version_alsa_ucm}.tar.bz2.sig
Source5:        alsa-topology-conf-%{version_alsa_tplg}.tar.bz2.sig
Source6:        gpgkey-F04DF50737AC1A884C4B3D718380596DA6E59C91.gpg
Source10:       asound.conf
Source11:       modprobe-dist-alsa.conf
Source12:       modprobe-dist-oss.conf
Patch1:         alsa-lib-1.2.3.1-config.patch
Patch2:         alsa-lib-1.2.10-glibc-open.patch

BuildRequires:  oreon-rpm-macros
BuildRequires:  gcc
BuildRequires:  make
BuildRequires:  gnupg2
BuildRequires:  doxygen
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  libtool

%description
The Advanced Linux Sound Architecture (ALSA) provides audio and MIDI
functionality to the Linux operating system.

This package includes the ALSA runtime libraries to simplify application
programming and provide higher level functionality as well as support for
the older OSS API, providing binary compatibility for most OSS programs.

%package devel
Summary:        Development files from the ALSA library
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       pkgconfig

%description devel
The Advanced Linux Sound Architecture (ALSA) provides audio and MIDI
functionality to the Linux operating system.

This package includes the ALSA development libraries for developing
against the ALSA libraries and interfaces.

%package -n alsa-ucm
Summary:        ALSA Use Case Manager configuration
BuildArch:      noarch
License:        BSD-3-Clause
Requires:       %{name} >= %{version_alsa_lib}

%description -n alsa-ucm
The Advanced Linux Sound Architecture (ALSA) Use Case Manager configuration
contains alsa-lib configuration of Audio input/output names and routing.

%package -n alsa-topology
Summary:        ALSA Topology configuration
BuildArch:      noarch
License:        BSD-3-Clause
Requires:       %{name} >= %{version_alsa_lib}

%description -n alsa-topology
The Advanced Linux Sound Architecture (ALSA) topology configuration
contains alsa-lib configuration of SoC topology.

%prep
%oreon_sha256
%oreon_gpgverify --key %{SOURCE6} --sig %{SOURCE3} --data %{SOURCE0}
%oreon_gpgverify --key %{SOURCE6} --sig %{SOURCE4} --data %{SOURCE1}
%oreon_gpgverify --key %{SOURCE6} --sig %{SOURCE5} --data %{SOURCE2}

%autosetup -p1

%build
%define _lto_cflags -flto -ffat-lto-objects -flto-partition=none

autoreconf -vif
%configure --disable-aload --with-plugindir=%{_libdir}/alsa-lib --disable-alisp

sed -i 's|^hardcode_libdir_flag_spec=.*|hardcode_libdir_flag_spec=""|g' libtool
sed -i 's|^runpath_var=LD_RUN_PATH|runpath_var=DIE_RPATH_DIE|g' libtool

%make_build V=1
make doc

%install
%make_install

mkdir -p -m 755 %{buildroot}%{_sysconfdir}
install -p -m 644 %{SOURCE10} %{buildroot}%{_sysconfdir}

mkdir -p -m 755 %{buildroot}%{sysmodprobedir}
install -p -m 644 %{SOURCE11} %{buildroot}%{sysmodprobedir}/dist-alsa.conf
install -p -m 644 %{SOURCE12} .

mkdir -p %{buildroot}%{_datadir}/alsa/ucm
mkdir -p %{buildroot}%{_datadir}/alsa/ucm2
tar xvjf %{SOURCE1} -C %{buildroot}%{_datadir}/alsa --strip-components=1 "*/ucm" "*/ucm2"

mkdir -p %{buildroot}%{_datadir}/alsa/topology
tar xvjf %{SOURCE2} -C %{buildroot}%{_datadir}/alsa --strip-components=1 "*/topology"

find %{buildroot} -name '*.la' -delete

rm %{buildroot}%{_includedir}/asoundlib.h

%ldconfig_scriptlets

%files
%license COPYING
%doc doc/asoundrc.txt modprobe-dist-oss.conf
%config %{_sysconfdir}/asound.conf
%{_libdir}/libasound.so.*
%{_libdir}/libatopology.so.*
%{_bindir}/aserver
%{_datadir}/alsa/
%exclude %{_datadir}/alsa/ucm
%exclude %{_datadir}/alsa/ucm2
%exclude %{_datadir}/alsa/topology
%{sysmodprobedir}/dist-*

%files devel
%doc TODO doc/doxygen/
%{_includedir}/alsa/
%{_includedir}/sys/asoundlib.h
%{_libdir}/libasound.so
%{_libdir}/libatopology.so
%{_libdir}/pkgconfig/alsa.pc
%{_libdir}/pkgconfig/alsa-topology.pc
%{_datadir}/aclocal/alsa.m4

%files -n alsa-ucm
%{_datadir}/alsa/ucm
%{_datadir}/alsa/ucm2

%files -n alsa-topology
%{_datadir}/alsa/topology

%changelog
%autochangelog
