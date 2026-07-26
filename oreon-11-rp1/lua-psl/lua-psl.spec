%global source0_hash c7d529d33fcd9d898668014d174ed1dc1257e9076da98729d94a4e8b8d231d40

%{!?luaver: %global luaver %(lua -e "print(string.sub(_VERSION, 5))" || echo 0)}
%global lualibdir %{_libdir}/lua/%{luaver}

%global luacompatver 5.1
%global luacompatlibdir %{_libdir}/lua/%{luacompatver}

%global luapkgname psl

Name:           lua-%{luapkgname}
Version:        0.3
Release:        18%{?dist}
Summary:        Lua bindings to Public Suffix List library

License:        MIT
URL:            https://github.com/daurnimator/lua-psl
Source0:        https://github.com/daurnimator/lua-psl/archive/v%{version}/%{name}-%{version}.tar.gz

BuildRequires:  pkgconfig
BuildRequires:  gcc
BuildRequires:  libpsl-devel
BuildRequires:  lua
BuildRequires:  lua-devel

%if 0%{?fedora} || 0%{?rhel} > 7
BuildRequires:  compat-lua
BuildRequires:  compat-lua-devel
%endif

Requires:       lua(abi) = %{luaver}

%description
Lua bindings to libpsl, a C library that handles the Public Suffix List (PSL).

The PSL is a list of domains where there may be sub-domains outside of the
administrator's control. e.g. the administrator of '.com' does not manage
'github.com'.

%if 0%{?fedora} || 0%{?rhel} > 7
%package -n lua%{luacompatver}-%{luapkgname}
Summary:        Lua %{luacompatver} bindings to Public Suffix List library
Requires:       lua(abi) = %{luacompatver}

%description -n lua%{luacompatver}-%{luapkgname}
Lua %{luacompatver} bindings to libpsl, a C library that handles the Public
Suffix List (PSL).

The PSL is a list of domains where there may be sub-domains outside of the
administrator's control. e.g. the administrator of '.com' does not manage
'github.com'.
%endif

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n %{name}-%{version}

%build
gcc -fPIC %{?optflags} $(pkg-config --cflags lua libpsl) -o psl/psl.o -c psl/psl.c
gcc -shared %{?build_ldflags} -o psl.so psl/psl.o $(pkg-config --libs lua libpsl)

%if 0%{?fedora} || 0%{?rhel} > 7
gcc -fPIC %{?optflags} $(pkg-config --cflags lua-%{luacompatver} libpsl) -o psl/psl.o -c psl/psl.c
gcc -shared %{?build_ldflags} -o psl-%{luacompatver}.so psl/psl.o $(pkg-config --libs lua-%{luacompatver} libpsl)
%endif

%install
install -d -m 0755 %{buildroot}%{lualibdir}
install -p -m 0755 psl.so %{buildroot}%{lualibdir}/psl.so
%if 0%{?fedora} || 0%{?rhel} > 7
install -d -m 0755 %{buildroot}%{luacompatlibdir}
install -p -m 0755 psl-%{luacompatver}.so %{buildroot}%{luacompatlibdir}/psl.so
%endif

%files
%license LICENSE
%{lualibdir}/psl.so

%if 0%{?fedora} || 0%{?rhel} > 7
%files -n lua%{luacompatver}-%{luapkgname}
%license LICENSE
%{luacompatlibdir}/psl.so
%endif

%changelog
%autochangelog
