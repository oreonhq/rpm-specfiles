%global source1_hash 2eda2a93592480a295fa338118aaf28cdcf24b7c6980740a1df94810652fc368
%global source0_hash 3cf7411b573eda2de2aec9761bd6b539a5d5d67739761357f5f773d1490db0fb
Name:           libarcus
Version:        5.3.0
Release:        1%{?dist}
Summary:        Communication library between internal components for Ultimaker software
License:        LGPL-3.0-or-later
URL:            https://github.com/Ultimaker/libArcus
Source0:        https://github.com/Ultimaker/libArcus/archive/%{version}.tar.gz#/%{name}-%{version}.tar.gz
Source1:        https://github.com/Ultimaker/pyArcus/archive/%{version}.tar.gz#/pyArcus-%{version}.tar.gz
Source2:        FindSIP.cmake
Source3:        SIPMacros.cmake
Source4:        CMakeLists.txt
Source5:        CPackConfig.cmake
Source6:        ArcusConfig.cmake.in
Source7:        COPYING-CMAKE-SCRIPTS
Patch:          libArcus-3.10.0-PyQt6.sip.patch
Patch:          libArcus-5.2.2-actually-export-symbols.patch
Patch:          https://github.com/Ultimaker/libArcus/pull/160.patch
ExcludeArch:    %{ix86}
# oreon:deps
BuildRequires:  (python3-setuptools if python3-devel >= 3.12)
BuildRequires:  /usr/bin/sip
BuildRequires:  cmake
BuildRequires:  gcc-c++
BuildRequires:  git-core
BuildRequires:  protobuf-devel
BuildRequires:  python3-devel
BuildRequires:  python3-protobuf
BuildRequires:  python3-pyqt6-sip
BuildRequires:  python3-sip-devel
# /oreon:deps
%description
Arcus library contains C++ code and Python 3 bindings for creating a socket in
a thread and using this socket to send and receive messages based on the
Protocol Buffers library. It is designed to facilitate the communication
between Cura and its backend and similar code.

%package        devel
License:        LGPLv3+ and BSD
Summary:        Development files for libarcus
Requires:       %{name}%{?_isa} = %{version}-%{release}
%description    devel
Arcus library contains C++ code and Python 3 bindings for creating a socket in
a thread and using this socket to send and receive messages based on the
Protocol Buffers library. It is designed to facilitate the communication
between Cura and its backend and similar code.

Development files.

%package -n     python3-arcus
Summary:        Python 3 libArcus bindings
Requires:       %{name}%{?_isa} = %{version}-%{release}
%{?_sip_api:Requires: python3-pyqt5-sip-api(%{_sip_api_major}) >= %{_sip_api}}
%description -n python3-arcus
Arcus Python 3 bindings for creating a socket in a thread and using this
socket to send and receive messages based on the
Protocol Buffers library. It is designed to facilitate the communication
between Cura and its backend and similar code.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n libArcus-%{version} -a 1

cp -a pyArcus-%{version}/python .
cp -a pyArcus-%{version}/include/pyArcus include
mkdir cmake
cp -a %{SOURCE2} %{SOURCE3} %{SOURCE7} cmake/
rm -rf CMakeLists.txt
cp -a %{SOURCE4} %{SOURCE5} %{SOURCE6} .
cp -a pyArcus-%{version}/src/PythonMessage.cpp python/

%autopatch -p1

%build

%cmake -DBUILD_EXAMPLES:BOOL=OFF -DCMAKE_SKIP_RPATH:BOOL=ON
%cmake_build
%install
%cmake_install
%oreon_autofiles python3-arcus usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%files -f %{oreon_filedir}/main.list
%files -n libarcus-devel -f %{oreon_filedir}/libarcus-devel.list
%files -n python3-arcus -f %{oreon_filedir}/python3-arcus.list

%changelog

%autochangelog
