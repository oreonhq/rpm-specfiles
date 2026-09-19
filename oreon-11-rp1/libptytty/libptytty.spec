%global source0_hash 8033ed3aadf28759660d4f11f2d7b030acf2a6890cb0f7926fb0cfa6739d31f7

Name:    libptytty
Version: 2.0
Release: 14%{?dist}
Summary: OS independent and secure pty/tty and utmp/wtmp/lastlog handling
License: GPL-2.0-or-later
URL:     http://software.schmorp.de/pkg/libptytty.html

Source0: http://dist.schmorp.de/%{name}/%{name}-%{version}.tar.gz
Source1: http://dist.schmorp.de/%{name}/%{name}-%{version}.tar.gz.sig
Source2: http://dist.schmorp.de/signing-key.pub
Source3: http://dist.schmorp.de/signing-key.pub.gpg.sig
Source4: gpgkey-84874CAB6D1A397A.gpg
# To recreate Source4:
#     gpg --recv-key 84874CAB6D1A397A
#     gpg --export --export-options export-minimal 84874CAB6D1A397A \
#         > gpgkey-84874CAB6D1A397A.gpg

Patch0: libptytty-cmake-c99.patch

BuildRequires: cmake
BuildRequires: gcc-g++
BuildRequires: gnupg2
BuildRequires: git
BuildRequires: ninja-build
BuildRequires: signify

%global desc \
libptytty is a small library that offers pseudo-tty management in an \
OS-independent way.  It also offers session database support (utmp and \
optional wtmp/lastlog updates for login shells) and supports fork'ing after \
startup and dropping privileges in the calling process.  Libptytty is \
written in C++, but it also offers a C-only API. \
%{nil}
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

%files
%{!?_licensedir:%global license %%doc}
%license COPYING
%{_libdir}/*.so.*

%files devel
%{_includedir}/*
%{_libdir}/*.so
%{_libdir}/pkgconfig/*.pc
%{_mandir}/man3/*
%doc Changes
%doc README

%changelog
%autochangelog
