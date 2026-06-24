%global source0_hash none

Name:           luarocks
Version:        3.13.0
Release:        2%{?dist}
Summary:        A deployment and management system for Lua modules

License:        MIT
URL:            http://luarocks.org
Source0:        http://luarocks.org/releases/luarocks-%{version}.tar.gz
Source1:        config-5.1.lua

# Use /usr/lib64 as default LUA_LIBDIR
Patch0:         luarocks-3.9.1-dynamic_libdir.patch

BuildArch:      noarch
# this package was previously arched, and needs to be obsoleted
# to have an upgrade path
Obsoletes:      luarocks < 3.5.0-1

BuildRequires:  lua-devel
BuildRequires:  make
%if 0%{?el7}
BuildRequires:  lua-rpm-macros
%endif
%if 0%{?rhel} && 0%{?rhel} < 9
Requires:       lua(abi) = %{lua_version}
%endif
Requires:       unzip
Requires:       zip
Requires:       gcc

%if 0%{?fedora}
Recommends:     lua-sec
Recommends:     lua-devel
Recommends:     compat-lua-devel
Recommends:     make
Recommends:     cmake
%endif

%description
LuaRocks allows you to install Lua modules as self-contained packages
called "rocks", which also contain version dependency
information. This information is used both during installation, so
that when one rock is requested all rocks it depends on are installed
as well, and at run time, so that when a module is required, the
correct version is loaded. LuaRocks supports both local and remote
repositories, and multiple local rocks trees.


%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1


%build
./configure \
  --prefix=%{_prefix} \
  --lua-version=%{lua_version} \
  --with-lua=%{_prefix}
%make_build


%install
%make_install

mkdir -p %{buildroot}%{_prefix}/lib/luarocks/rocks-%{lua_version}

install -m 0644 %{SOURCE1} %{buildroot}%{_sysconfdir}/luarocks/config-5.1.lua

%check
# TODO - find how to run this without having to pre-download entire rocks tree
# ./test/run_tests.sh


%files
%license COPYING
%doc README.md
%dir %{_sysconfdir}/luarocks
%config(noreplace) %{_sysconfdir}/luarocks/config-%{lua_version}.lua
%config(noreplace) %{_sysconfdir}/luarocks/config-5.1.lua
%{_bindir}/luarocks
%{_bindir}/luarocks-admin
%{_prefix}/lib/luarocks
%{lua_pkgdir}/luarocks


%changelog
%autochangelog

