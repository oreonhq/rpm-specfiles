%global source0_hash aff67d64027f747b4611646fd0421802eda60397da9076e3f7fb17227e542e99

%global commit 7a86bc22066858afeb23845a191a6ab680b46233
%global shortcommit %(c=%{commit}; echo ${c:0:7})

Name:           lua-json
Version:        1.3.4
Release:        12%{?dist}
Summary:        JSON Parser/Constructor for Lua
License:        MIT
URL:            https://github.com/harningt/luajson
Source0:        https://github.com/harningt/luajson/archive/%{version}/luajson-%{version}.tar.gz
# Support for lpeg 1.1.0
Patch0:         https://github.com/harningt/luajson/pull/48.patch
BuildRequires:  lua-devel
BuildRequires:  lua-lpeg >= 0.8.1
# for checks
BuildRequires:  lua-filesystem >= 1.4.1, lua-lunit >= 0.4
BuildRequires:  make
Requires:       lua(abi) >= %{lua_version}, lua-lpeg >= 0.8.1
BuildArch:      noarch

%description
LuaJSON is a customizable JSON decoder/encoder, using LPEG for parsing.

%prep
%(test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; })
%autosetup -p1 -n luajson-%{version}

%build

%install
mkdir -p $RPM_BUILD_ROOT%{lua_pkgdir}
cp -pr lua/* $RPM_BUILD_ROOT%{lua_pkgdir}

%check
make check-regression
# three tests that used to fail here now pass because of how numbers work in lua 5.2
# make check-unit | tee testlog.txt
# grep -q "0 failed, 0 errors" testlog.txt

%files
%doc LICENSE docs/LuaJSON.txt docs/ReleaseNotes-1.0.txt
%{lua_pkgdir}/*

%changelog
* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 1.3.4-12
- Prepare for Oreon 11 (RP1)
