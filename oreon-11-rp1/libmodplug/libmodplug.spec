# Copyright (C) 2026 Oreon HQ
# SPDX-License-Identifier: GPL-2.0-or-later

%global source0_hash d85366ca22cd27861811a2713545ff03d140dca38a111595dfe4bbd00d149d93
%{!?oreon_bootstrap:%global oreon_bootstrap %{nil}}
%bcond bootstrap 0
%oreon_bootstrap

Name:           libmodplug
Version:        0.8.9.2
Release:        %{autorelease}
Epoch:          1
Summary:        Modplug mod music file format library
License:        LicenseRef-Fedora-Public-Domain
URL:            https://modplug-xmms.sourceforge.net/
Source0:        https://github.com/Konstanty/libmodplug/archive/refs/tags/v%{version}/%{name}-%{version}.tar.gz

BuildRequires: oreon-rpm-macros
BuildRequires: clang
BuildRequires: gcc
BuildRequires: gcc-c++
BuildRequires: cmake
BuildRequires: make
Suggests:      %{_sysconfdir}/timidity.cfg

%description
%{summary}.

%package        devel
Summary:        Development files for the Modplug mod music file format library
Requires:       %{name}%{?_isa} = %{epoch}:%{version}-%{release}
Requires:       gcc-c++

%description    devel
%{summary}.

%prep
%oreon_sha256
%autosetup -p1
sed -i -e 's/\r//g' ChangeLog

%build
%cmake
%cmake_build

%install
%cmake_install

%check

%files
%license COPYING
%doc AUTHORS ChangeLog README TODO
%{_libdir}/libmodplug.so.1.0.0
%{_libdir}/libmodplug.so.1

%files devel
%{_includedir}/libmodplug/
%{_libdir}/libmodplug.so
%{_libdir}/pkgconfig/libmodplug.pc

%changelog
%autochangelog
