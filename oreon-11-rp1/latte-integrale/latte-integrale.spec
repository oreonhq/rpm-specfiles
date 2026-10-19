%global source0_hash f7d4fbd9f6edaddd9b602a70c94ffac761152c6191493b5cf3908104d7b87693
Name:           latte-integrale
Version:        1_7_6
Release:        1%{?dist}
Summary:        Lattice point enumeration
%global tarver  %(tr . _ <<< %{version})
%global lidiaver 2.3.0
%global lidiadate 2014-10-04
%global giturl  https://github.com/latte-int/latte
%global disturl https://github.com/latte-int/latte-distro
License:        GPL-2.0-or-later AND GPL-3.0-or-later
URL:            https://www.math.ucdavis.edu/~latte/software.php
VCS:            git:%{giturl}.git
Source0:        %{giturl}/releases/download/version_%{version}/latte-int-%{version}.tar.gz
Source1:        %{disturl}/raw/master/lidia-FF-%{lidiaver}+latte-patches-%{lidiadate}.tar.gz
Source2:        %{disturl}/raw/master/lidia-LA-%{lidiaver}+latte-patches-%{lidiadate}.tar.gz
Source3:        %{disturl}/raw/master/lidia-base-%{lidiaver}+latte-patches-%{lidiadate}.tar.gz
Patch:          %{name}-warning.patch
Patch:          %{name}-c++.patch
Patch:          %{name}-ifstream.patch
Patch:          lidia-warning.patch
Patch:          lidia-c++.patch
ExcludeArch:    %{ix86}
Requires:       cddlib-tools
Requires:       coreutils
Requires:       TOPCOM
Suggests:       lrslib-utils
Provides:       bundled(gnulib)
# oreon:deps
BuildRequires:  4ti2-devel
BuildRequires:  TOPCOM
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
# /oreon:deps
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
mkdir -p local%{_includedir}
ln -s lidia local%{_includedir}/LiDIA
cd lidia-%{lidiaver}+latte-patches-%{lidiadate}
%configure --disable-nf --disable-ec --disable-eco --disable-gec \
  CFLAGS='%{build_cflags} -fPIC -fno-strict-aliasing' \
  CXXFLAGS='%{build_cxxflags} -fPIC -fno-strict-aliasing'
sed -i 's/-m64/& -fPIC -fno-strict-aliasing/' libtool library/Makefile \
  library/base/Makefile library/linear_algebra/Makefile \
  library/finite_fields/Makefile
%make_build
make install DESTDIR=$PWD/../local
sed -i "s,%{_libdir},$PWD/../local&," ../local%{_libdir}/*.la
cd -
%configure --enable-DATABASE --enable-shared --disable-static \
  --with-4ti2=%{_prefix} --with-lidia=$PWD/local/%{_prefix} \
  CPPFLAGS="-I%{_includedir}/4ti2 -I%{_includedir}/cddlib -D_GNU_SOURCE=1 -DNTL_STD_CXX" \
  LDFLAGS="-L$PWD/local%{_libdir} %{build_ldflags}"
sed -e 's|^hardcode_libdir_flag_spec=.*|hardcode_libdir_flag_spec=""|g' \
    -e 's|^runpath_var=LD_RUN_PATH|runpath_var=DIE_RPATH_DIE|g' \
    -e 's|CC="\(g..\)"|CC="\1 -Wl,--as-needed"|' \
    -i libtool
%make_build
%install
%make_install
for bin in count integrate triangulate; do
  mv %{buildroot}%{_bindir}/$bin %{buildroot}%{_bindir}/latte-$bin
done
rm -f %{buildroot}%{_libdir}/lib{latte,normalize}.so
mv %{buildroot}%{_datadir}/latte-int _docs_staging
cp -p AUTHORS TODO _docs_staging
%oreon_autofiles main

%check

export LD_LIBRARY_PATH=$PWD/local%{_libdir}:$PWD/code/latte/.libs:$PWD/code/latte/normalize/.libs
make check
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
