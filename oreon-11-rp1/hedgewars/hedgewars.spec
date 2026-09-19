%global source0_hash none

%global _cmake_generator "Unix Makefiles"

Name:           hedgewars
Version:        1.0.3
Release:        4%{?dist}
Summary:        Funny turn-based artillery game, featuring fighting Hedgehogs!
License:        GPL-1.0-or-later
URL:            http://www.hedgewars.org/

ExcludeArch:    %{ix86}

Source0:        http://www.hedgewars.org/download/releases/%{name}-src-%{version}.tar.bz2
# SystemD service file for hedgewars-server
Source100:      hedgewars.service
# Environment file for systemd
Source101:      hedgewars.sysconfig
# FirewallD config
Source102:      hedgewars.xml

# Prevent use of rpath
Patch0:         rpath-fix.patch

# Tweak CFLAGS for clang
Patch1:         hedgewars-clang.patch

# Install hwengine.desktop
Patch2:        hedgewars-1.0.0-install-hwengine.patch

Patch3:        0a8921bf167481045830095c731eb3c67af913e4.patch

# fix pas2c for ghc-9.4
# https://github.com/hedgewars/hw/pull/75
Patch4:        https://patch-diff.githubusercontent.com/raw/hedgewars/hw/pull/75.patch
Patch5:        hedgewars-mtl-2.3.patch

BuildRequires:  cmake gcc-c++ fpc desktop-file-utils
BuildRequires:  libatomic
BuildRequires:  qt5-qtbase-devel
BuildRequires:  qt5-qtbase-private-devel
BuildRequires:  cmake(Qt5LinguistTools)
BuildRequires:  cmake(Qt5Quick)
BuildRequires:  SDL2_mixer-devel SDL2_net-devel SDL2_image-devel SDL2_ttf-devel
BuildRequires:  openssl-devel libpng-devel physfs-devel glew-devel
BuildRequires:  dejavu-sans-fonts wqy-zenhei-fonts clang
Requires:       dejavu-sans-fonts wqy-zenhei-fonts hicolor-icon-theme
Requires:       hedgewars-data = %{version}-%{release}

ExclusiveArch:  %{fpc_arches}
ExcludeArch: ppc64le

%description
Hedgewars is a turn based strategy game but the real buzz is from watching the
devastation caused by those pesky hedgehogs with those fantastic weapons.

Each player controls a team of several hedgehogs. During the course of the
game, players take turns with one of their hedgehogs. They then use whatever
tools and weapons are available to attack and kill the opponents' hedgehogs,
thereby winning the game. Hedgehogs may move around the terrain in a variety
of ways, normally by walking and jumping but also by using particular tools
such as the "Rope" or "Parachute", to move to otherwise inaccessible areas.

%package server
Summary:        Standalone server for hedgewars
Requires:       %{name}%{?_isa} = %{version}-%{release}
BuildRequires:  ghc-SHA-devel
BuildRequires:  ghc-containers-devel
BuildRequires:  ghc-deepseq-devel
BuildRequires:  ghc-entropy-devel
BuildRequires:  ghc-hslogger-devel
BuildRequires:  ghc-network-devel
BuildRequires:  ghc-network-bsd-devel
BuildRequires:  ghc-process-devel
BuildRequires:  ghc-random-devel
BuildRequires:  ghc-regex-tdfa-devel
BuildRequires:  ghc-sandi-devel
BuildRequires:  ghc-utf8-string-devel
BuildRequires:  ghc-vector-devel
BuildRequires:  ghc-zlib-devel
BuildRequires:  compat-lua-devel
BuildRequires:  systemd
BuildRequires:  chrpath
BuildRequires:  libavformat-free-devel
%{?systemd_requires}

%description server
A standalone server that can be used for LAN play or a private internet server.

%package data
BuildArch:      noarch
Summary:        Game data for %{name}

%description data
Game data for %{name}.

%prep
%autosetup -p1 -n %{name}-src-%{version}

# Make sure that we don't use bundled libraries
rm -r misc/liblua

# Fix these to files as pas2c choked on the UTF-8 files.
for file in hedgewars/uSound.pas hedgewars/uStats.pas; do
    iconv -f utf-8 -t ascii//TRANSLIT $file -o $file.tmp;
    mv $file.tmp $file;
done

%build
# We follow upstream and build with clang, some of the rpm macros need to know this:
# 1. This sets _lto_cflags for clang rather then gcc
# 2. This fixes armv7hl build in combination with .package.note generation
%define toolchain clang

# https://bugzilla.redhat.com/show_bug.cgi?id=1878396
%define _legacy_common_support 1

# -DMINIMAL_FLAGS=1 uses distro complie flags as much as possible

# -DNOVIDEOREC=1 disables video recording which for now needs
# things Fedora can't provide.

