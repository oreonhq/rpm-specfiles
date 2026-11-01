%global source0_hash 53d3a46c6e7571ee4e63af8f3e43f5c01092eec257b084f37ac1bbbf5d69679f
%global debug_package %{nil}

Name: lua-srpm-macros
Version: 1
Release: 1%{?dist}
Summary: SRPM macros for Lua packages
License: MIT
URL: https://www.lua.org/
BuildArch: noarch
Source0: macros.lua-srpm
Source1: LICENSE
Requires: rpm

BuildRequires: oreon-rpm-macros

%description
SRPM macros for Lua source packages.

%prep
%oreon_sha256
cp %{SOURCE1} .

%build

%install
mkdir -p %{buildroot}%{_rpmmacrodir}
install -m 644 %{SOURCE0} %{buildroot}%{_rpmmacrodir}/macros.lua-srpm

%files
%license LICENSE
%{_rpmmacrodir}/macros.lua-srpm
