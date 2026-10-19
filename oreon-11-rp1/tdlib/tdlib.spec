%global source0_hash 30d560205fe82fb811cd57a8fcbc7ac853a5b6195e9cb9e6ff142f5e2d8be217
Name: tdlib
Version: 1.8.67
Release:        1%{?dist}
License: BSL-1.0
URL: https://github.com/%{name}/td
Summary:        Cross-platform library for building Telegram clients
Source0:        https://github.com/%{name}/td/archive/v%{version}/%{name}-%{version}.tar.gz
Provides: bundled(sqlite) = 3.31.0
ExclusiveArch: x86_64 aarch64
# oreon:deps
BuildRequires:  cmake
BuildRequires:  gcc
BuildRequires:  gcc-c++
BuildRequires:  gperf
BuildRequires:  gperftools-devel
BuildRequires:  ninja-build
BuildRequires:  openssl-devel
BuildRequires:  zlib-devel
# /oreon:deps
%description
TDLib (Telegram Database library) is a cross-platform library for
building Telegram clients. It can be easily used from almost any
programming language.

%package devel
Summary: Development files for %{name}
Requires: %{name}%{?_isa} = %{?epoch:%{epoch}:}%{version}-%{release}
%package static
Summary: Static libraries for %{name}
Requires: %{name}%{?_isa} = %{?epoch:%{epoch}:}%{version}-%{release}
Requires: %{name}-devel%{?_isa} = %{?epoch:%{epoch}:}%{version}-%{release}
%description devel
%{summary}.

%description static
%{summary}.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n td-%{version} -p1
sed -e 's/"DEFAULT"/"PROFILE=SYSTEM"/g' -i tdnet/td/net/SslStream.cpp

%build

%cmake -G Ninja \
    -DCMAKE_BUILD_TYPE=Release \
    -DCMAKE_INSTALL_LIBDIR=%{_lib} \
    -DTD_ENABLE_JNI:BOOL=OFF \
    -DTD_ENABLE_DOTNET:BOOL=OFF
%cmake_build
%install
%cmake_install
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%files -f %{oreon_filedir}/main.list
%files -n tdlib-devel -f %{oreon_filedir}/tdlib-devel.list
%files -n tdlib-static -f %{oreon_filedir}/tdlib-static.list

%changelog

%autochangelog
