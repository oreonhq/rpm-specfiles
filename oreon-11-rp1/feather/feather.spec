%global source1_hash 36b260fd45598b4c9b577b37cfa698ba047975cf7094f475e5a6c0d5cdc9912f
%global source0_hash 1db8cbc5123abc8de63c96e6aedc08a8cda669b032b75c18f955e71ce8c4291e
Name:          feather
Version:       2.8.1
Release:        1%{?dist}
Summary:        Monero desktop wallet
License:       BSD-3-Clause
URL:           https://featherwallet.org/
Source0:        https://featherwallet.org/files/releases/source/%{name}-%{version}.tar.gz
Source1:       https://featherwallet.org/files/releases/source/%{name}-%{version}.tar.gz.asc
Source2:       gpgkey-featherwallet.gpg
Source3:       feather.metainfo.xml
Patch0:        cmath.patch
Requires:      tor
ExcludeArch:   %{arm} %{ix86}
# oreon:deps
BuildRequires:  boost-chrono
BuildRequires:  boost-devel
BuildRequires:  boost-filesystem
BuildRequires:  boost-regex
BuildRequires:  boost-thread
BuildRequires:  cmake
BuildRequires:  gcc
BuildRequires:  gcc-c++
BuildRequires:  gnupg2
BuildRequires:  libgcrypt-devel
BuildRequires:  libsodium-devel
BuildRequires:  libusb1-devel
BuildRequires:  libzip-devel
BuildRequires:  ninja-build
BuildRequires:  openssl-devel
BuildRequires:  protobuf-lite-devel
BuildRequires:  qrencode-devel
BuildRequires:  qt6-qtbase-devel
BuildRequires:  qt6-qtmultimedia-devel
BuildRequires:  qt6-qtsvg-devel
BuildRequires:  qt6-qtwayland-devel
BuildRequires:  qt6-qtwebsockets-devel
BuildRequires:  unbound-devel
BuildRequires:  wayland-devel
BuildRequires:  zbar-devel
BuildRequires:  zeromq-devel
BuildRequires:  zxing-cpp-devel
# /oreon:deps
%description
Feather is a wallet for the Monero cryptocurrency.

%prep

%{gpgverify} --keyring=%{SOURCE2} --signature=%{SOURCE1} --data=%{SOURCE0}
%autosetup -p0

%build

%cmake -GNinja -DCMAKE_BUILD_TYPE=RelWithDebInfo -DARCH=default -DMANUAL_SUBMODULES=ON -DBUILD_SHARED_LIBS=OFF -DTOR_BIN=OFF -DDONATE_BEG=OFF -DWITH_SCANNER=ON -DUSE_DEVICE_TREZOR=ON
%cmake_build
%install
%cmake_install
install -Dpm644 %{SOURCE3} %{buildroot}%{_metainfodir}/%{name}.metainfo.xml
%oreon_autofiles main

%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
