%global source0_hash 8016c800eca020a28ac2805841cce20562b617ffafe215d53a23dc9a3e252186
%global commit0 dfe1ccb1055af99be0232a26520d247b5fe093bc
%global shortcommit0 %(c=%{commit0}; echo ${c:0:7})
%global snapshotdate 20210601
%global libname libfoma
Name:           foma
Version:        0.10.0
Release:        1%{?dist}
Summary:        Xerox-compatible finite-state compiler
License:        Apache-2.0
URL:            https://github.com/mhulden/foma
Source0:        https://github.com/mhulden/%{name}/archive/%{commit0}.tar.gz#/%{name}-%{shortcommit0}.tar.gz
Patch0:         foma-harden-build-fedora.patch
Patch1: foma-c99.patch
Patch2: foma-avoid-deprecated-inet-functions.patch
Requires:       %{libname}%{?_isa} = %{version}-%{release}
# oreon:deps
BuildRequires:  bison
BuildRequires:  flex
BuildRequires:  gcc
BuildRequires:  make
BuildRequires:  readline-devel
BuildRequires:  zlib-devel
# /oreon:deps
%description
Foma can be used for constructing finite-state automata and transducers.
It has support for many natural language processing applications such as
producing morphological analyzers. It is sufficiently generic to use for
a large number of purposes in addition to NLP. The foma interface is
similar to the Xerox xfst interface.

This package includes the foma command line tools.

%package -n     %{libname}
Summary:        The foma C library
%description -n %{libname}
Foma can be used for constructing finite-state automata and transducers.
It has support for many natural language processing applications such as
producing morphological analyzers. It is sufficiently generic to use for
a large number of purposes in addition to NLP. The foma interface is
similar to the Xerox xfst interface.

This package includes the foma C library.

%package -n     %{libname}-devel
Summary:        Development files for %{libname}
Requires:       %{libname}%{?_isa} = %{version}-%{release}
Requires:       pkgconfig
%description -n %{libname}-devel
The libfoma-devel package contains libraries and header files for
developing applications that use libfoma.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%autosetup -n %{name}-%{commit0} -p1

%build

sed -i '/^CFLAGS/c\CFLAGS = %{optflags} -Wl,--as-needed -D_GNU_SOURCE -std=c99 -fvisibility=hidden -fPIC' foma/Makefile
sed -i '/^LDFLAGS/c\LDFLAGS = -lreadline -lz -ltermcap %{build_ldflags}' foma/Makefile
sed -i '/^FLOOKUPLDFLAGS/c\FLOOKUPLDFLAGS = libfoma.a -lz %{build_ldflags}' foma/Makefile
sed -i 's|echo "prefix=${prefix}"|echo "prefix=%{_prefix}"|' foma/Makefile
cd foma
%make_build
%install
sed -i '/^prefix/c\prefix = %{buildroot}%{_prefix}' foma/Makefile
sed -i '/^libdir/c\libdir = %{buildroot}%{_libdir}' foma/Makefile
cd foma
%make_install
find %{buildroot} -name '*.a' -exec rm -f {} ';'
%oreon_autofiles main usr/*/lib*.so.* usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*

%files -f %{oreon_filedir}/main.list
%files -n libfoma -f %{oreon_filedir}/libfoma.list
%files -n libfoma-devel -f %{oreon_filedir}/libfoma-devel.list

%changelog

* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 0.10.0-0.15.
- Prepare for Oreon 11 (RP1)
