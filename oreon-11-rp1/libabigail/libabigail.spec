# Copyright (C) 2026 Oreon HQ
# SPDX-License-Identifier: GPL-2.0-or-later

%global source0_hash d34ea7c4b150f61e22edb1d16157e12c43fd18f8e8f09abce053d82ccaf92e06
%{!?oreon_bootstrap:%global oreon_bootstrap %{nil}}
%bcond bootstrap 0
%oreon_bootstrap

%bcond abidb 1
%bcond inline_xxh 0

%global tarball_revision 1
%global tarball_name %{name}-%{version}

Name: libabigail
Version: 3.0
Release: 1%{?dist}
Summary: Set of ABI analysis tools

License: Apache-2.0 WITH LLVM-exception
URL: https://sourceware.org/libabigail/
Source0: https://mirrors.kernel.org/sourceware/libabigail/%{tarball_name}.tar.xz
Patch1: 0001-default-reporter-Fix-segfault-on-added-deleted-iface.patch
Patch2: 0002-dwarf-reader-Canonicalize-void-type.patch
Patch3: 0003-corpus-Record-pointer-to-member-sub-types-as-reachab.patch
Patch4: 0004-dwarf-reader-Remove-unfortunate-debugging-artifact.patch
Patch5: 0005-hash-dwarf-reader-reader-writer-Handle-decl-only-enu.patch

BuildRequires: oreon-rpm-macros
BuildRequires: git
BuildRequires: libbpf-devel
BuildRequires: binutils-devel
BuildRequires: clang
BuildRequires: libtool
BuildRequires: elfutils-devel >= 0.197
BuildRequires: tbb-devel
BuildRequires: libxml2-devel
BuildRequires: xxhash-devel
%if %{with inline_xxh}
BuildRequires: xxhash-static
%endif
BuildRequires: xz-devel >= 5.2.0
BuildRequires: doxygen
BuildRequires: python3-sphinx
BuildRequires: texinfo
%if %{with abidb}
BuildRequires: python3-GitPython
BuildRequires: python3-libarchive-c
Requires: python3-GitPython
Requires: python3-libarchive-c
%endif
BuildRequires: wget

%description
The libabigail package comprises seven command line utilities:
abidiff, kmidiff, abipkgdiff, abicompat, abidw, and abilint.
The abidiff command line tool compares the ABI of two
ELF shared libraries and emits meaningful textual reports about
changes impacting exported functions, variables and their types.
Simarly, the kmidiff compares the kernel module interface of two Linux
kernels.  abipkgdiff compares the ABIs of ELF binaries contained in
two packages.  abicompat checks if a subsequent version of a shared
library is still compatible with an application that is linked against
it.  abidw emits an XML representation of the ABI of a given ELF
shared library. abilint checks that a given XML representation of the
ABI of a shared library is correct.

Install libabigail if you need to compare the ABI of ELF shared
libraries.

%package devel
Summary: Shared library and header files to write ABI analysis tools
Requires: %{name}%{?_isa} = %{version}-%{release}

%description devel
This package contains a shared library and the associated header files
that are necessary to develop applications that use the C++ Libabigail
library.  The library provides facilities to analyze and compare
application binary interfaces of shared libraries in the ELF format.

%package doc
Summary: Man pages, texinfo files and html manuals of libabigail

%description doc
This package contains documentation for the libabigail tools in the
form of man pages, texinfo documentation and API documentation in html
format.


%prep
%oreon_sha256
%autosetup -v -S git

%build
%configure %{?with_abidb:--enable-abidb} %{?with_inline_xxh:--enable-inlined-xxhash} --enable-ctf --enable-btf --disable-silent-rules --disable-zip-archive --disable-static
make %{?_smp_mflags}
pushd doc
make html-doc
pushd manuals
make html-doc
make man
make info
popd
popd

%install
%make_install
find %{buildroot} -name '*.la' -exec rm -f {} ';'

make -C doc/manuals install-man-and-info-doc DESTDIR=%{buildroot}


%check
time make %{?_smp_mflags} check || (cat tests/test-suite.log && exit 2)
time make %{?_smp_mflags} check-self-compare || (cat tests/test-suite.log && exit 2)

%ldconfig_scriptlets

%files
%{_bindir}/abicompat
%{_bindir}/abidiff
%{_bindir}/abidw
%{_bindir}/abilint
%{_bindir}/abipkgdiff
%{_bindir}/kmidiff
%if %{with abidb}
%{_bindir}/abidb
%endif
%{_libdir}/libabigail.so.10
%{_libdir}/libabigail.so.10.0.0
%{_libdir}/libabigail/default.abignore
%doc README AUTHORS ChangeLog
%license LICENSE.txt license-change-2020.txt
%{_mandir}/man1/*
%{_mandir}/man7/*
%{_infodir}/abigail.info*

%files devel
%{_libdir}/libabigail.so
%{_libdir}/pkgconfig/libabigail.pc
%{_includedir}/*
%{_datadir}/aclocal/abigail.m4

%files doc
%license LICENSE.txt license-change-2020.txt
%doc doc/manuals/html/*


%changelog
%autochangelog
