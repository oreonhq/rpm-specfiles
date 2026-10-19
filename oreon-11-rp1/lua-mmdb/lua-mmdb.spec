%global source0_hash f81f06613eefaaa306e714abf425e69e2df6ec2007916d8acd910a044727cfa4
%{!?luaver: %global luaver %(lua -e "print(string.sub(_VERSION, 5))" || echo 0)}
%global luapkgdir %{_datadir}/lua/%{luaver}
%global luacompatver 5.1
%global luacompatpkgdir %{_datadir}/lua/%{luacompatver}
%global luapkgname mmdb
Name:           lua-%{luapkgname}
Version:        0.2
Release:        1%{?dist}
Summary:        MaxMind database parser for Lua
License:        MIT
URL:            https://github.com/daurnimator/mmdblua
Source0:        https://github.com/daurnimator/mmdblua/archive/v%{version}/%{name}-%{version}.tar.gz
BuildArch:      noarch
# oreon:deps
BuildRequires:  lua
# /oreon:deps
%description
A Lua library for reading MaxMind's Geolocation database format.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n mmdblua-%{version}

%install
install -d -m 0755 %{buildroot}/%{luapkgdir}/%{luapkgname}
install -p -m 0644 %{luapkgname}/init.lua %{buildroot}/%{luapkgdir}/%{luapkgname}/init.lua
%oreon_autofiles main

%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
