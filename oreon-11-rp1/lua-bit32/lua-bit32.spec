%global source0_hash d1ed32f091856f6fffab06232da79c48b437afd4cd89e5c1fc85d7905b011430
%global srcname lua-compat-5.3
%global srcver 0.10
%global lua_pkg_name bit32
%global lua51_version 5.1
%global lua51_libdir %{_libdir}/lua/%{lua51_version}
%global lua51_pkgdir %{_datadir}/lua/%{lua51_version}
%global lua51_builddir %{_builddir}/lua%{lua51_version}-%{lua_pkg_name}-%{version}-%{release}
Name:           lua-%{lua_pkg_name}
Version:        5.3.5.1
Release:        1%{?dist}
Summary:        Lua bit manipulation library
License:        MIT
URL:            https://luarocks.org/modules/siffiejoe/bit32
Source0:        https://github.com/keplerproject/%{srcname}/archive/v%{srcver}.tar.gz#/%{srcname}-%{srcver}.tar.gz
# oreon:deps
BuildRequires:  compat-lua-devel
BuildRequires:  gcc
BuildRequires:  lua-devel
# /oreon:deps
%description

%package -n lua%{lua51_version}-%{lua_pkg_name}
Summary:        Lua 5.2 bit manipulation library
Provides:       compat-%{name}
Requires:       lua(abi) = %{lua51_version}
%description -n lua%{lua51_version}-%{lua_pkg_name}

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n %{srcname}-%{srcver}

%build

gcc %{optflags} $(pkg-config --cflags lua) -I./c-api -DLUA_COMPAT_BITLIB \
    lbitlib.c \
    -shared -fPIC -o lua-bit32.so $(pkg-config --libs lua)
gcc %{optflags} $(pkg-config --cflags lua-5.1) -I./c-api -DLUA_COMPAT_BITLIB \
    lbitlib.c \
    -shared -fPIC -o compat-lua-bit32.so $(pkg-config --libs lua-5.1)
%install
install -d -m 0755 %{buildroot}%{lua_libdir}
install -m 0755 lua-bit32.so %{buildroot}%{lua_libdir}/bit32.so
install -d -m 0755 %{buildroot}%{lua51_libdir}
install -m 0755 compat-lua-bit32.so %{buildroot}%{lua51_libdir}/bit32.so
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%files -f %{oreon_filedir}/main.list
%files -n lua5.1-bit32 -f %{oreon_filedir}/lua5.1-bit32.list

%changelog

%autochangelog
