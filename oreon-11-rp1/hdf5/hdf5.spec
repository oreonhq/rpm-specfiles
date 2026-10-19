%global source2_hash fe7b967765ede48f132f4bc7d632515bd86e1130f1e643cc50d1a6405477029c
%global source0_hash 1a1ab8209b35586fbc1aa279ba76d102130b95badcb20ca329587219112d8c16
%ifarch %{java_arches}
%bcond_without java
%else
%bcond_with java
%endif
Name: hdf5
Version: 2.2.0
Release:        1%{?dist}
Summary:        A general purpose library and file format for storing scientific data
License: BSD-3-Clause
URL: https://www.hdfgroup.org/solutions/hdf5/
Source0:        https://github.com/HDFGroup/hdf5/releases/download/%{version}/hdf5-%{version}.tar.gz
%global so_version 320
%global plugin_dir %{_libdir}/hdf5/plugin
Source1: h5comp
Source2: http://ftp.us.debian.org/debian/pool/main/h/hdf5/hdf5_2.2.0+repack-5.debian.tar.xz
Patch: hdf5-wrappers.patch
Patch: hdf5-jarname.patch
Patch: hdf5-fmoddir.patch
%if %{with java}
%else
Obsoletes:     java-hdf5 < %{version}-%{release}
%endif
%global _hdf5_compat_version %(v=%{version}; echo ${v%.*})
Provides: %{name} = %{_hdf5_compat_version}
Provides: %{name}%{?_isa} = %{_hdf5_compat_version}
%global with_mpich %{undefined flatpak}
%global with_openmpi %{undefined flatpak}
%if %{with_mpich}
%global mpi_list mpich
%endif
# oreon:deps
BuildRequires:  cmake
BuildRequires:  gcc
BuildRequires:  gcc-c++
BuildRequires:  gcc-gfortran
BuildRequires:  git-core
BuildRequires:  hamcrest
BuildRequires:  hostname
BuildRequires:  java-devel
BuildRequires:  javapackages-tools
BuildRequires:  junit
BuildRequires:  krb5-devel
BuildRequires:  libaec-devel
BuildRequires:  libaec-static
BuildRequires:  mpich-devel
BuildRequires:  openssh-clients
BuildRequires:  openssl-devel
BuildRequires:  perl-interpreter
BuildRequires:  slf4j
BuildRequires:  time
BuildRequires:  zlib-devel
BuildRequires:  zlib-static
# /oreon:deps
%description
HDF5 is a general purpose library and file format for storing scientific data.
HDF5 can store two primary objects: datasets and groups. A dataset is
essentially a multidimensional array of data elements, and a group is a
structure for organizing objects in an HDF5 file. Using these two basic
objects, one can create and store almost any kind of scientific data
structure, such as images, arrays of vectors, and structured and unstructured
grids. You can also mix and match them in HDF5 files according to your needs.

%package devel
Summary: HDF5 development files
Requires: %{name}%{?_isa} = %{version}-%{release}
Requires: libaec-devel%{?_isa}
Requires: zlib-devel%{?_isa}
Requires: gcc-gfortran%{?_isa}
%description devel
HDF5 development headers and libraries.

%if %{with java}
%package -n java-hdf5
Summary: HDF5 java library
Requires: %{name}%{?_isa} = %{version}-%{release}
Requires:  slf4j
Obsoletes: jhdf5 < 3.3.2^
%description -n java-hdf5
HDF5 java library
%endif

%package static
Summary: HDF5 static libraries
Requires: %{name}-devel = %{version}-%{release}
%description static
HDF5 static libraries.

%if %{with_mpich}
%package mpich
Summary: HDF5 mpich libraries
BuildRequires: mpich-devel
Provides: %{name}-mpich = %{_hdf5_compat_version}
Provides: %{name}-mpich%{?_isa} = %{_hdf5_compat_version}
%description mpich
HDF5 parallel mpich libraries

%package mpich-devel
Summary: HDF5 mpich development files
Requires: %{name}-mpich%{?_isa} = %{version}-%{release}
Requires: libaec-devel%{?_isa}
Requires: zlib-devel%{?_isa}
Requires: mpich-devel%{?_isa}
%description mpich-devel
HDF5 parallel mpich development files

