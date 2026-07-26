%global source0_hash 378e61d5bfa58ba51bfbb645067f459214a9872da09b306f2c2c3f1902200547

# Test suite only works on x86_64
# https://github.com/mumble-voip/mumble/issues/3845
%ifarch x86_64
%bcond_without tests
%endif

%global build_number 287

Name:           mumble
Version:        1.4.%{build_number}
Release:        10%{?dist}
Summary:        Low-latency and high-quality voice-chat program
# primary license: BSD-3-Clause
# themes/Mumble: Unlicense and WTFPL
# 3rdparty/arc4random: ISC
# 3rdparty/celt-0.7.0-src: BSD-3-Clause and GPL-2.0-or-later
# 3rdparty/qqbonjour: BSD-3-Clause
# 3rdparty/smallft: BSD-3-Clause
License:        BSD-3-Clause AND Unlicense AND WTFPL AND ISC AND GPL-2.0-or-later
URL:            https://www.mumble.info
Source:         https://github.com/mumble-voip/mumble/releases/download/v%{version}/mumble-%{version}.tar.gz
Source1:        murmur.service
Source2:        mumble-server.sysusers

# patches from the upstream master branch
# https://github.com/mumble-voip/mumble/commit/f4cea62ed95e4967d8591f25e903f5e8fc2e2a30
Patch:          0001-BUILD-crypto-Migrate-to-OpenSSL-3.0-compatible-API.patch
# https://github.com/mumble-voip/mumble/commit/f8d47db318f302f5a7d343f15c9936c7030c49c4
Patch:          0002-FIX-crypto-Sharing-EVP-context-between-threads-crushes-Mumble.patch
# https://github.com/mumble-voip/mumble/pull/6775
Patch:          0003-BUILD-overlay-Fix-building-with-GCC-15.patch

# downstream-only patches
# https://docs.fedoraproject.org/en-US/packaging-guidelines/CryptoPolicies/
Patch:          0004-CHANGE-server-Default-to-system-crypto-policy.patch
Patch:          0005-FIX-client-Avoid-loading-unversioned-libraries.patch

BuildRequires:  cmake
BuildRequires:  gcc-c++

# Referencing build requirements:
#
# - Find instances of find_pkg and find_library in the mumble source code.
# - Ensure that the instance applies based on the conditionals.
# - Check if anything provides cmake(<name>).  If found use that.
# - Check the modules from cmake-data (/usr/share/cmake/Modules/) to see if any
#   locate it by a file path.  If found use exact package name.
# - Check if anything provides pkgconfig(<name>).  If found, use that.
#
# docs/dev/build-instructions/cmake_options.md
#
# That should cover most scenarios.  If you are working on this spec file and
# find another scenario, please add it to this list.

# cmake/os.cmake
BuildRequires:  pkgconfig(openssl)
BuildRequires:  cmake(Qt5)

# cmake/qt-utils.cmake
BuildRequires:  cmake(Qt5LinguistTools)
BuildRequires:  python3

# src/CMakeLists.txt
BuildRequires:  cmake(Qt5Core)
BuildRequires:  cmake(Qt5Network)
BuildRequires:  cmake(Qt5Xml)
BuildRequires:  pkgconfig(libcrypto)
BuildRequires:  pkgconfig(libssl)
BuildRequires:  pkgconfig(protobuf)

# src/mumble/CMakeLists.txt
BuildRequires:  cmake(Qt5Concurrent)
BuildRequires:  cmake(Qt5Sql)
BuildRequires:  cmake(Qt5Svg)
BuildRequires:  cmake(Qt5Widgets)
BuildRequires:  cmake(PocoXML)
BuildRequires:  cmake(PocoZip)
BuildRequires:  pkgconfig(sndfile)
BuildRequires:  boost-devel
BuildRequires:  libXext-devel
BuildRequires:  libXi-devel
BuildRequires:  glibc-devel
BuildRequires:  pkgconfig(opus)
BuildRequires:  pkgconfig(speex)
BuildRequires:  pkgconfig(speexdsp)
BuildRequires:  pkgconfig(rnnoise)
BuildRequires:  pkgconfig(speech-dispatcher)
BuildRequires:  cmake(Qt5DBus)
BuildRequires:  pkgconfig(avahi-compat-libdns_sd)
BuildRequires:  alsa-lib-devel
BuildRequires:  pipewire-jack-audio-connection-kit-devel
BuildRequires:  pipewire-devel
BuildRequires:  portaudio-devel
BuildRequires:  pulseaudio-libs-devel

%if %{with tests}
# src/tests/CMakeLists.txt
BuildRequires:  cmake(Qt5Test)
%endif

# multiple files in 3rdparty/celt-0.7.0-src
BuildRequires:  libogg-devel

# appstream-util in %%check
BuildRequires:  libappstream-glib
# desktop-file-validate in %%check
BuildRequires:  desktop-file-utils

