%global source0_hash aff67d64027f747b4611646fd0421802eda60397da9076e3f7fb17227e542e99
%global commit 7a86bc22066858afeb23845a191a6ab680b46233
%global shortcommit %(c=%{commit}; echo ${c:0:7})
Name:           lua-json
Version:        1.3.4
Release:        12%{?dist}
Summary:        JSON Parser/Constructor for Lua
License:        MIT
URL:            https://github.com/harningt/luajson
Source0:        https://github.com/harningt/luajson/archive/refs/tags/%{version}.tar.gz#/luajson-%{version}.tar.gz
Patch0:         https://github.com/harningt/luajson/pull/48.patch
Requires:       lua(abi) >= %{lua_version}, lua-lpeg >= 0.8.1
BuildArch:      noarch
# oreon:deps
BuildRequires:  lua-devel
BuildRequires:  lua-filesystem
BuildRequires:  lua-lpeg
BuildRequires:  lua-lunit
BuildRequires:  make
# /oreon:deps
%description
LuaJSON is a customizable JSON decoder/encoder, using LPEG for parsing.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%global oreon_srcdir luajson-%{version}
%oreon_prep
%build

%install
mkdir -p $RPM_BUILD_ROOT%{lua_pkgdir}
cp -pr lua/* $RPM_BUILD_ROOT%{lua_pkgdir}
%oreon_autofiles main

%check

make check-regression
%files -f %{oreon_filedir}/main.list

%changelog

* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 1.3.4-12
- Prepare for Oreon 11 (RP1)
