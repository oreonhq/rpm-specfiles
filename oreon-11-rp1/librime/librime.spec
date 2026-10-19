%global source3_hash 8718e37c5ee059433f5a1b3232f3b8efad47135ff3e5016094beb9f18342ffb2
%global source2_hash 6b3449b63fe234cbcadfc0d342d4d5c4d4b8c262597670b32217d4db3dfc8cef
%global source1_hash f173d4ab998c467b831a5e7e23b7f97af766dd582b0581628a6cd3b89ff4c6e3
%global source0_hash a60274da5d8b8a7187e6c7e9ba5023334ed7bdd182535e93c4e96de8cf188377
Name:           librime
Version:        1.17.0
Release:        1%{?dist}
Summary:        Rime Input Method Engine Library
License:        GPL-3.0-only
URL:            https://rime.im/
Source0:        https://github.com/rime/librime/archive/%{version}.tar.gz#/%{name}-%{version}.tar.gz
Source1:        https://github.com/hchunhui/librime-lua/archive/refs/heads/master.tar.gz#/librime-lua.tar.gz
Source2:        https://github.com/lotem/librime-octagram/archive/refs/heads/master.tar.gz#/librime-octagram.tar.gz
Source3:        https://github.com/lotem/librime-predict/archive/refs/heads/master.tar.gz#/librime-predict.tar.gz
# oreon:deps
BuildRequires:  boost-devel
BuildRequires:  cmake
BuildRequires:  gcc-c++
BuildRequires:  gflags-devel
BuildRequires:  glog-devel
BuildRequires:  gtest-devel
BuildRequires:  leveldb-devel
BuildRequires:  lua-devel
BuildRequires:  marisa-devel
BuildRequires:  opencc-devel
BuildRequires:  yaml-cpp-devel
BuildRequires:  zlib-devel
# /oreon:deps
%description
Rime Input Method Engine Library

Support for shape-based and phonetic-based input methods,
including those for Chinese dialects.

A selected dictionary in Traditional Chinese,
powered by opencc for Simplified Chinese output.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%package        tools
Summary:        Tools for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
%description    tools
The %{name}-tools package contains tools for %{name}.

%package        lua
Summary:        Lua plugin for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
%description    lua
The %{name}-lua package contains the lua plugin from the community.

%package        octagram
Summary:        Octagram plugin for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
%description    octagram
The %{name}-octagram package contains the octagram plugin from the community.

%package        predict
Summary:        Predict plugin for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
%description    predict
The %{name}-predict package contains the predict plugin from the community.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1

pushd plugins
tar xvf %{SOURCE1}
mv librime-lua-master lua
tar xvf %{SOURCE2}
mv librime-octagram-master octagram
tar xvf %{SOURCE3}
mv librime-predict-master predict
popd

%build

%cmake -DCMAKE_BUILD_TYPE=Release \
       -DBUILD_MERGED_PLUGINS=OFF \
       -DENABLE_EXTERNAL_PLUGINS=ON
%cmake_build
%install
%cmake_install
%ldconfig_scriptlets
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/* usr/*/lib*.so.* usr/*/lib*.so.* usr/*/lib*.so.* usr/*/lib*.so.*

%files -f %{oreon_filedir}/main.list
%files -n librime-devel -f %{oreon_filedir}/librime-devel.list
%files -n librime-tools -f %{oreon_filedir}/librime-tools.list
%files -n librime-lua -f %{oreon_filedir}/librime-lua.list
%files -n librime-octagram -f %{oreon_filedir}/librime-octagram.list
%files -n librime-predict -f %{oreon_filedir}/librime-predict.list

%changelog

%autochangelog
