%global source0_hash 1207c9293dcd52eb9dca6538d1b87352bd510f4e760938f5048433f7f272ce99

%{!?luaver: %global luaver %(lua -e "print(string.sub(_VERSION, 5))" || echo 0)}
%global lualibdir %{_libdir}/lua/%{luaver}

%global luacompatver 5.1
%global luacompatlibdir %{_libdir}/lua/%{luacompatver}

%if 0%{?fedora} || 0%{?rhel} > 7
%global lualib lua-%{luacompatver}
%else
%global lualib lua
%endif

%global luapkgname bitop

Name:           lua-%{luapkgname}
Version:        1.0.2
Release:        19%{?dist}
Summary:        C extension module for Lua which adds bit-wise operations on numbers

License:        MIT
URL:            http://bitop.luajit.org/
Source0:        http://bitop.luajit.org/download/LuaBitOp-%{version}.tar.gz

BuildRequires: make
BuildRequires:  pkgconfig
BuildRequires:  gcc
%if 0%{?fedora} || 0%{?rhel} > 7
BuildRequires:  compat-lua
BuildRequires:  compat-lua-devel
%else
BuildRequires:  lua
BuildRequires:  lua-devel
%endif

%if 0%{?rhel} && 0%{?rhel} <= 7
Requires:       lua
%endif

%description
Lua BitOp is a C extension module for Lua 5.1/5.2 which adds bit-wise
operations on numbers.

%if 0%{?fedora} || 0%{?rhel} > 7
%package -n lua%{luacompatver}-%{luapkgname}
Summary:        C extension module for Lua %{luacompatver} which adds bit-wise operations on numbers
Requires:       lua(abi) = %{luacompatver}

%description -n lua%{luacompatver}-%{luapkgname}
Lua BitOp is a C extension module for Lua 5.1/5.2 which adds bit-wise
operations on numbers.
%endif

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q  -n LuaBitOp-%{version}

%build
CFLAGS="%{optflags} -fPIC $(pkg-config --cflags %{lualib})"
LDFLAGS="%{build_ldflags} $(pkg-config --libs %{lualib})"
%make_build CFLAGS="$CFLAGS" LDFLAGS="$LDFLAGS"

%install
%if 0%{?fedora} || 0%{?rhel} > 7
install -d -m 0755 %{buildroot}%{luacompatlibdir}
install -p -m 0755 bit.so %{buildroot}%{luacompatlibdir}/bit.so
%else
install -d -m 0755 %{buildroot}%{lualibdir}
install -p -m 0755 bit.so %{buildroot}%{lualibdir}/bit.so
%endif

%if 0%{?rhel} && 0%{?rhel} <= 7
%files
%doc README
%{lualibdir}/bit.so
%endif

%if 0%{?fedora} || 0%{?rhel} > 7
%files -n lua%{luacompatver}-%{luapkgname}
%doc README
%{luacompatlibdir}/bit.so
%endif

%changelog
%autochangelog
