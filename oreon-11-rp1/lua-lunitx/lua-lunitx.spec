%global source0_hash e571ff01cb8f8f77dceeb098359bc5d7f5b4b696023e3b9d5ee1b4c3d986ac32

Name:           lua-lunitx
Version:        0.8.1
Release:        14%{?dist}
Summary:        Unit testing framework for Lua

License:        MIT
URL:            https://github.com/dcurrie/lunit/
Source0:        https://github.com/dcurrie/lunit/archive/%{version}.tar.gz#/lunitx-%{version}.tar.gz

# for running tests
# also, macros are in lua-devel
BuildRequires:  lua-devel >= 5.2

BuildArch:      noarch

Provides:       lua-lunit = %{version}-%{release}
Obsoletes:      lua-lunit <= 0.5-18

%description
This is lunitx Version 0.8.1, an extended version of Lunit
for Lua 5.2, 5.3, and 5.4.

Lunit is a unit testing framework for lua.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n lunit-%{version}

%install
mkdir -p %{buildroot}%{_bindir}
cp -p extra/lunit.sh %{buildroot}%{_bindir}/lunit

mkdir -p %{buildroot}%{lua_pkgdir}
cp -pr lua/* %{buildroot}%{lua_pkgdir}

%check
# for self test, without --dontforce lunit will try to load its launcher which is a shell script
LUA_PATH='%{buildroot}%{lua_pkgdir}/?.lua;;' %{buildroot}%{_bindir}/lunit --dontforce test/selftest.lua

%files
%license LICENSE
%doc ANNOUNCE CHANGES DOCUMENTATION examples README*
%{_bindir}/lunit
%{lua_pkgdir}/*

%changelog
%autochangelog
