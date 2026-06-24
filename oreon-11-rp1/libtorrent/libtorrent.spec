%global source0_hash none

Name:          libtorrent
# Automatically converted from old format: GPLv2+ - review is highly recommended.
License:       GPL-2.0-or-later
Version:       0.16.2
Release:       3%{?dist}
Summary:       BitTorrent library with a focus on high performance & good code
URL:           https://github.com/rakshasa/libtorrent/
Source0:       https://github.com/rakshasa/rtorrent/releases/download/v%{version}/libtorrent-%{version}.tar.gz

BuildRequires: autoconf
BuildRequires: automake
BuildRequires: curl-devel
BuildRequires: gcc
BuildRequires: gcc-c++
BuildRequires: libsigc++20-devel
BuildRequires: libtool
BuildRequires: openssl-devel
BuildRequires: pkgconfig
BuildRequires: zlib-devel
BuildRequires: make

%description
LibTorrent is a BitTorrent library written in C++ for *nix, with a focus 
on high performance and good code. The library differentiates itself 
from other implementations by transfering directly from file pages to 
the network stack. On high-bandwidth connections it is able to seed at 
3 times the speed of the official client.

%package devel
Summary: Libtorrent development environment
Requires: %{name} = %{version}-%{release}

%description devel
Header and library definition files for developing applications
with the libtorrent libraries.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1

%build
%configure --with-posix-fallocate
%make_build

%install
%make_install
rm -f $RPM_BUILD_ROOT%{_libdir}/*.la

%ldconfig_scriptlets

%files
%doc AUTHORS README.md
%license COPYING
%{_libdir}/libtorrent.so.*

%files devel
%{_libdir}/pkgconfig/libtorrent.pc
%{_includedir}/torrent
%{_libdir}/*.so

%changelog
%autochangelog

