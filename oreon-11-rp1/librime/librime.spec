%global source0_hash 8718e37c5ee059433f5a1b3232f3b8efad47135ff3e5016094beb9f18342ffb2

Name:           librime
Version:        1.16.1
Release:        2%{?dist}
Summary:        Rime Input Method Engine Library

License:        GPL-3.0-only
URL:            https://rime.im/
Source0:        https://github.com/rime/librime/archive/%{version}.tar.gz#/%{name}-%{version}.tar.gz
# The following librime lua plugin needs to access the librime internal API.
# Build the librime lua plugin when build the librime package.
Source1:        https://github.com/hchunhui/librime-lua/archive/refs/heads/master.tar.gz#/librime-lua.tar.gz
# For the librime octagram plugin
Source2:        https://github.com/lotem/librime-octagram/archive/refs/heads/master.tar.gz#/librime-octagram.tar.gz
# For the librime predict plugin
Source3:        https://github.com/lotem/librime-predict/archive/refs/heads/master.tar.gz#/librime-predict.tar.gz

BuildRequires:  gcc-c++
BuildRequires:  cmake, opencc-devel
BuildRequires:  boost-devel >= 1.46
BuildRequires:  zlib-devel
BuildRequires:  glog-devel, gtest-devel
BuildRequires:  yaml-cpp-devel
BuildRequires:  gflags-devel
BuildRequires:  marisa-devel
BuildRequires:  leveldb-devel
BuildRequires:  lua-devel

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

%files
%doc README.md LICENSE
%{_libdir}/*.so.*

%files devel
%doc
%{_includedir}/*
%{_libdir}/*.so
%{_libdir}/pkgconfig/rime.pc
%dir %{_datadir}/cmake/rime
%{_datadir}/cmake/rime/RimeConfig.cmake

%files tools
%{_bindir}/rime_deployer
%{_bindir}/rime_dict_manager
%{_bindir}/rime_patch
%{_bindir}/rime_table_decompiler

%files lua
%{_libdir}/rime-plugins/librime-lua.so

%files octagram
%{_libdir}/rime-plugins/librime-octagram.so

%files predict
%{_libdir}/rime-plugins/librime-predict.so

%changelog
%autochangelog
