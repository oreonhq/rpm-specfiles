%global source0_hash 89d83f2141edec31be576425637216928221918fe95dc3854d1b7fd4c627213f
%{!?lua_compat_version: %global lua_compat_version 5.1}
%{!?lua_compat_libdir: %global lua_compat_libdir %{_libdir}/lua/%{lua_compat_version}}
%{!?lua_compat_pkgdir: %global lua_compat_pkgdir %{_datadir}/lua/%{lua_compat_version}}
%{!?lua_compat_builddir: %global lua_compat_builddir %{_builddir}/compat-lua-%{name}-%{version}-%{release}}
Summary:        SAX XML parser based on the Expat library
Name:           lua-expat
Version:        1.5.2
Release:        1%{?dist}
License:        MIT
URL:            https://lunarmodules.github.io/luaexpat/
Source0:        https://github.com/lunarmodules/luaexpat/archive/refs/tags/%{version}.tar.gz#/luaexpat-%{version}.tar.gz
Requires:       lua(abi) = %{lua_version}
# oreon:deps
BuildRequires:  expat-devel
BuildRequires:  gcc
BuildRequires:  lua
BuildRequires:  lua-devel
BuildRequires:  make
# /oreon:deps
%description
LuaExpat is a SAX XML parser based on the Expat library.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%setup -q -n luaexpat-%{version}

%build

%make_build \
  CFLAGS="$RPM_OPT_FLAGS -fPIC -std=c99" LDFLAGS="$RPM_LD_FLAGS" \
  LUA_V=%{lua_version} \
  LUA_CDIR=%{lua_libdir} LUA_LDIR=%{lua_pkgdir} \
  LUA_INC=-I%{_includedir}
%install
%make_install LUA_CDIR=%{lua_libdir} LUA_LDIR=%{lua_pkgdir}
%oreon_autofiles main

%check

lua -e \
  'package.cpath="%{buildroot}%{lua_libdir}/?.so;"..package.cpath;
   package.path="%{buildroot}%{lua_pkgdir}/?.lua;"..package.path;
   local lxp = require("lxp"); print("Hello from "..lxp._VERSION.."!");'
%files -f %{oreon_filedir}/main.list

%changelog

* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 1.5.2-6
- Prepare for Oreon 11 (RP1)
