%global source0_hash da1ade826bc22858a9fb87ae052789bbd614d042b3ec2c22e6544ca83db6bc04
Name:           ncnn
Version:        20260526
Release:        1%{?dist}
Summary:        A high-performance neural network inference framework
License:        BSD-3-Clause AND BSD-2-Clause AND Zlib
URL:            https://github.com/Tencent/ncnn
Source0:        https://github.com/Tencent/%{name}/archive/%{version}/%{name}-%{version}.tar.gz
# oreon:deps
BuildRequires:  cmake
BuildRequires:  cmake(glslang)
BuildRequires:  gcc-c++
BuildRequires:  ninja-build
BuildRequires:  pkgconfig(protobuf)
# /oreon:deps
%description
ncnn is a high-performance neural network inference computing framework
optimized for mobile platforms. ncnn is deeply considerate about deployment and
uses on mobile phones from the beginning of design. ncnn does not have third
party dependencies. It is cross-platform, and runs faster than all known open
source frameworks on mobile phone cpu. Developers can easily deploy deep
learning algorithm models to the mobile platform by using efficient ncnn
implementation, create intelligent APPs, and bring the artificial intelligence
to your fingertips. ncnn is currently being used in many Tencent applications,
such as QQ, Qzone, WeChat, Pitu and so on.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
%description    devel
This package contains development files for %{name}.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%oreon_prep
%build

%cmake \
    -GNinja \
    -DNCNN_SHARED_LIB=ON \
    -DNCNN_ENABLE_LTO=ON \
    -DNCNN_BUILD_EXAMPLES=ON \
    -DNCNN_VULKAN=ON \
    -DNCNN_SYSTEM_GLSLANG=ON \
%cmake_build
%install
%cmake_install
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*

%files -f %{oreon_filedir}/main.list
%files -n ncnn-devel -f %{oreon_filedir}/ncnn-devel.list

%changelog

%autochangelog
