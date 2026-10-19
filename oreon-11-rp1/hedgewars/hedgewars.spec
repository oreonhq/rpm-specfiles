%global source0_hash c5c1877c0bae1354c75d2b9527b6f9a9f79e99932e5d08b1f6f7de1708066130
%global _cmake_generator "Unix Makefiles"
Name:           hedgewars
Version:        1.0.3
Release:        1%{?dist}
Summary:        Funny turn-based artillery game, featuring fighting Hedgehogs!
License:        GPL-1.0-or-later
URL:            http://www.hedgewars.org/
ExcludeArch:    %{ix86}
Source0:        http://www.hedgewars.org/download/releases/%{name}-src-%{version}.tar.bz2
Source100:      hedgewars.service
Source101:      hedgewars.sysconfig
Source102:      hedgewars.xml
Patch0:         rpath-fix.patch
Patch1:         hedgewars-clang.patch
Patch2:        hedgewars-1.0.0-install-hwengine.patch
Patch3:        0a8921bf167481045830095c731eb3c67af913e4.patch
Patch4:        https://patch-diff.githubusercontent.com/raw/hedgewars/hw/pull/75.patch
Patch5:        hedgewars-mtl-2.3.patch
Requires:       dejavu-sans-fonts wqy-zenhei-fonts hicolor-icon-theme
Requires:       hedgewars-data = %{version}-%{release}
ExclusiveArch:  %{fpc_arches}
ExcludeArch: ppc64le
# oreon:deps
BuildRequires:  SDL2_image-devel
BuildRequires:  SDL2_mixer-devel
BuildRequires:  SDL2_net-devel
BuildRequires:  SDL2_ttf-devel
BuildRequires:  chrpath
BuildRequires:  clang
BuildRequires:  cmake
BuildRequires:  cmake(Qt5LinguistTools)
BuildRequires:  cmake(Qt5Quick)
BuildRequires:  compat-lua-devel
BuildRequires:  dejavu-sans-fonts
BuildRequires:  desktop-file-utils
BuildRequires:  fpc
BuildRequires:  gcc-c++
BuildRequires:  ghc-SHA-devel
BuildRequires:  ghc-containers-devel
BuildRequires:  ghc-deepseq-devel
BuildRequires:  ghc-entropy-devel
BuildRequires:  ghc-hslogger-devel
BuildRequires:  ghc-network-bsd-devel
BuildRequires:  ghc-network-devel
BuildRequires:  ghc-process-devel
BuildRequires:  ghc-random-devel
BuildRequires:  ghc-regex-tdfa-devel
BuildRequires:  ghc-sandi-devel
BuildRequires:  ghc-utf8-string-devel
BuildRequires:  ghc-vector-devel
BuildRequires:  ghc-zlib-devel
BuildRequires:  glew-devel
BuildRequires:  libatomic
BuildRequires:  libavformat-free-devel
BuildRequires:  libpng-devel
BuildRequires:  openssl-devel
BuildRequires:  physfs-devel
BuildRequires:  qt5-qtbase-devel
BuildRequires:  qt5-qtbase-private-devel
BuildRequires:  systemd
BuildRequires:  wqy-zenhei-fonts
# /oreon:deps
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

%define toolchain clang
%define _legacy_common_support 1
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
%if "%{?_lib}" == "lib64"
  mv %{buildroot}/usr/lib %{buildroot}/usr/lib64
%endif
chrpath --delete %{buildroot}/usr/bin/*
desktop-file-validate %{buildroot}/%{_datadir}/applications/hedgewars.desktop
desktop-file-validate %{buildroot}/%{_datadir}/applications/hwengine.desktop
mkdir -p %{buildroot}%{_datadir}/icons/hicolor/32x32/apps
install -p -m 644 misc/hedgewars_ico.png \
  %{buildroot}%{_datadir}/icons/hicolor/32x32/apps/hedgewars.png
mkdir -p %{buildroot}%{_datadir}/icons/hicolor/512x512/apps
install -p -m 644 misc/hedgewars.png \
  %{buildroot}%{_datadir}/icons/hicolor/512x512/apps/%{name}.png
mkdir -p %{buildroot}%{_unitdir} %{buildroot}%{_sysconfdir}/sysconfig \
         %{buildroot}%{_prefix}/lib/firewalld/services
install -pm 0644 %{SOURCE100} %{buildroot}%{_unitdir}/
install -pm 0644 %{SOURCE101} %{buildroot}%{_sysconfdir}/sysconfig/%{name}
install -pm 0644 %{SOURCE102} %{buildroot}%{_prefix}/lib/firewalld/services/
%ldconfig_scriptlets
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%post server

%systemd_post %{name}.service
%{?firewalld_reload}
%preun server

%systemd_preun %{name}.service
%postun server

%systemd_postun_with_restart %{name}.service
%files -f %{oreon_filedir}/main.list
%files -n hedgewars-server -f %{oreon_filedir}/hedgewars-server.list
%files -n hedgewars-data -f %{oreon_filedir}/hedgewars-data.list

%changelog

%autochangelog
