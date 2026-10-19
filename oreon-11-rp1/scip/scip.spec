%global source0_hash abf11e86f5d2025a8f5652e818ff02eb60e41bcf61f6ad4d2ddbe6762ac7f7d0
%global giturl  https://github.com/scipopt/scip
Name:           scip
Version:        10.0.1
Release:        1%{?dist}
Summary:        Solving Constraint Integer Programs
License:        Apache-2.0 AND EPL-1.0 AND MIT AND SMLNJ AND dtoa
URL:            https://scipopt.org/
VCS:            git:%{giturl}.git
Source0:        %{giturl}/archive/v%{version}/%{name}-%{version}.tar.gz
Patch:          %{name}-no-rpath.patch
Patch:          %{name}-unbundle.patch
Patch:          %{name}-headers.patch
Patch:          %{name}-uninitialized-memory.patch
Patch:          %{name}-zlib-ng.patch
ExcludeArch:    %{ix86}
Requires:       libscip%{?_isa} = %{version}-%{release}
%global _desc %{expand:Welcome to what is currently one of the fastest academically developed solvers
for mixed integer programming (MIP) and mixed integer nonlinear programming
(MINLP).  In addition, SCIP provides a highly flexible framework for
constraint integer programming and branch-cut-and-price.  It allows for total
control of the solution process and the access of detailed information down to
the guts of the solver.}
# oreon:deps
BuildRequires:  cmake
BuildRequires:  cmake(soplex)
BuildRequires:  cmake(zimpl)
BuildRequires:  doxygen
BuildRequires:  gcc-c++
BuildRequires:  gcc-gfortran
BuildRequires:  gnuplot
BuildRequires:  mathjax
BuildRequires:  php-cli
BuildRequires:  pkgconfig(gmp)
BuildRequires:  pkgconfig(ipopt)
BuildRequires:  pkgconfig(libnauty)
BuildRequires:  pkgconfig(readline)
BuildRequires:  pkgconfig(zlib-ng)
BuildRequires:  python3
BuildRequires:  soplex
BuildRequires:  vipr
BuildRequires:  zimpl
# /oreon:deps
%description
%_desc

This package contains a command-line tool to access SCIP functionality.

%package -n     libscip
Summary:        Library for solving constraint integer programs
Provides:       bundled(cppad) = 20180000
Provides:       bundled(mp) = 4.0.3
Provides:       bundled(fmt) = 3.0.1
Provides:       bundled(sassy) = 2.0
%description -n libscip
%_desc

This package contains a library for solving constraint integer programs.

%package -n     libscip-devel
Summary:        Headers and library links for libscip
Requires:       scip%{?_isa} = %{version}-%{release}
Requires:       libscip%{?_isa} = %{version}-%{release}
Requires:       gmp-devel%{?_isa}
Requires:       libnauty-devel%{?_isa}
Requires:       mpfr-devel%{?_isa}
Requires:       zlib-devel%{?_isa}
%description -n libscip-devel
This package contains headers and library links for developing applications
that use libscip.

%package -n     libscip-doc
License:        Apache-2.0 AND GPL-1.0-or-later AND MIT
Summary:        API documentation for libscip
BuildArch:      noarch
Provides:       bundled(jquery) = 3.6.0
%description -n libscip-doc
API documentation for libscip.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1

%conf
# We want to know about overflow errors, as the compiler can do surprising
# things if we don't fix them!
sed -i 's/ -Wno-strict-overflow//' CMakeLists.txt make/make.project

# Turn off HTML timestamps for repeatable builds
sed -i '/HTML_TIMESTAMP/s/= YES/= NO/' doc/scip.dxy
sed -i 's/ on \$date//' doc/scipfooter.html

# Use a fixed 'linux' value in OSTYPE for repeatable builds
sed -i 's/OSTYPE=@.*@/OSTYPE=linux/' src/scipbuildflags.c.in

# Ensure we cannot use the bundled bliss or nauty
rm -fr src/{bliss,nauty}

%build

%ifarch %{power64}
export CFLAGS='%{build_cflags} -DBOOST_MP_BITS_OF_FLOAT128_DEFINED'
export CXXFLAGS='%{build_cxxflags} -DBOOST_MP_BITS_OF_FLOAT128_DEFINED'
%endif
%cmake \
    -DCMAKE_INSTALL_LIBDIR:PATH=%{_libdir} \
    -DNAUTY_DIR:PATH=%{_prefix} \
    -DSYM:STRING=snauty \
    -DTPI:STRING=omp
%cmake_build
cd doc
ln -s %{_datadir}/javascript/mathjax MathJax
ln -s ../check .
../%{_vpath_builddir}/bin/scip < inc/shelltutorial/commands \
  > inc/shelltutorial/shelltutorialraw.tmp
python3 inc/shelltutorial/insertsnippetstutorial.py
cd inc/faq
python3 parser.py --linkext shtml
php localfaq.php > faq.inc
cd -
../%{_vpath_builddir}/bin/scip -c "set default set save inc/parameters.set quit"
../%{_vpath_builddir}/bin/scip -c "read inc/simpleinstance/simple.lp optimize quit" \
  > inc/simpleinstance/output.log
doxygen scip.dxy
cd ..
%install
%cmake_install
rm -fr %{buildroot}%{_defaultlicensedir}
%oreon_autofiles libscip usr/*/lib*.so.*
%oreon_autofiles libscip-devel usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*
%oreon_autofiles libscip-doc usr/*/lib*.so.*
%oreon_autofiles main usr/*/lib*.so.* usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/* usr/*/lib*.so.*

%check

export LD_LIBRARY_PATH=%{buildroot}%{_libdir}
%ctest -E '(classical_20_0)|(examples-)'
%files -f %{oreon_filedir}/main.list
%files -n libscip -f %{oreon_filedir}/libscip.list
%files -n libscip-devel -f %{oreon_filedir}/libscip-devel.list
%files -n libscip-doc -f %{oreon_filedir}/libscip-doc.list

%changelog

%autochangelog
