%global source3_hash 8d00077fa8b16f489f3355911564de647f468b4e7a8516375a2c0ca2ee32427b
%global source2_hash 48ef5720d77a870f25737b8f66fe2c1f88a01810013df70cb8155add904288e4
%global source1_hash 2afa2f572b6d4840ea2b4f9cf5ce5b71fc14fd6d91d2d315c38cac80c01bd7ef
%global source0_hash 8033ed3aadf28759660d4f11f2d7b030acf2a6890cb0f7926fb0cfa6739d31f7
Name:    libptytty
Version: 2.0
Release:        1%{?dist}
Summary:        OS independent and secure pty/tty and utmp/wtmp/lastlog handling
License: GPL-2.0-or-later
URL:     http://software.schmorp.de/pkg/libptytty.html
Source0:        http://dist.schmorp.de/%{name}/%{name}-%{version}.tar.gz
Source1: http://dist.schmorp.de/%{name}/%{name}-%{version}.tar.gz.sig
Source2: http://dist.schmorp.de/signing-key.pub
Source3: http://dist.schmorp.de/signing-key.pub.gpg.sig
Source4: gpgkey-84874CAB6D1A397A.gpg
Patch0: libptytty-cmake-c99.patch
%global desc \
libptytty is a small library that offers pseudo-tty management in an \
OS-independent way.  It also offers session database support (utmp and \
optional wtmp/lastlog updates for login shells) and supports fork'ing after \
startup and dropping privileges in the calling process.  Libptytty is \
written in C++, but it also offers a C-only API. \
%{nil}
# oreon:deps
BuildRequires:  cmake
BuildRequires:  gcc-g++
BuildRequires:  git
BuildRequires:  gnupg2
BuildRequires:  ninja-build
BuildRequires:  signify
# /oreon:deps
%description %{desc}

%package devel
Summary: Development headers for libptytty
Requires: %{name}%{?_isa} = %{version}-%{release}
%description devel
%desc

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%{gpgverify} --keyring='%{SOURCE4}' --signature='%{SOURCE3}' --data='%{SOURCE2}'
signify -V -p '%{SOURCE2}' -m '%{SOURCE0}'
%autosetup -S git

%build

%cmake -G Ninja
%cmake_build
%install
%cmake_install
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*

%files -f %{oreon_filedir}/main.list
%files -n libptytty-devel -f %{oreon_filedir}/libptytty-devel.list

%changelog

%autochangelog
