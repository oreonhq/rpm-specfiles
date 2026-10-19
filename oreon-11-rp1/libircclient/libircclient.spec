%global source0_hash bbb26f3af348b252c5204917a7f91cfdf172f1b6afbf4df1e561b03e20503c2d
%global major	1
%global with_docs	0
Name:		libircclient
Summary:        C library to create IRC clients
Version:	1.10
Release:        4%{?dist}
License:	LGPL-3.0-or-later
URL:		https://www.ulduzsoft.com/libircclient/
Source0:        https://downloads.sourceforge.net/libircclient/%{name}-%{version}.tar.gz
Patch0:		libircclient-rfc.patch
Patch1:		libircclient-1.8-nostrip.patch
# oreon:deps
BuildRequires:  gcc-c++
BuildRequires:  make
BuildRequires:  openssl-devel
# /oreon:deps
%description
libircclient is a small but extremely powerful library which implements
the IRC protocol. It is designed to be small, fast, portable and compatible
with the RFC standards as well as non-standard but popular features.
It is perfect for building the IRC clients and bots.

%package	devel
Summary:	Development files for libircclient
Requires:	%{name}%{?_isa} = %{version}-%{release}
%description	devel
This package contains development files for libircclient.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q
# Correct use of deprecated function to detect ssl
sed -e 's/SSL_library_init/SSL_CTX_new/g' -i configure
rm -rvf cocoa
%patch -P0 -p1
%patch -P1 -p1

%build

%configure --enable-shared --enable-threads --enable-openssl --enable-ipv6
make %{?_smp_mflags}
%install
make install DESTDIR=%{buildroot}
mkdir -p %{buildroot}%{_mandir}/man1
cp -p man/%{name}.1 %{buildroot}%{_mandir}/man1
%ldconfig_scriptlets
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*

%files -f %{oreon_filedir}/main.list
%files -n libircclient-devel -f %{oreon_filedir}/libircclient-devel.list

%changelog

%autochangelog
