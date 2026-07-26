%global source0_hash cf12d4eb6b5530ab047a9c49e46aa1a19d77fd0ba90fb35e429b23e8ff659378

%global tarname FreeFem-sources
%global tarvers 4.15
%global ffvers 4.15

%bcond_without serial

# Allow disabling building with/against openmpi
# Build with --without openmpi to not build openmpi
%bcond_without openmpi

# Allow disabling building with/against mpich
# Build with --without openmpi to not build mpich
%bcond_without mpich

%bcond_without xfail

# Don't exercise %%check on the archs below.
# They fail/hang for yet undetermined causes.
# Build with --with checks to force building them.
# Build with --without checks to skip building them.
%ifarch ppc64le aarch64 s390x armv7hl %{ix86} riscv64
%bcond check 1s
%else
%bcond check 0s
%endif

Summary: PDE solving tool
Name: freefem++
Version: %{expand:%(echo %tarvers | tr - .)}
Release: 8%{?dist}
URL: https://freefem.org
Source0: https://github.com/FreeFem/FreeFem-sources/archive/v%{tarvers}.tar.gz#/%{tarname}-%{tarvers}.tar.gz

# Fedora patches
Patch01: 0001-Build-fixes.patch
Patch02: 0002-Fix-formating-buffers.patch
Patch03: 0003-Wsign-compare.patch
Patch04: 0004-Wimplicit-function-declaration.patch
Patch05: 0005-Wreorder.patch
Patch06: 0006-Remove-src-medit-eigenv.h.patch
Patch07: 0007-Wformat-overflow.patch
Patch08: 0008-Use-test-e-instead-of-test-f.patch
Patch09: 0009-Fix-quoting.patch
Patch10: 0010-Use-prebuilt-FreeFEM-documentation.pdf.patch
Patch11: 0011-Install-docs-into-docdir.patch
Patch12: 0012-Use-libdir-to-setup-ff_prefix_dir.patch
Patch13: 0013-Wmisleading-indentation.patch
Patch14: 0014-Fix-missing-includes-for-gcc-11.patch
Patch15: 0015-Modernize-autotools.patch
Patch16: 0016-Unbundle-boost.patch
Patch17: 0017-Fedora-hacks.patch
Patch18: 0018-Comment-out-LD_LBFGS_NOCEDAL.patch

# --disable-download doesn't work
# Bundle hpddm.zip to prevent downloading during builds.
# cf. hpddm in 3rdparty/getall
%if 0%{fedora} > 42
# bleeding edge petsc
# Fails to build on Fedora <= 42
%global hpddm_git_hash acc20d7ad9c28d5cc57e794818689a166a4ccf8a
%global hpddm_git_md5sum 655e35271b8167df4ed0816df8cfe915
%global hpddm_gitdate 20240925
%else
# petsc-3.20.x compatible
# hpddm-20231112gita789a19
%global hpddm_git_hash a789a193f3c9c7c3c2674eb8d1f8db95cd1ae48c
%global hpddm_git_md5sum debcabc4cb0100cd5e79f9efb8cbafe3
%global hpddm_gitdate 20231112
%endif
%global hpddm_gitcommit %(c=%{hpddm_git_hash}; echo ${c:0:7})

%global htool_git_hash 1a3b198ffc6f73cd62059094ca7b606d151da976
%global htool_git_md5sum 325ab9411e7a50212f99c1302f4cf81f
%global htool_gitcommit %(c=%{htool_git_hash}; echo ${c:0:7})
%global htool_gitdate 20240802

