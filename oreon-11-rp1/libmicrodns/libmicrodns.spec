# Copyright (C) 2026 Oreon HQ
# SPDX-License-Identifier: GPL-2.0-or-later

%global source0_hash 9864a088ffef4d4255d5abf63c6f603d1dc343dfec2809ff0c3f1624045b80fa
%{!?oreon_bootstrap:%global oreon_bootstrap %{nil}}
%bcond bootstrap 0
%oreon_bootstrap

Name:           libmicrodns
Version:        0.2.0
Release:        1%{?dist}
Summary:        Minimal mDNS resolver library

License:        LGPL-2.1-or-later
URL:            https://github.com/videolabs/libmicrodns
Source0:        %{url}/archive/%{version}/%{name}-%{version}.tar.gz

BuildRequires: oreon-rpm-macros
BuildRequires: clang
BuildRequires: gcc
BuildRequires:  meson
%description
Minimal mDNS resolver (and announcer) library.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%prep
%oreon_sha256
%autosetup -p1

%build
%meson
%meson_build

%install
%meson_install

%check
%meson_test

%ldconfig_scriptlets

%files
%license COPYING
%doc AUTHORS NEWS README.md
%{_libdir}/libmicrodns.so.1*

%files devel
%{_includedir}/microdns
%{_libdir}/libmicrodns.so
%{_libdir}/pkgconfig/microdns.pc

%changelog
%autochangelog
