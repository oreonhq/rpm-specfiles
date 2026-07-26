%global source0_hash f7d4fbd9f6edaddd9b602a70c94ffac761152c6191493b5cf3908104d7b87693

Name:           latte-integrale
Version:        1.7.6
Release:        15%{?dist}
Summary:        Lattice point enumeration

%global tarver  %(tr . _ <<< %{version})
%global lidiaver 2.3.0
%global lidiadate 2014-10-04
%global giturl  https://github.com/latte-int/latte
%global disturl https://github.com/latte-int/latte-distro

# The LattE code is GPL-2.0-or-later.
# The bundled gnulib code is GPL-3.0-or-later.
# The bundled LiDIA code was relicensed GPL-2.0-or-later at the time it was
# abandoned by upstream.  See:
# - https://groups.google.com/g/sage-devel/c/kTxgPSqrbUM/m/5Txj3_IKhlQJ
# - https://lists.debian.org/debian-legal/2007/07/msg00120.html
License:        GPL-2.0-or-later AND GPL-3.0-or-later
URL:            https://www.math.ucdavis.edu/~latte/software.php
VCS:            git:%{giturl}.git
Source0:        %{giturl}/releases/download/version_%{tarver}/latte-int-%{version}.tar.gz
Source1:        %{disturl}/raw/master/lidia-FF-%{lidiaver}+latte-patches-%{lidiadate}.tar.gz
Source2:        %{disturl}/raw/master/lidia-LA-%{lidiaver}+latte-patches-%{lidiadate}.tar.gz
Source3:        %{disturl}/raw/master/lidia-base-%{lidiaver}+latte-patches-%{lidiadate}.tar.gz
# Fix warnings that indicate possible runtime problems.
Patch:          %{name}-warning.patch
# Update obsolete C++ constructs: throw() specifiers
Patch:          %{name}-c++.patch
# Update obsolete usage of std::ifstream
Patch:          %{name}-ifstream.patch
# Fix LiDIA warnings that indicate possible runtime problems.
Patch:          lidia-warning.patch
# Update obsolete C++ constructs: throw() specifiers, register keyword, auto_ptr
Patch:          lidia-c++.patch

# See https://fedoraproject.org/wiki/Changes/EncourageI686LeafRemoval
ExcludeArch:    %{ix86}

BuildRequires:  4ti2-devel
BuildRequires:  cddlib-devel
BuildRequires:  cddlib-tools
BuildRequires:  gcc
BuildRequires:  gcc-c++
BuildRequires:  gmp-devel
BuildRequires:  libtool
BuildRequires:  lrslib-utils
BuildRequires:  make
BuildRequires:  perl-interpreter
BuildRequires:  pkgconfig(ntl)
BuildRequires:  sqlite-devel
BuildRequires:  TOPCOM

Requires:       cddlib-tools
Requires:       coreutils
Requires:       TOPCOM

Suggests:       lrslib-utils

# latte-integrale contains a copy of gnulib, which has been granted a bundling
# exception: https://fedoraproject.org/wiki/Packaging:No_Bundled_Libraries#Packages_granted_exceptions
Provides:       bundled(gnulib)

%description
LattE (Lattice point Enumeration) is a computer software dedicated to the
problems of counting lattice points and integration inside convex polytopes.
LattE contains the first ever implementation of Barvinok's algorithm.  The
LattE macchiato version (by M. Köppe) incorporated fundamental improvements
and speed ups.  Now the latest version, LattE integrale, has the ability to
directly compute integrals of polynomial functions over polytopes and in
particular to do volume computations.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n latte-int-%{version}
%setup -q -n latte-int-%{version} -T -D -a 1
%setup -q -n latte-int-%{version} -T -D -a 2
%setup -q -n latte-int-%{version} -T -D -a 3
%autopatch -p0

%conf
# Add a missing executable bit
chmod a+x ltmain.sh

# Fix the lrslib binary name
sed -i "s/lrs1/lrs/" configure

# Fix the 4ti2 library search paths
sed -ri "s|\{?FORTYTWO_HOME\}?/include|&/4ti2|g" configure
if [ %{_lib} = "lib64" ]; then
  sed -i "s|{FORTYTWO_HOME}/lib|&64|" configure
fi