%if "%{version}" >= "4.15"
%global bemtool_git_hash 6e61fbf86d8cd53994d9f597e60fde537650ba14
%global bemtool_git_md5sum 2de5404f4a88d7c8847bd85209fd69a1
%global bemtool_gitcommit %(c=%{bemtool_git_hash}; echo ${c:0:7})
%global bemtool_gitdate 20230923
%else
%global bemtool_git_hash 629c44513698405b58c50650cba69419474062ad
%global bemtool_git_md5sum 869832f5cbec4dfb2c16e2d94bad0b7d
%global bemtool_gitcommit %(c=%{bemtool_git_hash}; echo ${c:0:7})
%global bemtool_gitdate 20230917
%endif
Source1: https://github.com/hpddm/hpddm/archive/%{hpddm_gitcommit}/master.zip#/hpddm-%{hpddm_gitdate}git%{hpddm_gitcommit}.zip

# FreeFEM doesn't build docs anymore.
# Use pre-build binary, d/l'ed from
# https://doc.freefem.org/pdf/FreeFEM-documentation.pdf
Source2: https://raw.githubusercontent.com/FreeFem/FreeFem-doc/pdf/FreeFEM-documentation.pdf#/FreeFEM-documentation-4.13-20241205.pdf

# Bundled libraries
Source3: https://www.ljll.math.upmc.fr/frey/ftp/archives/freeyams.2012.02.05.tgz
Source4: https://github.com/htool-ddm/htool/archive/%{htool_gitcommit}/master.zip#/htool-%{htool_gitdate}git%{htool_gitcommit}.zip
%if "%{version}" >= "4.15"
# from branch update_htool
Source5: https://github.com/PierreMarchand20/BemTool/archive/%{bemtool_gitcommit}.zip#/bemtool-%{bemtool_gitdate}git%{bemtool_gitcommit}.zip
%else
Source5: https://github.com/PierreMarchand20/BemTool/archive/%{bemtool_gitcommit}/master.zip#/bemtool-%{bemtool_gitdate}git%{bemtool_gitcommit}.zip
%endif
Source6: https://www.ljll.math.upmc.fr/frey/ftp/archives/mshmet.2012.04.25.tgz

%if 0%{fedora} > 41
%global MUMPS_VERS 5.7.3
%else
%global MUMPS_VERS 5.6.2
%endif
Source7: https://mumps-solver.org/MUMPS_%{MUMPS_VERS}.tar.gz

License: LGPL-3.0-or-later

# See https://fedoraproject.org/wiki/Changes/EncourageI686LeafRemoval
ExcludeArch:    %{ix86}

# for 3rdparty/getall
BuildRequires: perl(strict) perl(Getopt::Std) perl(Digest::MD5)

# FreeFEM uses a wild mixture of autotools and cmake
BuildRequires:	automake
BuildRequires:	cmake
BuildRequires:	make
BuildRequires:	wget

BuildRequires:	flex
BuildRequires:	bison
BuildRequires:	gcc-c++
BuildRequires:	gcc-gfortran
BuildRequires:	glut-devel
BuildRequires:	gsl-devel
BuildRequires:	libGLU-devel

BuildRequires:	arpack-devel
BuildRequires:	boost-devel
BuildRequires:	coin-or-Ipopt-devel
BuildRequires:	asio-devel
#BuildRequires:	gmm-devel
BuildRequires:	fftw-devel
BuildRequires:	hdf5-devel
BuildRequires:	metis-devel
# mmg's packaging is a mess
# By installing mmg* packages, mmg3d plugin will be automatically enabled and test files will require mmg3d-v4 bundled library
# BuildRequires:	mmg-devel mmg2d-devel mmgs-devel mmg3d-devel
BuildRequires:	MUMPS-devel
BuildRequires:	NLopt-devel
BuildRequires:	flexiblas-devel
BuildRequires:	petsc-devel
BuildRequires:	scotch-devel
BuildRequires:	suitesparse-devel
BuildRequires:	SuperLU-devel
BuildRequires:	tetgen-devel

%description
A PDE oriented language using Finite Element Method FreeFem++ is an
implementation of a language dedicated to the finite element method. It
provides you a way to solve Partial Differential Equations (PDE) simply.

Problems involving partial differential equations (pde) of  several
branches of physics such as fluid-structure interactions require
interpolations of data on several meshes and their manipulation within
one program.

FreeFem++ is an extension of freefem, freefem+ written in C++.

