# Copyright (C) 2026 Oreon HQ
# SPDX-License-Identifier: GPL-2.0-or-later

%global source0_hash 1e42b9fc4ad7db7befd414d45ab2f8a159c0b30fcd6eee452be662298766a849
%global source1_hash 88bf0d3c16dda0ce30df44f72823388b637f4996eadddb05667953b4ac12375a
%global source2_hash c5f895b9e9de805f775bef69d71c6beea1acce4aa7303a1e303285930a9c426c
%global source3_hash d5009eb955eba735709107d377001e3dbd994335d7170aaf7e0d4d21d94c9199
%{!?oreon_bootstrap:%global oreon_bootstrap %{nil}}
%bcond bootstrap 0
%oreon_bootstrap

%global bootstrap 1

%global groupname jackuser
%global pagroup   pulse-rt

%define _lto_cflags %{nil}

Summary:       The Jack Audio Connection Kit
Name:          jack-audio-connection-kit
Version:       1.9.22
Release:       1%{?dist}
License:       GPL-2.0-only AND GPL-2.0-or-later AND LicenseRef-Callaway-LGPLv2+
URL:           https://www.jackaudio.org
Source0:       https://github.com/jackaudio/jack2/archive/v%{version}/v%{version}.tar.gz#/jack2-%{version}.tar.gz
Source1:       %{name}-README.Oreon
Source2:       %{name}-script.pa
Source3:       %{name}-limits.conf
Patch0:        jack2-py312.patch
Patch1:        jack-realtime-compat.patch

BuildRequires: oreon-rpm-macros
BuildRequires: clang
BuildRequires: gcc-c++
BuildRequires: alsa-lib-devel
BuildRequires: dbus-devel
BuildRequires: libdb-devel < 6.0.20
BuildRequires: doxygen
BuildRequires: expat-devel
%ifnarch s390 s390x
%if !0%{?bootstrap} && !0%{?flatpak} && 0%{?rhel} < 9
BuildRequires: libffado-devel
%endif
%endif
BuildRequires: libsamplerate-devel
BuildRequires: libsndfile-devel
BuildRequires: ncurses-devel
BuildRequires: opus-devel
BuildRequires: pkgconfig
BuildRequires: python3

Requires:      pam

Obsoletes:     %{name}-example-clients < 1.9.22

%description
JACK is a low-latency audio server, written primarily for the Linux operating
system. It can connect a number of different applications to an audio device, as
well as allowing them to share audio between themselves. Its clients can run in
their own processes (i.e. as a normal application), or can they can run within a
JACK server (i.e. a "plugin").

JACK is different from other audio server efforts in that it has been designed
from the ground up to be suitable for professional audio work. This means that
it focuses on two key areas: synchronous execution of all clients, and low
latency operation.

%package dbus
Summary:       Jack D-Bus launcher
Requires:      %{name} = %{version}-%{release}

%description dbus
Launcher to start Jack through D-Bus.

%package devel
Summary:       Header files for Jack
Requires:      %{name} = %{version}-%{release}

%description devel
Header files for the Jack Audio Connection Kit.

%package example-clients
Summary:       Example clients that use Jack 

%description example-clients
Small example clients that use the Jack Audio Connection Kit.

%prep
%oreon_sha256
echo '%{source1_hash}  %{SOURCE1}' | sha256sum -c -
echo '%{source2_hash}  %{SOURCE2}' | sha256sum -c -
echo '%{source3_hash}  %{SOURCE3}' | sha256sum -c -
%autosetup -p1 -n jack2-%{version}

cat >jack-audio-connection-kit.sysusers.conf <<EOF
g jackuser -
EOF

%build
%set_build_flags
export PREFIX=%{_prefix}
python3 ./waf configure \
   --mandir=%{_mandir}/man1 \
   --libdir=%{_libdir} \
   --doxygen \
   --dbus \
   --db \
   --classic \
%ifnarch s390 s390x
%if !0%{?bootstrap} && !0%{?flatpak} && 0%{?rhel} < 9
   --firewire \
%endif
%endif
   --alsa \
   --clients 256 \
   --ports-per-application=2048

python3 ./waf build %{?_smp_mflags} -v

%install
python3 ./waf --destdir=%{buildroot} install

mv %{buildroot}%{_datadir}/jack-audio-connection-kit/reference .
rm -rf %{buildroot}%{_datadir}/jack-audio-connection-kit

mkdir -p %{buildroot}%{_sysconfdir}/security/limits.d
sed -e 's,@groupname@,%groupname,g; s,@pagroup@,%pagroup,g;' \
    %{SOURCE3} > %{buildroot}%{_sysconfdir}/security/limits.d/95-jack.conf

install -p -m644 %{SOURCE1} README.Oreon

install -p -m644 %{SOURCE2} jack.pa

chmod 755 %{buildroot}%{_libdir}/jack/*.so %{buildroot}%{_libdir}/libjack*.so.*.*.*

install -m0644 -D jack-audio-connection-kit.sysusers.conf %{buildroot}%{_sysusersdir}/jack-audio-connection-kit.conf

%files
%doc ChangeLog.rst README.rst README_NETJACK2
%doc README.Oreon
%doc jack.pa
%license COPYING
%{_bindir}/jackd
%{_libdir}/jack/
%{_libdir}/libjack.so.0*
%{_libdir}/libjacknet.so.0*
%{_libdir}/libjackserver.so.0*
%config(noreplace) %{_sysconfdir}/security/limits.d/*.conf

%{_mandir}/man1/jackd*.1*
%{_sysusersdir}/jack-audio-connection-kit.conf

%files dbus
%{_bindir}/jackdbus
%{_datadir}/dbus-1/services/org.jackaudio.service
%{_bindir}/jack_control

%files devel
%doc reference/html/
%{_includedir}/jack/
%{_libdir}/libjack.so
%{_libdir}/libjacknet.so
%{_libdir}/libjackserver.so
%{_libdir}/pkgconfig/jack.pc

%changelog
%autochangelog
