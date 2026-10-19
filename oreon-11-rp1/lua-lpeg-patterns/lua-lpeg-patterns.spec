%global source0_hash d1fabf897024822eb2544fd811fc80b85655972804511b9fd8cfea377fb16e0e
%{!?luaver: %global luaver %(lua -e "print(string.sub(_VERSION, 5))" || echo 0)}
%global luapkgdir %{_datadir}/lua/%{luaver}
%global luacompatver 5.1
%global luacompatpkgdir %{_datadir}/lua/%{luacompatver}
%global luapkgname lpeg-patterns
Name:           lua-%{luapkgname}
Version:        0.5
Release:        1%{?dist}
Summary:        A collection of LPEG patterns
License:        MIT
URL:            https://github.com/daurnimator/lpeg_patterns
Source0:        https://github.com/daurnimator/lpeg_patterns/archive/v%{version}/%{name}-%{version}.tar.gz
BuildArch:      noarch
Requires:       lua-lpeg
# oreon:deps
BuildRequires:  lua
# /oreon:deps
%description
A collection of LPEG patterns for validating/searching user input.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n lpeg_patterns-%{version}

%install
install -d -m 0755 %{buildroot}%{luapkgdir}/lpeg_patterns
install -p -m 0644 lpeg_patterns/* -t %{buildroot}%{luapkgdir}/lpeg_patterns/
%oreon_autofiles main

%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
