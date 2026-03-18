# Fedora spec file for librabbitmq
#
# Copyright (c) 2012-2024 Remi Collet
# License: CC-BY-SA-4.0
# http://creativecommons.org/licenses/by-sa/4.0/
#
# Please, preserve the changelog entries
#

%bcond_without      tests

%global gh_commit   84b81cd97a1b5515d3d4b304796680da24c666d8
%global gh_short    %(c=%{gh_commit}; echo ${c:0:7})
%global gh_owner    alanxz
%global gh_project  rabbitmq-c
%global libname     librabbitmq
%global soname      4

Name:      %{libname}
Summary:   Client library for AMQP
Version:   0.15.0
Release:   4%{?dist}
License:   MIT
URL:       https://github.com/alanxz/rabbitmq-c

Source0:   https://github.com/%{gh_owner}/%{gh_project}/archive/%{gh_commit}/%{gh_project}-%{version}-%{gh_short}.tar.gz


BuildRequires: gcc
BuildRequires: cmake >= 3.22
BuildRequires: openssl-devel >= 1.1.1
# For tools
BuildRequires: popt-devel >= 1.14
# For man page
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
%setup -q -n %{gh_project}-%{gh_commit}

# Copy sources to be included in -devel docs.
cp -pr examples Examples

# This test requires a running server
sed -e '/test_basic/d' -i tests/CMakeLists.txt


%build
# static lib required for tests
%cmake \
  -DBUILD_TOOLS:BOOL=ON \
  -DBUILD_TOOLS_DOCS:BOOL=ON \
%if %{with tests}
  -DINSTALL_STATIC_LIBS:BOOL=OFF \
%else
  -DBUILD_TESTING:BOOL=OFF \
  -DBUILD_STATIC_LIBS:BOOL=OFF \
%endif
  -S .

%if 0%{?cmake_build:1}
%cmake_build
%else
make %{_smp_mflags}
%endif


%install
%if 0%{?cmake_install:1}
%cmake_install
%else
make install  DESTDIR="%{buildroot}"
%endif


%check
: check .pc is usable
grep @ %{buildroot}%{_libdir}/pkgconfig/librabbitmq.pc && exit 1
grep %{version} %{buildroot}%{_libdir}/pkgconfig/librabbitmq.pc || exit 1
: check cmake files are usable
grep static %{buildroot}%{_libdir}/cmake/rabbitmq-c/*.cmake && exit 1


%if %{with tests}
: upstream tests
%if 0%{?ctest:1}
%ctest
%else
make test
%endif
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
* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 0.15.0-4
- Prepare for Oreon 11 (RP1)
