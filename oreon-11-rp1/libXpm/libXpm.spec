# Copyright (C) 2026 Oreon HQ
# SPDX-License-Identifier: GPL-2.0-or-later

%global source0_hash ad3576d689221a39dc728f0e0dc02ca7bb6a0d724c9a77fd1bfa1e9af83be900
%global source1_hash e33484cfcb06069c0e1fdf5224286ec0972bf402c0699b9bbb4fc00937a7ef02
%global source2_hash 0f6afe1c35bf4207f3ed53f7155267e1c333108fc7f262f21c9b14c3712a8476
%{!?oreon_bootstrap:%global oreon_bootstrap %{nil}}
%bcond bootstrap 0
%oreon_bootstrap

Summary: X.Org X11 libXpm runtime library
Name: libXpm
Version: 3.5.19
Release:        %{autorelease}
License: MIT AND X11-distribute-modifications-variant
URL: https://www.x.org

Source0: https://www.x.org/pub/individual/lib/%{name}-%{version}.tar.xz
Source1: https://www.x.org/pub/individual/lib/%{name}-%{version}.tar.xz.sig
Source2: gpgkey-67DC86F2623FC5FD4BB5225D14706DBE1E4B4540.gpg

BuildRequires: oreon-rpm-macros
BuildRequires: clang
BuildRequires: gcc
BuildRequires: gettext
BuildRequires: gnupg2
BuildRequires: gzip
BuildRequires: make
BuildRequires: ncompress
BuildRequires: pkgconfig(glib-2.0)
BuildRequires: pkgconfig(x11)
BuildRequires: pkgconfig(xext)
BuildRequires: pkgconfig(xorg-macros) >= 1.16
BuildRequires: pkgconfig(xt)

%description
X.Org X11 libXpm runtime library

%package devel
Summary: X.Org X11 libXpm development package
Requires: %{name}%{?_isa} = %{version}-%{release}

%description devel
X.Org X11 libXpm development package

%prep
%oreon_sha256
echo '%{source1_hash}  %{SOURCE1}' | sha256sum -c -
echo '%{source2_hash}  %{SOURCE2}' | sha256sum -c -
%{gpgverify} --keyring=%{SOURCE2} --signature=%{SOURCE1} --data=%{SOURCE0}
%autosetup

%build
%configure --disable-static
%make_build

%check
%make_build check

%install
%make_install

find %{buildroot} -name '*.la' -delete

%files
%license COPYING
%doc AUTHORS ChangeLog README.md
%{_libdir}/libXpm.so.4
%{_libdir}/libXpm.so.4.11.0

%files devel
%{_bindir}/cxpm
%{_bindir}/sxpm
%{_includedir}/X11/xpm.h
%{_libdir}/libXpm.so
%{_libdir}/pkgconfig/xpm.pc
%{_mandir}/man1/*.1*
%{_mandir}/man3/*.3*

%changelog
%autochangelog
