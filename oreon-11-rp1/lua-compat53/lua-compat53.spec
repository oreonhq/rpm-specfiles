%global source0_hash bec3a23114a3d9b3218038309657f0f506ad10dfbc03bb54e91da7e5ffdba0a2
%{!?luaver: %global luaver %(lua -e "print(string.sub(_VERSION, 5))" || echo 0)}
%global luapkgdir %{_datadir}/lua/%{luaver}
%global lualibdir %{_libdir}/lua/%{luaver}
%global luaincdir %{_includedir}/lua-%{luaver}
%global luacompatver 5.1
%global luacompatpkgdir %{_datadir}/lua/%{luacompatver}
%global luacompatlibdir %{_libdir}/lua/%{luacompatver}
%global luacompatincdir %{_includedir}/lua-%{luacompatver}
%global lualib lua
%global luapkgname compat53
Name:           lua-%{luapkgname}
Version:        0.7
Release:        1%{?dist}
Summary:        Compatibility module providing Lua-5.3-style APIs for Lua 5.1
License:        MIT
URL:            https://github.com/keplerproject/lua-compat-5.3
Source0:        https://github.com/keplerproject/lua-compat-5.3/archive/v%{version}/%{name}-%{version}.tar.gz
# oreon:deps
BuildRequires:  gcc
BuildRequires:  lua-devel
BuildRequires:  pkgconfig
# /oreon:deps
%description
This is a small module that aims to make it easier to write code in a
Lua-5.3-style that is compatible with Lua 5.1, Lua 5.2, and Lua 5.3. This does
not make Lua 5.2 (or even Lua 5.1) entirely compatible with Lua 5.3, but it
brings the API closer to that of Lua 5.3.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n lua-compat-5.3-%{version}

%build

CFLAGS="%{?optflags} -fPIC $(pkg-config --cflags %{lualib})"
LDFLAGS="%{?build_ldflags} $(pkg-config --libs %{lualib})"
gcc $CFLAGS -c lutf8lib.c -o lutf8lib.o
gcc $CFLAGS -c lstrlib.c -o lstrlib.o
gcc $CFLAGS -c ltablib.c -o ltablib.o
gcc -shared $LDFLAGS -o utf8.so lutf8lib.o
gcc -shared $LDFLAGS -o string.so lstrlib.o
gcc -shared $LDFLAGS -o table.so ltablib.o
%install
PKGDIR=%{buildroot}/%{luapkgdir}
LIBDIR=%{buildroot}/%{lualibdir}
mkdir -p "$PKGDIR/%{luapkgname}"
mkdir -p "$LIBDIR/%{luapkgname}"
install -d -m 0755 "$PKGDIR/%{luapkgname}"
install -d -m 0755 "$LIBDIR/%{luapkgname}"
install -p -m 0644 %{luapkgname}/{init,module}.lua -t "$PKGDIR/%{luapkgname}/"
install -p -m 0755 {utf8,string,table}.so -t "$LIBDIR/%{luapkgname}/"
%oreon_autofiles main

%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
