%global source0_hash 3d249ec11b7bf01f12cd5976a9003cf28cf0d593e35327e302dda8a2838c2671
Name: tgbot-cpp
Version: 1.13
Release:        1%{?dist}
Summary:        C++ library for Telegram bot API
License: MIT
URL: https://github.com/reo7sp/%{name}
Source0:        https://github.com/reo7sp/%{name}/archive/v%{version}/%{name}-%{version}.tar.gz
# oreon:deps
BuildRequires:  boost-devel
BuildRequires:  cmake
BuildRequires:  curl-devel
BuildRequires:  gcc
BuildRequires:  gcc-c++
BuildRequires:  ninja-build
BuildRequires:  openssl-devel
BuildRequires:  zlib-devel
# /oreon:deps
%description
C++ library for Telegram bot API.

%package devel
Summary: Development files for %{name}
Requires: %{name}%{?_isa} = %{?epoch:%{epoch}:}%{version}-%{release}
%description devel
%{summary}.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%oreon_prep
%build

%cmake -G Ninja \
    -DCMAKE_BUILD_TYPE=Release \
    -DENABLE_TESTS=ON
%cmake_build
%check

%ctest
%install
%cmake_install
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*

%files -f %{oreon_filedir}/main.list
%files -n tgbot-cpp-devel -f %{oreon_filedir}/tgbot-cpp-devel.list

%changelog

%autochangelog
