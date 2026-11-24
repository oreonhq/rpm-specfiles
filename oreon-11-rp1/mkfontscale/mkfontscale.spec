# Copyright (C) 2026 Oreon HQ
# SPDX-License-Identifier: GPL-2.0-or-later

%global source0_hash a01492a17a9b6c0ee3f92ee578850e305315b9f298da5f006a1cd4b51db01a5e
%global source1_hash d9982e3988128eba31f4384504618bddf4e1fd4228e8268c8ccdc7af643b2858
%global source2_hash 0b2174ac1add86ca6ebe076e2dab00446aa5f2816d2d71389d570fdd0bf68cc8
%{!?oreon_bootstrap:%global oreon_bootstrap %{nil}}
%bcond bootstrap 0
%oreon_bootstrap

Name:       mkfontscale
Version:    1.2.4
Release:        %{autorelease}
Summary:    Tool to generate legacy X11 font system index files

License:    MIT-open-group AND X11 AND MIT AND HPND-sell-variant
URL:        https://www.x.org
Source0:    https://www.x.org/pub/individual/app/%{name}-%{version}.tar.xz
Source1:    https://www.x.org/pub/individual/app/%{name}-%{version}.tar.xz.sig
Source2:    gpgkey-3AB285232C46AE43D8E192F4DAB0F78EA6E7E2D2.gpg

Patch0:     mkfontscale-examine-all-encodings.patch

BuildRequires: oreon-rpm-macros
BuildRequires: clang
BuildRequires: gcc
BuildRequires: gnupg2
BuildRequires: meson
BuildRequires: pkgconfig(fontenc)
BuildRequires: pkgconfig(freetype2)
BuildRequires: pkgconfig(xproto) >= 7.0.25
BuildRequires: pkgconfig(zlib)

Provides:   mkfontdir = %{version}

%description
mkfontscale creates the fonts.scale and fonts.dir index files used by the
legacy X11 font system.  It now includes the mkfontdir script previously
distributed separately for compatibility with older X11 versions.

%prep
%oreon_sha256
echo '%{source1_hash}  %{SOURCE1}' | sha256sum -c -
echo '%{source2_hash}  %{SOURCE2}' | sha256sum -c -
%{gpgverify} --keyring='%{SOURCE2}' --signature='%{SOURCE1}' --data='%{SOURCE0}'
%autosetup

%build
%meson
%meson_build

%install
%meson_install

%check
%meson_test

%files
%license COPYING
%{_bindir}/mkfontdir
%{_bindir}/mkfontscale
%{_mandir}/man1/mkfontdir.1*
%{_mandir}/man1/mkfontscale.1*

%changelog
%autochangelog
