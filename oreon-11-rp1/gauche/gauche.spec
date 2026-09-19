%global source0_hash b4ae64921b07a96661695ebd5aac0dec813d1a68e546a61609113d7843f5b617

%ifarch aarch64
# ext/termios currently crashing:
# Testing termios ...
# *** ERROR: A string containing NUL character is not allowed: #**"\xb0;\xfd;\xbb;\xa3;\xff;\xff;\0"
#     While loading "././test.scm" at line 162
%bcond_with tests
%else
%bcond_without tests
%endif

%define abi_version 0.98

Name:			gauche
Version:		0.9.12
Release:		12%{?dist}
Summary:		Scheme script interpreter with multibyte character handling

License:		BSD-3-Clause AND MIT
URL:			http://practical-scheme.net/gauche
Source0:		https://github.com/shirok/Gauche/releases/download/release0_9_12/Gauche-%{version}.tgz

Patch0:			%{name}-ext-ldflags.patch
Patch1:			%{name}-xz-info.patch

ExcludeArch:	armv7hl

BuildRequires:	gcc
BuildRequires:	gdbm-devel
BuildRequires:  libxcrypt-devel
BuildRequires:	make
BuildRequires:	mbedtls-devel
BuildRequires:	openssl
BuildRequires:	texinfo
BuildRequires:	zlib-devel
Requires:		lib%{name}%{?_isa} = %{version}-%{release}
Recommends:		slib

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

%autosetup -n Gauche-%{version} -p1

%build
%configure --with-rpath=no --enable-threads=pthreads --enable-multibyte=utf-8 --with-slib=%{_datadir}/slib --enable-ipv6
LD_LIBRARY_PATH=`pwd`/src %make_build

%install
LD_LIBRARY_PATH=`pwd`/src %make_install

# correct permissions
chmod -R u+w %{buildroot}
# make .c files readable for debuginfo
find -name '*.c' | xargs chmod 0644

%if %{with tests}
%check
LD_LIBRARY_PATH=`pwd`/src make check
%endif

%post
# creates slib catalog, if possible.
/usr/bin/gosh -u slib -e "(require 'logical)" -e "(exit 0)" > /dev/null 2>&1 || echo

%files
%license COPYING
%doc ChangeLog AUTHORS README.adoc VERSION
%{_bindir}/gauche-cesconv
%{_bindir}/gosh
%{_datadir}/gauche-%{abi_version}
%{_libdir}/gauche-%{abi_version}
%{_mandir}/man*/gauche-cesconv.*
%{_mandir}/man*/gosh.*
%exclude %{_libdir}/gauche-%{abi_version}/%{version}/include
%exclude %{_libdir}/gauche-%{abi_version}/%{version}/*/libgauche-%{abi_version}.so*
%exclude %{_libdir}/gauche-%{abi_version}/%{version}/*/libgauche-static-%{abi_version}.a
%exclude %{_datadir}/gauche-%{abi_version}/%{version}/aclocal.m4
%exclude %{_datadir}/gauche-%{abi_version}/%{version}/lib/build-standalone
%exclude %{_datadir}/gauche-%{abi_version}/%{version}/lib/gencomp
%exclude %{_datadir}/gauche-%{abi_version}/%{version}/lib/genstub
%exclude %{_datadir}/gauche-%{abi_version}/%{version}/lib/precomp
%exclude %{_datadir}/gauche-%{abi_version}/%{version}/package-templates
%exclude %{_libdir}/libgauche-%{abi_version}.so.*
%exclude %{_libdir}/libgauche-static-%{abi_version}.a

%files devel
%doc HACKING.adoc
%{_bindir}/gauche-config
%{_bindir}/gauche-install
%{_bindir}/gauche-package
%{_datadir}/aclocal/gauche.m4
%{_datadir}/gauche-%{abi_version}/%{version}/aclocal.m4
%{_datadir}/gauche-%{abi_version}/%{version}/lib/build-standalone
%{_datadir}/gauche-%{abi_version}/%{version}/lib/gencomp
%{_datadir}/gauche-%{abi_version}/%{version}/lib/genstub
%{_datadir}/gauche-%{abi_version}/%{version}/lib/precomp
%{_datadir}/gauche-%{abi_version}/%{version}/package-templates
%{_libdir}/gauche-%{abi_version}/%{version}/*/libgauche-%{abi_version}.so
%{_libdir}/libgauche-%{abi_version}.so
%{_libdir}/gauche-%{abi_version}/%{version}/include
%{_mandir}/man*/gauche-config*
%{_mandir}/man*/gauche-install.*
%{_mandir}/man*/gauche-package.*

%files doc
%{_infodir}/gauche-*

%files -n lib%{name}
%{_libdir}/gauche-%{abi_version}/%{version}/*/libgauche-%{abi_version}.so.*
%{_libdir}/libgauche-%{abi_version}.so.*

%files -n lib%{name}-static
%{_libdir}/gauche-%{abi_version}/%{version}/*/libgauche-static-%{abi_version}.a
%{_libdir}/libgauche-static-%{abi_version}.a

%ldconfig_scriptlets -n lib%{name}

%changelog
%autochangelog
