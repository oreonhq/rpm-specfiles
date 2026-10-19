%global source0_hash 245bf6ec560c042cb8948e3d661189292587c5949104677f1eecddc54dbe7e37
Name:           luarocks
Version:        3.13.0
Release:        1%{?dist}
Summary:        A deployment and management system for Lua modules
License:        MIT
URL:            http://luarocks.org
Source0:        http://luarocks.org/releases/luarocks-%{version}.tar.gz
Source1:        config-5.1.lua
Patch0:         luarocks-3.9.1-dynamic_libdir.patch
BuildArch:      noarch
Obsoletes:      luarocks < 3.5.0-1
%if 0%{?el7}
%endif
Requires:       unzip
Requires:       zip
Requires:       gcc
# oreon:deps
BuildRequires:  lua-devel
BuildRequires:  make
# /oreon:deps
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
%oreon_prep
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
%oreon_autofiles main

%check

%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
