%global source0_hash a1242d100b61fe1fffbbf706e919ed51d6a341c9fb8293fb42046e32ae2b3338
Name:           shairport-sync
Version:        4.3.7
Release:        1%{?dist}
Summary:        AirTunes emulator. Multi-Room with Audio Synchronisation
License:        LicenseRef-Callaway-MIT AND LicenseRef-Callaway-BSD AND GPL-3.0-or-later AND ISC
URL:            https://github.com/mikebrady/shairport-sync
Source0:        https://github.com/mikebrady/%{name}/archive/%{version}/%{name}-%{version}.tar.gz
%{?systemd_requires}
Requires: avahi
# oreon:deps
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  gcc
BuildRequires:  gcc-c++
BuildRequires:  make
BuildRequires:  pkgconfig(alsa)
BuildRequires:  pkgconfig(avahi-core)
BuildRequires:  pkgconfig(libconfig)
BuildRequires:  pkgconfig(libdaemon)
BuildRequires:  pkgconfig(libpipewire-0.3)
BuildRequires:  pkgconfig(libpulse)
BuildRequires:  pkgconfig(openssl)
BuildRequires:  pkgconfig(popt)
BuildRequires:  pkgconfig(soxr)
BuildRequires:  systemd
# /oreon:deps
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
%oreon_autofiles main

%post

%systemd_post %{name}.service
%preun

%systemd_preun %{name}.service
%postun

%systemd_postun_with_restart %{name}.service
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
