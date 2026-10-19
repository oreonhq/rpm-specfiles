%global source0_hash 016ac5ece1808cd1100be72f90da4fa59ea41de487587a3283c6c981381cc216
%global forgeurl https://github.com/boost-ext/ut
Version:        2.3.1
%forgemeta
Name:           ut
Release:        1%{?dist}
Summary:        UT: C++20 μ(micro)/Unit Testing Framework
License:        BSL-1.0
URL:            %{forgeurl}
Source0:        %{forgeurl}/archive/v%{version}/%{name}-%{version}.tar.gz
# oreon:deps
BuildRequires:  cmake
BuildRequires:  gcc-c++
BuildRequires:  ninja-build
# /oreon:deps
%description
%{summary}.

%package        devel
Summary:        Development files for %{name}
Provides:       %{name}-static = %{version}-%{release}
%description    devel
The %{name}-devel package contains development files for %{name}.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%forgeautosetup -p1

sed -i -e "s/-Werror//g" cmake/WarningsAsErrors.cmake

%build

%cmake \
    -GNinja \
    -DBOOST_UT_ALLOW_CPM_USE=OFF \
    -DBOOST_UT_ENABLE_RUN_AFTER_BUILD=OFF \
%cmake_build
%install
%cmake_install
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*

%check

%ctest -E ut_test
%files -f %{oreon_filedir}/main.list
%files -n ut-devel -f %{oreon_filedir}/ut-devel.list

%changelog

%autochangelog
