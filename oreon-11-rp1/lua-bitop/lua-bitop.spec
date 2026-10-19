%global source0_hash 1207c9293dcd52eb9dca6538d1b87352bd510f4e760938f5048433f7f272ce99
%{!?luaver: %global luaver %(lua -e "print(string.sub(_VERSION, 5))" || echo 0)}
%global lualibdir %{_libdir}/lua/%{luaver}
%global luacompatver 5.1
%global luacompatlibdir %{_libdir}/lua/%{luacompatver}
%global lualib lua
%global luapkgname bitop
Name:           lua-%{luapkgname}
Version:        1.0.2
Release:        19%{?dist}
Summary:        C extension module for Lua which adds bit-wise operations on numbers
License:        MIT
URL:            http://bitop.luajit.org/
Source0:        http://bitop.luajit.org/download/LuaBitOp-%{version}.tar.gz
# oreon:deps
BuildRequires:  gcc
BuildRequires:  lua
BuildRequires:  lua-devel
BuildRequires:  make
BuildRequires:  pkgconfig
# /oreon:deps
%description
Lua BitOp is a C extension module for Lua 5.1/5.2 which adds bit-wise
operations on numbers.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q  -n LuaBitOp-%{version}

%build

CFLAGS="%{optflags} -fPIC $(pkg-config --cflags %{lualib})"
LDFLAGS="%{build_ldflags} $(pkg-config --libs %{lualib})"
%make_build CFLAGS="$CFLAGS" LDFLAGS="$LDFLAGS"
%install
install -d -m 0755 %{buildroot}%{lualibdir}
install -p -m 0755 bit.so %{buildroot}%{lualibdir}/bit.so
%oreon_autofiles main

%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
