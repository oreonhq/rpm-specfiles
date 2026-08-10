%global source0_hash f3054e1ce26ca65ecaa7dcf193ea97d6a06933e4aa516779ebb89a6727d8a28f

%{!?luaver: %global luaver %(lua -e "print(string.sub(_VERSION, 5))" || echo 0)}
%global lualibdir %{_libdir}/lua/%{luaver}
%global luapkgdir %{_datadir}/lua/%{luaver}

%global luacompatver 5.1
%global luacompatlibdir %{_libdir}/lua/%{luacompatver}
%global luacompatpkgdir %{_datadir}/lua/%{luacompatver}

%global luapkgname luaossl

Name:           lua-%{luapkgname}
Version:        20200709
Release:        10%{?dist}
Summary:        Most comprehensive OpenSSL module in the Lua universe

License:        MIT
URL:            https://github.com/wahern/%{luapkgname}
Source0:        https://github.com/wahern/%{luapkgname}/archive/rel-%{version}/%{name}-%{version}.tar.gz
Patch0:         luaossl-lua55.patch

Patch1:         openssl-3-compat.patch

BuildRequires:  gcc
BuildRequires:  make
BuildRequires:  openssl-devel
BuildRequires:  lua
BuildRequires:  lua-devel

%if 0%{?fedora} || 0%{?rhel} > 7
# BuildRequires:  compat-lua
BuildRequires:  compat-lua-devel
%endif

Requires:       lua(abi) = %{luaver}

%description
luaossl is a comprehensive binding to OpenSSL for Lua 5.1, 5.2, and later.

%if 0%{?fedora} || 0%{?rhel} > 7
%package -n lua%{luacompatver}-%{luapkgname}
Summary:        Most comprehensive OpenSSL module in the Lua universe
Requires:       lua(abi) = %{luacompatver}

%description -n lua%{luacompatver}-%{luapkgname}
luaossl is a comprehensive binding to OpenSSL for Lua 5.1, 5.2, and later.
%endif

%package doc
Summary:        Documentation for OpenSSL Lua module
BuildArch:      noarch
Requires:       %{name} = %{version}
%if 0%{?fedora} || 0%{?rhel} > 7
Requires:       lua%{luacompatver}-%{luapkgname} = %{version}
%endif

%description doc
Documentation for the Stackable Continuation Queues library
for the Lua Programming Language

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1 -n %{luapkgname}-rel-%{version}

%patch -P1 -p1

%build
export CFLAGS="%{?optflags} -fPIC"
export LDFLAGS="%{?build_ldflags}"
make LUA_APIS="%{luaver}" %{?_smp_mflags} prefix=%{_prefix} libdir=%{_libdir}

%if 0%{?fedora} || 0%{?rhel} > 7
make LUA_APIS="%{luacompatver}" %{?_smp_mflags} prefix=%{_prefix} libdir=%{_libdir} CFLAGS="$CFLAGS -I%{_includedir}/lua-%{luacompatver}"
%endif

%install
make DESTDIR=%{buildroot} prefix=%{_prefix} libdir=%{_libdir} install%{luaver}
install -d -m 0755 %{buildroot}%{_pkgdocdir}
install -p -m 0644 doc/luaossl.pdf %{buildroot}%{_pkgdocdir}/luaossl.pdf

%if 0%{?fedora} || 0%{?rhel} > 7
make DESTDIR=%{buildroot} prefix=%{_prefix} libdir=%{_libdir} install%{luacompatver}
%endif

%files
%{luapkgdir}/openssl
%{luapkgdir}/openssl.lua
%{lualibdir}/_openssl.so
%license LICENSE

%if 0%{?fedora} || 0%{?rhel} > 7
%files -n lua%{luacompatver}-%{luapkgname}
%{luacompatpkgdir}/openssl
%{luacompatpkgdir}/openssl.lua
%{luacompatlibdir}/_openssl.so
%license LICENSE
%endif

%files doc
%{_pkgdocdir}

%changelog
%autochangelog
