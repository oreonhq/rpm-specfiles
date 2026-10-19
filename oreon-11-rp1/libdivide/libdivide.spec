%global source0_hash 077e8ce6c783d1b4402aa6d77f643f88f37feb80e9896c30e19a62cc0a3f5576
%bcond ctest 1
Name:           libdivide
Version:        5.4.0
Release:        1%{?dist}
Summary:        Optimized integer division
License:        Zlib OR BSL-1.0
URL:            https://libdivide.com/
%global forgeurl  https://github.com/ridiculousfish/libdivide
VCS:            git:%{forgeurl}.git
Source0:        %{forgeurl}/archive/v%{version}/%{name}-%{version}.tar.gz
%global debug_package %{nil}
# oreon:deps
BuildRequires:  cmake
BuildRequires:  gcc-c++
# /oreon:deps
%description

%package        devel
Summary:        Development files for libdivide
Provides:       libdivide-static = %{version}-%{release}
%description    devel

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%autosetup -n %{name}-%{version}
# Disable -Werror
sed --in-place 's/;-Werror//;/-Werror/d' CMakeLists.txt

%build

%cmake -DLIBDIVIDE_BUILD_TESTS:BOOL=%{?with_ctest:ON}%{?!with_ctest:OFF}
%cmake_build
%install
%cmake_install
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*
%if %{with ctest}
%check

%ctest
%endif
%files -f %{oreon_filedir}/main.list
%files -n libdivide-devel -f %{oreon_filedir}/libdivide-devel.list

%changelog

%autochangelog
