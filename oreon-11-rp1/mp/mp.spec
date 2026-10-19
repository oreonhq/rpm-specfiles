%global source0_hash d0401ab85dc30ea1659f0083df4f5525bfcf3f716a0dfb767707c4d60feba280
%global with_jacop     0
%global with_gecode    0
%global with_highs     0
%global with_scip      0
%global blaslib openblas
%global commit      d66148218b3557708f7f2271c43d30ac6ee1935c
%global date        20260210
%global forgeurl    https://github.com/ampl/mp
Name: mp
Version: %{date}
Summary:        An open-source library for mathematical programming
%forgemeta
License: SMLNJ AND BSD-2-Clause
Release:        1%{?dist}
URL: https://mp.ampl.com/
VCS: git:%{forgeurl}.git
Source0:        %{forgeurl}/archive/%{commit}/%{name}-%{commit}.tar.gz
Patch0:  %{name}-unbundle-asl.patch
Patch1:  %{name}-3.1.0-jni.patch
Patch2:  %{name}-python3.patch
Patch8: %{name}-rhbz2380479.patch
ExcludeArch: %{ix86}
Provides: bundled(fmt) = 3.0.1
%if 0%{?with_scip}
%endif
%if 0%{?with_gecode}
%endif
%if 0%{?with_jacop}
Requires: jacop
%endif
%if 0%{?with_highs}
%endif
Obsoletes:     %{name}-doc < 20240115
%global majver %(cut -d. -f1 <<< %{version})
# oreon:deps
BuildRequires:  asl-devel
BuildRequires:  cmake
BuildRequires:  doxygen
BuildRequires:  gcc-c++
BuildRequires:  gdb
BuildRequires:  git-core
BuildRequires:  openblas-devel
BuildRequires:  pkgconfig(gsl)
BuildRequires:  python3-devel
# /oreon:deps
%description
An open-source library for mathematical programming.
Features
  * Reusable high-performance .nl reader
  * Efficient type-safe C++ API for connecting solvers to AMPL and
    other systems: source
  * Interfaces to solvers supporting AMPL extensions for logic and
    constraint programming:
      * IBM ILOG CPLEX and CPLEX CP Optimizer (ilogcp)
      * Gecode
      * JaCoP
  * Interfaces to the following solvers:
      * LocalSolver
      * Sulum
  * Interfaces to other solvers via AMPL Solver Library
  * Cross-platform build support with CMake and continuous
    integration systems. This includes third-party solvers and
    libraries (COIN-OR solvers with CMake support are available
    in the ampl/coin repository).
  * AMPLGSL, an AMPL function library providing access to the GNU
    Scientific Library (GSL) functions. See the AMPLGSL
    documentation.
  * Database support on Linux and MacOS X. See Database and
    spreadsheet connection guide.
  * SMPSWriter, a converter from deterministic equivalent of a
    two-stage stochastic programming (SP) problem written in AMPL
    to an SP problem in SMPS format.

%package devel
Summary: Development files for %{name}
Requires: %{name}%{?_isa} = %{version}-%{release}
Requires: asl-devel%{?_isa}
%description devel
This package contains the header files for %{name}.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%forgeautosetup -p1

%if 0%{?with_jacop}
jacopver=$(sed -n 's,^    <version>\(.*\)</version>,\1,p' %{_mavenpomdir}/jacop/jacop.pom)
ln -s %{_javadir}/jacop/jacop.jar thirdparty/jacop/jacop-$jacopver.jar
%endif

# Fix library installation location
if [ '%{_lib}' != 'lib' ]; then
  sed -i 's/\(DESTINATION \)lib/\1%{_lib}/' CMakeLists.txt src/asl/CMakeLists.txt
fi

# Install the AMPL function libraries in libexec
sed -i 's,\(AMPL_LIBRARY_DIR \)bin,\1libexec/mp,' CMakeLists.txt

# Link with an optimized blas library
sed -i 's/gslcblas/%{blaslib}/' src/gsl/CMakeLists.txt

# Enable the gsl interface
sed -i '/add_subdirectory(solvers)/i\\tadd_subdirectory(src/gsl)' CMakeLists.txt

# Link the HiGHS interface with the actual HiGHS library
%if 0%{?with_highs}
sed -i '/target_link_libraries/s/\${RT_LIBRARY}/& -lhighs/' CMakeLists.txt
%endif

# Link the SCIP interface with the actual SCIP library
%if 0%{?with_scip}
sed -i '/target_link_libraries/s/\${RT_LIBRARY}/& -lscip/' CMakeLists.txt
%endif

# Build the jacop interface for JDK 8 at a minimum
%if 0%{?with_jacop}
sed -i 's/1\.7/1.8/g' solvers/jacop/CMakeLists.txt
%endif

%build

BUILD='asl,smpswriter'
%if 0%{?with_gecode}
BUILD="gecode,$BUILD"
%endif
%if 0%{?with_jacop}
BUILD="jacop,$BUILD"
%endif
%if 0%{?with_highs}
BUILD="highsmp,$BUILD"
%endif
%if 0%{?with_scip}
BUILD="scipmp,$BUILD"
%endif
commonflags="-I%{_includedir}/asl -I$PWD/src/asl/solvers -I%{_includedir}/highs -I%{_includedir}/scip -DNDEBUG"
export CFLAGS="%{build_cflags} $commonflags"
export CXXFLAGS="%{build_cxxflags} $commonflags"
%cmake \
 -DCMAKE_SHARED_LINKER_FLAGS:STRING="$LDFLAGS" \
 -DCMAKE_CXX_FLAGS_RELEASE:STRING="$CXXFLAGS" \
 -DCMAKE_C_FLAGS_RELEASE:STRING="$CFLAGS" \
 -DCMAKE_SKIP_INSTALL_RPATH:BOOL=NO \
 -DCMAKE_SKIP_RPATH:BOOL=NO \
 -DCMAKE_VERBOSE_MAKEFILE:BOOL=YES \
 -DBUILD_SHARED_LIBS:BOOL=YES \
 -DBUILD:STRING=$BUILD
%cmake_build
%install
%cmake_install
rm -rf %{buildroot}%{_datadir}
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*

%files -f %{oreon_filedir}/main.list
%files -n mp-devel -f %{oreon_filedir}/mp-devel.list

%changelog

%autochangelog
