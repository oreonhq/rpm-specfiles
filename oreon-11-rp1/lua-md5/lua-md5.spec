%global source0_hash 0747a88d89c5d9b71e15fd614ac77a027627ce9ed222d3eb9ddee66f9fd46da4

%global luaver 5.4
%global lualibdir %{_libdir}/lua/%{luaver}
%global luapkgdir %{_datadir}/lua/%{luaver}

Name:           lua-md5
Version:        1.3
Release:        13%{?dist}
Summary:        Cryptographic Library for MD5 hashes for Lua

License:        MIT
URL:            https://github.com/keplerproject/md5
Source0:        https://github.com/keplerproject/md5/archive/1.3.tar.gz
# https://github.com/keplerproject/md5/commit/ceb84044ad481409ea1179f1bed98440c29abb59

BuildRequires:  lua >= %{luaver}, lua-devel >= %{luaver}
Requires:       lua >= %{luaver}
BuildRequires:  gcc
BuildRequires: make

%description
MD5 offers basic cryptographic facilities for Lua: a hash (digest)
function, a pair crypt/decrypt based on MD5 and CFB, and a pair crypt/decrypt
based on DES with 56-bit keys.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n md5-%{version}

%build
make CFLAGS="%{optflags} -fPIC"

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}%{lualibdir}
mkdir -p %{buildroot}%{luapkgdir}
make install LUA_DIR=%{buildroot}%{luapkgdir} LUA_LIBDIR=%{buildroot}%{lualibdir}

%files
%doc README.md doc/us/*
%{luapkgdir}/*
%{lualibdir}/*

%changelog
%autochangelog
