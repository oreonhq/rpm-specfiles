# Copyright (C) 2026 Oreon HQ
# SPDX-License-Identifier: GPL-2.0-or-later

%global source0_hash 0779bd4f00175ff2f722f9dc43b542bea3bc606ed079e7099fa8a18627c2ddc9
%{!?oreon_bootstrap:%global oreon_bootstrap %{nil}}
%bcond bootstrap 0
%oreon_bootstrap

%bcond_without      tests

%global gh_owner    alanxz
%global gh_project  rabbitmq-c
%global libname     librabbitmq
%global soname      4
%global forgeurl    https://github.com/%{gh_owner}/%{gh_project}

Name:      %{libname}
Summary:   Client library for AMQP
License:   MIT
Version:   0.18.1
Release:   1%{?dist}
%forgemeta
URL:       %{forgeurl}
Source0:   %{forgesource}

BuildRequires: oreon-rpm-macros
BuildRequires: clang
BuildRequires: gcc
BuildRequires: cmake >= 3.22
BuildRequires: openssl-devel >= 1.1.1
BuildRequires: popt-devel >= 1.14
BuildRequires: xmlto
BuildRequires: make

%description
This is a C-language AMQP client library for use with AMQP servers
speaking protocol versions 0-9-1.

%package devel
Summary:    Header files and development libraries for %{name}
Requires:   %{name}%{?_isa} = %{version}-%{release}

%description devel
This package contains the header files and development libraries
for %{name}.

%package tools
Summary:    Example tools built using the librabbitmq package
Requires:   %{name}%{?_isa} = %{version}-%{release}

%description tools
This package contains example tools built using %{name}.

It provides:
amqp-consume        Consume messages from a queue on an AMQP server
amqp-declare-queue  Declare a queue on an AMQP server
amqp-delete-queue   Delete a queue from an AMQP server
amqp-get            Get a message from a queue on an AMQP server
amqp-publish        Publish a message on an AMQP server

%prep
%oreon_sha256
%forgesetup

cp -pr examples Examples

sed -e '/test_basic/d' -i tests/CMakeLists.txt

%build
%cmake \
  -DBUILD_TOOLS:BOOL=ON \
  -DBUILD_TOOLS_DOCS:BOOL=ON \
%if %{with tests}
  -DINSTALL_STATIC_LIBS:BOOL=OFF
%else
  -DBUILD_TESTING:BOOL=OFF \
  -DBUILD_STATIC_LIBS:BOOL=OFF
%endif

%cmake_build

%install
%cmake_install

%check
: check .pc is usable
grep @ %{buildroot}%{_libdir}/pkgconfig/librabbitmq.pc && exit 1
grep %{version} %{buildroot}%{_libdir}/pkgconfig/librabbitmq.pc || exit 1
: check cmake files are usable
grep static %{buildroot}%{_libdir}/cmake/rabbitmq-c/*.cmake && exit 1

%if %{with tests}
: upstream tests
%ctest
%else
: Tests disabled
%endif

%files
%license LICENSE
%{_libdir}/%{libname}.so.%{soname}
%{_libdir}/%{libname}.so.%{version}

%files devel
%doc AUTHORS THANKS *.md
%doc Examples
%{_libdir}/%{libname}.so
%{_includedir}/amqp*
%{_includedir}/rabbitmq-c
%{_libdir}/pkgconfig/%{libname}.pc
%{_libdir}/cmake/rabbitmq-c

%files tools
%{_bindir}/amqp-*
%doc %{_mandir}/man1/amqp-*.1*
%doc %{_mandir}/man7/librabbitmq-tools.7*

%changelog
%autochangelog
