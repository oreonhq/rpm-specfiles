%global source0_hash 8d130430a2776e250e941ee16f51dba301d5f0a00cc288e05f5b985cf1f426cd

%global		module		Bonmin
%global		with_asl	1
%global		with_mpi	0

Name:		coin-or-%{module}
Summary:	Basic Open-source Nonlinear Mixed INteger programming
Version:	1.8.9
Release:	7%{?dist}

# EPL-1.0: the project as a whole
# SMLNJ: Bonmin/src/Interfaces/Ampl/sos_kludge.cpp
License:	EPL-1.0 AND SMLNJ
URL:		https://projects.coin-or.org/%{module}
Source0:	https://github.com/coin-or/Bonmin/archive/releases/%{version}/%{module}-%{version}.tar.gz
BuildRequires:	coin-or-Cgl-doc
BuildRequires:	coin-or-Clp-doc
BuildRequires:	coin-or-Ipopt-common
%if %{with_mpi}
BuildRequires:	coin-or-Ipopt-openmpi-devel
%else
BuildRequires:	pkgconfig(ipopt)
%endif
BuildRequires:	doxygen-latex
BuildRequires:	gcc-c++
BuildRequires:	help2man
BuildRequires:	make
%if %{with_asl}
BuildRequires:	asl-devel
%endif
%if %{with_mpi}
BuildRequires:	pkgconfig(ompi)
BuildRequires:	scalapack-openmpi-devel
BuildRequires:	openssh-clients
%endif
BuildRequires:	pkgconfig(cbc)
BuildRequires:	tex(tex4ht.sty)
BuildRequires:	tex(threeparttable.sty)

# See https://fedoraproject.org/wiki/Changes/EncourageI686LeafRemoval
ExcludeArch:    %{ix86}

# Install documentation in standard rpm directory
Patch0:		%{name}-docdir.patch

# Fix mixed signed/unsigned operations
Patch1:		%{name}-sign.patch

# https://github.com/coin-or/Bonmin/issues/24
Patch2:         %{name}-bug24.patch

# Fix Modern C issues in the configure script
Patch3:         %{name}-configure-c99.patch

%global _docdir_fmt %{name}

%description
Bonmin (Basic Open-source Nonlinear Mixed INteger programming) is an
experimental open-source C++ code for solving general MINLP (Mixed Integer
NonLinear Programming) problems of the form:

   min     f(x)

s.t.	   g_L <= g(x) <= g_U
	   x_L <=  x   <= x_U
	   x_i in Z for all i in I and,
	   x_i in R for all i not in I.

where f(x): R^n --> R, g(x): R^n --> R^m are twice continuously differentiable
functions and I is a subset of {1,..,n}.

Bonmin features several algorithms

  * B-BB is a NLP-based branch-and-bound algorithm,
  * B-OA is an outer-approximation decomposition algorithm,
  * B-QG is an implementation of Quesada and Grossmann's branch-and-cut
    algorithm,
  * B-Hyb is a hybrid outer-approximation based branch-and-cut algorithm. 

The algorithms in Bonmin are exact when the functions f and g are convex;
in the case where f or g or both are non-convex they are heuristics.

%package	devel
Summary:	Development files for %{name}
Requires:	coin-or-Cbc-devel%{?_isa}
Requires:	coin-or-Cgl-devel%{?_isa}
%if %{with_mpi}
Requires:	coin-or-Ipopt-openmpi-devel%{?_isa}
%else
Requires:	coin-or-Ipopt-devel%{?_isa}
%endif
Requires:	%{name}%{?_isa} = %{version}-%{release}

%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%package	doc
Summary:	Documentation files for %{name}
Requires:	coin-or-Cgl-doc
Requires:	coin-or-Clp-doc
Requires:	coin-or-Ipopt-common
Requires:	%{name} = %{version}-%{release}

%description	doc
This package contains the documentation for %{name}.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1 -n %{module}-releases-%{version}

# The pkgconfig file lists transitive dependencies.  Those are necessary when
# using static libraries, but not with shared libraries.
sed -i 's/ @BONMINLIB_PCLIBS@/\nLibs.private:&/' Bonmin/bonmin.pc.in

%build
%if %{with_mpi}
%_openmpi_load
%endif
%configure	\
%if %{with_asl}
	--with-asl-lib="-lasl -lipoptamplinterface" \
	--with-asl-incdir="%{_includedir}/asl"
%endif

# Get rid of undesirable hardcoded rpaths; workaround libtool reordering
# -Wl,--as-needed after all the libraries.
sed -e 's|^hardcode_libdir_flag_spec=.*|hardcode_libdir_flag_spec=""|g' \
    -e 's|^runpath_var=LD_RUN_PATH|runpath_var=DIE_RPATH_DIE|g' \
    -e 's|CC="\(g..\)"|CC="\1 -Wl,--as-needed"|' \
    -i libtool

%make_build all
%make_build -C Bonmin doxydoc

%install
%make_install
rm -f %{buildroot}%{_libdir}/*.la
rm %{buildroot}%{_pkgdocdir}/LICENSE
cp -a Bonmin/{AUTHORS,README} Bonmin/doxydoc/{bonmin_doxy.tag,html} \
  %{buildroot}%{_pkgdocdir}
mkdir -p %{buildroot}%{_mandir}/man1
LD_LIBRARY_PATH=%{buildroot}%{_libdir} help2man -N \
  Bonmin/src/Apps/.libs/bonmin > %{buildroot}%{_mandir}/man1/bonmin.1

%check
%if %{with_mpi}
%_openmpi_load
%endif
LD_LIBRARY_PATH=%{buildroot}%{_libdir}:$LD_LIBRARY_PATH make test

%files
%license LICENSE
%dir %{_pkgdocdir}
%{_pkgdocdir}/AUTHORS
%{_pkgdocdir}/README
%{_bindir}/bonmin
%{_libdir}/libbonmin.so.4
%{_libdir}/libbonmin.so.4.*
%if %{with_asl}
%{_libdir}/libbonminampl.so.4
%{_libdir}/libbonminampl.so.4.*
%endif
%{_mandir}/man1/bonmin.1*

%files devel
%{_includedir}/coin/*
%{_libdir}/libbonmin.so
%{_libdir}/pkgconfig/bonmin.pc
%if %{with_asl}
%{_libdir}/libbonminampl.so
%{_libdir}/pkgconfig/bonminamplinterface.pc
%endif

%files doc
%{_pkgdocdir}/html/
%{_pkgdocdir}/bonmin_doxy.tag

%changelog
%autochangelog
