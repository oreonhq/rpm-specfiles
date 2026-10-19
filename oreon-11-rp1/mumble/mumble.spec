%global source0_hash 378e61d5bfa58ba51bfbb645067f459214a9872da09b306f2c2c3f1902200547
%ifarch x86_64
%bcond_without tests
%endif
%global build_number 287
Name:           mumble
Version:        1.4.%{build_number}
Release:        10%{?dist}
Summary:        Low-latency and high-quality voice-chat program
License:        BSD-3-Clause AND Unlicense AND WTFPL AND ISC AND GPL-2.0-or-later
URL:            https://www.mumble.info
Source0:        https://github.com/mumble-voip/mumble/releases/download/v%{version}/mumble-%{version}.tar.gz
Source1:        murmur.service
Source2:        mumble-server.sysusers
Patch:          0001-BUILD-crypto-Migrate-to-OpenSSL-3.0-compatible-API.patch
Patch:          0002-FIX-crypto-Sharing-EVP-context-between-threads-crushes-Mumble.patch
Patch:          0003-BUILD-overlay-Fix-building-with-GCC-15.patch
Patch:          0004-CHANGE-server-Default-to-system-crypto-policy.patch
Patch:          0005-FIX-client-Avoid-loading-unversioned-libraries.patch
%if %{with tests}
%endif
%if 0%{?__isa_bits} == 32
%global libsymbolsuffix %{nil}
%else
%global libsymbolsuffix ()(%{__isa_bits}bit)
%endif
Recommends:     libjack.so.0%{libsymbolsuffix}
Suggests:       pipewire-jack-audio-connection-kit
Recommends:     libportaudio.so.2%{libsymbolsuffix}
Recommends:     libpipewire-0.3.so.0%{libsymbolsuffix}
Recommends:     libpulse.so.0%{libsymbolsuffix}
Provides:       bundled(arc4random)
Provides:       bundled(celt) = 0.7.0
Provides:       bundled(qqbonjour)
Provides:       bundled(smallft)
ExcludeArch:    %{ix86}
%global _privatelibs libcelt0[.]so.*
%global __provides_exclude ^(%{_privatelibs})$
%global __requires_exclude ^(%{_privatelibs})$
# oreon:deps
BuildRequires:  alsa-lib-devel
BuildRequires:  boost-devel
BuildRequires:  cmake
BuildRequires:  cmake(PocoXML)
BuildRequires:  cmake(PocoZip)
BuildRequires:  cmake(Qt5)
BuildRequires:  cmake(Qt5Concurrent)
BuildRequires:  cmake(Qt5Core)
BuildRequires:  cmake(Qt5DBus)
BuildRequires:  cmake(Qt5LinguistTools)
BuildRequires:  cmake(Qt5Network)
BuildRequires:  cmake(Qt5Sql)
BuildRequires:  cmake(Qt5Svg)
BuildRequires:  cmake(Qt5Test)
BuildRequires:  cmake(Qt5Widgets)
BuildRequires:  cmake(Qt5Xml)
BuildRequires:  desktop-file-utils
BuildRequires:  gcc-c++
BuildRequires:  glibc-devel
BuildRequires:  libXext-devel
BuildRequires:  libXi-devel
BuildRequires:  libappstream-glib
BuildRequires:  libcap-devel
BuildRequires:  libogg-devel
BuildRequires:  pipewire-devel
BuildRequires:  pipewire-jack-audio-connection-kit-devel
BuildRequires:  pkgconfig(avahi-compat-libdns_sd)
BuildRequires:  pkgconfig(libcrypto)
BuildRequires:  pkgconfig(libssl)
BuildRequires:  pkgconfig(openssl)
BuildRequires:  pkgconfig(opus)
BuildRequires:  pkgconfig(protobuf)
BuildRequires:  pkgconfig(rnnoise)
BuildRequires:  pkgconfig(sndfile)
BuildRequires:  pkgconfig(speech-dispatcher)
BuildRequires:  pkgconfig(speex)
BuildRequires:  pkgconfig(speexdsp)
BuildRequires:  portaudio-devel
BuildRequires:  pulseaudio-libs-devel
BuildRequires:  python3
BuildRequires:  systemd-rpm-macros
# /oreon:deps
%description
Mumble is an Open Source, low-latency and high-quality voice-chat program
written on top of Qt and Opus.

