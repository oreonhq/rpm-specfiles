%global source0_hash ec7a5a54deb39c7c0fa746d17767752154e9cb94dbcf3d15b795083b3f0f154b
%global bootstrap 0
Name: mlton
Version: 20210117
Release:        1%{?dist}
Summary:        Optimizing compiler for Standard ML
License: MIT
URL: http://mlton.org/
Source0:        http://downloads.sourceforge.net/%{name}/%{name}-%{version}.src.tgz
ExcludeArch: %{ix86}
%if ! 0%{?bootstrap}
%endif
Requires: gmp-devel gcc
%global __provides_exclude_from ^(%{_docdir}|%{_libdir}/mlton/sml)/.*$
%global __requires_exclude_from ^(%{_docdir}|%{_libdir}/mlton/sml)/.*$
# oreon:deps
BuildRequires:  gcc
BuildRequires:  gmp-devel
BuildRequires:  make
BuildRequires:  mlton
BuildRequires:  tex(latex)
# /oreon:deps
%description
MLton is a whole-program optimizing compiler for Standard ML.  MLton
generates standalone executables with excellent runtime performance,
is SML 97 compliant, and has a complete basis library. MLton has
source-level profiling, a fast C FFI, an interface to the GNU
multiprecision library, and lots of useful libraries.

%prep

%autosetup -T -b 0 -p1

# https://fedoraproject.org/wiki/Packaging:Guidelines#Shebang_lines
sed -i -e '1 s;^#! */usr/bin/env *;#!/usr/bin/;' bin/*

%build

%if 0%{?bootstrap}
make dirs runtime CFLAGS="$RPM_OPT_FLAGS"
for s in mlton/mlton.*.c; do
  gcc $RPM_OPT_FLAGS -O1 -c -Ibuild/lib/mlton/include \
     -Ibuild/lib/mlton/targets/self/include -w "${s}"
done
gcc $RPM_OPT_FLAGS -o build/lib/mlton/mlton-compile \
    -Lbuild/lib/mlton/targets/self \
    -L/usr/local/lib \
    mlton.*.o \
    -lmlton -lgmp -lgdtoa -lm
make basis-no-check script constants libraries tools CFLAGS="$RPM_OPT_FLAGS"
make install PREFIX=$(pwd)/../bootstrap
export PATH=$PATH:$(pwd)/../bootstrap/bin
make clean
%endif
make all docs PREFIX=%{_prefix} libdir=%{_libdir} CFLAGS="$RPM_OPT_FLAGS"
%install
make install-no-strip install-docs PREFIX=%{_prefix} libdir=%{_libdir} \
     docdir=%{_pkgdocdir} DESTDIR=$RPM_BUILD_ROOT
rm -rf $RPM_BUILD_ROOT%{_libdir}/mlton/sml/ckit-lib/regression
%oreon_autofiles main

%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
