%global source0_hash 1ec7be26a1428b007feaafea4e234ce81b75634e993d6bd80b925215134d9ed3
%global debug_package %{nil}
%global    commit        93f6621b979f64aed4f31448cb3ce4b21b758f05
%global    date          20241207
%global    shortcommit   %(c=%{commit}; echo ${c:0:7})
%global    versiontag    1187
Name:           GENie
Version:        %{versiontag}^%{date}.%{shortcommit}
Release:        1%{?dist}
Summary:        Project generator tool
License:        BSD-3-Clause AND MIT
URL:            https://github.com/bkaradzic/GENie
Source0:        https://github.com/bkaradzic/%{name}/archive/%{commit}/%{name}-93f6621.tar.gz
Patch:          arch.patch
Recommends:     cmake
Recommends:     make
Recommends:     ninja-build
# oreon:deps
BuildRequires:  compat-lua-devel
BuildRequires:  gcc
BuildRequires:  lua-devel
BuildRequires:  make
# /oreon:deps
%description
GENie (pronounced as Jenny) is project generator tool. It automagically
generates project from Lua script, making applying the same settings for
multiple projects easy.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n %{name}-%{commit} -p 1
# Fix version information
# https://github.com/bkaradzic/GENie/pull/576
pushd src
pushd host
sed -i 's/1181/1187/g' version.h
sed -i 's/29e6832fdf3b106c0906d288c8ced6c0761b8985/6d94bd661b120b2b14432527d2d82fb79111cef0/g' version.h
popd
popd

%build

%make_build 
%install
install -D -p -m 755 bin/linux/genie %{buildroot}%{_bindir}/genie
%oreon_autofiles main

%check

%{buildroot}%{_bindir}/genie --version 2>&1 | grep 'version %{versiontag}'
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
