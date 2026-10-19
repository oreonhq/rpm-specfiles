%global source0_hash ed9c478e2a7bfe19739d1776e53b2a1d7e5a75edb58aea38f11002470c027cc0
%global		_hardened_build 1
Summary:        Whirlpool cryptographic hash function library
Name:		libwhirlpool
Version:	1.1
Release:        11%{?dist}
License:	Unlicense-libwhirlpool
URL:		https://github.com/dfateyev/libwhirlpool
Source0:        https://github.com/dfateyev/libwhirlpool/archive/v%{version}.tar.gz
# oreon:deps
BuildRequires:  coreutils
BuildRequires:  gcc
BuildRequires:  make
# /oreon:deps
%description
WHIRLPOOL cryptographic hash function library for UNIX and Linux.
Also provides 'whirlpoolsum' utility for easy calculation and checking
WHIRLPOOL hashes similar to 'md5sum' and 'shaXXXsum'.

%package devel
Summary:	Development files for %{name}
Requires:	%{name}%{?_isa} = %{version}-%{release}
%description devel
This package contains the header files and libraries for developing
with %{name}.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q

%build

%configure \
	--enable-shared \
	--disable-static
make
%install
make install DESTDIR=%{buildroot}
rm -f %{buildroot}%{_libdir}/*.la
%ldconfig_scriptlets
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*

%files -f %{oreon_filedir}/main.list
%files -n libwhirlpool-devel -f %{oreon_filedir}/libwhirlpool-devel.list

%changelog

%autochangelog
