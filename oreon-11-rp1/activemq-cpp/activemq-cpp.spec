%global source0_hash 5858106f21bb541d5a3947906731a2187b00dc91870fa4e02866a03e98bea292
Name:           activemq-cpp
Version:        3.9.5
Release:        1%{?dist}
Summary:        C++ implementation of JMS-like messaging client
License:        Apache-2.0
URL:            http://activemq.apache.org/cms/
Source0:        http://www.apache.org/dist/activemq/activemq-cpp/%{version}/activemq-cpp-library-%{version}-src.tar.gz
Patch:          activemq-cpp-3.8.2-system-zlib.patch
# oreon:deps
BuildRequires:  apr-util-devel
BuildRequires:  cppunit-devel
BuildRequires:  gcc
BuildRequires:  gcc-c++
BuildRequires:  libuuid-devel
BuildRequires:  openssl-devel
BuildRequires:  zlib-devel
# /oreon:deps
%description
activemq-cpp is a JMS-like API for C++ for interfacing with Message
Brokers such as Apache ActiveMQ.  C++ messaging service helps to make your
C++ client code much neater and easier to follow. To get a better feel for
CMS try the API Reference.
ActiveMQ-CPP is a client only library, a message broker such as Apache
ActiveMQ is still needed for your clients to communicate.

%package devel
Summary:        C++ implementation header files for JMS-like messaging
Requires:       %{name} = %{version}-%{release}
Requires:       pkgconfig
Requires:       libuuid-devel
%description devel
activemq-cpp is a JMS-like API for C++ for interfacing with Message
Brokers such as Apache ActiveMQ.  C++ messaging service helps to make
your C++ client code much neater and easier to follow. To get a better
feel for CMS try the API Reference.  ActiveMQ-CPP is a client only
library, a message broker such as Apache ActiveMQ is still needed
for your clients to communicate.

%{name}-devel contains development header files.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n activemq-cpp-library-%{version} -p1
rm -r src/main/decaf/internal/util/zip
chmod 644 LICENSE.txt
chmod 644 src/main/activemq/transport/mock/MockTransport.cpp

%configure --disable-static

%build

%make_build
%install
%make_install
rm %{buildroot}%{_libdir}/lib%{name}.la
rm %{buildroot}%{_bindir}/example
%oreon_autofiles activemq-cpp-devel usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*

%check

make check
%ldconfig_scriptlets
%files -f %{oreon_filedir}/main.list
%files -n activemq-cpp-devel -f %{oreon_filedir}/activemq-cpp-devel.list

%changelog

%autochangelog