# -DGHFLAGS=-dynamic uses dynamic linking for Haskell, but this isn't
# available on arm.

# -DFONTS_DIRS="`find %{_datadir}/fonts -type d -printf '%p;'`"
# makes sure the system fonts are used. This avoids problems with physfs access
# and having to symlink font files.

export CFLAGS="%{build_cflags} -DGL_GLEXT_PROTOTYPES"
export CXXFLAGS="%{build_cxxflags} -DGL_GLEXT_PROTOTYPES"
%ifarch %{arm}
%cmake -DMINIMAL_FLAGS=1 -DNOVIDEOREC=1 -DBUILD_ENGINE_C=1 -DFONTS_DIRS="`find %{_datadir}/fonts -type d -printf '%p;'`"
%else
%cmake -DMINIMAL_FLAGS=1 -DNOVIDEOREC=1 -DBUILD_ENGINE_C=1 -DGHFLAGS=-dynamic -DFONTS_DIRS="`find %{_datadir}/fonts -type d -printf '%p;'`"i
%endif

sed -i "s|/usr/local|/usr|g" redhat-linux-build/cmake_install.cmake
sed -i "s|/usr/local|/usr|g" redhat-linux-build/CMakeCache.txt

%cmake_build

%install
%cmake_install

# Ugh. If you can get cmake to do the right thing, be my guest. GC 9/26/2025
%if "%{?_lib}" == "lib64"
  mv %{buildroot}/usr/lib %{buildroot}/usr/lib64
%endif

chrpath --delete %{buildroot}/usr/bin/*

# below is the desktop file and icon stuff.
desktop-file-validate %{buildroot}/%{_datadir}/applications/hedgewars.desktop
desktop-file-validate %{buildroot}/%{_datadir}/applications/hwengine.desktop
mkdir -p %{buildroot}%{_datadir}/icons/hicolor/32x32/apps
install -p -m 644 misc/hedgewars_ico.png \
  %{buildroot}%{_datadir}/icons/hicolor/32x32/apps/hedgewars.png
mkdir -p %{buildroot}%{_datadir}/icons/hicolor/512x512/apps
install -p -m 644 misc/hedgewars.png \
  %{buildroot}%{_datadir}/icons/hicolor/512x512/apps/%{name}.png

# Install systemd and firewalld files for hedgewars-server
mkdir -p %{buildroot}%{_unitdir} %{buildroot}%{_sysconfdir}/sysconfig \
         %{buildroot}%{_prefix}/lib/firewalld/services
install -pm 0644 %{SOURCE100} %{buildroot}%{_unitdir}/
install -pm 0644 %{SOURCE101} %{buildroot}%{_sysconfdir}/sysconfig/%{name}
install -pm 0644 %{SOURCE102} %{buildroot}%{_prefix}/lib/firewalld/services/

%ldconfig_scriptlets

%post server
%systemd_post %{name}.service
%{?firewalld_reload}

%preun server
%systemd_preun %{name}.service

%postun server
%systemd_postun_with_restart %{name}.service

%files
%doc README README.md
%license COPYING
%{_bindir}/%{name}
%{_bindir}/hwengine
%attr(644, -, -) %{_datadir}/appdata/*
%{_datadir}/applications/hedgewars.desktop
%{_datadir}/icons/hicolor/*/apps/%{name}.png
%{_datadir}/pixmaps/hedgewars.xpm
%{_datadir}/applications/hwengine.desktop
%{_libdir}/libphyslayer.so.1.0
%{_libdir}/libphyslayer.so
%{_libdir}/libavwrapper.so.1.0
%{_libdir}/libavwrapper.so

%files server
%{_bindir}/%{name}-server
%{_prefix}/lib/firewalld/services/%{name}.xml
%{_sysconfdir}/sysconfig/%{name}
%{_unitdir}/%{name}.service

%files data
%dir %{_datadir}/%{name}
%dir %{_datadir}/%{name}/Data
%{_datadir}/%{name}/Data/Graphics
%{_datadir}/%{name}/Data/Maps
%{_datadir}/%{name}/Data/Missions
%{_datadir}/%{name}/Data/Names
%{_datadir}/%{name}/Data/Sounds
%{_datadir}/%{name}/Data/Forts
%{_datadir}/%{name}/Data/Locale
%{_datadir}/%{name}/Data/misc
%{_datadir}/%{name}/Data/Music
%{_datadir}/%{name}/Data/Scripts
%{_datadir}/%{name}/Data/Themes
# Symlinking fonts doesn't work, we have to bundle them.
%{_datadir}/%{name}/Data/Fonts/DejaVuSans-Bold.ttf
%{_datadir}/%{name}/Data/Fonts/wqy-zenhei.ttc

%changelog
%autochangelog
