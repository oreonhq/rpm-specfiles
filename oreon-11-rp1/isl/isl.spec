%global source0_hash none
%global source1_hash none

Summary: Integer point manipulation library
Name: isl
Version: 0.16.1
License: MIT
URL: http://isl.gforge.inria.fr/

%global libmajor 15
%global libversion %{libmajor}.1.1

%global oldversion 0.14
%global oldlibmajor 13
%global oldlibversion %{oldlibmajor}.1.0

# Please set buildid below when building a private version of this rpm to
# differentiate it from the stock rpm.
#
# % global buildid .local

Release: 24%{?buildid}%{?dist}

BuildRequires:  gcc
BuildRequires: gmp-devel
BuildRequires: pkgconfig
BuildRequires: make
Provides: isl = %{oldversion}

Source0:        http://isl.gforge.inria.fr/isl-%{version}.tar.xz

# Current gcc requires exactly 0.14
Source1:        http://isl.gforge.inria.fr/isl-0.14.tar.xz

%description
isl is a library for manipulating sets and relations of integer points
bounded by linear constraints.  Supported operations on sets include
intersection, union, set difference, emptiness check, convex hull,
(integer) affine hull, integer projection, computing the lexicographic
minimum using parametric integer programming, coalescing and parametric
vertex enumeration.  It also includes an ILP solver based on generalized
basis reduction, transitive closures on maps (which may encode infinite
graphs), dependence analysis and bounds on piecewise step-polynomials.

%package devel
Summary: Development for building integer point manipulation library
Requires: isl%{?_isa} == %{version}-%{release}
Requires: gmp-devel%{?_isa}

%description devel
isl is a library for manipulating sets and relations of integer points
bounded by linear constraints.  Supported operations on sets include
intersection, union, set difference, emptiness check, convex hull,
(integer) affine hull, integer projection, computing the lexicographic
minimum using parametric integer programming, coalescing and parametric
vertex enumeration.  It also includes an ILP solver based on generalized
basis reduction, transitive closures on maps (which may encode infinite
graphs), dependence analysis and bounds on piecewise step-polynomials.

%prep
%(test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; })
%(test "%{source1_hash}" = "none" || { f="%{SOURCE1}"; test -f "$f" || { echo "oreon: missing Source1 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source1_hash}" || { echo "oreon: Source1 hash mismatch" >&2; exit 1; }; })
%global docdir isl-%{version}
%setup -a 1 -q -n isl -c

%build
cd isl-%{oldversion}
%configure
%make_build
cd ..

cd isl-%{version}
%configure
%make_build

%install
cd isl-%{oldversion}
%make_install install-libLTLIBRARIES
cd ..

cd isl-%{version}
%make_install
rm -f %{buildroot}/%{_libdir}/libisl.a
rm -f %{buildroot}/%{_libdir}/libisl.la
mkdir -p %{buildroot}/%{_datadir}
%global gdbprettydir %{_datadir}/gdb/auto-load/%{_libdir}
mkdir -p %{buildroot}/%{gdbprettydir}
mv %{buildroot}/%{_libdir}/*-gdb.py* %{buildroot}/%{gdbprettydir}

%check
cd isl-%{oldversion}
#make check
cd ..

cd isl-%{version}
#make check

%ldconfig_scriptlets

%files
%{_libdir}/libisl.so.%{libmajor}
%{_libdir}/libisl.so.%{libversion}
%{_libdir}/libisl.so.%{oldlibmajor}
%{_libdir}/libisl.so.%{oldlibversion}
%{gdbprettydir}/*
%license %{docdir}/LICENSE
%doc %{docdir}/AUTHORS %{docdir}/ChangeLog %{docdir}/README

%files devel
%{_includedir}/*
%{_libdir}/libisl.so
%{_libdir}/pkgconfig/isl.pc
%doc %{docdir}/doc/manual.pdf


%changelog
* Mon May 25 2026 Oreon Packaging Team <packaging@oreonhq.com> - 0.16.1-24
- Import
