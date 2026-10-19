%global source0_hash 6be27e0b3a4907f0cd3cfadec255ee1b925569e1bd06e67a4d2f4267299b69c4
%global commit ca1bf4b810e2d188d04cb6286f957008ee1b7681
%global short_commit %(c=%{commit}; echo ${c:0:7})	
%global date 20190529
Name: crossguid2
Version: 0.2.2
Release:        1%{?dist}
Summary:        Lightweight cross platform C++ GUID/UUID library
License: MIT
URL: https://github.com/graeme-hill/crossguid/
Source0:        https://github.com/graeme-hill/crossguid//archive/%{commit}/crossguid-%{commit}.tar.gz
Patch0: %{name}-fix_name.patch
Patch1: %{name}-fix_GCC13.patch
# oreon:deps
BuildRequires:  cmake
BuildRequires:  gcc-c++
BuildRequires:  libuuid-devel
BuildRequires:  make
BuildRequires:  marshalparser
# /oreon:deps
%description
CrossGuid is a minimal, cross platform, C++ GUID library. It uses the best
native GUID/UUID generator on the given platform and has a generic class for
parsing, stringifying, and comparing IDs.

%package devel
Summary:  Development files for %{name}
Requires: %{name}%{?_isa} = %{version}-%{release}
Requires: libuuid-devel%{?_isa}
Requires: cmake%{?_isa}
%description devel
The %{name}-devel package contains libraries and header files for developing
applications that use %{name}.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n crossguid-%{commit} -N

%patch -P 0 -p0 -b .fix_name
%patch -P 1 -p1 -b .fix_name

%build

%cmake -DCROSSGUID_SOVERSION_STRING:STRING=0 -DCROSSGUID_VERSION_STRING:STRING=0.0 \
 -DCMAKE_INSTALL_INCLUDEDIR:PATH=%{_includedir}/%{name}
%cmake_build
%install
%cmake_install
%oreon_autofiles crossguid2-devel usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*

%check

%__cmake_builddir/%{name}-test
%files -f %{oreon_filedir}/main.list
%files -n crossguid2-devel -f %{oreon_filedir}/crossguid2-devel.list

%changelog

%autochangelog
