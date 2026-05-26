# oreon source sha256 begin
# URL sources: global sourceN_sha256 = 64-char hex from sha256sum. Omit a sourceN_sha256 line to skip verify for that source.
%global source0_sha256 f590407fc51badb351973fc1333ee33111f05ec83a8f954fd8cf0c5e30439806
%global oreon_verify_sources \
%{?source0_sha256:%(test -z "%{source0_sha256}" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_sha256}" || { echo "oreon: Source0 sha256 mismatch" >&2; exit 1; }; })}
%(true)
# oreon source sha256 end

Name:       recode
Version:    3.7.15
Release:    3%{?dist}
Summary:    Conversion between character sets and surfaces
# COPYING:              GPLv3 text
# COPYING-LIB:          LGPLv3 text
# doc/recode.info:      OFSFDL
# doc/recode.texi:      OFSFDL
# lib/error.h:              GPLv3+
# lib/strerror-override.c:  GPLv3+
# lib/vasnprintf.c:         GPLv3+
# src/ansellat1.l:      BSD
# src/lat1asci.c:       GPLv3+
# src/merged.c:         BSD
# src/recode.h:         LGPLv3+
# src/ucs.c:            LGPLv3+
## Not in any binary package
# aclocal.m4:               FSFULLR
# build-aux/bootstrap.in:   MIT or GPLv3+ (bundled gnulib-modules/bootstrap)
# build-aux/compile:        GPLv2+ with exceptions
# build-aux/config.guess:   GPLv3+ with exceptions
# build-aux/config.rpath:   FSFULLR
# build-aux/config.sub:     GPLv3+ with exceptions
# build-aux/depcomp:        GPLv2+ with exceptions
# build-aux/extract-trace:  MIT or GPLv3+ (bundled gnulib-modules/bootstrap)
# build-aux/funclib.sh:     MIT or GPLv3+ (bundled gnulib-modules/bootstrap)
# build-aux/inline-source:  MIT or GPLv3+ (bundled gnulib-modules/bootstrap)
# build-aux/install-sh:     MIT
# build-aux/ltmain.sh:      GPLv2+ with exceptions and GPLv3+ with exceptions
#                           and GPLv3+
# build-aux/mdate-sh:       GPLv2+ with exceptions
# build-aux/missing:        GPLv2+ with exceptions
# build-aux/options-parser: MIT or GPLv3+ (bundled gnulib-modules/bootstrap)
# build-aux/texinfo.tex:    GPLv3+ with exceptions
# config.rpath:         FSFULLR
# configure:            FSFUL and GPLv2+ with exceptions
# doc/Makefile.am:      GPLv3+
# doc/Makefile.in:      FSFULLR and GPLv3+
# doc/texinfo.tex:      GPLv2+ with exceptions
# INSTALL:              FSFAP
# Makefile.am:          GPLv3+
# m4/gettext.m4:        FSFULLR
# m4/gnulib-cache.m4:   GPLv3+ with exceptions
# m4/libtool.m4:        GPLv2+ with exceptions and FSFUL
# m4/mbstate_t.m4:      FSFULLR
# m4/minmax.m4:         FSFULLR
# m4/ssize_t.m4:        FSFULLR
# m4/sys_stat_h.m4:     FSFULLR
# tables.py:            GPLv3+
# tests/Makefile.am:    GPLv3+
# tests/Makefile.in:    FSFULLR and GPLv3+
# tests/Recode.pyx:     GPLv3+
License:    GPL-3.0-or-later AND LGPL-3.0-or-later AND BSD-2-Clause AND LicenseRef-OFSFDL
URL:        https://github.com/rrthomas/recode
Source:        https://github.com/rrthomas/recode/releases/download/v3.7.15/recode-3.7.15.tar.gz
Patch:      recode-3.7.13-Rename-coliding-hash-functions.patch


BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  coreutils
BuildRequires:  gcc
BuildRequires:  gettext-devel
# help2man is executed from ./src/Makefile if main.c or configure.ac is newer
# than recode.1.
BuildRequires:  make
BuildRequires:  libtool
BuildRequires:  texinfo
# Tests:
BuildRequires:  python3-Cython
BuildRequires:  python3-devel >= 3.7.5
BuildRequires:  python3-setuptools

%description
The recode tool and library convert files between character sets and surfaces.
It recognizes or produces over 200 different character sets (or about 300 if
combined with an iconv library) and transliterates files between almost any
pair. When exact transliteration is not possible, it gets rid of the offending
character or falls back on an approximations.

%package devel
Summary:    Header files for development using recode library
# Header files are LGPLv3+
License:    LGPL-3.0-or-later
Requires:   %{name}%{?_isa} = %{version}-%{release}

%description devel
This package provides the header files for a recode library.

%prep
%oreon_verify_sources
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

# remove unpackaged file from the buildroot
rm -r $RPM_BUILD_ROOT%{_infodir}/dir

# remove libtool archives
rm $RPM_BUILD_ROOT%{_libdir}/*.la

%files -f %{name}.lang
%license COPYING COPYING-LIB
# Changelog is not helpful
%doc AUTHORS NEWS README THANKS TODO
%{_mandir}/*/*
%{_infodir}/recode.info*
%{_bindir}/*
%{_libdir}/librecode.so.3
%{_libdir}/librecode.so.3.*

%files devel
%{_libdir}/*.so
%{_includedir}/*

%changelog
* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 3.7.15-3
- Prepare for Oreon 11 (RP1)
