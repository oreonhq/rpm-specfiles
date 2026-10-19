%global source0_hash 8e3e493427a1704ee0d8cacb65e61b544d4b3a7159f5a4e55517272e1fb25c8f
Name:           trantor
Version:        1.5.28
Release:        1%{?dist}
Summary:        A non-blocking I/O tcp network lib based on c++14/17
License:        BSD-3-Clause
URL:            https://github.com/an-tao/trantor
Source0:        https://github.com/an-tao/%{name}/archive/v%{version}/%{name}-%{version}.tar.gz
Patch0:          %{url}/pull/395.patch
Patch1:         trantor-use-the-system-ciphers.patch
ExcludeArch:    %{ix86}
Provides:       bundled(muduo)
# oreon:deps
BuildRequires:  cmake
BuildRequires:  cmake(GTest)
BuildRequires:  cmake(c-ares)
BuildRequires:  cmake(spdlog)
BuildRequires:  gcc-c++
BuildRequires:  pkgconfig(openssl)
# /oreon:deps
%description
%{summary}.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
%description    devel
This package contains development files for %{name}.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1
rm -r third_party/

%build

%cmake -DBUILD_C-ARES=ON -DTRANTOR_USE_TLS=openssl -DUSE_SPDLOG=ON -DBUILD_TESTING=ON
%cmake_build
%install
%cmake_install
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*

%check

%ctest
%files -f %{oreon_filedir}/main.list
%files -n trantor-devel -f %{oreon_filedir}/trantor-devel.list

%changelog

%autochangelog