%package mpich-static
Summary: HDF5 mpich static libraries
Requires: %{name}-mpich-devel%{?_isa} = %{version}-%{release}
Provides: %{name}-mpich2-static = %{version}-%{release}
Obsoletes: %{name}-mpich2-static < 1.8.11-4
%description mpich-static
HDF5 parallel mpich static libraries
%endif

%prep

%autosetup -a 2 -n %{name}-%{version}%{?snaprel} -p1

%if %{with java}
find . -name "*.jar" -delete
ln -s $(build-classpath hamcrest/core) java/lib/hamcrest-core.jar
ln -s $(build-classpath junit) java/lib/org.junit.jar
junit_ver=$(sed -n '/<version>/{s/^.*>\([0-9]\.[0-9.]*\)<.*/\1/;p;q}' /usr/share/maven-poms/junit.pom)
sed -i -e "s/JUnit version .*/JUnit version $junit_ver/" java/test/testfiles/JUnit-*.txt
ln -s $(build-classpath slf4j/api) java/lib/slf4j-api-2.0.16.jar
ln -s $(build-classpath slf4j/nop) java/lib/ext/slf4j-nop-2.0.16.jar
ln -s $(build-classpath slf4j/simple) java/lib/ext/slf4j-simple-2.0.16.jar
export JAVA_HOME=%{java_home}
%endif

