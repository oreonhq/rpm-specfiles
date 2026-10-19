%global source0_hash b4ae64921b07a96661695ebd5aac0dec813d1a68e546a61609113d7843f5b617
%ifarch aarch64
%bcond_with tests
%else
%bcond_without tests
%endif
%define abi_version 0.98
Name:			gauche
Version:		0.9.12
Release:        1%{?dist}
Summary:        Scheme script interpreter with multibyte character handling
License:		BSD-3-Clause AND MIT
URL:			http://practical-scheme.net/gauche
Source0:        https://github.com/shirok/Gauche/releases/download/release0_9_12/Gauche-%{version}.tgz
Patch0:			%{name}-ext-ldflags.patch
Patch1:			%{name}-xz-info.patch
ExcludeArch:	armv7hl
Requires:		lib%{name}%{?_isa} = %{version}-%{release}
Recommends:		slib
# oreon:deps
BuildRequires:  gcc
BuildRequires:  gdbm-devel
BuildRequires:  libxcrypt-devel
BuildRequires:  make
BuildRequires:  mbedtls-devel
BuildRequires:  openssl
BuildRequires:  texinfo
BuildRequires:  zlib-devel
# /oreon:deps
%description
Gauche is a Scheme interpreter conforming Revised^5 Report on
Algorithmic Language Scheme. It is designed for rapid development of
daily tools like system management and text processing. It can handle
multibyte character strings natively.

%package -n lib%{name}
Summary: Gauche runtime shared library
%description -n lib%{name}
This package contains Gauche runtime shared library

%package -n lib%{name}-static
Summary: Statically linked library for Gauce
Requires:	lib%{name}%{?_isa} = %{version}-%{release}
%description -n lib%{name}-static
This package contains statically linked library for Gauce.
Most users should *not* install this.

%package devel
Summary: Development files for Gauche
Requires:	lib%{name}%{?_isa} = %{version}-%{release}
%description devel
This package contains development files for Gauche.

%package doc
Summary: Documentation files for Gauche
%description doc
This package contains info documents of the reference manual of Gauche
(English, Japanese).

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%global oreon_srcdir Gauche-%{version}
%oreon_prep
%build

%configure --with-rpath=no --enable-threads=pthreads --enable-multibyte=utf-8 --with-slib=%{_datadir}/slib --enable-ipv6
LD_LIBRARY_PATH=`pwd`/src %make_build
%install
LD_LIBRARY_PATH=`pwd`/src %make_install
chmod -R u+w %{buildroot}
find -name '*.c' | xargs chmod 0644
%oreon_autofiles main usr/*/lib*.so.* usr/*/lib*.so.* usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%if %{with tests}
%check

LD_LIBRARY_PATH=`pwd`/src make check
%endif
%post

/usr/bin/gosh -u slib -e "(require 'logical)" -e "(exit 0)" > /dev/null 2>&1 || echo
%files -f %{oreon_filedir}/main.list
%files -n libgauche -f %{oreon_filedir}/libgauche.list
%files -n libgauche-static -f %{oreon_filedir}/libgauche-static.list
%files -n gauche-devel -f %{oreon_filedir}/gauche-devel.list
%files -n gauche-doc -f %{oreon_filedir}/gauche-doc.list

%changelog

%autochangelog
