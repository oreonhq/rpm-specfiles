%global source0_hash 10b1b6c6f2d22560f512f9896a6672ec5ae0eea1390ff8e662be1d5d9625b438

%{!?luaver: %global luaver %(lua -e "print(string.sub(_VERSION, 5))" || echo 0)}
%global luapkgdir %{_datadir}/lua/%{luaver}

%global luacompatver 5.1
%global luacompatpkgdir %{_datadir}/lua/%{luacompatver}

%global majorversion 0
%global minorversion 4
%global tagname version_%{majorversion}v%{minorversion}

%global luapkgname binaryheap

Name:           lua-%{luapkgname}
Version:        %{majorversion}.%{minorversion}
Release:        16%{?dist}
Summary:        Binary heap implementation for Lua

License:        MIT
URL:            https://github.com/Tieske/%{luapkgname}.lua
Source0:        https://github.com/Tieske/%{luapkgname}.lua/archive/%{tagname}/%{name}-%{version}.tar.gz
BuildArch:      noarch

BuildRequires:  lua

%description
A Lua library implementing binary heap algorithm.

%if 0%{?fedora} || 0%{?rhel} > 7
%package -n lua%{luacompatver}-%{luapkgname}
Summary:        Binary heap implementation for Lua %{luacompatver}

%description -n lua%{luacompatver}-%{luapkgname}
A Lua library implementing binary heap algorithm.
%endif

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n binaryheap.lua-%{tagname}

%install
install -D -p -m 0644 src/binaryheap.lua %{buildroot}/%{luapkgdir}/binaryheap.lua

%if 0%{?fedora} || 0%{?rhel} > 7
install -D -p -m 0644 src/binaryheap.lua %{buildroot}/%{luacompatpkgdir}/binaryheap.lua
%endif

%files
%doc docs/*
%doc examples
%{luapkgdir}/binaryheap.lua

%if 0%{?fedora} || 0%{?rhel} > 7
%files -n lua%{luacompatver}-%{luapkgname}
%doc docs/*
%doc examples
%{luacompatpkgdir}/binaryheap.lua
%endif

%changelog
%autochangelog
