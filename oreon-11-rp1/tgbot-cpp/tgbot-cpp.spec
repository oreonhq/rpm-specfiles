%global source0_hash 5ebbd5934305cd07339696c75f6edb43f6b4a91bcc82fca898e1ebc9c960a03b

Name: tgbot-cpp
Version: 1.6
Release: 7%{?dist}

Summary: C++ library for Telegram bot API
License: MIT
URL: https://github.com/reo7sp/%{name}
Source0: %{url}/archive/v%{version}/%{name}-%{version}.tar.gz

BuildRequires: openssl-devel
BuildRequires: ninja-build
BuildRequires: boost-devel
BuildRequires: curl-devel
BuildRequires: zlib-devel
BuildRequires: gcc-c++
BuildRequires: cmake
BuildRequires: gcc

%description
C++ library for Telegram bot API.

%package devel
Summary: Development files for %{name}
Requires: %{name}%{?_isa} = %{?epoch:%{epoch}:}%{version}-%{release}

%description devel
%{summary}.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup

%build
%cmake -G Ninja \
    -DCMAKE_BUILD_TYPE=Release \
    -DENABLE_TESTS=ON
%cmake_build

%check
%ctest

%install
%cmake_install

%files
%doc README.md
%license LICENSE
%{_libdir}/libTgBot.so.1*

%files devel
%{_includedir}/tgbot
%{_libdir}/libTgBot.so

%changelog
%autochangelog
