%global source0_hash b67ba0383ef7e8a8563734e2e889ef5ec3c3b898a01d00fa0a6869ad81c6ce01

Summary: C library for multiple-precision floating-point computations
Name: mpfr
Version: 4.2.2
Release: 3%{?dist}
URL: https://www.mpfr.org/
VCS: git:https://gitlab.inria.fr/mpfr/mpfr.git

License: LGPL-3.0-or-later
BuildRequires: gcc
BuildRequires: gmp-devel
BuildRequires: make
BuildRequires: texinfo

Source: https://www.mpfr.org/%{name}-%{version}/%{name}-%{version}.tar.xz

# Upstream post-release patches.  This currently contains:
#Patch0: https://www.mpfr.org/%%{name}-%%{version}/allpatches

%description
The MPFR library is a C library for multiple-precision floating-point
computations with "correct rounding". The MPFR is efficient and
also has a well-defined semantics. It copies the good ideas from the
ANSI/IEEE-754 standard for double-precision floating-point arithmetic
(53-bit mantissa). MPFR is based on the GMP multiple-precision library.

%package devel
Summary: Development files for the MPFR library
Requires: %{name}%{?_isa} = %{version}-%{release}
Requires: gmp-devel%{?_isa}

%description devel
Header files and documentation for using the MPFR
multiple-precision floating-point library in applications.

If you want to develop applications which will use the MPFR library,
you'll need to install the mpfr-devel package. You'll also need to
install the mpfr package.

%package doc
Summary: Documentation for the MPFR library
License: GFDL-1.2-no-invariants-or-later
BuildArch: noarch

%description doc
Documentation for the MPFR library.

%prep
%(test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; })
%autosetup -p1

%build
%configure --disable-assert --disable-static

# Get rid of undesirable hardcoded rpaths; workaround libtool reordering
# -Wl,--as-needed after all the libraries.
sed -e 's|^hardcode_libdir_flag_spec=.*|hardcode_libdir_flag_spec=""|g' \
    -e 's|^runpath_var=LD_RUN_PATH|runpath_var=DIE_RPATH_DIE|g' \
    -e 's|CC="\(g..\)"|CC="\1 -Wl,--as-needed"|' \
    -i libtool

%make_build

%install
%make_install
cp -p ChangeLog PATCHES README %{buildroot}%{_pkgdocdir}
rm -f %{buildroot}%{_libdir}/*.la
rm -f %{buildroot}%{_infodir}/dir

#these go into licenses, not doc
rm -f %{buildroot}%{_pkgdocdir}/COPYING{,.LESSER}

%check
export LD_LIBRARY_PATH=%{buildroot}%{_libdir}
%make_build check

%files
%license COPYING COPYING.LESSER
%dir %{_pkgdocdir}
%{_pkgdocdir}/NEWS
%{_pkgdocdir}/README
%{_libdir}/libmpfr.so.6*

%files devel
%{_libdir}/libmpfr.so
%{_includedir}/mpfr.h
%{_includedir}/mpf2mpfr.h
%{_libdir}/pkgconfig/mpfr.pc

%files doc
%license COPYING COPYING.LESSER
%dir %{_pkgdocdir}
%{_pkgdocdir}/AUTHORS
%{_pkgdocdir}/BUGS
%{_pkgdocdir}/ChangeLog
%{_pkgdocdir}/FAQ.html
%{_pkgdocdir}/PATCHES
%{_pkgdocdir}/TODO
%{_pkgdocdir}/examples
%{_infodir}/mpfr.info*

%changelog
* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 4.2.2-3
- Prepare for Oreon 11 (RP1)
