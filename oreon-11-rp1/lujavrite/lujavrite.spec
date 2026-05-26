Name:           lujavrite
Version:        1.2.3
Release:        %autorelease
Summary:        Lua library for calling Java code
License:        Apache-2.0
URL:            https://github.com/mizdebsk/lujavrite
ExclusiveArch:  %{java_arches}

Source:         https://github.com/mizdebsk/lujavrite/releases/download/%{version}/lujavrite-%{version}.tar.zst
# oreon url source checksums begin
%global source0_sha256 7a8ab005fbb8665758c90ba40fdab9d289997ff0e13bc8b47cbe230a213d9d8b
%global source0_file lujavrite-1.2.3.tar.zst
# oreon url source checksums end

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
# oreon verify url source checksums begin
%(f=%{_sourcedir}/lujavrite-1.2.3.tar.zst; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "7a8ab005fbb8665758c90ba40fdab9d289997ff0e13bc8b47cbe230a213d9d8b" || { echo "oreon: Source0 SHA256 mismatch for lujavrite-1.2.3.tar.zst" >&2; exit 1; })
# oreon verify url source checksums end
%autosetup -p1 -C

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
