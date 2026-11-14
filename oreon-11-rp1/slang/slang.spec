# Copyright (C) 2026 Oreon HQ
# SPDX-License-Identifier: GPL-2.0-or-later

%global source0_hash f9145054ae131973c61208ea82486d5dd10e3c5cdad23b7c4a0617743c8f5a18

%{!?oreon_bootstrap:%global oreon_bootstrap %{nil}}
%bcond bootstrap 0
%oreon_bootstrap

Name: slang
Version: 2.3.3
Release: 1%{?dist}
Summary: Shared library for the S-Lang extension language
License: GPL-2.0-or-later
URL: https://www.jedsoft.org/slang/
Source0: https://www.jedsoft.org/releases/slang/slang-%{version}.tar.bz2
Source1: slang-%{version}.tar.bz2.asc
Source2: gpgkey-64083373E9E1DE997EBBE7784B82D0B82930237D.gpg
Patch0: slang-sighuptest.patch

BuildRequires: oreon-rpm-macros
BuildRequires: gcc
BuildRequires: gnupg2
BuildRequires: libpng-devel
BuildRequires: make
BuildRequires: oniguruma-devel
BuildRequires: zlib-devel

%description
S-Lang is an interpreted language and a programming library. The
S-Lang language was designed so that it can be easily embedded into
a program to provide the program with a powerful extension language.
The S-Lang library, provided in this package, provides the S-Lang
extension language. S-Lang's syntax resembles C, which makes it easy
to recode S-Lang procedures in C if you need to.

%package slsh
Summary: Interpreter for S-Lang scripts
Requires: %{name}%{?_isa} = %{version}-%{release}

%description slsh
slsh (slang-shell) is a program for interpreting S-Lang scripts.
It supports dynamic loading of S-Lang modules and includes a readline
interface for interactive use.

This package also includes S-Lang modules that are distributed with
the S-Lang distribution.

%package devel
Summary: Development files for the S-Lang extension language
Requires: %{name}%{?_isa} = %{version}-%{release}
Provides: pkgconfig(slang) = %{version}

%description devel
This package contains files which you'll need if you want to
develop S-Lang based applications. Documentation which may help
you write S-Lang based applications is also included.

%prep
%oreon_sha256
%oreon_gpgverify --key %{SOURCE2} --sig %{SOURCE1} --data %{SOURCE0}
%autosetup -p1

%build
%configure \
    --with-pnglib=%{_libdir} \
    --with-zlib=%{_libdir} \
    --with-pnginc=%{_includedir} \
    --with-zinc=%{_includedir} \
    --without-pcre \
    --with-oniglib=%{_libdir} \
    --with-oniginc=%{_includedir}
make RPATH="" install_doc_dir=%{_pkgdocdir} all

%install
make install-all INSTALL="install -p" RPATH="" DESTDIR=%{buildroot}
rm -rf %{buildroot}%{_docdir}/{slang,slsh}
rm -f %{buildroot}%{_libdir}/libslang.a
mkdir %{buildroot}%{_includedir}/slang
for h in slang.h slcurses.h; do
    ln -s ../$h %{buildroot}%{_includedir}/slang/$h
done

%check
make check

%ldconfig_scriptlets

%files
%license COPYING
%doc NEWS
%{_libdir}/libslang*.so.2*

%files slsh
%doc slsh/doc/html/slsh*.html
%config(noreplace) %{_sysconfdir}/slsh.rc
%{_bindir}/slsh
%{_libdir}/slang
%{_mandir}/man1/slsh.1*
%{_datadir}/slsh

%files devel
%doc doc/*/cslang*.txt doc/*/cref.txt doc/README doc/*/slang*.txt doc/*.txt
%{_libdir}/libslang*.so
%{_libdir}/pkgconfig/slang.pc
%{_includedir}/sl*.h
%{_includedir}/slang

%changelog
%autochangelog
