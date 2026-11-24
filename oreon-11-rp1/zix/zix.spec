# Copyright (C) 2026 Oreon HQ
# SPDX-License-Identifier: GPL-2.0-or-later

%global source0_hash 4c73aab0f8cbbfe56b00c8c6d648316021e699c5ae6cbf254391ef309047e67b
%global source1_hash 4e04228dbcf451bde8ee29237ae17ed38bc72e66e4fb16e08f6e4e55fb95f039
%global source2_hash 29c8ffc9ffee2982ad3c3355736ed043377c1f0f4ea4776df4b98a464692b70e
%{!?oreon_bootstrap:%global oreon_bootstrap %{nil}}
%bcond bootstrap 0
%oreon_bootstrap

%global         maj 0

Name:           zix
Version:        0.8.2
Release:        %{autorelease}
Summary:        A lightweight C library of portability wrappers and data structures

License:        ISC
URL:            https://gitlab.com/drobilla/%{name}
Source0:        https://download.drobilla.net/%{name}-%{version}.tar.xz
Source1:        https://download.drobilla.net/%{name}-%{version}.tar.xz.sig
Source2:        https://drobilla.net/drobilla.gpg

BuildRequires: oreon-rpm-macros
BuildRequires: clang
BuildRequires: gcc
BuildRequires: gcc-c++
BuildRequires:  meson
BuildRequires:  gnupg2

%description
%{name} is a lightweight C library of portability wrappers and data structures.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%package        doc
Summary:        Documentation files for %{name}
Provides:       bundled(js-jquery) = 3.6.0
Buildarch:      noarch

%description    doc
The %{name}-doc package contains documentation files for
developing applications that use %{name}. Actually
it doesn't contain files, because of doc building errors.

%prep
%oreon_sha256
echo '%{source1_hash}  %{SOURCE1}' | sha256sum -c -
echo '%{source2_hash}  %{SOURCE2}' | sha256sum -c -
%{gpgverify} --keyring='%{SOURCE2}' --signature='%{SOURCE1}' --data='%{SOURCE0}'
%autosetup

%build
%meson -Dbenchmarks=disabled -Ddocs=disabled
%meson_build

%install
%meson_install

%check
%meson_test

%files
%license COPYING
%doc README.md
%{_libdir}/lib%{name}-%{maj}.so.%{maj}*

%files devel
%{_includedir}/%{name}-%{maj}
%{_libdir}/lib%{name}-%{maj}.so
%{_libdir}/pkgconfig/%{name}-%{maj}.pc

%files doc
%license COPYING

%changelog
%autochangelog
