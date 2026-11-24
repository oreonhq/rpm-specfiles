# Copyright (C) 2026 Oreon HQ
# SPDX-License-Identifier: GPL-2.0-or-later

%global source0_hash 4dae6fdcd2bb0bb6c37b5f97c33c2be954da743985369cddac3546e3218bffb8
%global source1_hash b3480bc76adf5f220c21331d0efe24bc139c52ea687495765daad2b696b563c2
%global source2_hash e4a6d3ba2b047677f83b9884e3fdbd066c1cc01a603ba7a4cacb727a7ff660ec
%{!?oreon_bootstrap:%global oreon_bootstrap %{nil}}
%bcond bootstrap 0
%oreon_bootstrap

Name:       pcre
Version:    8.45
Release:        1%{?dist}
%global myversion %{version}%{?rcversion:-%rcversion}
Summary:    Perl-compatible regular expression library
License:    BSD-3-Clause
URL:        https://www.pcre.org/
Source0:        https://ftp.exim.org/pub/pcre/%{name}-%{myversion}.tar.bz2
Source1:        https://ftp.exim.org/pub/pcre/%{name}-%{myversion}.tar.bz2.sig
Source2:        Public-Key
Patch0:     pcre-8.21-multilib.patch
Patch1:     pcre-8.32-refused_spelling_terminated.patch
Patch2:     pcre-8.41-fix_stack_estimator.patch
Patch3:     pcre-8.42-Declare-POSIX-regex-function-names-as-macros-to-PCRE.patch
Patch4:     pcre-8.44-Inicialize-name-table-memory-region.patch
Patch5:     pcre-8.44-JIT-compiler-update-for-Intel-CET.patch
Patch6:     pcre-8.44-Pass-mshstk-to-the-compiler-when-Intel-CET-is-enable.patch

BuildRequires: oreon-rpm-macros
BuildRequires:  readline-devel
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  coreutils
BuildRequires:  clang
BuildRequires:  glibc-common
BuildRequires:  gnupg2
BuildRequires:  libtool
BuildRequires:  make
BuildRequires:  bash
BuildRequires:  diffutils
BuildRequires:  grep

%description
PCRE, Perl-compatible regular expression, library has its own native API, but
a set of wrapper functions that are based on the POSIX API are also supplied
in the libpcreposix library. Note that this just provides a POSIX calling
interface to PCRE: the regular expressions themselves still follow Perl syntax
and semantics. This package provides support for strings in 8-bit and UTF-8
encodings. Detailed change log is provided by %{name}-doc package.

%package utf16
Summary:    UTF-16 variant of PCRE
Conflicts:  %{name}%{?_isa} < 8.38-12

%description utf16
This is Perl-compatible regular expression library working on UTF-16 strings.
Detailed change log is provided by %{name}-doc package.

%package utf32
Summary:    UTF-32 variant of PCRE
Conflicts:  %{name}%{?_isa} < 8.38-12

%description utf32
This is Perl-compatible regular expression library working on UTF-32 strings.
Detailed change log is provided by %{name}-doc package.

%package cpp
Summary:    C++ bindings for PCRE
Requires:   %{name}%{?_isa} = %{version}-%{release}

%description cpp
This is C++ bindings for the Perl-compatible regular expression library.
Detailed change log is provided by %{name}-doc package.

%package doc
Summary:    Change log for %{name}
BuildArch:  noarch

%description doc
These are large documentation files about PCRE.

%package devel
Summary:    Development files for %{name}
Requires:   %{name}%{?_isa} = %{version}-%{release}
Requires:   %{name}-cpp%{?_isa} = %{version}-%{release}
Requires:   %{name}-utf16%{?_isa} = %{version}-%{release}
Requires:   %{name}-utf32%{?_isa} = %{version}-%{release}

%description devel
Development files (Headers, libraries for dynamic linking, etc) for %{name}.

%package static
Summary:    Static library for %{name}
Requires:   %{name}-devel%{_isa} = %{version}-%{release}

%description static
Library for static linking for %{name}.

%package tools
Summary:    Auxiliary utilities for %{name}
Requires:   %{name}%{_isa} = %{version}-%{release}

%description tools
Utilities demonstrating PCRE capabilities like pcregrep or pcretest.

%prep
%oreon_sha256
echo '%{source1_hash}  %{SOURCE1}' | sha256sum -c -
echo '%{source2_hash}  %{SOURCE2}' | sha256sum -c -
%{gpgverify} --keyring='%{SOURCE2}' --signature='%{SOURCE1}' --data='%{SOURCE0}'
%setup -q -n %{name}-%{myversion}
%patch -P0 -p1
%patch -P1 -p1
%patch -P2 -p2
%patch -P3 -p1
%patch -P4 -p1
%patch -P5 -p1
%patch -P6 -p1
libtoolize --copy --force
autoreconf -vif
for F in ChangeLog; do
    iconv -f latin1 -t utf8 "$F" >"${F}.utf8"
    touch --reference "$F" "${F}.utf8"
    mv "${F}.utf8" "$F"
done

%build
%ifarch ppc64
%global optflags %{optflags} -fno-strict-aliasing
%endif
%configure \
%ifarch s390 s390x sparc64 sparcv9 riscv64
    --disable-jit \
%else
    --enable-jit \
%endif
    --enable-pcretest-libreadline \
    --enable-utf \
    --enable-unicode-properties \
    --enable-pcre8 \
    --enable-pcre16 \
    --enable-pcre32 \
    --disable-silent-rules
%{make_build}

%install
%{make_install}
rm -f $RPM_BUILD_ROOT%{_libdir}/*.la
rm -rf $RPM_BUILD_ROOT%{_docdir}/pcre

%check
%ifarch s390 s390x ppc
ulimit -s 10240
%endif
make %{?_smp_mflags} check VERBOSE=yes

%files
%{_libdir}/libpcre.so.1
%{_libdir}/libpcre.so.1.*
%{_libdir}/libpcreposix.so.0
%{_libdir}/libpcreposix.so.0.*
%license COPYING LICENCE
%doc AUTHORS NEWS

%files utf16
%{_libdir}/libpcre16.so.0
%{_libdir}/libpcre16.so.0.*
%license COPYING LICENCE
%doc AUTHORS NEWS

%files utf32
%{_libdir}/libpcre32.so.0
%{_libdir}/libpcre32.so.0.*
%license COPYING LICENCE
%doc AUTHORS NEWS

%files cpp
%{_libdir}/libpcrecpp.so.0
%{_libdir}/libpcrecpp.so.0.*

%files doc
%doc ChangeLog

%files devel
%{_libdir}/*.so
%{_libdir}/pkgconfig/*
%{_includedir}/*.h
%{_mandir}/man1/pcre-config.*
%{_mandir}/man3/*
%{_bindir}/pcre-config
%doc doc/*.txt doc/html
%doc README HACKING pcredemo.c

%files static
%{_libdir}/*.a
%license COPYING LICENCE

%files tools
%{_bindir}/pcregrep
%{_bindir}/pcretest
%{_mandir}/man1/pcregrep.*
%{_mandir}/man1/pcretest.*

%changelog
%autochangelog
