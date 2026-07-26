%global source0_hash a1242d100b61fe1fffbbf706e919ed51d6a341c9fb8293fb42046e32ae2b3338

Name:           shairport-sync
Version:        4.3.7
Release:        3%{?dist}
Summary:        AirTunes emulator. Multi-Room with Audio Synchronisation
# MIT licensed except for tinysvcmdns under BSD, 
# FFTConvolver/ under GPLv3+ and audio_sndio.c 
# under ISC
# Automatically converted from old format: MIT and BSD and GPLv3+ and ISC - review is highly recommended.
License:        LicenseRef-Callaway-MIT AND LicenseRef-Callaway-BSD AND GPL-3.0-or-later AND ISC
URL:            https://github.com/mikebrady/shairport-sync
Source0:        https://github.com/mikebrady/%{name}/archive/%{version}/%{name}-%{version}.tar.gz

%{?systemd_requires}
Requires: avahi
BuildRequires: make
BuildRequires:  systemd
BuildRequires:  pkgconfig(libconfig)
BuildRequires:  pkgconfig(popt)
BuildRequires:  pkgconfig(openssl)
BuildRequires:  pkgconfig(libdaemon)
BuildRequires:  pkgconfig(avahi-core)
BuildRequires:  pkgconfig(alsa)
BuildRequires:  pkgconfig(soxr)
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:	gcc
BuildRequires:	gcc-c++
BuildRequires:	pkgconfig(libpulse)
BuildRequires:	pkgconfig(libpipewire-0.3)
# airplay2 support
#Requires:       libavcodec-freeworld
#Requires:       nqptp
#BuildRequires:  pkgconfig(uuid)
#BuildRequires:  pkgconfig(libavformat)
#BuildRequires:  pkgconfig(libavcodec)
#BuildRequires:  pkgconfig(libavutil)
#BuildRequires:  pkgconfig(libgcrypt)
#BuildRequires:  pkgconfig(libsodium)
#BuildRequires:  pkgconfig(libplist-2.0)
#BuildRequires:  xxd

%description
Shairport Sync emulates an AirPort Express for the purpose of streaming audio
 from iTunes, iPods, iPhones, iPads and AppleTVs. Audio played by a Shairport
 Sync-powered device stays synchronised with the source and hence with similar
 devices playing the same source. Thus, for example, synchronised multi-room
 audio is possible without difficulty. (Hence the name Shairport Sync, BTW.)

Shairport Sync does not support AirPlay video or photo streaming.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q

# Create a sysusers.d config file
cat >shairport-sync.sysusers.conf <<EOF
u shairport-sync - '%{name} User' %{_sharedstatedir}/%{name} -
m shairport-sync audio
EOF

%build
autoreconf -i -f
%configure --sysconfdir=/etc --with-alsa --with-pipe --with-dummy \
           --with-stdout --with-pa --with-metadata --with-pw \
           --with-soxr --with-avahi --with-systemd --with-ssl=openssl \
           --with-create-user-group=false # --with-airplay-2

%make_build

%install
%make_install
rm %{buildroot}/etc/shairport-sync.conf.sample
mkdir -p %{buildroot}/%{_sharedstatedir}/%{name}

install -m0644 -D shairport-sync.sysusers.conf %{buildroot}%{_sysusersdir}/shairport-sync.conf

%post
%systemd_post %{name}.service

%preun
%systemd_preun %{name}.service

%postun
%systemd_postun_with_restart %{name}.service

%files
%config(noreplace) /etc/shairport-sync.conf
/usr/bin/shairport-sync
/usr/share/man/man1/shairport-sync.1.gz
%{_unitdir}/%{name}.service
%doc README.md RELEASENOTES.md TROUBLESHOOTING.md
%license LICENSES
%attr(-, %{name}, %{name}) %{_sharedstatedir}/%{name}
%{_sysusersdir}/shairport-sync.conf

%changelog
%autochangelog
