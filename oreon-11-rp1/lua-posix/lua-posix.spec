# oreon source sha256 begin
# URL sources: global sourceN_sha256 = 64-char hex from sha256sum. Omit a sourceN_sha256 line to skip verify for that source.
%global source0_sha256 82cd9a96c41a4a3205c050206f0564ff4456f773a8f9ffc9235ff8f1907ca5e6
%global oreon_verify_sources \
%{?source0_sha256:%(test -z "%{source0_sha256}" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_sha256}" || { echo "oreon: Source0 sha256 mismatch" >&2; exit 1; }; })}
%(true)
# oreon source sha256 end

# Tests require specl which is not yet packaged
%bcond_with check

Name:           lua-posix
Version:        36.3
Release:        %autorelease
Summary:        POSIX library for Lua
License:        MIT
URL:            http://luaposix.github.io/luaposix/
Source0:        https://github.com/luaposix/luaposix/archive/v%{version}/lua-posix-%{version}.tar.gz
BuildRequires:  gcc
BuildRequires:  libxcrypt-devel
BuildRequires:  lua-devel
%{?lua_requires}

%description
This is a POSIX library for Lua which provides access to many POSIX features
to Lua programs.


%prep
%oreon_verify_sources
%autosetup -p1 -n luaposix-%{version}


%build
build-aux/luke CFLAGS="%build_cflags" LDFLAGS="%build_ldflags"


%install
build-aux/luke install PREFIX=%{buildroot}%{_prefix} INST_LIBDIR=%{buildroot}%{lua_libdir}


%check
lua -e \
  'package.cpath="%{buildroot}%{lua_libdir}/?.so;"..package.cpath;
   package.path="%{buildroot}%{lua_pkgdir}/?.lua;"..package.path;
   local posix = require("posix.errno"); print("Hello from "..posix.version.."!");'

%if %{with check}
lua ./spec/spec_helper.lua
%endif


%files
%license LICENSE
%doc AUTHORS NEWS.md README.md
%{lua_libdir}/*
%{lua_pkgdir}/posix/


%changelog
* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 36.3-1
- Prepare for Oreon 11 (RP1)