# Some tests fail because they timeout on slower processors.  Eliminate the
# timeouts and let koji kill us if a test infloops.  Also, use a consistent
# hostname for reproducibility.
sed -e 's/ulimit -t $MAXRUNTIME; //' \
    -e 's,.*HOSTNAME = `hostname`.*,$HOSTNAME = "build.fedoraproject.org";,' \
    -i code/test-suite/test.pl.in

# Update lidia build scripts
cd lidia-%{lidiaver}+latte-patches-%{lidiadate}
cp -p %{_datadir}/libtool/build-aux/config.guess .
cp -p %{_datadir}/libtool/build-aux/config.sub .
cp -p %{_datadir}/libtool/build-aux/depcomp .
cp -p %{_datadir}/libtool/build-aux/install-sh .
cp -p %{_datadir}/libtool/build-aux/missing .
cd -

%build
module load lrslib-%{_arch}

# Make a place for a fake install of LiDIA
mkdir -p local%{_includedir}
ln -s lidia local%{_includedir}/LiDIA

# Build LiDia
cd lidia-%{lidiaver}+latte-patches-%{lidiadate}
%configure --disable-nf --disable-ec --disable-eco --disable-gec \
  CFLAGS='%{build_cflags} -fPIC -fno-strict-aliasing' \
  CXXFLAGS='%{build_cxxflags} -fPIC -fno-strict-aliasing'
sed -i 's/-m64/& -fPIC -fno-strict-aliasing/' libtool library/Makefile \
  library/base/Makefile library/linear_algebra/Makefile \
  library/finite_fields/Makefile
%make_build

# Do a fake install of LiDia for building latte-integrale
make install DESTDIR=$PWD/../local
sed -i "s,%{_libdir},$PWD/../local&," ../local%{_libdir}/*.la
cd -

# Now build latte-integrale itself
%configure --enable-DATABASE --enable-shared --disable-static \
  --with-4ti2=%{_prefix} --with-lidia=$PWD/local/%{_prefix} \
  CPPFLAGS="-I%{_includedir}/4ti2 -I%{_includedir}/cddlib -D_GNU_SOURCE=1 -DNTL_STD_CXX" \
  LDFLAGS="-L$PWD/local%{_libdir} %{build_ldflags}"

# Get rid of undesirable hardcoded rpaths; workaround libtool reordering
# -Wl,--as-needed after all the libraries.
sed -e 's|^hardcode_libdir_flag_spec=.*|hardcode_libdir_flag_spec=""|g' \
    -e 's|^runpath_var=LD_RUN_PATH|runpath_var=DIE_RPATH_DIE|g' \
    -e 's|CC="\(g..\)"|CC="\1 -Wl,--as-needed"|' \
    -i libtool

%make_build

%install
# Install latte-integrale
%make_install

# Some binaries have too-generic names
for bin in count integrate triangulate; do
  mv %{buildroot}%{_bindir}/$bin %{buildroot}%{_bindir}/latte-$bin
done

# Internal libraries only; don't install the .so since there are no headers
rm -f %{buildroot}%{_libdir}/lib{latte,normalize}.so

# We don't want documentation in _datadir
mv %{buildroot}%{_datadir}/latte-int _docs_staging

# Install missing documentation files
cp -p AUTHORS TODO _docs_staging

%check
export LD_LIBRARY_PATH=$PWD/local%{_libdir}:$PWD/code/latte/.libs:$PWD/code/latte/normalize/.libs
make check

%files
%doc AUTHORS NEWS README doc/manual.pdf
%license COPYING
%{_bindir}/ConvertCDDextToLatte
%{_bindir}/ConvertCDDineToLatte
%{_bindir}/count-linear-forms-from-polynomial
%{_bindir}/ehrhart
%{_bindir}/ehrhart3
%{_bindir}/hilbert-from-rays
%{_bindir}/hilbert-from-rays-symm
%{_bindir}/latte-count
%{_bindir}/latte-integrate
%{_bindir}/latte-maximize
%{_bindir}/latte-minimize
%{_bindir}/latte-triangulate
%{_bindir}/latte2ext
%{_bindir}/latte2ine
%{_bindir}/polyhedron-to-cones
%{_bindir}/top-ehrhart-knapsack
%{_libdir}/liblatte.so.0{,.*}
%{_libdir}/libnormalize.so.0{,.*}

%changelog
%autochangelog
