# Copyright (C) 2026 Oreon HQ
# SPDX-License-Identifier: GPL-2.0-or-later

%global source0_hash 0209b7d0f22c96abb416722ed735b0933be47931ecff4aa4b26ded7760b4f252
%global source1_hash bea1633b4536765683a82dbe280368388c49da91fffd032d465b0d4ca931887b
%global source2_hash 29c8ffc9ffee2982ad3c3355736ed043377c1f0f4ea4776df4b98a464692b70e
%{!?oreon_bootstrap:%global oreon_bootstrap %{nil}}
%bcond bootstrap 0
%oreon_bootstrap

%global maj 0

Name:       sratom
Version:    0.6.22
Release:        %{autorelease}
Summary:    A C library for serializing LV2 plugins

License:    MIT
URL:        https://drobilla.net/software/%{name}
Source0:    https://download.drobilla.net/%{name}-%{version}.tar.xz
Source1:    https://download.drobilla.net/%{name}-%{version}.tar.xz.sig
Source2:    https://drobilla.net/drobilla.gpg

BuildRequires: oreon-rpm-macros
BuildRequires: clang
BuildRequires: gcc
BuildRequires:  doxygen
BuildRequires:  gnupg2
BuildRequires:  graphviz
BuildRequires:  meson
BuildRequires:  pkgconfig(sord-0) >= 0.16.16
BuildRequires:  pkgconfig(serd-0) >= 0.30.10
BuildRequires:  pkgconfig(lv2) >= 1.18.4
BuildRequires:  python3-sphinx
BuildRequires:  python3-sphinx_lv2_theme
BuildRequires:  python3-sphinxygen

%description
%{name} is a C library for serializing LV2 atoms to/from Turtle. It is
intended to be a full serialization solution for LV2 atoms, allowing
implementations to serialize binary atoms to strings and read them back again.
This is particularly useful for saving plugin state, or implementing plugin
control with network transparency.

%package devel
Summary:    Development libraries and headers for %{name}
Requires:   %{name}%{_isa} = %{version}-%{release}

%description devel
%{name} is a C library for serializing LV2 atoms to/from Turtle. It is
intended to be a full serialization solution for LV2 atoms, allowing
implementations to serialize binary atoms to strings and read them back again.
This is particularly useful for saving plugin state, or implementing plugin
control with network transparency.

This package contains the headers and development libraries for %{name}.

%prep
%oreon_sha256
echo '%{source1_hash}  %{SOURCE1}' | sha256sum -c -
echo '%{source2_hash}  %{SOURCE2}' | sha256sum -c -
%{gpgverify} --keyring='%{SOURCE2}' --signature='%{SOURCE1}' --data='%{SOURCE0}'
%autosetup -p1

%build
%meson
%meson_build

%install
%meson_install

install -d %{buildroot}%{_docdir}/%{name}
mv %{buildroot}%{_docdir}/%{name}-%{maj} %{buildroot}%{_docdir}/%{name}

%check
%meson_test

%files
%doc README.md
%license COPYING
%{_libdir}/lib%{name}-%{maj}.so.*

%files devel
%doc %{_docdir}/%{name}/%{name}-%{maj}/
%{_libdir}/lib%{name}-%{maj}.so
%{_libdir}/pkgconfig/%{name}-%{maj}.pc
%{_includedir}/%{name}-%{maj}/

%changelog
%autochangelog
