%global source0_hash 97293092ba385ab390decb6678bc8cbeffd5899bfbc49eb7ef4aa00f5e31c3d4
%{!?lua_compat_version: %global lua_compat_version 5.1}
%{!?lua_compat_libdir: %global lua_compat_libdir %{_libdir}/lua/%{lua_compat_version}}
%{!?lua_compat_pkgdir: %global lua_compat_pkgdir %{_datadir}/lua/%{lua_compat_version}}
%{!?lua_compat_builddir: %global lua_compat_builddir %{_builddir}/compat-lua-%{name}-%{version}-%{release}}
Summary:        Lua binding for OpenSSL library
Name:           lua-sec
Version:        1.3.2
Release:        8%{?dist}
License:        MIT
URL:            https://github.com/brunoos/luasec
Source0:        https://github.com/brunoos/luasec/archive/v%{version}/luasec-%{version}.tar.gz
Requires:       lua(abi) = %{lua_version}
Requires:       lua-socket
# oreon:deps
BuildRequires:  gcc
BuildRequires:  lua
BuildRequires:  lua-devel
BuildRequires:  make
BuildRequires:  openssl3-devel
# /oreon:deps
%description
Lua binding for OpenSSL library to provide TLS/SSL communication.
It takes an already established TCP connection and creates a secure
session between the peers.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n luasec-%{version}

%build

%make_build linux \
  CFLAGS="$RPM_OPT_FLAGS -fPIC -I. -I%{_includedir} -DWITH_LUASOCKET -DLUASOCKET_DEBUG -DLUA_COMPAT_APIINTCASTS $OPENSSL_CFLAGS" \
  LD="gcc -shared" LDFLAGS="-fPIC -shared -L./luasocket $RPM_LD_FLAGS $OPENSSL_LDFLAGS"
%install
%make_install \
  CFLAGS="$RPM_OPT_FLAGS -fPIC -I. -I%{_includedir} -DWITH_LUASOCKET -DLUASOCKET_DEBUG -DLUA_COMPAT_APIINTCASTS $OPENSSL_CFLAGS" \
  LD="gcc -shared" LDFLAGS="-fPIC -shared -L./luasocket $RPM_LD_FLAGS $OPENSSL_LDFLAGS" \
  LUAPATH=%{lua_pkgdir} LUACPATH=%{lua_libdir}
%oreon_autofiles main

%check

lua -e \
  'package.cpath="%{buildroot}%{lua_libdir}/?.so;"..package.cpath;
   package.path="%{buildroot}%{lua_pkgdir}/?.lua;"..package.path;
   local ssl = require("ssl"); print("Hello from "..ssl._VERSION.."!");'
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
