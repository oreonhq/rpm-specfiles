%global source0_hash 516044e684ff13abf56632e87a9db6b4bca2bfe5d87f108012bf4f74ae7df0b8
%global commit c5830721
%global build_type_safety_c 1
Name:		libsmi
Version:	0.4.8
Release:        1%{?dist}
Summary:        A library to access SMI MIB information
License:	TCL AND BSD-3-Clause
URL:		http://www.ibr.cs.tu-bs.de/projects/libsmi/index.html
Source0:        https://gitlab.ibr.cs.tu-bs.de/nm/%{name}/-/archive/%{commit}/%{name}-%{commit}.tar.gz
Source1:        smi.conf
Source2:        IETF-MIB-LICENSE.txt
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
Requires:	gawk, wget
# oreon:deps
BuildRequires:  bison
BuildRequires:  flex
BuildRequires:  libtool
BuildRequires:  make
# /oreon:deps
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

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
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
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*

%check

make check ||:
%ldconfig_scriptlets
%files -f %{oreon_filedir}/main.list
%files -n libsmi-devel -f %{oreon_filedir}/libsmi-devel.list

%changelog

* Mon May 25 2026 Oreon Packaging Team <packaging@oreonhq.com> - 0.4.8-45
- Import
