%global source0_hash c81a86e0e81d4f02d61744cac4b4645e727c440dea0cd74c207401d3e55b0438
%global appname blurhash
Name: %{appname}-cpp
Version: 0.2.0
Release:        1%{?dist}
License: BSL-1.0
Summary:        C++ blurhash encoder/decoder
URL: https://github.com/Nheko-Reborn/%{appname}
Source0:        https://github.com/Nheko-Reborn/%{appname}/archive/v%{version}/%{appname}-%{version}.tar.gz
# oreon:deps
BuildRequires:  cmake
BuildRequires:  doctest-devel
BuildRequires:  gcc
BuildRequires:  gcc-c++
BuildRequires:  meson
# /oreon:deps
%description
Simple encoder and decoder for blurhashes. In large parts inspired by the
reference implementation.

%package devel
Summary: Development files for %{name}
Requires: %{name}%{?_isa} = %{?epoch:%{epoch}:}%{version}-%{release}
%description devel
%{summary}.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n %{appname}-%{version} -p1
rm -f stb_*.h

%build

%meson -Dtests=true -Dwerror=false
%meson_build
%install
%meson_install
%oreon_autofiles blurhash-cpp-devel usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*

%check

%meson_test
%files -f %{oreon_filedir}/main.list
%files -n blurhash-cpp-devel -f %{oreon_filedir}/blurhash-cpp-devel.list

%changelog

%autochangelog
