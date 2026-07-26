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
BuildRequires:  gcc
BuildRequires:  make
BuildRequires:  lua >= %{lua_version}
BuildRequires:  lua-devel >= %{lua_version}
%if 0%{?fedora} || 0%{?rhel} >= 9
BuildRequires:  openssl-devel >= 1.0.2
%else
BuildRequires:  openssl3-devel
%endif

%description
Lua binding for OpenSSL library to provide TLS/SSL communication.
It takes an already established TCP connection and creates a secure
session between the peers.

%if 0%{?fedora}
%package -n lua%{lua_compat_version}-sec
Summary:        Lua %{lua_compat_version} binding for OpenSSL library
Obsoletes:      lua-sec-compat < 0.7
Provides:       lua-sec-compat = %{version}-%{release}
Provides:       lua-sec-compat%{?_isa} = %{version}-%{release}
Requires:       lua(abi) = %{lua_compat_version}
BuildRequires:  compat-lua >= %{lua_compat_version}
BuildRequires:  compat-lua-devel >= %{lua_compat_version}

%description -n lua%{lua_compat_version}-sec
Lua %{lua_compat_version} binding for OpenSSL library to provide TLS/SSL communication.
It takes an already established TCP connection and creates a secure
session between the peers.
%endif

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n luasec-%{version}

%if 0%{?fedora}
rm -rf %{lua_compat_builddir}
cp -a . %{lua_compat_builddir}
%endif

%build
%if 0%{?rhel} == 8
OPENSSL_CFLAGS="$(pkg-config --cflags-only-I openssl3)"
OPENSSL_LDFLAGS="$(pkg-config --libs-only-L openssl3)"
%endif

%make_build linux \
  CFLAGS="$RPM_OPT_FLAGS -fPIC -I. -I%{_includedir} -DWITH_LUASOCKET -DLUASOCKET_DEBUG -DLUA_COMPAT_APIINTCASTS $OPENSSL_CFLAGS" \
  LD="gcc -shared" LDFLAGS="-fPIC -shared -L./luasocket $RPM_LD_FLAGS $OPENSSL_LDFLAGS"

%if 0%{?fedora}
pushd %{lua_compat_builddir}
%make_build linux \
  CFLAGS="$RPM_OPT_FLAGS -fPIC -I. -I%{_includedir}/lua-%{lua_compat_version} -DWITH_LUASOCKET -DLUASOCKET_DEBUG -DLUA_COMPAT_APIINTCASTS" \
  LD="gcc -shared" LDFLAGS="-fPIC -shared -L./luasocket $RPM_LD_FLAGS"
popd
%endif

%install
%make_install \
  CFLAGS="$RPM_OPT_FLAGS -fPIC -I. -I%{_includedir} -DWITH_LUASOCKET -DLUASOCKET_DEBUG -DLUA_COMPAT_APIINTCASTS $OPENSSL_CFLAGS" \
  LD="gcc -shared" LDFLAGS="-fPIC -shared -L./luasocket $RPM_LD_FLAGS $OPENSSL_LDFLAGS" \
  LUAPATH=%{lua_pkgdir} LUACPATH=%{lua_libdir}

%if 0%{?fedora}
pushd %{lua_compat_builddir}
%make_install \
  CFLAGS="$RPM_OPT_FLAGS -fPIC -I. -I%{_includedir}/lua-%{lua_compat_version} -DWITH_LUASOCKET -DLUASOCKET_DEBUG -DLUA_COMPAT_APIINTCASTS" \
  LD="gcc -shared" LDFLAGS="-fPIC -shared -L./luasocket $RPM_LD_FLAGS" \
  LUAPATH=%{lua_compat_pkgdir} LUACPATH=%{lua_compat_libdir}
popd
%endif

%check
lua -e \
  'package.cpath="%{buildroot}%{lua_libdir}/?.so;"..package.cpath;
   package.path="%{buildroot}%{lua_pkgdir}/?.lua;"..package.path;
   local ssl = require("ssl"); print("Hello from "..ssl._VERSION.."!");'

%if 0%{?fedora}
lua-%{lua_compat_version} -e \
  'package.cpath="%{buildroot}%{lua_compat_libdir}/?.so;"..package.cpath;
   package.path="%{buildroot}%{lua_compat_pkgdir}/?.lua;"..package.path;
   local ssl = require("ssl"); print("Hello from "..ssl._VERSION.."!");'
%endif

%files
%license LICENSE
%doc CHANGELOG
%{lua_libdir}/ssl.so
%{lua_pkgdir}/ssl.lua
%dir %{lua_pkgdir}/ssl/
%{lua_pkgdir}/ssl/*.lua

%if 0%{?fedora}
%files -n lua%{lua_compat_version}-sec
%license LICENSE
%doc CHANGELOG
%{lua_compat_libdir}/ssl.so
%{lua_compat_pkgdir}/ssl.lua
%dir %{lua_compat_pkgdir}/ssl/
%{lua_compat_pkgdir}/ssl/*.lua
%endif

%changelog
%autochangelog