%if %{with openmpi}
%package openmpi
Summary: PDE solving tool - OpenMPI version
BuildRequires:	/etc/profile.d/modules.sh
BuildRequires:	openmpi-devel
BuildRequires:	arpack-devel
BuildRequires:	flexiblas-devel
BuildRequires:	fftw-devel
BuildRequires:	hdf5-devel
BuildRequires:	suitesparse-devel
BuildRequires:	SuperLU-devel

BuildRequires:	hdf5-openmpi-devel
BuildRequires:	blacs-openmpi-devel
BuildRequires:	MUMPS-openmpi-devel
BuildRequires:	petsc-openmpi-devel
BuildRequires:	ptscotch-openmpi-devel
BuildRequires:	ptscotch-openmpi-devel-parmetis
BuildRequires:	scalapack-openmpi-devel
BuildRequires:	hypre-openmpi-devel
BuildRequires:	cgnslib-openmpi-devel
BuildRequires:	superlu_dist-openmpi-devel
BuildRequires:	flexiblas-devel

Requires: %{name} = %{version}-%{release}

%description openmpi
This package contains the OpenMPI version of FreeFem++.
%endif

%if %{with mpich}
%package mpich
Summary: PDE solving tool - MPICH version
BuildRequires:	/etc/profile.d/modules.sh
BuildRequires:	mpich-devel
BuildRequires:	arpack-devel
BuildRequires:	flexiblas-devel
BuildRequires:	fftw-devel
BuildRequires:	hdf5-devel
BuildRequires:	suitesparse-devel
BuildRequires:	SuperLU-devel

BuildRequires:	hdf5-mpich-devel
BuildRequires:	blacs-mpich-devel
BuildRequires:	MUMPS-mpich-devel
BuildRequires:	petsc-mpich-devel
BuildRequires:	ptscotch-mpich-devel
BuildRequires:	ptscotch-mpich-devel-parmetis
BuildRequires:	scalapack-mpich-devel
BuildRequires:	hypre-mpich-devel
BuildRequires:	cgnslib-mpich-devel
BuildRequires:	superlu_dist-mpich-devel
BuildRequires:	flexiblas-devel

Requires: %{name} = %{version}-%{release}

%description mpich
This package contains the MPICH version of FreeFem++.
%endif

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -c -T -a 0

mv %{tarname}-%{tarvers} serial
pushd serial
%patch -P 01 -p1
%patch -P 02 -p1
%patch -P 03 -p1
%patch -P 04 -p1
%patch -P 05 -p1
%patch -P 06 -p1
%patch -P 07 -p1
%patch -P 08 -p1
%patch -P 09 -p1
%patch -P 10 -p1
%patch -P 11 -p1
%patch -P 12 -p1
%patch -P 13 -p1
%patch -P 14 -p1
%patch -P 15 -p1
%patch -P 16 -p1
%patch -P 17 -p1
%patch -P 18 -p1

sed -i \
  -e 's,5.0.2,%{MUMPS_VERS},' \
  3rdparty/getall \
  3rdparty/mumps-seq/Makefile
sed \
  -e 's,5.0.2,%{MUMPS_VERS},' \
  3rdparty/mumps-seq/Makefile-mumps-5.0.2.inc \
  > 3rdparty/mumps-seq/Makefile-mumps-%{MUMPS_VERS}.inc

sed -i \
  -e 's,/hpddm/zip/7113b9a6b77fceee3f52490cb27941a87b96542f,/hpddm/zip/%{hpddm_git_hash},' \
  -e "s,'6910b7b974f0b60d9c247c666e7f3862','%{hpddm_git_md5sum}'," \
  3rdparty/getall

sed -i \
  -e 's,/htool/archive/946875d79d0036afb4dc2c0c13c165a607d830df.zip,/htool/archive/%{htool_git_hash}.zip,' \
  -e "s,'1403db4800a2d4b69f3da7eb3f6687a2','%{htool_git_md5sum}'," \
  3rdparty/getall

