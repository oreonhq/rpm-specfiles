%global source0_hash f3dcd30e85626d8eff13a98009f0b75b2a4d0cbf91520830a67202157dc63d6d
%global proton_datadir %{_datadir}/proton
%global __cmake_in_source_build 1
%global __provides_exclude_from ^%{proton_datadir}/examples/.*$
%global __requires_exclude_from ^%{proton_datadir}/examples/.*$
%undefine __brp_mangle_shebangs
Name:           qpid-proton
Version:        0.40.0
Release:        1%{?dist}
Summary:        A high performance, lightweight messaging library
License:        Apache-2.0
URL:            http://qpid.apache.org/proton/
Source0:        %{name}-%{version}.tar.gz
Patch0:         proton.patch
Source1:        licenses.xml
%global proton_licensedir %{_licensedir}/proton
%{!?_licensedir:%global license %doc}
%{!?_licensedir:%global proton_licensedir %{proton_datadir}}
# oreon:deps
BuildRequires:  cmake
BuildRequires:  cyrus-sasl-devel
BuildRequires:  cyrus-sasl-md5
BuildRequires:  cyrus-sasl-plain
BuildRequires:  doxygen
BuildRequires:  gcc
BuildRequires:  gcc-c++
BuildRequires:  jsoncpp-devel
BuildRequires:  libuuid-devel
BuildRequires:  make
BuildRequires:  openssl-devel
BuildRequires:  pkgconfig
BuildRequires:  python3-build
BuildRequires:  python3-cffi
BuildRequires:  python3-devel
BuildRequires:  python3-pip
BuildRequires:  python3-setuptools
BuildRequires:  python3-sphinx
BuildRequires:  python3-wheel
# /oreon:deps
%description
Proton is a high performance, lightweight messaging library. It can be used in
the widest range of messaging applications including brokers, client libraries,
routers, bridges, proxies, and more. Proton is based on the AMQP 1.0 messaging
standard. Using Proton it is trivial to integrate with the AMQP 1.0 ecosystem
from any platform, environment, or language.

%package c
Summary:   C libraries for Qpid Proton
Requires:  cyrus-sasl-lib
Obsoletes: qpid-proton
Obsoletes: perl-qpid-proton
%description c
%{summary}.

%package   cpp
Summary:   C++ libraries for Qpid Proton
Requires:  qpid-proton-c%{?_isa} = %{version}-%{release}
Requires:  jsoncpp
%description cpp
%{summary}.

%package c-devel
Requires:  qpid-proton-c%{?_isa} = %{version}-%{release}
Summary:   Development libraries for writing messaging apps with Qpid Proton
Obsoletes: qpid-proton-devel
%description c-devel
%{summary}.

%package cpp-devel
Requires:  qpid-proton-cpp%{?_isa} = %{version}-%{release}
Requires:  qpid-proton-c-devel%{?_isa} = %{version}-%{release}
Summary:   Development libraries for writing messaging apps with Qpid Proton
%description cpp-devel
%{summary}.

%package c-docs
Summary:   Documentation for the C development libraries for Qpid Proton
BuildArch: noarch
Obsoletes: qpid-proton-c-devel-doc
Obsoletes: qpid-proton-c-devel-docs
%description c-docs
%{summary}.

%package   cpp-docs
Summary:   Documentation for the C++ development libraries for Qpid Proton
BuildArch: noarch
Obsoletes: qpid-proton-cpp-devel-doc
Obsoletes: qpid-proton-cpp-devel-docs
%description cpp-docs
%{summary}.

%package -n python3-qpid-proton
Summary:  Python language bindings for the Qpid Proton messaging framework
Requires: qpid-proton-c%{?_isa} = %{version}-%{release}
Requires: python3
Provides: python%{python3_version}dist(python-%name)
%description -n python3-qpid-proton
%{summary}.

%package -n python-qpid-proton-docs
Summary:   Documentation for the Python language bindings for Qpid Proton
BuildArch: noarch
Obsoletes:  python-qpid-proton-doc
%description -n python-qpid-proton-docs
%{summary}.

%package tests
Summary:   Qpid Proton Tests
BuildArch: noarch
%description tests
%{summary}.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n %{name}-%{version}
%patch -p1 0

%build

mkdir -p BLD
cd BLD
%cmake \
    -DCMAKE_SKIP_RPATH:BOOL=OFF \
   "-DCMAKE_C_FLAGS=$CFLAGS -Wno-deprecated-declarations" \
    -DENABLE_FUZZ_TESTING=NO \
    -DENABLE_PYTHON_ISOLATED=NO \
    ..
