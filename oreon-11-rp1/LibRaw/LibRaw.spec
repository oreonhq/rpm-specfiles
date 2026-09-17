%global source0_hash a789dc4e2409e2901d93793a4e0b80c7b49d0d97cf6ad71c850eb7616acfd786

%global somajor 25

Summary: Library for reading RAW files obtained from digital photo cameras
Name: LibRaw
Version: 0.22.1
Release: 2%{?dist}
License: BSD-3-Clause and (CDDL-1.0 or LGPL-2.1-only)
URL: https://www.libraw.org
Source0:        https://www.libraw.org/data/LibRaw-0.22.1.tar.gz
Patch0: LibRaw-pkgconfig.patch

BuildRequires: gcc-c++
BuildRequires: pkgconfig(lcms2)
BuildRequires: pkgconfig(libjpeg)
BuildRequires: pkgconfig(zlib)
BuildRequires: autoconf automake libtool
BuildRequires: make

Provides: bundled(dcraw) = 9.25

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
%autosetup -p1 -n %{name}-%{version}

%build
autoreconf -if
%configure \
    --enable-examples=yes \
    --enable-jpeg \
    --enable-lcms \
    --enable-openmp \
    --enable-zlib

# https://fedoraproject.org/wiki/Packaging:Guidelines#Beware_of_Rpath
sed -i 's|^hardcode_libdir_flag_spec=.*|hardcode_libdir_flag_spec=""|g' libtool
sed -i 's|^runpath_var=LD_RUN_PATH|runpath_var=DIE_RPATH_DIE|g' libtool

%make_build

%install
cp -pr doc manual
chmod 644 LICENSE.CDDL LICENSE.LGPL COPYRIGHT Changelog.txt
chmod 644 manual/*.html

# The Libraries
%make_install

rm -rfv samples/.deps
rm -fv samples/.dirstamp
rm -fv samples/*.o

rm -fv %{buildroot}%{_libdir}/lib*.la

%files
%doc Changelog.txt
%license LICENSE.CDDL LICENSE.LGPL COPYRIGHT
%{_libdir}/libraw.so.%{somajor}{,.*}
%{_libdir}/libraw_r.so.%{somajor}{,.*}

%files static
%{_libdir}/libraw.a
%{_libdir}/libraw_r.a

%files devel
%doc manual
%doc samples
%{_includedir}/libraw/
%{_libdir}/libraw.so
%{_libdir}/libraw_r.so
%{_libdir}/pkgconfig/libraw.pc
%{_libdir}/pkgconfig/libraw_r.pc
%exclude %{_docdir}/libraw/*

%files samples
%{_bindir}/*


%changelog
* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 0.22.0-1
- Prepare for Oreon 11 (RP1)