sed -i \
  -e 's,/BemTool/archive/629c44513698405b58c50650cba69419474062ad.zip,/BemTool/archive/%{bemtool_git_hash}.zip,' \
  -e "s,'869832f5cbec4dfb2c16e2d94bad0b7d','%{bemtool_git_md5sum}'," \
  3rdparty/getall

%if %{with xfail}
sed -i -e 's,XFAIL_TESTS = ,XFAIL_TESTS = Pinocchio.edp ,' examples/3dSurf/Makefile.am
sed -i -e 's,XFAIL_TESTS = ,XFAIL_TESTS = testvtk.edp ,' examples/3dSurf/Makefile.am
sed -i -e 's,XFAIL_TESTS =$,XFAIL_TESTS = ,' examples/3d/Makefile.am
sed -i -e 's,XFAIL_TESTS =,XFAIL_TESTS = fallingspheres.edp ,'	examples/3d/Makefile.am
%endif

# Bogus permissions
find . -type f -perm 755 \( -name "*.c*" -o -name "*.h*" -o -name "*.edp" -o -name "*.idp" \) | xargs chmod 644

autoreconf -vif

mkdir -p 3rdparty/pkg
cp %{SOURCE1} 3rdparty/pkg/hpddm.zip
cp %{SOURCE2} FreeFEM-documentation.pdf
cp %{SOURCE3} 3rdparty/pkg/
cp %{SOURCE4} 3rdparty/pkg/htool.zip
cp %{SOURCE5} 3rdparty/pkg/bemtool.zip
cp %{SOURCE6} 3rdparty/pkg/
cp %{SOURCE7} 3rdparty/pkg/
popd

# MPI flavors
%{?with_openmpi:cp -r serial openmpi}
%{?with_mpich:cp -r serial mpich}

%build
%if %{with serial}
pushd serial
%configure \
	INSTALL="%{__install} -p" \
	--disable-optim \
	--disable-download \
	--with-petsc=%{_libdir}/petsc/conf/petscvariables \
	--enable-hpddm --enable-download_hpddm \
	--enable-yams --enable-download_yams \
	--disable-gmm --disable-download_gmm \
	--enable-mumps \
	--enable-mumps_seq --enable-download_mumps_seq \
	--enable-bem --enable-download_bem \
	--enable-htool --enable-download_htool \
	--disable-scalapack --disable-download_scalapack \
	--enable-mshmet --enable-download_mshmet \
	--enable-boost \
	--disable-mmg3d \
	--disable-parmetis --disable-parmmg \
	--with-blas="-L%{_libdir} -lflexiblas" \
	--with-arpack="-L%{_libdir} -larpack" \
	--without-cadna \
	--with-mpi=no \
	--docdir=%{_pkgdocdir} \
	CPPFLAGS="-I$(pwd) -I/usr/include/scotch" \
	CFLAGS="%{optflags} -fPIC" \
	CXXFLAGS="%{optflags} -fPIC"

%define _smp_mflags -j48
make %{?_smp_mflags}
popd
%endif

for mpi in %{?with_mpich:mpich} %{?with_openmpi:openmpi} ; do
  pushd ${mpi}
  . /etc/profile.d/modules.sh
  module load mpi/${mpi}-%{_arch}
  %configure \
	INSTALL="%{__install} -p" \
	--disable-optim \
	--disable-download \
	--with-petsc=%{_libdir}/${mpi}/lib/petsc/conf/petscvariables \
	--enable-hpddm --enable-download_hpddm \
	--enable-yams --enable-download_yams \
	--disable-gmm --disable-download_gmm \
	--enable-mumps \
	--enable-mumps_seq --enable-download_mumps_seq \
	--enable-bem --enable-download_bem \
	--enable-htool --enable-download_htool \
	--enable-scalapack --disable-download_scalapack --with-scalapack-ldflags="-L%{_libdir}/${mpi}/lib" \
	--enable-mshmet --enable-download_mshmet \
	--enable-boost \
	--disable-mmg3d \
	--disable-parmetis --disable-parmmg \
	--with-blas="-L%{_libdir} -lflexiblas" \
	--with-arpack="-L%{_libdir} -larpack" \
	--without-cadna \
	--with-mpi=yes \
	--docdir=%{_pkgdocdir} \
	CPPFLAGS="-I$(pwd) -I/usr/include/scotch" \
	CFLAGS="%{optflags} -fPIC" \
	CXXFLAGS="%{optflags} -fPIC" \
	MPICXX=$MPI_BIN/mpic++ \
	MPIFC=$MPI_BIN/mpifort \
	MPICC=$MPI_BIN/mpicc \
	CXX=$MPI_BIN/mpic++ \
	FC=$MPI_BIN/mpifort \
	CC=$MPI_BIN/mpicc

