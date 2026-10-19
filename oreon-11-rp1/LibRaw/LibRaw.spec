%global source0_hash de86b035655accff8d4010f1a221fdf50d353cb7b1422ba26f14a0db92612cfa
%global somajor 25
Summary:        Library for reading RAW files obtained from digital photo cameras
Name: LibRaw
Version: 0.22.2
Release:        1%{?dist}
License: BSD-3-Clause and (CDDL-1.0 or LGPL-2.1-only)
URL: https://www.libraw.org
Source0:        https://www.libraw.org/data/LibRaw-0.22.2.tar.gz
Patch0: LibRaw-pkgconfig.patch
Provides: bundled(dcraw) = 9.25
# oreon:deps
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  gcc-c++
BuildRequires:  libtool
BuildRequires:  make
BuildRequires:  pkgconfig(lcms2)
BuildRequires:  pkgconfig(libjpeg)
BuildRequires:  pkgconfig(zlib)
# /oreon:deps
%description
LibRaw is a library for reading RAW files obtained from digital photo
cameras (CRW/CR2, NEF, RAF, DNG, and others).

LibRaw is based on the source codes of the dcraw utility, where part of
drawbacks have already been eliminated and part will be fixed in future.

%package devel
Summary: LibRaw development libraries
Requires: %{name}%{?_isa} = %{version}-%{release}
%description devel
LibRaw development libraries.

This package contains libraries that applications can use to build
against LibRaw.

%package static
Summary: LibRaw static development libraries
Requires: %{name}-devel%{?_isa} = %{version}-%{release}
%description static
LibRaw static development libraries.

%package samples
Summary: LibRaw sample programs
Requires: %{name}%{?_isa} = %{version}-%{release}
%description samples
LibRaw sample programs

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%global oreon_srcdir %{name}-%{version}
%oreon_prep
%build

autoreconf -if
%configure \
    --enable-examples=yes \
    --enable-jpeg \
    --enable-lcms \
    --enable-openmp \
    --enable-zlib
sed -i 's|^hardcode_libdir_flag_spec=.*|hardcode_libdir_flag_spec=""|g' libtool
sed -i 's|^runpath_var=LD_RUN_PATH|runpath_var=DIE_RPATH_DIE|g' libtool
%make_build
%install
cp -pr doc manual
chmod 644 LICENSE.CDDL LICENSE.LGPL COPYRIGHT Changelog.txt
chmod 644 manual/*.html
%make_install
rm -rfv samples/.deps
rm -fv samples/.dirstamp
rm -fv samples/*.o
rm -fv %{buildroot}%{_libdir}/lib*.la
%oreon_autofiles LibRaw-devel usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*
%oreon_autofiles LibRaw-static usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles LibRaw-samples usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%files -f %{oreon_filedir}/main.list
%files -n LibRaw-devel -f %{oreon_filedir}/LibRaw-devel.list
%files -n LibRaw-static -f %{oreon_filedir}/LibRaw-static.list
%files -n LibRaw-samples -f %{oreon_filedir}/LibRaw-samples.list

%changelog

* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 0.22.0-1
- Prepare for Oreon 11 (RP1)
