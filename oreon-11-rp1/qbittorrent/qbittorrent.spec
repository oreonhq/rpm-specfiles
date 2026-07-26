%global source0_hash d5d0c2b78386cde08951eaad930ec353d22e69205e163cc39dcfca2400353979

Name:    qbittorrent
Summary: A Bittorrent Client
Epoch:   1
Version: 5.1.4
Release: 2%{?dist}
# Automatically converted from old format: GPLv2+ - review is highly recommended.
License: GPL-2.0-or-later
URL:     https://www.qbittorrent.org

Source0: https://downloads.sourceforge.net/%{name}/%{name}-%{version}.tar.xz
Source1: https://downloads.sourceforge.net/%{name}/%{name}-%{version}.tar.xz.asc
Source2: https://github.com/qbittorrent/qBittorrent/raw/master/5B7CC9A2.asc
Source3: qbittorrent-nox.README

ExcludeArch:   %{ix86}

BuildRequires: cmake
BuildRequires: gcc-c++
BuildRequires: gnupg2
BuildRequires: ninja-build
BuildRequires: systemd
BuildRequires: cmake(Qt6Core)
BuildRequires: cmake(Qt6Gui)
BuildRequires: cmake(Qt6Svg)
BuildRequires: cmake(Qt6LinguistTools)
BuildRequires: libxkbcommon-devel
BuildRequires: qt6-qtbase-private-devel
BuildRequires: qt6-linguist
BuildRequires: rb_libtorrent-devel >= 1.2.12
BuildRequires: desktop-file-utils
BuildRequires: boost-devel >= 1.60
BuildRequires: libappstream-glib
BuildRequires: openssl-devel-engine
BuildRequires: zlib-ng-compat-static

Requires: python3
Recommends: (qgnomeplatform-qt6%{?_isa} if gnome-shell)
Recommends: (qgnomeplatform-qt6%{?_isa} if cinnamon)
Requires:   qt6-qtsvg%{?_isa}

%description
A Bittorrent client using rb_libtorrent and a Qt6 Graphical User Interface.
It aims to be as fast as possible and to provide multi-OS, unicode support.

%package nox
Summary: A Headless Bittorrent Client

%description nox
A Headless Bittorrent client using rb_libtorrent.
It aims to be as fast as possible and to provide multi-OS, unicode support.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%{gpgverify} --keyring='%{SOURCE2}' --signature='%{SOURCE1}' --data='%{SOURCE0}'
%autosetup -p1
cp %{SOURCE3} .

%build
mkdir build-nox
pushd build-nox
%cmake \
 -DSYSTEMD=ON \
 -Wno-dev \
 -GNinja \
 -DQT6=ON \
 -DGUI=OFF \
 ..
%cmake_build
popd

# Build gui version
mkdir build
pushd build
%cmake \
 -Wno-dev \
 -DQT6=ON \
 -GNinja \
 ..
%cmake_build
popd

%install
# install headless version
pushd build-nox
%cmake_install
popd

# install gui version
pushd build
%cmake_install
popd

desktop-file-install \
  --dir=%{buildroot}%{_datadir}/applications/ \
  %{buildroot}%{_datadir}/applications/org.qbittorrent.qBittorrent.desktop

appstream-util validate-relax --nonet %{buildroot}%{_metainfodir}/org.qbittorrent.qBittorrent.metainfo.xml

%files
%license COPYING
%doc README.md AUTHORS Changelog
%{_bindir}/qbittorrent
%{_metainfodir}/org.qbittorrent.qBittorrent.metainfo.xml
%{_datadir}/applications/org.qbittorrent.qBittorrent.desktop
%{_datadir}/icons/hicolor/*/apps/qbittorrent.*
%{_datadir}/icons/hicolor/*/status/qbittorrent-tray*
%{_mandir}/man1/qbittorrent.1*
%{_mandir}/ru/man1/qbittorrent.1*

%files nox
%license COPYING
%doc qbittorrent-nox.README AUTHORS Changelog
%{_bindir}/qbittorrent-nox
%{_unitdir}/qbittorrent-nox@.service
%{_mandir}/man1/qbittorrent-nox.1*
%{_mandir}/ru/man1/qbittorrent-nox.1*

%changelog
%autochangelog
