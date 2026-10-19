%global source0_hash 73bdb408ae98812c5c2b7f00b2ae7c4fdb9798424abe5a7f7afb13c8fd462156
Name:           paho-cpp
Version:        1.6.0
Release:        1%{?dist}
Summary:        Eclipse Paho MQTT C++ Client Library
License:        EPL-2.0
URL:            https://github.com/eclipse/paho.mqtt.cpp
Source0:        https://github.com/eclipse/paho.mqtt.cpp/archive/v%{version}/%{name}-%{version}.tar.gz
# oreon:deps
BuildRequires:  cmake
BuildRequires:  doxygen
BuildRequires:  gcc-c++
BuildRequires:  graphviz
BuildRequires:  openssl-devel
BuildRequires:  paho-c-devel
# /oreon:deps
%description
Eclipse Paho MQTT C++ client library for memory-managed operating systems such
as Linux, MacOS, and Windows.

%package            devel
Summary:            Development files for %{name}
Requires:           %{name}%{?_isa} = %{version}-%{release}
%description        devel
The %{name}-devel package contains development files for %{name}.

%package            doc
Summary:            Documentation for %{name}
BuildArch:          noarch
%description        doc
This %{name}-doc package contains documentation for %{name}.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1 -n paho.mqtt.cpp-%{version}

sed -i 's|lib/cmake|%{_lib}/cmake|g' cmake/CMakeLists.txt

%build

%cmake \
    -DCMAKE_BUILD_TYPE=RelWithDebInfo \
    -DPAHO_WITH_SSL=ON \
    -DPAHO_BUILD_SAMPLES=OFF \
    -DPAHO_BUILD_DOCUMENTATION=ON
%cmake_build
%install
%cmake_install
mkdir -p %{buildroot}%{_docdir}/%{name}/examples/
cp -a examples/*.cpp %{buildroot}%{_docdir}/%{name}/examples/
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%files -f %{oreon_filedir}/main.list
%files -n paho-cpp-devel -f %{oreon_filedir}/paho-cpp-devel.list
%files -n paho-cpp-doc -f %{oreon_filedir}/paho-cpp-doc.list

%changelog

%autochangelog
