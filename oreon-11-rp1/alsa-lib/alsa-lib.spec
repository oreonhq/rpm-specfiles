%global source0_hash f740db7f488255944ffd4428416ee3390a96742856916433df468c281436480e
%global source1_hash 9f79e813c08fc86cfa46dd75c4fcda1a4a51b482db2607e1fcfaafb92f588a31
%global source2_hash 8bfa8306ca63e1d0cbe80be984660273b91bd5b7dd0800a6c5aa71dd8c8d775c
%define version_alsa_lib  1.2.16.1
%define version_alsa_ucm  1.2.16.1
%define version_alsa_tplg 1.2.5
%global lib_patch         0
%global ucm_patch         0
Summary:        The Advanced Linux Sound Architecture (ALSA) library
Name:     alsa-lib
Version:  %{version_alsa_lib}
Release:        1%{?dist}
License:  LGPL-2.1-or-later
URL:      https://www.alsa-project.org/
Source0:        https://www.alsa-project.org/files/pub/lib/%{name}-%{version}.tar.bz2
Source1:        https://www.alsa-project.org/files/pub/lib/alsa-ucm-conf-1.2.15.3.tar.bz2
Source2:        https://www.alsa-project.org/files/pub/lib/alsa-topology-conf-1.2.5.tar.bz2
Source10: asound.conf
Source11: modprobe-dist-alsa.conf
Source12: modprobe-dist-oss.conf
Patch1:   alsa-lib-1.2.3.1-config.patch
Patch2:   alsa-lib-1.2.10-glibc-open.patch
# oreon:deps
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  doxygen
BuildRequires:  libtool
BuildRequires:  make
# /oreon:deps
%description
The Advanced Linux Sound Architecture (ALSA) provides audio and MIDI
functionality to the Linux operating system.

This package includes the ALSA runtime libraries to simplify application
programming and provide higher level functionality as well as support for
the older OSS API, providing binary compatibility for most OSS programs.

%package  devel
Summary:  Development files from the ALSA library
Requires: %{name} = %{version}-%{release}
Requires: pkgconfig
%description devel
The Advanced Linux Sound Architecture (ALSA) provides audio and MIDI
functionality to the Linux operating system.

This package includes the ALSA development libraries for developing
against the ALSA libraries and interfaces.

%package  -n alsa-ucm
Summary:   ALSA Use Case Manager configuration
BuildArch: noarch
License:   BSD-3-Clause
Requires:  %{name} >= %{version_alsa_lib}
%description -n alsa-ucm
The Advanced Linux Sound Architecture (ALSA) Use Case Manager configuration
contains alsa-lib configuration of Audio input/output names and routing

%package  -n alsa-topology
Summary:   ALSA Topology configuration
BuildArch: noarch
License:   BSD-3-Clause
Requires:  %{name} >= %{version_alsa_lib}
%description -n alsa-topology
The Advanced Linux Sound Architecture (ALSA) topology configuration
contains alsa-lib configuration of SoC topology

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
test "%{source1_hash}" = "none" || { f="%{SOURCE1}"; test -f "$f" || { echo "oreon: missing Source1 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source1_hash}" || { echo "oreon: Source1 hash mismatch" >&2; exit 1; }; }
test "%{source2_hash}" = "none" || { f="%{SOURCE2}"; test -f "$f" || { echo "oreon: missing Source2 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source2_hash}" || { echo "oreon: Source2 hash mismatch" >&2; exit 1; }; }
%setup -q -n %{name}-%{version}%{?prever}%{?postver}
%patch -P1 -p1 -b .config
%patch -P2 -p1 -b .glibc-open

%build

%define _lto_cflags -flto -ffat-lto-objects -flto-partition=none
autoreconf -vif
%configure --disable-aload --with-plugindir=%{_libdir}/alsa-lib --disable-alisp
sed -i 's|^hardcode_libdir_flag_spec=.*|hardcode_libdir_flag_spec=""|g' libtool
sed -i 's|^runpath_var=LD_RUN_PATH|runpath_var=DIE_RPATH_DIE|g' libtool
make %{?_smp_mflags} V=1
make doc
%install
%global sysmodprobedir %{_prefix}/lib/modprobe.d
make DESTDIR=%{buildroot} install
mkdir -p -m 755 %{buildroot}/etc
install -p -m 644 %{SOURCE10} %{buildroot}/etc
mkdir -p -m 755 %{buildroot}%{sysmodprobedir}
install -p -m 644 %{SOURCE11} %{buildroot}%{sysmodprobedir}/dist-alsa.conf
install -p -m 644 %{SOURCE12} .
mkdir -p %{buildroot}/%{_datadir}/alsa/ucm
mkdir -p %{buildroot}/%{_datadir}/alsa/ucm2
tar xvjf %{SOURCE1} -C %{buildroot}/%{_datadir}/alsa --strip-components=1 "*/ucm" "*/ucm2"
mkdir -p %{buildroot}/%{_datadir}/alsa/topology
tar xvjf %{SOURCE2} -C %{buildroot}/%{_datadir}/alsa --strip-components=1 "*/topology"
find %{buildroot} -name '*.la' -delete
rm %{buildroot}/%{_includedir}/asoundlib.h
%ldconfig_scriptlets
%oreon_autofiles alsa-lib-devel usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*
%oreon_autofiles alsa-ucm usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles alsa-topology usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%files -f %{oreon_filedir}/main.list
%files -n alsa-lib-devel -f %{oreon_filedir}/alsa-lib-devel.list
%files -n alsa-ucm -f %{oreon_filedir}/alsa-ucm.list
%files -n alsa-topology -f %{oreon_filedir}/alsa-topology.list

%changelog

* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - %{version_alsa_lib}-3
- Prepare for Oreon 11 (RP1)
