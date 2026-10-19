%global source0_hash 7a8ab005fbb8665758c90ba40fdab9d289997ff0e13bc8b47cbe230a213d9d8b
Name:           lujavrite
Version:        1.2.3
Release:        1%{?dist}
Summary:        Lua library for calling Java code
License:        Apache-2.0
URL:            https://github.com/mizdebsk/lujavrite
ExclusiveArch:  %{java_arches}
Source0:        https://github.com/mizdebsk/lujavrite/releases/download/%{version}/lujavrite-%{version}.tar.zst
%{?lua_requires}
# oreon:deps
BuildRequires:  cmake
BuildRequires:  gcc
BuildRequires:  java-25-openjdk-devel
BuildRequires:  lua-devel
# /oreon:deps
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
%oreon_autofiles main

%check

%ctest
%files -f %{oreon_filedir}/main.list

%changelog

* Mon May 25 2026 Oreon Packaging Team <packaging@oreonhq.com> - 1.2.3-1
- Import