sed -i -e '/^STATIC_AVAILABLE=/s/=.*/=no/' */*/h5[cf]*.in

%conf
%if %{with java}
export JAVA_HOME=%{java_home}
%endif
%global cmake_opts \\\
  -DH5_DEFAULT_PLUGINDIR=%{plugin_dir} \\\
  -DHDF5_BUILD_FORTRAN:BOOL=ON \\\
  -DHDF5_BUILD_HL_LIB:BOOL=ON \\\
  -DHDF5_BUILD_TOOLS:BOOL=ON \\\
  -DHDF5_ENABLE_SZIP_SUPPORT:BOOL=ON \\\
  -DHDF5_ENABLE_ZLIB_SUPPORT:BOOL=ON \\\
  -DBUILD_TESTING:BOOL=ON \\\
%{nil}

export CC=gcc
export CXX=g++
export FC=gfortran
mkdir build-serial
pushd build-serial
%cmake .. \
  %{cmake_opts} \
  ${libopt} \
  -DHDF5_BUILD_CPP_LIB:BOOL=ON \
%ifnarch %{ix86}
  -DHDF5_BUILD_JAVA:BOOL=ON \
%endif
  -DHDF5_INSTALL_CMAKE_DIR=%{_lib}/cmake/%{name} \
  -DHDF5_INSTALL_DATA_DIR=share/%{name} \
  -DHDF5_INSTALL_JAR_DIR=%{_jnidir} \
  -DHDF5_INSTALL_JNI_LIB_DIR=%{_lib}/%{name} \
  -DHDF5_INSTALL_LIB_DIR=%{_lib} \
  -DHDF5_INSTALL_MODULE_DIR=%{_fmoddir}
popd

export CC=mpicc
export CXX=mpicxx
export FC=mpif90
for mpi in %{?mpi_list}
do
  mkdir $mpi
  pushd $mpi
  module load mpi/$mpi-%{_arch}
  export FCFLAGS="%{build_fflags} -I$MPI_FORTRAN_MOD_DIR"
  export FFLAGS="%{build_fflags} -I$MPI_FORTRAN_MOD_DIR"
  %cmake .. \
    %{cmake_opts} \
    ${libopt} \
    -DMPIEXEC_MAX_NUMPROCS=4 \
    -DHDF5_ENABLE_PARALLEL:BOOL=ON \
    -DHDF5_INSTALL_LIB_DIR=%{_lib}/$mpi/lib \
    -DHDF5_INSTALL_BIN_DIR=%{_lib}/$mpi/bin \
    -DHDF5_INSTALL_INCLUDE_DIR=include/$mpi-%{_arch} \
    -DHDF5_INSTALL_DATA_DIR=%{_lib}/$mpi/share/%{name} \
    -DHDF5_INSTALL_CMAKE_DIR=%{_lib}/$mpi/lib/cmake/%{name} \
    -DHDF5_INSTALL_MAN_DIR=%{_lib}/$mpi/share/man \
    -DHDF5_INSTALL_MODULE_DIR=%{_fmoddir}/$mpi
  module purge
  popd
done

%build

%if %{with java}
export JAVA_HOME=%{java_home}
%endif
pushd build-serial
%cmake_build
popd
for mpi in %{?mpi_list}
do
  pushd $mpi
  module load mpi/$mpi-%{_arch}
  %cmake_build
  module purge
  popd
done
%install
cd build-serial
%cmake_install
cd -
mkdir -p %{buildroot}%{plugin_dir}
for mpi in %{?mpi_list}
do
  pushd $mpi
  module load mpi/$mpi-%{_arch}
  %cmake_install
  mkdir -p %{buildroot}%{_libdir}/$mpi/hdf5/plugin
  module purge
  popd
done
%ifarch x86_64 ppc64 ia64 s390x sparc64 alpha
sed -i -e s/H5pubconf.h/H5pubconf-64.h/ ${RPM_BUILD_ROOT}%{_includedir}/H5public.h
mv ${RPM_BUILD_ROOT}%{_includedir}/H5pubconf.h \
   ${RPM_BUILD_ROOT}%{_includedir}/H5pubconf-64.h
for x in h5c++ h5cc h5fc
do
  mv ${RPM_BUILD_ROOT}%{_bindir}/${x} \
     ${RPM_BUILD_ROOT}%{_bindir}/${x}-64
  install -m 0755 %SOURCE1 ${RPM_BUILD_ROOT}%{_bindir}/${x}
done
%else
sed -i -e s/H5pubconf.h/H5pubconf-32.h/ ${RPM_BUILD_ROOT}%{_includedir}/H5public.h
mv ${RPM_BUILD_ROOT}%{_includedir}/H5pubconf.h \
   ${RPM_BUILD_ROOT}%{_includedir}/H5pubconf-32.h
for x in h5c++ h5cc h5fc
do
  mv ${RPM_BUILD_ROOT}%{_bindir}/${x} \
     ${RPM_BUILD_ROOT}%{_bindir}/${x}-32
  install -m 0755 %SOURCE1 ${RPM_BUILD_ROOT}%{_bindir}/${x}
done
%endif
mkdir -p %{buildroot}%{_rpmmacrodir}
cat >%{buildroot}%{_rpmmacrodir}/macros.hdf5 <<EOF
%%_hdf5_version %{_hdf5_compat_version}
%%_hdf5_plugin_dir %{plugin_dir}
EOF
mkdir -p %{buildroot}%{_mandir}/man1
rm -f debian/man/*gif* debian/man/h5redeploy.1
cp -p debian/man/*.1 %{buildroot}%{_mandir}/man1/
rm %{buildroot}%{_mandir}/man1/h5p[cf]c*.1
for mpi in %{?mpi_list}
do
  mkdir -p %{buildroot}%{_libdir}/${mpi}/share/man/man1
  cp -p debian/man/h5p[cf]c*.1 %{buildroot}%{_libdir}/${mpi}/share/man/man1/
done
%if %{with java}
rm %{buildroot}%{_jnidir}/slf*.jar
%oreon_autofiles java-hdf5 usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%endif
%check

%ifarch %{ix86} ppc64le
fail=0
%else
fail=1
%endif
cd build-serial
ctest -V %{?_smp_mflags} || exit $fail
cd -
%ifarch %{ix86} ppc64le s390x
fail=0
%else
fail=1
%endif
export OMPI_MCA_rmaps_base_oversubscribe=1
export PRTE_MCA_rmaps_default_mapping_policy=:oversubscribe
export HDF5_ALARM_SECONDS=8000
for mpi in %{?mpi_list}
do
  if [ "$mpi-%{_arch}" != mpich-aarch64 -a "$mpi-%{_arch}" != mpich-ppc64le -a "$mpi-%{_arch}" != mpich-riscv64 ]
  then
    module load mpi/$mpi-%{_arch}
    cd build-serial
    ctest -V %{?_smp_mflags} || exit $fail
    cd -
    module purge
  fi
done
%files -f %{oreon_filedir}/main.list
%files -n hdf5-devel -f %{oreon_filedir}/hdf5-devel.list
%files -n java-hdf5 -f %{oreon_filedir}/java-hdf5.list
%files -n hdf5-static -f %{oreon_filedir}/hdf5-static.list
%files -n hdf5-mpich -f %{oreon_filedir}/hdf5-mpich.list
%files -n hdf5-mpich-devel -f %{oreon_filedir}/hdf5-mpich-devel.list
%files -n hdf5-mpich-static -f %{oreon_filedir}/hdf5-mpich-static.list

%changelog

%autochangelog