# There are multiple available audio backends which are opened at runtime.
# They aren't linked against, but they are opened by the library name.
# https://github.com/mumble-voip/mumble/issues/3794
%if 0%{?__isa_bits} == 32
%global libsymbolsuffix %{nil}
%else
%global libsymbolsuffix ()(%{__isa_bits}bit)
%endif
# src/mumble/JackAudio.cpp
Recommends:     libjack.so.0%{libsymbolsuffix}
# to prefer the pipewire implementation of libjack
Suggests:       pipewire-jack-audio-connection-kit
# src/mumble/PAAudio.cpp
Recommends:     libportaudio.so.2%{libsymbolsuffix}
# src/mumble/PipeWire.cpp
Recommends:     libpipewire-0.3.so.0%{libsymbolsuffix}
# src/mumble/PulseAudio.cpp
Recommends:     libpulse.so.0%{libsymbolsuffix}

# modified version of OpenBSD's arc4random
Provides:       bundled(arc4random)
# old version of celt for compatibility
Provides:       bundled(celt) = 0.7.0
# modified version of Qt Quarterly example code
Provides:       bundled(qqbonjour)
# modified version of vorbis's smallft
Provides:       bundled(smallft)

ExcludeArch:    %{ix86}

%global _privatelibs libcelt0[.]so.*
%global __provides_exclude ^(%{_privatelibs})$
%global __requires_exclude ^(%{_privatelibs})$

%description
Mumble is an Open Source, low-latency and high-quality voice-chat program
written on top of Qt and Opus.

%package server
Summary:        Mumble voice chat server

# Renamed from murmur to mumble-server, per upstream preference.  Obsoletes
# added in F37, can be removed in F39.
# https://github.com/mumble-voip/mumble/issues/5436#issuecomment-1084917505
Provides:       murmur = %{version}-%{release}
Obsoletes:      murmur < 1.3.4-10

# src/murmur/CMakeLists.txt
BuildRequires:  cmake(Qt5Sql)
BuildRequires:  libcap-devel
BuildRequires:  pkgconfig(avahi-compat-libdns_sd)
BuildRequires:  cmake(Qt5DBus)

BuildRequires:  systemd-rpm-macros

# To be able to announce the presence of the server via Bonjour.
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

# translations
install -d -m 0755 %{buildroot}%{_datadir}/mumble/translations
install -p -m 0644 %{_vpath_builddir}/src/mumble/*.qm %{buildroot}%{_datadir}/mumble/translations

install -D -p -m 0664 scripts/murmur.ini %{buildroot}%{_sysconfdir}/murmur.ini
install -D -p -m 0644 %{SOURCE1} %{buildroot}%{_unitdir}/murmur.service
install -D -p -m 0644 %{SOURCE2} %{buildroot}%{_sysusersdir}/mumble-server.conf
install -D -p -m 0755 scripts/mumble-server-user-wrapper %{buildroot}%{_bindir}/mumble-server-user-wrapper

# dir for mumble-server.sqlite
mkdir -p %{buildroot}%{_localstatedir}/lib/mumble-server/

# compatibility symlinks
mkdir -p %{buildroot}%{_sbindir}
ln -s %{_bindir}/mumble-server %{buildroot}%{_sbindir}/murmurd

%check
appstream-util validate-relax --nonet %{buildroot}%{_metainfodir}/info.mumble.Mumble.appdata.xml
desktop-file-validate %{buildroot}%{_datadir}/applications/info.mumble.Mumble.desktop

%if %{with tests}
# TestSelfSignedCertificate worked as recently as F41, but something has
# changed that is causing it to fail now and I haven't figured out what yet.
%ctest --exclude-regex 'TestSelfSignedCertificate'
%endif

# added in F37, can be removed in F39
%posttrans server
# relocation of config file
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

%files
%license LICENSE
%doc README.md CHANGES
%{_bindir}/mumble
%{_mandir}/man1/mumble.1*
%{_datadir}/icons/hicolor/256x256/apps/mumble.png
%{_datadir}/icons/hicolor/scalable/apps/mumble.svg
%{_datadir}/applications/info.mumble.Mumble.desktop
%{_metainfodir}/info.mumble.Mumble.appdata.xml
%{_datadir}/mumble/
%dir %{_libdir}/mumble/
%{_libdir}/mumble/libcelt0.so
%{_libdir}/mumble/libcelt0.so.0.7.0

%files server
%license LICENSE
%doc README.md CHANGES
%{_bindir}/mumble-server
%{_bindir}/mumble-server-user-wrapper
%{_mandir}/man1/mumble-server.1*
%{_mandir}/man1/mumble-server-user-wrapper.1*
%{_sbindir}/murmurd
%{_unitdir}/murmur.service
%{_sysusersdir}/mumble-server.conf
%config(noreplace) %attr(664,mumble-server,mumble-server) %{_sysconfdir}/murmur.ini
%dir %attr(-,mumble-server,mumble-server) %{_localstatedir}/lib/mumble-server/

%files plugins
%{_libdir}/mumble/plugins/

%files overlay
%{_bindir}/mumble-overlay
%{_mandir}/man1/mumble-overlay.1*
%{_libdir}/mumble/libmumbleoverlay.so
%{_libdir}/mumble/libmumbleoverlay.so.%{version}

%changelog
%autochangelog
