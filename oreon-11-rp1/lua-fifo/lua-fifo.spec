%global source0_hash 85cad0c2f9eac1cd3e08c5134feb655e0b928e1e22363c3ef3293a194c0eb53f

%{!?luaver: %global luaver %(lua -e "print(string.sub(_VERSION, 5))" || echo 0)}
%global luapkgdir %{_datadir}/lua/%{luaver}

%global luacompatver 5.1
%global luacompatpkgdir %{_datadir}/lua/%{luacompatver}

%global luapkgname fifo

Name:           lua-%{luapkgname}
Version:        0.2
Release:        16%{?dist}
Summary:        FIFO library for Lua

License:        MIT
URL:            https://github.com/daurnimator/%{luapkgname}.lua
Source0:        https://github.com/daurnimator/%{luapkgname}.lua/archive/%{version}/%{name}-%{version}.tar.gz
BuildArch:      noarch

BuildRequires:  lua
BuildRequires:  pandoc

%description
A lua library/'class' that implements a FIFO. Objects in the fifo
can be of any type, including nil.

%if 0%{?fedora} || 0%{?rhel} > 7
%package -n lua%{luacompatver}-%{luapkgname}
Summary:        FIFO library for Lua %{luacompatver}

%description -n lua%{luacompatver}-%{luapkgname}
A lua library/'class' that implements a FIFO. Objects in the fifo
can be of any type, including nil.
%endif

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n fifo.lua-%{version}

%build
pandoc doc/index.md -s -t man -o fifo.lua.3

%install
install -D -p -m 0644 fifo.lua %{buildroot}/%{luapkgdir}/fifo.lua
install -D -p -m 0644 fifo.lua.3 %{buildroot}/%{_mandir}/man3/fifo.lua.3

%if 0%{?fedora} || 0%{?rhel} > 7
install -D -p -m 0644 fifo.lua %{buildroot}/%{luacompatpkgdir}/fifo.lua
%endif

%files
%license LICENSE
%{_mandir}/man3/fifo.lua.3*
%{luapkgdir}/fifo.lua

%if 0%{?fedora} || 0%{?rhel} > 7
%files -n lua%{luacompatver}-%{luapkgname}
%license LICENSE
%{_mandir}/man3/fifo.lua.3*
%{luacompatpkgdir}/fifo.lua
%endif

%changelog
%autochangelog
