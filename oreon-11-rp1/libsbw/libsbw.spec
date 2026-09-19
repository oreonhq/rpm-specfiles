%global source0_hash d311b3c899cba8d25e76ca2d3547f542fa469aa74c6b63a914f6d8cdf04c4dc9

%global __cmake_in_source_build 1

Name:           libsbw
Summary:        C++ Broker library 
Version:        2.12.2
Release:        21%{?dist}
URL:            http://sourceforge.net/projects/sbw/
Source0:        https://sourceforge.net/projects/sbw/files/sbw/%{version}/sbw-core-%{version}.tar.bz2
License:        BSD-3-Clause

BuildRequires: cmake
BuildRequires: gcc-c++
BuildRequires: gcc
BuildRequires: zlib-devel
BuildRequires: libxml2-devel
BuildRequires: dos2unix
BuildRequires: help2man
BuildRequires: make

%description
The Systems Biology Workbench (SBW) is a framework for application
intercommunications. It uses a broker-based, distributed,
message-passing architecture, supports many languages
including Java, C++, Perl & Python, and runs under Linux,OSX & Win32.
By default, the Broker opens a port for inter-Broker communications
by searching for the first free port in the range 10102 through 10202,
inclusive.
By default, in Fedora this port range is not opened.
See man-page for further informations.

libSBW is the C++ Broker port from the original SBW Broker (written in Java)
to C++. The current version implements all the functionality for the local side.
Meaning if you will just use the Broker on a single machine you should be fine
using the C++ Broker.

%package devel
Summary: Development files of libSBW
Requires: %{name}%{?_isa} = %{version}-%{release}

%description devel
This package provides header files, shared and static library files of libSBW.

##Static library may be useful for COPASI build
%package static
Summary: Static library of libSBW
Requires: %{name}-devel%{?_isa} = %{version}-%{release}

%description static
This package provides static library file of libSBW.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n sbw-core-%{version}
dos2unix ReadMe.txt
rm -rf VisualStudio

##Remove bundled/pre-compiled files
rm -rf bin/*
rm -rf include/libxml include/iconv.h include/libcharset.h include/localcharset.h

##Fix installation paths of CMake config files
sed -e 's|lib/cmake|%{_lib}/cmake|g' -i CMakeLists.txt

##Fix permissions of header and cpp files
sed -e 's|DESTINATION include/SBW|PERMISSIONS OWNER_WRITE OWNER_READ GROUP_READ WORLD_READ DESTINATION include/SBW|g' -i CMakeLists.txt
find ./SBWBroker \( -name \*.cpp -o -name \*.h \) -print0 | xargs -0 chmod -x
find ./SBWCore \( -name \*.cpp -o -name \*.h \) -print0 | xargs -0 chmod -x
find ./include/SBW \( -name \*.h \) -print0 | xargs -0 chmod -x

%build
# TODO: Please submit an issue to upstream (rhbz#2380752)
export CMAKE_POLICY_VERSION_MINIMUM=3.5
export CXXFLAGS="-std=c++14 %{optflags} -Wl,-z,now -Wno-deprecated"
export LDFLAGS="%{__global_ldflags} -Wl,-z,now -Wl,--as-needed"
%cmake -Wno-cpp \
 -DLIBXML_INCLUDE_DIR:PATH=%{_includedir}/libxml2 -DLIBXML_LIBRARY:FILEPATH=%{_libdir}/libxml2.so \
 -DCMAKE_BUILD_TYPE:STRING=Release -DCMAKE_INSTALL_LIBDIR:PATH=%{_libdir} -DWITH_STRICT_INCLUDES:BOOL=ON \
 -DCMAKE_INSTALL_PREFIX:PATH=%{_prefix} -DWITH_BUILD_BROKER:BOOL=ON  -DWITH_BUILD_SHARED:BOOL=ON \
 -DCMAKE_VERBOSE_MAKEFILE:BOOL=TRUE -DCMAKE_COLOR_MAKEFILE:BOOL=ON -DWITH_BUILD_STATIC:BOOL=ON \
 -DCPACK_BINARY_TZ:BOOL=OFF -DCPACK_BINARY_TGZ:BOOL=OFF -DCPACK_SOURCE_TBZ2:BOOL=OFF \
 -DCPACK_SOURCE_TGZ:BOOL=OFF -DCPACK_SOURCE_TZ:BOOL=OFF \
 -DCMAKE_SKIP_INSTALL_RPATH:BOOL=YES -DCMAKE_SKIP_RPATH:BOOL=YES

%cmake_build

%install
export LIBDIR=%{_libdir}
%cmake_install

## Make Broker man page
help2man SBWBroker/Broker -o Broker.1 --version-string=%{version}
mkdir -p $RPM_BUILD_ROOT%{_mandir}/man1
install -pm 644 Broker.1 $RPM_BUILD_ROOT%{_mandir}/man1

%files
%doc ReadMe.txt VERSION
%license LICENSE
%{_bindir}/Broker
%{_libdir}/libSBW.so.*
%{_mandir}/man1/Broker.1*

%files devel
%{_libdir}/libSBW.so
%{_includedir}/SBW/
%{_libdir}/cmake/SBW-config-*.cmake
%{_libdir}/cmake/SBW-config.cmake

%files static
%{_libdir}/libSBW-static.a
%{_libdir}/cmake/SBW-static-config-*.cmake
%{_libdir}/cmake/SBW-static-config.cmake

%changelog
%autochangelog
