%global source0_hash f3dcd30e85626d8eff13a98009f0b75b2a4d0cbf91520830a67202157dc63d6d

%global proton_datadir %{_datadir}/proton
%global __cmake_in_source_build 1

%global __provides_exclude_from ^%{proton_datadir}/examples/.*$
%global __requires_exclude_from ^%{proton_datadir}/examples/.*$

%undefine __brp_mangle_shebangs

Name:           qpid-proton
Version:        0.40.0
Release:        13%{?dist}
Summary:        A high performance, lightweight messaging library
# Automatically converted from old format: ASL 2.0 - review is highly recommended.
License:        Apache-2.0
URL:            http://qpid.apache.org/proton/

Source0:        %{name}-%{version}.tar.gz
Patch0:         proton.patch
Source1:        licenses.xml

%global proton_licensedir %{_licensedir}/proton
%{!?_licensedir:%global license %doc}
%{!?_licensedir:%global proton_licensedir %{proton_datadir}}

BuildRequires:  gcc
BuildRequires:  gcc-c++
BuildRequires:  make
BuildRequires:  cmake
BuildRequires:  libuuid-devel
BuildRequires:  openssl-devel
BuildRequires:  cyrus-sasl-devel
BuildRequires:  cyrus-sasl-plain
BuildRequires:  cyrus-sasl-md5
BuildRequires:  doxygen
BuildRequires:  jsoncpp-devel
BuildRequires:  python3-devel
BuildRequires:  python3-build
BuildRequires:  python3-cffi
BuildRequires:  python3-pip
BuildRequires:  python3-setuptools
BuildRequires:  python3-sphinx
BuildRequires:  python3-wheel
BuildRequires:  pkgconfig

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

%files c
%dir %{proton_datadir}
%license %{proton_licensedir}/LICENSE.txt
%license %{proton_licensedir}/licenses.xml
%doc %{proton_datadir}/README*
%{_libdir}/libqpid-proton.so.*
%{_libdir}/libqpid-proton-core.so.*
%{_libdir}/libqpid-proton-proactor.so.*

%ldconfig_scriptlets c

%package   cpp
Summary:   C++ libraries for Qpid Proton
Requires:  qpid-proton-c%{?_isa} = %{version}-%{release}
Requires:  jsoncpp
#Requires:  opentelemetry-cpp

%description cpp
%{summary}.

%files cpp
%dir %{proton_datadir}
%doc %{proton_datadir}/README*
%{_libdir}/libqpid-proton-cpp.so.*

%ldconfig_scriptlets cpp

%package c-devel
Requires:  qpid-proton-c%{?_isa} = %{version}-%{release}
Summary:   Development libraries for writing messaging apps with Qpid Proton
Obsoletes: qpid-proton-devel

%description c-devel
%{summary}.

%files c-devel
%{_includedir}/proton
%exclude %{_includedir}/proton/*.hpp
%exclude %{_includedir}/proton/**/*.hpp
%{_libdir}/libqpid-proton.so
%{_libdir}/libqpid-proton-core.so
%{_libdir}/libqpid-proton-proactor.so
%{_libdir}/pkgconfig/libqpid-proton.pc
%{_libdir}/pkgconfig/libqpid-proton-core.pc
%{_libdir}/pkgconfig/libqpid-proton-proactor.pc
%{_libdir}/cmake/Proton

%package cpp-devel
Requires:  qpid-proton-cpp%{?_isa} = %{version}-%{release}
Requires:  qpid-proton-c-devel%{?_isa} = %{version}-%{release}
Summary:   Development libraries for writing messaging apps with Qpid Proton

%description cpp-devel
%{summary}.

%files cpp-devel
%{_includedir}/proton/*.hpp
%{_includedir}/proton/**/*.hpp
%{_libdir}/pkgconfig/libqpid-proton-cpp.pc
%{_libdir}/libqpid-proton-cpp.so
%{_libdir}/cmake/ProtonCpp

%package c-docs
Summary:   Documentation for the C development libraries for Qpid Proton
BuildArch: noarch
Obsoletes: qpid-proton-c-devel-doc
Obsoletes: qpid-proton-c-devel-docs

%description c-docs
%{summary}.

%files c-docs
%license %{proton_licensedir}/LICENSE.txt
%doc %{proton_datadir}/docs/api-c
%doc %{proton_datadir}/examples/README.md
%doc %{proton_datadir}/examples/c/ssl-certs
%doc %{proton_datadir}/examples/c/*.c
%doc %{proton_datadir}/examples/c/*.h
%doc %{proton_datadir}/examples/c/README.dox
%doc %{proton_datadir}/examples/c/CMakeLists.txt

%package   cpp-docs
Summary:   Documentation for the C++ development libraries for Qpid Proton
BuildArch: noarch
Obsoletes: qpid-proton-cpp-devel-doc
Obsoletes: qpid-proton-cpp-devel-docs

%description cpp-docs
%{summary}.

%files cpp-docs
%license %{proton_licensedir}/LICENSE.txt
%doc %{proton_datadir}/docs/api-cpp
%doc %{proton_datadir}/examples/cpp/*.cpp
%doc %{proton_datadir}/examples/cpp/*.hpp
%doc %{proton_datadir}/examples/cpp/README.dox
%doc %{proton_datadir}/examples/cpp/CMakeLists.txt
%doc %{proton_datadir}/examples/cpp/ssl-certs
%doc %{proton_datadir}/examples/cpp/tutorial.dox

%package -n python3-qpid-proton
Summary:  Python language bindings for the Qpid Proton messaging framework
Requires: qpid-proton-c%{?_isa} = %{version}-%{release}
Requires: python3
Provides: python%{python3_version}dist(python-%name)

%description -n python3-qpid-proton
%{summary}.

%files -n python3-qpid-proton
%{python3_sitearch}/__pycache__/*
%{python3_sitearch}/*.so
%{python3_sitearch}/*.py*
%{python3_sitearch}/proton
%{python3_sitearch}/python_qpid_proton-%{version}.dist-info

%package -n python-qpid-proton-docs
Summary:   Documentation for the Python language bindings for Qpid Proton
BuildArch: noarch
Obsoletes:  python-qpid-proton-doc

%description -n python-qpid-proton-docs
%{summary}.

%files -n python-qpid-proton-docs
%license %{proton_licensedir}/LICENSE.txt
%doc %{proton_datadir}/docs/api-py
%doc %{proton_datadir}/examples/python

%package tests
Summary:   Qpid Proton Tests
BuildArch: noarch

%description tests
%{summary}.

%files tests
%doc %{proton_datadir}/tests

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
# Need to remove anything built by the python cmake build in proton
# so that we rebuild from scratch
rm -rf build
%global whl_tags cp%{python3_version_nodots}-cp%{python3_version_nodots}-%(echo %{python3_platform} | tr -- - _)
%global _pyproject_wheeldir %{buildroot}/../qpid-proton-%{version}/BLD/python/dist
cd ..
%pyproject_install
# We seem to need to strip the build extension otherwise it seems to embed a reference to
# the buildroot in the debug info which fails the rpmbuild - probably because we massaged
# the pkgconfig path above
strip %{buildroot}%{python3_sitearch}/cproton*.so)

install -dm 755 %{buildroot}%{proton_licensedir}
install -pm 644 %{SOURCE1} %{buildroot}%{proton_licensedir}
install -pm 644 %{buildroot}%{proton_datadir}/LICENSE.txt %{buildroot}%{proton_licensedir}
rm -f %{buildroot}%{proton_datadir}/LICENSE.txt

# clean up files that are not shipped
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

%check

%changelog
%autochangelog
