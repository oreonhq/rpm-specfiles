%global source0_hash e01947316c177ac2084a4fe587e06f33377a196f711613e9d4a7b1b1c7cec000
Name:           spasm
Version:        1.2
Release:        1%{?dist}
Summary:        Sparse gaussian elimination modulo a small prime
License:        GPL-2.0-or-later AND BSD-3-Clause
URL:            https://github.com/cbouilla/spasm
VCS:            git:%{url}.git
Source0:        https://github.com/cbouilla/%{name}/archive/v%{version}/%{name}-%{version}.tar.gz
Source1:        spasm.module.in
Patch:          %{name}-m4-update.patch
Patch:          %{name}-wrong-and.patch
Patch:          %{name}-printf-format.patch
Patch:          %{name}-clobbered.patch
Patch:          %{name}-cycleclock.patch
Patch:          %{name}-endian.patch
Patch:          %{name}-c++.patch
ExcludeArch:    %{ix86}
Requires:       environment(modules)
Requires:       libspasm%{?_isa} = %{version}-%{release}
%global _desc %{expand:SpaSM is a software library devoted to sparse gaussian elimination modulo a
small prime _p_.}
# oreon:deps
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  environment(modules)
BuildRequires:  gcc-c++
BuildRequires:  libtool
BuildRequires:  metis-devel
BuildRequires:  pkgconfig(fflas-ffpack)
BuildRequires:  pkgconfig(flint)
BuildRequires:  pkgconfig(givaro)
BuildRequires:  pkgconfig(lemon)
BuildRequires:  pkgconfig(linbox)
BuildRequires:  pkgconfig(mpfr)
BuildRequires:  pkgconfig(ntl)
# /oreon:deps
%description
%_desc

This package contains command line binaries for accessing spasm
functionality.

%package     -n libspasm
Summary:        Sparse gaussian elimination modulo a small prime
%description -n libspasm
%_desc

This package contains the spasm shared library.

%package     -n libspasm-devel
Summary:        Development files for libspasm
Requires:       libspasm%{?_isa} = %{version}-%{release}
%description -n libspasm-devel
%_desc

This package contains headers and library links for developing
applications that use libspasm.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1

%conf
# Generate the configure script
autoreconf -fi .

%build

%configure --disable-static --with-givaro --with-fflas-ffpack --with-linbox
sed -e 's|^hardcode_libdir_flag_spec=.*|hardcode_libdir_flag_spec=""|g' \
    -e 's|^runpath_var=LD_RUN_PATH|runpath_var=DIE_RPATH_DIE|g' \
    -e 's|CC="\(g..\)"|CC="\1 -Wl,--as-needed"|' \
    -i libtool
%make_build
%install
%make_install
mkdir -p %{buildroot}%{_libdir}/%{name}
mv %{buildroot}%{_bindir} %{buildroot}%{_libdir}/%{name}
mkdir -p %{buildroot}%{_modulesdir}
sed 's,@LIBDIR@,'%{_libdir}/%{name}',g;' < %{SOURCE1} \
  > %{buildroot}%{_modulesdir}/%{name}-%{_arch}
sed -e '/define SPASM_TIMING/d' \
    -e '/include "config.h"/d' \
    -i.orig %{buildroot}%{_includedir}/spasm.h
touch -r %{buildroot}%{_includedir}/spasm.h.orig %{buildroot}%{_includedir}/spasm.h
rm %{buildroot}%{_includedir}/spasm.h.orig
%oreon_autofiles libspasm usr/*/lib*.so.*
%oreon_autofiles libspasm-devel usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*
%oreon_autofiles main usr/*/lib*.so.* usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*

%check

make check
%files -f %{oreon_filedir}/main.list
%files -n libspasm -f %{oreon_filedir}/libspasm.list
%files -n libspasm-devel -f %{oreon_filedir}/libspasm-devel.list

%changelog

%autochangelog