make all docs %{?_smp_mflags}
%install
rm -rf %{buildroot}
cd BLD
%make_install
(cd python/dist
rm -rf build
%global whl_tags cp%{python3_version_nodots}-cp%{python3_version_nodots}-%(echo %{python3_platform} | tr -- - _)
%global _pyproject_wheeldir %{buildroot}/../qpid-proton-%{version}/BLD/python/dist
cd ..
%pyproject_install
strip %{buildroot}%{python3_sitearch}/cproton*.so)
install -dm 755 %{buildroot}%{proton_licensedir}
install -pm 644 %{SOURCE1} %{buildroot}%{proton_licensedir}
install -pm 644 %{buildroot}%{proton_datadir}/LICENSE.txt %{buildroot}%{proton_licensedir}
rm -f %{buildroot}%{proton_datadir}/LICENSE.txt
rm -rf %{buildroot}%{_exec_prefix}/bindings
rm -rf %{buildroot}%{_libdir}/java
rm -rf %{buildroot}%{_libdir}/libproton-jni.so
rm -rf %{buildroot}%{_datarootdir}/java
rm -rf %{buildroot}%{_libdir}/proton.cmake
rm -fr %{buildroot}%{proton_datadir}/examples/CMakeFiles
rm -f  %{buildroot}%{proton_datadir}/examples/Makefile
rm -f  %{buildroot}%{proton_datadir}/examples/*.cmake
rm -fr %{buildroot}%{proton_datadir}/examples/c/CMakeFiles
rm -f  %{buildroot}%{proton_datadir}/examples/c/*.cmake
rm -f  %{buildroot}%{proton_datadir}/examples/c/Makefile
rm -f  %{buildroot}%{proton_datadir}/examples/c/Makefile.pkgconfig
rm -f  %{buildroot}%{proton_datadir}/examples/c/broker
rm -f  %{buildroot}%{proton_datadir}/examples/c/direct
rm -f  %{buildroot}%{proton_datadir}/examples/c/receive
rm -f  %{buildroot}%{proton_datadir}/examples/c/send
rm -f  %{buildroot}%{proton_datadir}/examples/c/send-abort
rm -f  %{buildroot}%{proton_datadir}/examples/c/send-ssl
rm -f  %{buildroot}%{proton_datadir}/examples/c/raw_connect
rm -f  %{buildroot}%{proton_datadir}/examples/c/raw_echo
rm -fr %{buildroot}%{proton_datadir}/examples/cpp/CMakeFiles
rm -f  %{buildroot}%{proton_datadir}/examples/cpp/*.cmake
rm -f  %{buildroot}%{proton_datadir}/examples/cpp/Makefile
rm -f  %{buildroot}%{proton_datadir}/examples/cpp/Makefile.pkgconfig
rm -f  %{buildroot}%{proton_datadir}/examples/cpp/broker
rm -f  %{buildroot}%{proton_datadir}/examples/cpp/client
rm -f  %{buildroot}%{proton_datadir}/examples/cpp/connection_options
rm -f  %{buildroot}%{proton_datadir}/examples/cpp/direct_recv
rm -f  %{buildroot}%{proton_datadir}/examples/cpp/direct_send
rm -f  %{buildroot}%{proton_datadir}/examples/cpp/encode_decode
rm -f  %{buildroot}%{proton_datadir}/examples/cpp/flow_control
rm -f  %{buildroot}%{proton_datadir}/examples/cpp/helloworld
rm -f  %{buildroot}%{proton_datadir}/examples/cpp/helloworld_direct
rm -f  %{buildroot}%{proton_datadir}/examples/cpp/queue_browser
rm -f  %{buildroot}%{proton_datadir}/examples/cpp/scheduled_send_03
rm -f  %{buildroot}%{proton_datadir}/examples/cpp/scheduled_send
rm -f  %{buildroot}%{proton_datadir}/examples/cpp/selected_recv
rm -f  %{buildroot}%{proton_datadir}/examples/cpp/server
rm -f  %{buildroot}%{proton_datadir}/examples/cpp/server_direct
rm -f  %{buildroot}%{proton_datadir}/examples/cpp/service_bus
rm -f  %{buildroot}%{proton_datadir}/examples/cpp/simple_connect
rm -f  %{buildroot}%{proton_datadir}/examples/cpp/simple_recv
rm -f  %{buildroot}%{proton_datadir}/examples/cpp/simple_send
rm -f  %{buildroot}%{proton_datadir}/examples/cpp/ssl
rm -f  %{buildroot}%{proton_datadir}/examples/cpp/ssl_client_cert
rm -f  %{buildroot}%{proton_datadir}/examples/cpp/message_properties
rm -f  %{buildroot}%{proton_datadir}/examples/cpp/multithreaded_client
rm -f  %{buildroot}%{proton_datadir}/examples/cpp/multithreaded_client_flow_control
rm -f  %{buildroot}%{proton_datadir}/examples/cpp/reconnect_client
rm -f  %{buildroot}%{proton_datadir}/examples/cpp/colour_send
rm -fr %{buildroot}%{proton_datadir}/examples/engine/java
rm -fr %{buildroot}%{proton_datadir}/examples/go
rm -fr %{buildroot}%{proton_datadir}/examples/java
rm -fr %{buildroot}%{proton_datadir}/examples/javascript
rm -fr %{buildroot}%{proton_datadir}/examples/perl
rm -fr %{buildroot}%{proton_datadir}/examples/php
rm -f  %{buildroot}%{proton_datadir}/CMakeLists.txt
%oreon_autofiles python3-qpid-proton usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles python-qpid-proton-docs usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/* usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%check

%files -f %{oreon_filedir}/main.list
%files -n qpid-proton-c -f %{oreon_filedir}/qpid-proton-c.list
%files -n qpid-proton-cpp -f %{oreon_filedir}/qpid-proton-cpp.list
%files -n qpid-proton-c-devel -f %{oreon_filedir}/qpid-proton-c-devel.list
%files -n qpid-proton-cpp-devel -f %{oreon_filedir}/qpid-proton-cpp-devel.list
%files -n qpid-proton-c-docs -f %{oreon_filedir}/qpid-proton-c-docs.list
%files -n qpid-proton-cpp-docs -f %{oreon_filedir}/qpid-proton-cpp-docs.list
%files -n python3-qpid-proton -f %{oreon_filedir}/python3-qpid-proton.list
%files -n python-qpid-proton-docs -f %{oreon_filedir}/python-qpid-proton-docs.list
%files -n qpid-proton-tests -f %{oreon_filedir}/qpid-proton-tests.list

%changelog

%autochangelog