%define _smp_mflags -j48
  make %{?_smp_mflags}
  module unload mpi/${mpi}-%{_arch}
  popd
done

%install
%if %{with serial}
pushd serial
make DESTDIR=%{buildroot} install
chmod 744 %{buildroot}%{_libdir}/ff++/%{ffvers}/lib/*.so
chmod 644 %{buildroot}%{_libdir}/ff++/%{ffvers}/lib/WHERE*
pushd %{buildroot}%{_datadir}/FreeFEM
popd
# the binary with no suffix should be the generic X11 one according to README
# the build system makes it identical to -nw version, so overwrite it
ln -sf FreeFem++-nw %{buildroot}%{_bindir}/FreeFem++
popd
%endif

for mpi in %{?with_mpich:mpich} %{?with_openmpi:openmpi} ; do
  pushd $mpi
  make DESTDIR=`pwd`/buildtree install
  for bin in FreeFem++-mpi ff-mpirun ; do
    install -D -m 755 -p buildtree/%{_bindir}/$bin %{buildroot}%{_libdir}/${mpi}/bin/${bin}_${mpi}
  done
  for lib in MPICG.so mpi-cmaes.so ; do
    install -D -m 744 -p buildtree/%{_libdir}/ff++/%{ffvers}/lib/mpi/$lib %{buildroot}%{_libdir}/${mpi}/lib/ff++/lib/$lib
  done
  popd
done

%check
%if %{with checks}
%if %{with serial}
pushd serial
export OMP_NUM_THREADS=4
make -j1 check
popd
%endif

for mpi in %{?with_mpich:mpich} %{?with_openmpi:openmpi} ; do
  pushd ${mpi}
  . /etc/profile.d/modules.sh
  module load mpi/${mpi}-%{_arch}
  make -j1 check
  module unload mpi/${mpi}-%{_arch}
  popd
done
%endif

%if %{with serial}
%files
%doc serial/AUTHORS serial/CHANGELOG.md
%doc FreeFEM-documentation.pdf
%license serial/readme/COPYRIGHT
%{_bindir}/FreeFem++
%{_bindir}/FreeFem++-nw
%{_bindir}/bamg
%{_bindir}/cvmsh2
%{_bindir}/ffglut
%{_bindir}/ffmedit
%{_bindir}/ffmaster
%{_libdir}/ff++
%{_bindir}/ff-c++
%{_bindir}/ff-get-dep
%{_datadir}/FreeFEM
# Not useful to install
%exclude %{_bindir}/ff-pkg-download
# Unclear, if to be shipped
%exclude %{_bindir}/md2edp
%endif

%if %{with openmpi}
%files openmpi
%{_libdir}/openmpi/bin/FreeFem++-mpi_openmpi
%{_libdir}/openmpi/bin/ff-mpirun_openmpi
%{_libdir}/openmpi/lib/ff++
%endif

%if %{with mpich}
%files mpich
%{_libdir}/mpich/bin/FreeFem++-mpi_mpich
%{_libdir}/mpich/bin/ff-mpirun_mpich
%{_libdir}/mpich/lib/ff++
%endif

%changelog
%autochangelog
