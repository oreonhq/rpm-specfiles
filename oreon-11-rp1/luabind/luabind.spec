%global source0_hash 80de5e04918678dd8e6dac3b22a34b3247f74bf744c719bae21faaa49649aaae

Name:		luabind
Version:	0.9.1
Release:	50%{?dist}
Summary:	A library that helps create bindings between C++ and Lua
License:	MIT
URL:		http://www.rasterbar.com/products/luabind.html
Source0:	http://download.sourceforge.net/luabind/%{name}-%{version}.tar.gz
BuildRequires:	boost-devel, boost-build, lua-devel >= 5.1
BuildRequires:	gcc-c++
# https://github.com/devurandom/luabind/commit/78509cc0242161116c989a08439ea28386deeca2
Patch0:		luabind-0.9.1-boost149fix.patch
# Lua 5.2 support
# https://github.com/luabind/luabind/commits/0.9
Patch1:		001-luabind-use-lua_compare.patch
Patch2:		002-luabind-deprecated-LUA_GLOBALSINDEX.patch
Patch3:		003-luabind-use-lua_rawlen.patch
Patch4:		004-luabind-getsetuservalue.patch
Patch5:		005-luabind-lua_resume_extra_param.patch
Patch6:		006-luabind-luaL_newstate.patch
Patch7:		007-luabind-lua-52-fix-test.patch
Patch8:		008-luabind-lua_pushglobaltable.patch
Patch9:		luabind-0.9.1-boost157fix.patch
Patch10:	luabind-0.9.1-lua-5.4.patch
# https://github.com/luabind/luabind/pull/34
Patch11:	luabind-0.9.1-orderfix.patch

%description
Luabind is a library that helps you create bindings between C++ and Lua. It 
has the ability to expose functions and classes, written in C++, to Lua. It 
will also supply the functionality to define classes in Lua and let them derive 
from other Lua classes or C++ classes. Lua classes can override virtual 
functions from their C++ base classes. It is written towards Lua 5.0, and does 
not work with Lua 4.

%package devel
Summary:	Development libraries and headers for luabind
Requires:	%{name} = %{version}-%{release}
Requires:	boost-devel

%description devel
This package contains the development libraries and headers for luabind.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q
%patch -P0 -p1 -b .boost
%patch -P1 -p1
%patch -P2 -p1
%patch -P3 -p1
%patch -P4 -p1
%patch -P5 -p1
%patch -P6 -p1
%patch -P7 -p1
%patch -P8 -p1
%patch -P9 -p1
%patch -P10 -p1 -b .lua54
%patch -P11 -p1 -b .orderfix
sed -i 's|$(prefix)/lib|$(prefix)/%{_lib}|g' Jamroot

# Perms cleanup
chmod -x doc/*.rst doc/*.png src/*.cpp luabind/*.hpp luabind/detail/*.hpp

%build
export BOOST_BUILD_PATH=%{_datadir}/boost-build/src/kernel
b2 %{?jobs:-j%{jobs}} -d+2 "cxxflags=%{optflags}" release

%install
export BOOST_BUILD_PATH=%{_datadir}/boost-build/src/kernel
b2 -d2 --prefix=%{buildroot}%{_prefix} --libdir=%{buildroot}%{_libdir} release install

%ldconfig_scriptlets

%files
%doc LICENSE
%{_libdir}/*.so.*

%files devel
%doc doc/*
%{_includedir}/luabind/
%{_libdir}/*.so

%changelog
%autochangelog
