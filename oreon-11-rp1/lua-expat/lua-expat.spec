# oreon source sha256 begin
# URL sources: global sourceN_sha256 = 64-char hex from sha256sum. Omit a sourceN_sha256 line to skip verify for that source.
%global source0_sha256 89d83f2141edec31be576425637216928221918fe95dc3854d1b7fd4c627213f
%global oreon_verify_sources \
%{?source0_sha256:%(test -z "%{source0_sha256}" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_sha256}" || { echo "oreon: Source0 sha256 mismatch" >&2; exit 1; }; })}
%(true)
# oreon source sha256 end

%{!?lua_compat_version: %global lua_compat_version 5.1}
%{!?lua_compat_libdir: %global lua_compat_libdir %{_libdir}/lua/%{lua_compat_version}}
%{!?lua_compat_pkgdir: %global lua_compat_pkgdir %{_datadir}/lua/%{lua_compat_version}}
%{!?lua_compat_builddir: %global lua_compat_builddir %{_builddir}/compat-lua-%{name}-%{version}-%{release}}

Summary:        SAX XML parser based on the Expat library
Name:           lua-expat
Version:        1.5.2
Release:        6%{?dist}
License:        MIT
URL:            https://lunarmodules.github.io/luaexpat/
Source0:        https://github.com/lunarmodules/luaexpat/archive/%{version}/luaexpat-%{version}.tar.gz
Requires:       lua(abi) = %{lua_version}
BuildRequires:  gcc
BuildRequires:  make
BuildRequires:  lua >= %{lua_version}
BuildRequires:  lua-devel >= %{lua_version}
BuildRequires:  expat-devel >= 2.4.0

%description
LuaExpat is a SAX XML parser based on the Expat library.

%if 0%{?fedora}
%package -n lua%{lua_compat_version}-expat
Summary:        SAX XML parser based on the Expat library for Lua %{lua_compat_version}
Obsoletes:      lua-expat-compat < 1.3.0-16
Provides:       lua-expat-compat = %{version}-%{release}
Provides:       lua-expat-compat%{?_isa} = %{version}-%{release}
Requires:       lua(abi) = %{lua_compat_version}
BuildRequires:  compat-lua >= %{lua_compat_version}
BuildRequires:  compat-lua-devel >= %{lua_compat_version}

%description -n lua%{lua_compat_version}-expat
LuaExpat is a SAX XML parser based on the Expat library for Lua %{lua_compat_version}.
%endif

%prep
%oreon_verify_sources
%setup -q -n luaexpat-%{version}

%if 0%{?fedora}
rm -rf %{lua_compat_builddir}
cp -a . %{lua_compat_builddir}
%endif

%build
%make_build \
  CFLAGS="$RPM_OPT_FLAGS -fPIC -std=c99" LDFLAGS="$RPM_LD_FLAGS" \
  LUA_V=%{lua_version} \
  LUA_CDIR=%{lua_libdir} LUA_LDIR=%{lua_pkgdir} \
  LUA_INC=-I%{_includedir}

%if 0%{?fedora}
pushd %{lua_compat_builddir}
%make_build \
  CFLAGS="$RPM_OPT_FLAGS -fPIC -std=c99" LDFLAGS="$RPM_LD_FLAGS" \
  LUA_V=%{lua_compat_version} \
  LUA_CDIR=%{lua_compat_libdir} LUA_LDIR=%{lua_compat_pkgdir} \
  LUA_INC=-I%{_includedir}/lua-%{lua_compat_version}
popd
%endif

%install
%make_install LUA_CDIR=%{lua_libdir} LUA_LDIR=%{lua_pkgdir}

%if 0%{?fedora}
pushd %{lua_compat_builddir}
%make_install LUA_CDIR=%{lua_compat_libdir} LUA_LDIR=%{lua_compat_pkgdir}
popd
%endif

%check
lua -e \
  'package.cpath="%{buildroot}%{lua_libdir}/?.so;"..package.cpath;
   package.path="%{buildroot}%{lua_pkgdir}/?.lua;"..package.path;
   local lxp = require("lxp"); print("Hello from "..lxp._VERSION.."!");'

%if 0%{?fedora}
lua-%{lua_compat_version} -e \
  'package.cpath="%{buildroot}%{lua_compat_libdir}/?.so;"..package.cpath;
   package.path="%{buildroot}%{lua_compat_pkgdir}/?.lua;"..package.path;
   local lxp = require("lxp"); print("Hello from "..lxp._VERSION.."!");'
%endif

%files
%license LICENSE
%doc README.md docs/*
%{lua_libdir}/lxp.so
%{lua_pkgdir}/lxp/

%if 0%{?fedora}
%license LICENSE
%files -n lua%{lua_compat_version}-expat
%doc README.md docs/*
%{lua_compat_libdir}/lxp.so
%{lua_compat_pkgdir}/lxp/
%endif

%changelog
* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 1.5.2-6
- Prepare for Oreon 11 (RP1)
