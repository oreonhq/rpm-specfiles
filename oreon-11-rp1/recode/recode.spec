%global source0_hash c3d407f54f74bae76360312096e2ed46622f01c86e50b09ef45b2d93c8fcff2d
Name:       recode
Version:    3.7.16
Release:        1%{?dist}
Summary:        Conversion between character sets and surfaces
License:    GPL-3.0-or-later AND LGPL-3.0-or-later AND BSD-2-Clause AND LicenseRef-OFSFDL
URL:        https://github.com/rrthomas/recode
Source0:        https://github.com/rrthomas/recode/releases/download/v%{version}/recode-%{version}.tar.gz
Patch:      recode-3.7.13-Rename-coliding-hash-functions.patch
# oreon:deps
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  coreutils
BuildRequires:  gcc
BuildRequires:  gettext-devel
BuildRequires:  libtool
BuildRequires:  make
BuildRequires:  python3-Cython
BuildRequires:  python3-devel
BuildRequires:  python3-setuptools
BuildRequires:  texinfo
# /oreon:deps
%description
The recode tool and library convert files between character sets and surfaces.
It recognizes or produces over 200 different character sets (or about 300 if
combined with an iconv library) and transliterates files between almost any
pair. When exact transliteration is not possible, it gets rid of the offending
character or falls back on an approximations.

%package devel
Summary:    Header files for development using recode library
License:    LGPL-3.0-or-later
Requires:   %{name}%{?_isa} = %{version}-%{release}
%description devel
This package provides the header files for a recode library.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%autosetup -p1 -n %{name}-%{version}
autoreconf -fi

%build

export PYTHON=%{__python3}
%configure \
    --without-dmalloc \
    --disable-gcc-warnings \
    --enable-largefile \
    --enable-nls \
    --disable-rpath \
    --enable-shared \
    --disable-static
%{make_build}
%check

make check
%install
%{make_install}
%find_lang %{name}
rm -r $RPM_BUILD_ROOT%{_infodir}/dir
rm $RPM_BUILD_ROOT%{_libdir}/*.la
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*

%files -f %{oreon_filedir}/main.list
%files -n recode-devel -f %{oreon_filedir}/recode-devel.list

%changelog

%autochangelog
