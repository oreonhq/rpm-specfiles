%global source0_hash 85cafd4dcfdfbbe51bd7e62639e04cd2e56d0a5ac2c200261f13edffbd3f55d3
%global date 20260109
%global commit d2058fd1d4800203e1ded1cfad74fa73fdbf622a
%global shortcommit %(c=%{commit}; echo ${c:0:7})
Name:           libunifex
Version:        0.4.0^%{date}git%{shortcommit}
Release:        1%{?dist}
Summary:        A prototype implementation of the C++ sender/receiver async programming model
License:        Apache-2.0 WITH LLVM-exception
URL:            https://github.com/facebookexperimental/libunifex
Source0:        https://github.com/facebookexperimental/%{name}/archive/%{commit}/%{name}-%{shortcommit}.tar.gz
ExcludeArch:    %{ix86}
# oreon:deps
BuildRequires:  cmake
BuildRequires:  gcc-c++
BuildRequires:  gmock-devel
BuildRequires:  gtest-devel
BuildRequires:  ninja-build
# /oreon:deps
%description
The 'libunifex' project is a prototype implementation of the C++ sender/receiver
async programming model that is currently being considered for standardisation.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
%description    devel
This package contains development files for %{name}.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%oreon_prep
%build

export CXXFLAGS="%{optflags} -Wno-error=maybe-uninitialized -Wno-error=template-body"
%cmake \
    -GNinja \
    -DUNIFEX_USE_SYSTEM_GTEST=ON \
    -DCMAKE_CXX_STANDARD=20
%cmake_build
%install
%cmake_install
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*

%check

%ctest
%files -f %{oreon_filedir}/main.list
%files -n libunifex-devel -f %{oreon_filedir}/libunifex-devel.list

%changelog

%autochangelog