%package server
Summary:        Mumble voice chat server
Provides:       murmur = %{version}-%{release}
Obsoletes:      murmur < 1.3.4-10
BuildRequires:  cmake(Qt5Sql)
BuildRequires:  libcap-devel
BuildRequires:  pkgconfig(avahi-compat-libdns_sd)
BuildRequires:  cmake(Qt5DBus)
BuildRequires:  systemd-rpm-macros
Recommends:     avahi
%{?systemd_requires}
%{?sysusers_requires_compat}
%description server
mumble-server (also called murmur) is part of the VoIP suite Mumble primarily
aimed at gamers.

%package plugins
Summary:        Plugins for VoIP program Mumble
Requires:       %{name} = %{version}-%{release}
%description plugins
Mumble-plugins is part of VoIP suite Mumble primarily intended for gamers. This
plugin allows game linking so the voice of players will come from the direction
of their characters.

%package overlay
Summary:        Start games with the mumble overlay
Requires:       %{name} = %{version}-%{release}
%description overlay
Mumble-overlay is part of the Mumble VoIP suite aimed at gamers. If supported,
starting your game with this script will enable an ingame Mumble overlay.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p 1 -n mumble-%{version}.src

pushd 3rdparty

# remove bundled libraries that we have system copies of
rm -r jack opus pipewire portaudio pulseaudio rnnoise* speex*

# remove bundled libraries for windows
rm -r GL minhook xinputcheck*

# remove bundled libraries for mac
rm -r mach-override*

popd

# use system headers for audio backends
sed \
    -e 's|"${3RDPARTY_DIR}/jack"|"%{_includedir}/jack"|' \
    -e 's|"${3RDPARTY_DIR}/portaudio"|"%{_includedir}"|' \
    -e 's|"${3RDPARTY_DIR}/pipewire"|"%{_includedir}/pipewire-0.3" "%{_includedir}/spa-0.2"|' \
    -e 's|"${3RDPARTY_DIR}/pulseaudio"|"%{_includedir}/pulse"|' \
    -i src/mumble/CMakeLists.txt

%build

%cmake \
    -DBUILD_NUMBER=%{build_number} \
    %{?with_tests:-Dtests=ON} \
    -Dupdate=OFF \
    -Dbundled-opus=OFF \
    -Dbundled-speex=OFF \
    -Dbundled-rnnoise=OFF \
    -Dice=OFF \
    -Doverlay-xcompile=OFF \
    -DCMAKE_BUILD_TYPE=Release
%cmake_build
%install
%cmake_install
install -d -m 0755 %{buildroot}%{_datadir}/mumble/translations
install -p -m 0644 %{_vpath_builddir}/src/mumble/*.qm %{buildroot}%{_datadir}/mumble/translations
install -D -p -m 0664 scripts/murmur.ini %{buildroot}%{_sysconfdir}/murmur.ini
install -D -p -m 0644 %{SOURCE1} %{buildroot}%{_unitdir}/murmur.service
install -D -p -m 0644 %{SOURCE2} %{buildroot}%{_sysusersdir}/mumble-server.conf
install -D -p -m 0755 scripts/mumble-server-user-wrapper %{buildroot}%{_bindir}/mumble-server-user-wrapper
mkdir -p %{buildroot}%{_localstatedir}/lib/mumble-server/
mkdir -p %{buildroot}%{_sbindir}
ln -s %{_bindir}/mumble-server %{buildroot}%{_sbindir}/murmurd
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%check

appstream-util validate-relax --nonet %{buildroot}%{_metainfodir}/info.mumble.Mumble.appdata.xml
desktop-file-validate %{buildroot}%{_datadir}/applications/info.mumble.Mumble.desktop
%if %{with tests}
%ctest --exclude-regex 'TestSelfSignedCertificate'
%endif
%posttrans server

if [ -f %{_sysconfdir}/murmur/murmur.ini.rpmsave ]; then
    mv -vf %{_sysconfdir}/murmur.ini %{_sysconfdir}/murmur.ini.rpmnew
    mv -vf %{_sysconfdir}/murmur/murmur.ini.rpmsave %{_sysconfdir}/murmur.ini
fi
rmdir --ignore-fail-on-non-empty %{_sysconfdir}/murmur
%pre server

%sysusers_create_compat %{SOURCE2}
%post server

%systemd_post murmur.service
%preun server

%systemd_preun murmur.service
%postun server

%systemd_postun_with_restart murmur.service
%files -f %{oreon_filedir}/main.list
%files -n mumble-server -f %{oreon_filedir}/mumble-server.list
%files -n mumble-plugins -f %{oreon_filedir}/mumble-plugins.list
%files -n mumble-overlay -f %{oreon_filedir}/mumble-overlay.list

%changelog

%autochangelog
