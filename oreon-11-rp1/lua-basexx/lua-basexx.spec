%global source0_hash f87570e849253d69cbda6dbdcbf1227f416e1dd3d145df341a397b858717a6fe

%{!?luaver: %global luaver %(lua -e "print(string.sub(_VERSION, 5))" || echo 0)}
%global luapkgdir %{_datadir}/lua/%{luaver}

%global luacompatver 5.1
%global luacompatpkgdir %{_datadir}/lua/%{luacompatver}

%global luapkgname basexx

Name:           lua-%{luapkgname}
Version:        0.4.0
Release:        17%{?dist}
Summary:        BaseXX encoding and decoding library for Lua

License:        MIT
URL:            https://github.com/aiq/%{luapkgname}/
Source0:        https://github.com/aiq/%{luapkgname}/archive/v%{version}/%{name}-%{version}.tar.gz
BuildArch:      noarch

BuildRequires:  lua

%description
A Lua library for base2, base16, base32, base64, base85 decoding and encoding
of data strings.

%if 0%{?fedora} || 0%{?rhel} > 7
%package -n lua%{luacompatver}-%{luapkgname}
Summary:        BaseXX encoding and decoding library for Lua %{luacompatver}

%description -n lua%{luacompatver}-%{luapkgname}
A Lua library for base2, base16, base32, base64, base85 decoding and encoding
of data strings.
%endif

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n basexx-%{version}

%install
install -D -p -m 0644 lib/basexx.lua %{buildroot}/%{luapkgdir}/basexx.lua

%if 0%{?fedora} || 0%{?rhel} > 7
install -D -p -m 0644 lib/basexx.lua %{buildroot}/%{luacompatpkgdir}/basexx.lua
%endif

%files
%doc README.adoc
%license LICENSE
%{luapkgdir}/basexx.lua

%if 0%{?fedora} || 0%{?rhel} > 7
%files -n lua%{luacompatver}-%{luapkgname}
%doc README.adoc
%license LICENSE
%{luacompatpkgdir}/basexx.lua
%endif

%changelog
%autochangelog
