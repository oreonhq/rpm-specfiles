%global source0_hash f2dafd7a70ed732c2ab1811205379775540ef1190417daa5f508cfcad0dd8ec6

%global date          20210115
%global commit0       3bdb0b13e5ceb6b686f4e7f9424179b5bcb71ab8
%global shortcommit0  %(c=%{commit0}; echo ${c:0:7})
%global the_owner     srdgame

Name:           librs232
Version:        1.0.4
Release:        17.%{date}git%{shortcommit0}%{?dist}
Summary:        Library for serial communications over RS-232 with Lua bindings
License:        MIT
Url:            https://github.com/%{the_owner}/%{name}/
Source:         https://github.com/%{the_owner}/%{name}/archive/%{commit0}.tar.gz#/%{name}-%{version}-%{date}git%{shortcommit0}.tar.gz
# Fix FTBFS on gcc 13:
# Upstrem reference: https://patch-diff.githubusercontent.com/raw/srdgame/librs232/pull/10.patch
Patch0:         https://patch-diff.githubusercontent.com/raw/%{the_owner}/%{name}/pull/10.patch#/%{name}-%{version}-Fix-rs232_set_-prototypes-mismatch.patch

BuildRequires:  /usr/bin/git
BuildRequires:  gcc
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  libtool
BuildRequires:  pkgconfig
BuildRequires:  lua >= 5.1
BuildRequires:  lua-devel >= 5.1
BuildRequires:  make

%description
%{name} is a multi-platform library that provides support for communicating
over serial ports (e.g. RS-232). It also provides Lua bindings.

%package devel
Summary: Development files for %{name}
License: MIT
Requires: %{name}%{?_isa} = %{version}-%{release}

%description devel
The %{name}-devel package contains C header files for developing
applications that use %{name} library.

%package -n lua-%{name}
Requires: %{name}%{?_isa} = %{version}-%{release}
Summary: Lua bindings for %{name}
License: MIT
Requires: lua(abi) = %{lua_version}

%description -n lua-%{name}
The lua-%{name} package provides Lua binding for %{name} library.
It allows Lua programs to communicate over serial ports.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -S git -n %{name}-%{commit0}
export LUA_INCLUDE=

%build
./autogen.sh
%configure --disable-static

%make_build

%install
%make_install
# Remove unneeded .la files
find %{buildroot} -name '*.la' -exec rm {} \;

%files
%license COPYING
%doc AUTHORS doc/example.lua
%{_libdir}/*.so.*

%ldconfig_scriptlets

%files devel
%{_libdir}/*.so
%{_includedir}/%{name}
%{_libdir}/pkgconfig/%{name}*.pc

%files -n lua-%{name}
%{lua_libdir}/*.so

%changelog
%autochangelog
