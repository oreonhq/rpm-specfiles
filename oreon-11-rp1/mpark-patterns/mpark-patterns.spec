%global source0_hash 80e6af808a4d74d5d7358666303eb1dbfc5582313ff9fa31d1c0d3280d3bd9e7
%global debug_package %{nil}
Name:           mpark-patterns
Version:        0.3.0
Release:        1%{?dist}
Summary:        An experimental pattern matching library for C++17
License:        BSL-1.0
URL:            https://github.com/mpark/patterns
Source0:        https://github.com/mpark/patterns/archive/v%{version}/%{name}-%{version}.tar.gz
Patch:          cmake.patch
ExcludeArch:    %{ix86}
# oreon:deps
BuildRequires:  cmake
BuildRequires:  gcc-c++
BuildRequires:  gmock-devel
BuildRequires:  gtest-devel
# /oreon:deps
%description
%{summary}.

%package        devel
Summary:        Header files for %{name}
BuildArch:      noarch
Provides:       %{name}-static = %{version}-%{release}
%description    devel
%{summary}.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%global oreon_srcdir patterns-%{version}
%oreon_prep
%build

%cmake -DMPARK_PATTERNS_INCLUDE_TESTS=ON
%cmake_build
%install
%cmake_install
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*

%check

%ctest
%files -f %{oreon_filedir}/main.list
%files -n mpark-patterns-devel -f %{oreon_filedir}/mpark-patterns-devel.list

%changelog

%autochangelog
