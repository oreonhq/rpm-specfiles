# Copyright (C) 2026 Oreon HQ
# SPDX-License-Identifier: GPL-2.0-or-later

%global source0_hash 35b4d5882d675c9ab3063d534b3c5fd51542fcb5ce0396eb9a67dc5b5c1ec3f6
%global source1_hash 458dc0fe80fde08ff4298b362b3bce8219f519e3c323657b4f3e3fbc8a25fb99
%{!?oreon_bootstrap:%global oreon_bootstrap %{nil}}
%bcond bootstrap 0
%oreon_bootstrap

Name:           decklink
Version:        16.0
Release:        %{autorelease}
Summary:        BlackMagic Design SDK for DeckLink

License:        BSL-1.0
URL:            https://www.blackmagicdesign.com/desktopvideo_sdk
Source0:        %{name}-%{version}.tar.gz
Source1:        %{name}-tarball.sh

BuildArch:      noarch

%description
This is a bare version of the DeckLink SDK from BlackMagic Design. The
original, fully featured with examples, can be found at
https://www.blackmagicdesign.com/desktopvideo_sdk

The C++ Header and Source files are licensed under the Boost License
with the copyright owned by BlackMagic Design. This license is an OSI
approved MIT-like and compatible with the GPLv2.

%package devel
Summary: BlackMagic Design SDK for DeckLink - header files
Provides: %{name}-static = %{version}-%{release}

%description devel
This is a bare version of the DeckLink SDK from BlackMagic Design. The
original, fully featured with examples, can be found at
https://www.blackmagicdesign.com/desktopvideo_sdk

The C++ Header and Source files are licensed under the Boost License
with the copyright owned by BlackMagic Design. This license is an OSI
approved MIT-like and compatible with the GPLv2.

%prep
%oreon_sha256
echo '%{source1_hash}  %{SOURCE1}' | sha256sum -c -
%autosetup

%build

%install
install -d %{buildroot}%{_includedir}/decklink
install -pm644 Linux/include/*.{h,cpp} %{buildroot}%{_includedir}/decklink

%files devel
%dir %{_includedir}/decklink
%{_includedir}/decklink/DeckLinkAPI*.h
%{_includedir}/decklink/DeckLinkAPIDispatch*.cpp
%{_includedir}/decklink/LinuxCOM.h

%changelog
%autochangelog
