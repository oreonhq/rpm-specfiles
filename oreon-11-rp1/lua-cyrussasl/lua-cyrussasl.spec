%global source0_hash b2fa6ce9a69f35bc37e40ae0f6a7a81fdf8237cd6a5d708681f037f3049809d7

Summary:        Cyrus SASL library for Lua
Name:           lua-cyrussasl
Version:        1.1.0
Release:        22%{?dist}
License:        BSD-3-Clause
URL:            https://github.com/JorjBauer/lua-cyrussasl
Source0:        https://github.com/JorjBauer/lua-cyrussasl/archive/v%{version}/%{name}-%{version}.tar.gz
Requires:       lua(abi) = %{lua_version}
BuildRequires:  gcc
BuildRequires:  make
BuildRequires:  lua >= %{lua_version}
BuildRequires:  lua-devel >= %{lua_version}
BuildRequires:  cyrus-sasl-devel

%description
Lua bindings for the Cyrus SASL APIs.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q

%build
%make_build CFLAGS="$RPM_OPT_FLAGS -fPIC" LDFLAGS="-shared -fPIC -lsasl2 $RPM_LD_FLAGS" 

%install
install -D -p -m 755 cyrussasl.so $RPM_BUILD_ROOT%{lua_libdir}/cyrussasl.so

%check
lua -e \
  'package.cpath="%{buildroot}%{lua_libdir}/?.so;"..package.cpath;
   local cyrussasl = require("cyrussasl");
   print("Hello from "..cyrussasl.get_version().."!");'

%files
%license LICENSE
%doc README
%{lua_libdir}/cyrussasl.so

%changelog
%autochangelog
