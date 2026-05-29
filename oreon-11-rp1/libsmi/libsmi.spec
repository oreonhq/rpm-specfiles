%global source0_hash 516044e684ff13abf56632e87a9db6b4bca2bfe5d87f108012bf4f74ae7df0b8

# Upstream was putting changes silently into svn over a number of years
# When they moved to gitlab, this became visible
# It does not seem that they've ever done a proper release since 0.4.8
# Leaving the version as is and using the gitlab source from the latest commit (2021)
%global commit c5830721

# One of the bison-generated parsers uses an int as a List *.  This
# seems to be an actual bug.  However, the parser cannot be
# regenerated with current bison in Fedora.
# <https://bugzilla.redhat.com/show_bug.cgi?id=2256912>
%global build_type_safety_c 1

Name:		libsmi
Version:	0.4.8
Release:	45%{?dist}
Summary:	A library to access SMI MIB information
# lib/parser-smi.c is GPL-2.0-or-later, but with the Bison exception that says it can be used under any terms
# as part of the larger libsmi work, so we are choosing to use it under the core libsmi licenses instead.
License:	TCL AND BSD-3-Clause
URL:		http://www.ibr.cs.tu-bs.de/projects/libsmi/index.html
Source0:        https://gitlab.ibr.cs.tu-bs.de/nm/libsmi/-/archive/%{commit}/libsmi-%{commit}.tar.gz
Source1:	smi.conf
Source2:	IETF-MIB-LICENSE.txt
Patch0:		libsmi-0.4.8-wget111.patch
Patch2:		libsmi-c5830721-symbols-clash.patch
Patch4:		libsmi-c5830721-configure-c99.patch
Patch5:		libsmi-c99.patch
Patch6:		libsmi-c5830721-fix-missing-declaration.patch
Patch7:		libsmi-c5830721-switch-fixes.patch
Patch8:		libsmi-c5830721-include-fix.patch
Patch9:		libsmi-c5830721-missing-semicolon.patch
Patch10:	libsmi-c5830721-cleanups.patch
Patch11:	libsmi-c5830721-test-fix-typo.patch
BuildRequires:	libtool
BuildRequires:	flex, bison
BuildRequires:	make
Requires:	gawk, wget

%description
Libsmi is a C library to access MIB module information through
a well defined API that hides the nasty details of locating
and parsing SMIv1/v2 MIB modules.

This package contains tools to check, dump, and convert MIB
definitions and a steadily maintained and revised archive
of all IETF and IANA maintained standard MIB modules.


%package devel
Summary:	Development environment for libsmi library
Requires:	%{name}%{?_isa} = %{version}-%{release}
Requires:	pkgconfig

%description devel
Libsmi is a C library to access MIB module information through
a well defined API that hides the nasty details of locating
and parsing SMIv1/v2 MIB modules.

This package contains development files needed to develop
libsmi-based applications.

%prep
%(test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; })
%setup -q -n %{name}-%{commit}
%patch -P 0 -p1 -b .wget111
%patch -P 2 -p1 -b .clash
%patch -P 4 -p1
%patch -P 5 -p1
%patch -P 6 -p1 -b .fix-missing-declaration
%patch -P 7 -p1 -b .switch-fixes
%patch -P 8 -p1 -b .include-fix
%patch -P 9 -p1 -b .missing-semicolon
%patch -P 10 -p1 -b .cleanups
%patch -P 11 -p1 -b .fix-test-typo

# We need to prime the pump here.
pushd lib
bison -v -t -d -psming parser-sming.y
bison -v -t -d -pyang parser-yang.y
popd
cp %{SOURCE2} .

%build
%set_build_flags
export CFLAGS="$CFLAGS -std=gnu99"
autoreconf -iv
%configure \
    --enable-smi \
    --enable-sming \
    --enable-shared \
    --with-yangdir=%{_datadir}/libsmi-yang/ \
    --disable-static
make LIBTOOL=/usr/bin/libtool %{?_smp_mflags}

iconv -f latin1 -t utf-8 <COPYING >COPYING.utf8
mv COPYING.utf8 COPYING

%install
rm -rf $RPM_BUILD_ROOT
%{make_install}

install -d -m 755 $RPM_BUILD_ROOT%{_sysconfdir}
install -p -m 644 %{SOURCE1} $RPM_BUILD_ROOT%{_sysconfdir}/smi.conf

rm -f $RPM_BUILD_ROOT%{_libdir}/*.a
rm -f $RPM_BUILD_ROOT%{_libdir}/*.la

%check
# fails a couple of tests (2 in {0.4.4, 0.4.5}, 3 as of 2024-01-03)
# BUT... it shouldn't segfault or crash.
make check ||:

%ldconfig_scriptlets


%files
%doc ANNOUNCE ChangeLog COPYING README THANKS TODO
%doc doc/draft-irtf-nmrg-sming-02.txt smi.conf-example
%doc IETF-MIB-LICENSE.txt
%config(noreplace) %{_sysconfdir}/smi.conf
%{_bindir}/*
%{_libdir}/*.so.*
%{_datadir}/mibs/
%{_datadir}/pibs/
%{_datadir}/libsmi-yang/
%{_mandir}/man1/*.1*

%files devel
%{_datadir}/aclocal/libsmi.m4
%{_libdir}/pkgconfig/libsmi.pc
%{_libdir}/*.so
%{_includedir}/*
%{_mandir}/man3/*.3*


%changelog
* Mon May 25 2026 Oreon Packaging Team <packaging@oreonhq.com> - 0.4.8-45
- Import
