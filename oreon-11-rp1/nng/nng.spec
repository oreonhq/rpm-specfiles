%global source0_hash ff882bda0a854abd184a7c1eb33329e526928ef98e80ef0457dd9a708bb5b0b1

Name:     nng
Version:  1.9.0
Release:  5%{?dist}
Summary:  Light-weight brokerless messaging

License:  MIT
URL:      https://nanomsg.github.io/nng/
Source0:  https://github.com/nanomsg/nng/archive/v%{version}/%{name}-%{version}.tar.gz

BuildRequires: gcc
BuildRequires: gcc-c++
BuildRequires: cmake
BuildRequires: libnsl2-devel
BuildRequires: mbedtls-devel
BuildRequires: rubygem-asciidoctor

%description
nng (nanomsg next generation) is a socket library that provides several 
common communication patterns. It aims to make the networking layer fast, 
scalable, and easy to use. Implemented in C, it works on a wide range 
of operating systems with no further dependencies.

The communication patterns, also called "scalability protocols", are
basic blocks for building distributed systems. By combining them you can
create a vast array of distributed applications.

%package  devel
Summary:  Development files for the nng socket library
Requires: %{name}%{?_isa} = %{version}-%{release}

%description devel
This package contains files needed to develop applications using nanomsg,
a socket library that provides several common communication patterns.

%package  utils
Summary:  Command line interface for communicating with nng
Requires: %{name}%{?_isa} = %{version}-%{release}

%description utils
Includes nngcat, a simple utility for reading and writing to nanomsg
sockets and bindings, which can include local and remote connections.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup

%build
%cmake -DCMAKE_CXX_FLAGS="%optflags -fPIC" -DBUILD_SHARED_LIBS=ON \
       -DNNG_ENABLE_TLS=ON -DNNG_ENABLE_NNGCAT=ON \
       -DNNG_TESTS=ON -DNNG_ENABLE_DOC=ON .

%cmake_build

%install
%cmake_install
# No need to ship dev docs as both html and man format
rm -rf %{buildroot}/%{_mandir}/man[3-7]*

%ldconfig_scriptlets

%files
%license LICENSE.txt
%{_libdir}/libnng.so.1*

%files devel
%{_docdir}/nng/
%{_includedir}/nng/
%{_libdir}/libnng.so
%{_libdir}/cmake/nng/

%files utils
%{_bindir}/nngcat
%{_mandir}/man1/nngcat.1.gz

%changelog
%autochangelog
