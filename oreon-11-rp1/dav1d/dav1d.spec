# Copyright (C) 2026 Oreon HQ
# SPDX-License-Identifier: GPL-2.0-or-later

%global source0_hash afc5378daba30eafd11d7b4f0ec863270d7b175f38393a2e1e0ff76f3a45c8b9
%{!?oreon_bootstrap:%global oreon_bootstrap %{nil}}
%bcond bootstrap 0
%oreon_bootstrap

Name:           dav1d
Version:        1.5.5
Release:        %{autorelease}
Summary:        AV1 cross-platform Decoder

License:        BSD-2-Clause AND ISC
URL:            https://code.videolan.org/videolan/dav1d
Source0:        %{url}/-/archive/%{version}/%{name}-%{version}.tar.bz2

BuildRequires: oreon-rpm-macros
BuildRequires: clang
BuildRequires: gcc
BuildRequires:  nasm >= 2.14
BuildRequires:  meson >= 0.49.0
BuildRequires:  pkgconfig(libxxhash)

Requires:       libdav1d%{?_isa} = %{version}-%{release}

%description
dav1d is a new AV1 cross-platform Decoder, open-source, and focused on speed
and correctness.

%package     -n libdav1d
Summary:        Library files for dav1d

%description -n libdav1d
Library files for dav1d, the AV1 cross-platform Decoder.

%package     -n libdav1d-devel
Summary:        Development files for dav1d
Requires:       libdav1d%{?_isa} = %{version}-%{release}

%description -n libdav1d-devel
Development files for dav1d, the AV1 cross-platform Decoder.

%prep
%oreon_sha256
%autosetup -p1 -n %{name}-%{version}

%build
%meson
%meson_build

%install
%meson_install

%check
%meson_test

%files
%doc CONTRIBUTING.md NEWS README.md
%{_bindir}/dav1d

%files -n libdav1d
%license COPYING doc/PATENTS
%{_libdir}/libdav1d.so.7{,.*}

%files -n libdav1d-devel
%{_includedir}/dav1d/
%{_libdir}/libdav1d.so
%{_libdir}/pkgconfig/dav1d.pc

%changelog
%autochangelog
