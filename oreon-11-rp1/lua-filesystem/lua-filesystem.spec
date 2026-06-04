%global source0_hash none

%if 0%{?el7} || 0%{?el10}
%bcond_with compat
%else
%bcond_without compat
%endif

%if %{with compat}
%{!?lua_compat_version: %global lua_compat_version 5.1}
%{!?lua_compat_libdir: %global lua_compat_libdir %{_libdir}/lua/%{lua_compat_version}}
%{!?lua_compat_builddir: %global lua_compat_builddir %{_builddir}/compat-lua-%{name}-%{version}-%{release}}
%endif

Name:           lua-filesystem
Version:        1.9.0
Release:        1%{?dist}
Summary:        File System Library for the Lua Programming Language

%global gitowner lunarmodules
%global gitproject luafilesystem
%global gittag %(echo %{version} | sed -e 's/\\./_/g')

License:        MIT
URL:            https://%{gitowner}.github.io/%{gitproject}/
Source0:        https://github.com/%{gitowner}/%{gitproject}/archive/refs/tags/v%{gittag}.tar.gz#/%{gitproject}-%{version}.tar.gz

BuildRequires:  gcc
BuildRequires:  make
BuildRequires:  lua-devel >= 5.1
%if 0%{?el7}
BuildRequires:  lua-rpm-macros
%endif
%if %{with compat}
BuildRequires:  compat-lua >= %{lua_compat_version}
BuildRequires:  compat-lua-devel >= %{lua_compat_version}
%endif
%if 0%{?fedora} < 33 && 0%{?rhel} < 9
Requires:       lua(abi) = %{lua_version}
%endif

%global _description %{expand:
LuaFileSystem is a Lua library developed to complement the set of functions
related to file systems offered by the standard Lua distribution.

LuaFileSystem offers a portable way to access the underlying directory
structure and file attributes.}

%description %{_description}


%if %{with compat}
%package -n lua%{lua_compat_version}-filesystem
Summary:        File System Library for the Lua Programming Language %{lua_compat_version}
%if 0%{?fedora} < 33 && 0%{?rhel} < 9
Requires:       lua(abi) = %{lua_compat_version}
%endif
Obsoletes:      lua-filesystem-compat < 1.8.0-3
Provides:       lua-filesystem-compat = %{version}-%{release}
Provides:       lua-filesystem-compat%{?_isa} = %{version}-%{release}

%description -n lua%{lua_compat_version}-filesystem %{_description}
%endif


%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%autosetup -n %{gitproject}-%{gittag}

%if %{with compat}
rm -rf %{lua_compat_builddir}
cp -a . %{lua_compat_builddir}
%endif

%build
%make_build LUA_LIBDIR=%{lua_libdir} CFLAGS="%{optflags} -fPIC %{?__global_ldflags}"

%if %{with compat}
pushd %{lua_compat_builddir}
%make_build LUA_LIBDIR=%{lua_compat_libdir} CFLAGS="-I%{_includedir}/lua-%{lua_compat_version} %{optflags} -fPIC %{?__global_ldflags}"
popd
%endif

%install
%make_install LUA_LIBDIR=%{lua_libdir}

%if %{with compat}
pushd %{lua_compat_builddir}
%make_install LUA_LIBDIR=%{lua_compat_libdir}
popd
%endif

%check
LUA_CPATH=%{buildroot}%{lua_libdir}/\?.so lua tests/test.lua

%if %{with compat}
LUA_CPATH=%{buildroot}%{lua_compat_libdir}/\?.so lua-%{lua_compat_version} tests/test.lua
%endif

%files
%license LICENSE
%doc docs/*
%doc README.md
%{lua_libdir}/*

%if %{with compat}
%files -n lua%{lua_compat_version}-filesystem
%license LICENSE
%doc docs/*
%doc README.md
%{lua_compat_libdir}/*
%endif

%changelog
* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 1.9.0-1
- Prepare for Oreon 11 (RP1)
