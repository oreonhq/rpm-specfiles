%global source0_hash 8864a3e9bebde6ebed71b49ac2a036cedf9ae0f02ce758bc28c21e6a2ae15803
%global debug_package %{nil}
Name:           functionalplus
Version:        0.2.28
Release:        1%{?dist}
Summary:        Functional Programming Library for C++
License:        BSL-1.0
URL:            https://github.com/Dobiasd/FunctionalPlus
Source0:        https://github.com/Dobiasd/FunctionalPlus/archive/v%{version}/%{name}-%{version}.tar.gz
# oreon:deps
BuildRequires:  cmake
BuildRequires:  doctest-devel
BuildRequires:  gcc
BuildRequires:  gcc-c++
# /oreon:deps
%description
Functional Programming Library for C++. Write concise and readable C++ code.

%package        devel
Summary:        Header files for %{name}
BuildArch:      noarch
Provides:       %{name}-static = %{version}-%{release}
%description    devel
%{summary}.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n FunctionalPlus-%{version}
sed '/-Werror/d' -i cmake/warnings.cmake

%build

%cmake -DFunctionalPlus_INSTALL_CMAKEDIR=%{_datadir}/cmake/FunctionalPlus
%cmake_build
%ifnarch %{ix86}
pushd test
%cmake
%cmake_build
popd
%endif
%install
%cmake_install
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*

%check

%ifnarch %{ix86}
pushd test
%ctest
%endif
%files -f %{oreon_filedir}/main.list
%files -n functionalplus-devel -f %{oreon_filedir}/functionalplus-devel.list

%changelog

%autochangelog
