%global source0_hash 0ee07cb3e2ec4f5688b4b2971c42e5a4f4a41c7bf4aa130e6b118bea4b6340ab
%global debug_package %{nil}
Name:           KDBindings
Version:        1.1.0
Release:        1%{?dist}
Summary:        Reactive programming & data binding in C++
License:        BSD-3-Clause AND MIT
URL:            https://github.com/KDAB/KDBindings
Source0:        https://github.com/KDAB/%{name}/archive/refs/tags/v%{version}.tar.gz
# oreon:deps
BuildRequires:  cmake
BuildRequires:  gcc
BuildRequires:  gcc-c++
# /oreon:deps
%description
%{summary}.

%package        devel
Summary:        Development files for %{name}
Provides:       %{name}-static = %{version}-%{release}
Provides:       %{name} = %{version}-%{release}
%description    devel
Reactive programming & data binding in C++.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%oreon_prep
%build

%cmake
%cmake_build
%install
%cmake_install
rm -rf %{buildroot}%{_datadir}/doc/KDBindings
%oreon_autofiles KDBindings-devel usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*

%check

%ctest
%files -f %{oreon_filedir}/main.list
%files -n KDBindings-devel -f %{oreon_filedir}/KDBindings-devel.list

%changelog

%autochangelog
