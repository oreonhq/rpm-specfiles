%global source0_hash none

Name:           lujavrite
Version:        1.2.3
Release:        %autorelease
Summary:        Lua library for calling Java code
License:        Apache-2.0
URL:            https://github.com/mizdebsk/lujavrite
ExclusiveArch:  %{java_arches}

Source:        https://github.com/mizdebsk/lujavrite/releases/download/%{version}/lujavrite-%{version}.tar.zst

BuildRequires:  cmake
BuildRequires:  gcc
BuildRequires:  lua-devel
BuildRequires:  java-25-openjdk-devel

%{?lua_requires}

%description
LuJavRite is a rock-solid Lua library that allows calling Java code
from Lua code.  It does so by launching embedded Java Virtual Machine
and using JNI interface to invoke Java methods.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%autosetup -p1 -n lujavrite-1.2.3

%conf
%cmake

%build
%cmake_build

%install
%cmake_install

%check
%ctest

%files
%{lua_libdir}/*
%license LICENSE NOTICE
%doc README.md

%changelog
* Mon May 25 2026 Oreon Packaging Team <packaging@oreonhq.com> - 1.2.3-1
- Import
