%global source0_hash 26b813ad39c94fc930b168c3418e2e746af3b2e80b92f94f306f6f954cc31e7d

%global forgeurl https://github.com/brimworks/lua-zlib
%global tag v%{version}

Name:      lua-zlib
Version:   1.2
Release:   8%{?dist}
Summary:   Simple streaming interface to zlib for Lua
License:   MIT
URL:       %{forgeurl}

%forgemeta
Source:    %{forgesource}

BuildRequires: lua-devel
BuildRequires: gcc
BuildRequires: make
BuildRequires: zlib-devel

%description
%{summary}.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%forgesetup

%build
%make_build linux \
  LUAPATH=%{lua_pkgdir} \
  LUACPATH=%{lua_libdir} \
  INCDIR="-I%{_includedir}" \
  CFLAGS="$CFLAGS -fPIC" \
  LDFLAGS="$LDFLAGS -shared -fPIC"

%install
install -dD %{buildroot}%{lua_libdir}
%make_install LUACPATH=%{buildroot}%{lua_libdir}

%check
lua test.lua

%files
%license README
%doc README
%{lua_libdir}/zlib.so

%changelog
%autochangelog
