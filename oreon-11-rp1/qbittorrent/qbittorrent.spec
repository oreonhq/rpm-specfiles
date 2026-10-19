%global source2_hash ec02d1f01620c19ee2392a71d4bfb6402a686fd79ada2397027a7885c2e37f31
%global source1_hash 473cce7003f17647602897ab7ef197b4607708945e3e611e51f10b104f7c6172
%global source0_hash 7573621859da7287ba708378ea9f5eb12f30962a1a7c28eba5f44ecf8c4c114c
Name:    qbittorrent
Summary:        A Bittorrent Client
Epoch:   1
Version: 5.2.3
Release:        1%{?dist}
License: GPL-2.0-or-later
URL:     https://www.qbittorrent.org
Source0:        https://downloads.sourceforge.net/%{name}/%{name}-%{version}.tar.xz
Source1: https://downloads.sourceforge.net/%{name}/%{name}-%{version}.tar.xz.asc
Source2: https://github.com/qbittorrent/qBittorrent/raw/master/5B7CC9A2.asc
Source3: qbittorrent-nox.README
ExcludeArch:   %{ix86}
Requires: python3
Recommends: (qgnomeplatform-qt6%{?_isa} if gnome-shell)
Recommends: (qgnomeplatform-qt6%{?_isa} if cinnamon)
Requires:   qt6-qtsvg%{?_isa}
# oreon:deps
BuildRequires:  boost-devel
BuildRequires:  cmake
BuildRequires:  cmake(Qt6Core)
BuildRequires:  cmake(Qt6Gui)
BuildRequires:  cmake(Qt6LinguistTools)
BuildRequires:  cmake(Qt6Svg)
BuildRequires:  desktop-file-utils
BuildRequires:  gcc-c++
BuildRequires:  gnupg2
BuildRequires:  libappstream-glib
BuildRequires:  libxkbcommon-devel
BuildRequires:  ninja-build
BuildRequires:  openssl-devel-engine
BuildRequires:  qt6-linguist
BuildRequires:  qt6-qtbase-private-devel
BuildRequires:  rb_libtorrent-devel
BuildRequires:  systemd
BuildRequires:  zlib-ng-compat-static
# /oreon:deps
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
pushd build-nox
%cmake_install
popd
pushd build
%cmake_install
popd
desktop-file-install \
  --dir=%{buildroot}%{_datadir}/applications/ \
  %{buildroot}%{_datadir}/applications/org.qbittorrent.qBittorrent.desktop
appstream-util validate-relax --nonet %{buildroot}%{_metainfodir}/org.qbittorrent.qBittorrent.metainfo.xml
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%files -f %{oreon_filedir}/main.list
%files -n qbittorrent-nox -f %{oreon_filedir}/qbittorrent-nox.list

%changelog

%autochangelog
