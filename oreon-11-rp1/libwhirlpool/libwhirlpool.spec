%global source0_hash ed9c478e2a7bfe19739d1776e53b2a1d7e5a75edb58aea38f11002470c027cc0

%global		_hardened_build 1

Summary:	Whirlpool cryptographic hash function library
Name:		libwhirlpool
Version:	1.1
Release:	11%{?dist}

License:	Unlicense-libwhirlpool
URL:		https://github.com/dfateyev/libwhirlpool

Source0:	https://github.com/dfateyev/libwhirlpool/archive/v%{version}.tar.gz

BuildRequires:  gcc
BuildRequires:	coreutils
BuildRequires:	make

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

# disable parallel build to get proper linking order
make

%install
make install DESTDIR=%{buildroot}
rm -f %{buildroot}%{_libdir}/*.la

%ldconfig_scriptlets

%files
%license COPYING
%doc ChangeLog AUTHORS README
%{_mandir}/man1/*.1*
%{_libdir}/libwhirlpool.so.*
%{_bindir}/whirlpoolsum

%files devel
%{_includedir}/whirlpool.h
%{_libdir}/libwhirlpool.so

%changelog
%autochangelog
