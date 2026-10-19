%global source0_hash 39edf6790c4af25679ab46e361091f177d40ad8f8cfff1b4bf81e775fc59f0c1
Name:           scorep
Version:        10.1
Release:        1%{?dist}
Summary:        Scalable Performance Measurement Infrastructure for Parallel Codes
License:        BSD-3-Clause
URL:            http://www.vi-hps.org/projects/score-p/
Source0:        http://perftools.pages.jsc.fz-juelich.de/cicd/scorep/tags/scorep-%{version}/scorep-%{version}.tar.gz
Patch1:         gcc16.diff
Requires:       %{name}-libs%{?_isa} = %{version}-%{release}
Requires:       binutils-devel%{?_isa}
Requires:       cube-libs-devel%{?_isa} >= 4.9
Requires:       otf2-devel%{?_isa} >= 3.1
Requires:       papi-devel%{?_isa}
Requires:       ocl-icd-devel%{?_isa}
Requires:       opari2%{?_isa} >= 2.0.9
Requires:       gotcha-devel%{?_isa} >= 1.0.5
Requires:       libunwind-devel%{?_isa}
ExcludeArch: s390 s390x armv7hl i686
%global with_mpich 1
%global with_openmpi 1
%global mpi_list mpich
%global mpi_list %{?mpi_list} openmpi
%global oshmem 1
%ifarch ppc64le
%endif
%undefine _ld_as_needed
%undefine _hardened_build
%global __requires_exclude_from ^%{_libdir}(/(openmpi|mpich)/lib)?/libscorep_.*|^%{_docdir}/.*$
%global desc \
The Score-P (Scalable Performance Measurement Infrastructure for\
Parallel Codes) measurement infrastructure is a highly scalable and\
easy-to-use tool suite for profiling and event trace recording of\
HPC applications.\
Reference DOI: 10.1007/978-3-642-31476-6_7
# oreon:deps
BuildRequires:  automake
BuildRequires:  binutils-devel
BuildRequires:  bison
BuildRequires:  chrpath
BuildRequires:  clang
BuildRequires:  clang-devel
BuildRequires:  cube-libs-devel
BuildRequires:  flex
BuildRequires:  gcc-c++
BuildRequires:  gcc-gfortran
BuildRequires:  gcc-plugin-devel
BuildRequires:  gotcha-devel(x86-64)
BuildRequires:  libtool
BuildRequires:  libunwind-devel
BuildRequires:  llvm-devel
BuildRequires:  make
BuildRequires:  mpich-devel
BuildRequires:  ocl-icd-devel
BuildRequires:  opari2
BuildRequires:  openmpi-devel
BuildRequires:  otf2-devel
BuildRequires:  papi-devel
# /oreon:deps
%description
%desc

%package        doc
Summary:        Documentation for %{name}
BuildArch:      noarch
%description    doc
The %{name}-doc package contains documentation for %{name}

%package libs
Summary:        Score-P runtime libraries
Requires:       %{name}-config%{?_isa} = %{version}-%{release}
%description libs
Score-P runtime libraries.

# This is relevant for Scalasca analysis, at least, without the libraries.
%package config
Summary:        Score-P configuration files
%description config
Score-P configuration files.

%package mpich
Summary:        Scalable Performance Measurement Infrastructure for Parallel Codes for mpich
BuildRequires:  mpich-devel
Requires:       %{name}-mpich-libs%{?_isa} = %{version}-%{release}
Requires:       cube-libs-devel%{?_isa} >= 4.9
Requires:       otf2-devel%{?_isa} >= 3.1
Requires:       papi-devel%{?_isa}
%description mpich
%desc

This package was compiled with mpich.

%package mpich-libs
Summary:        Score-P mpich runtime libraries
Requires:       %{name}-mpich-config%{?_isa} = %{version}-%{release}
%description mpich-libs
Score-P mpich runtime libraries.

%package mpich-config
Summary:        Score-P mpich configuration files
%description mpich-config
Score-P mpich configuration files.

%package openmpi
Summary:        Scalable Performance Measurement Infrastructure for Parallel Codes for openmpi
BuildRequires:  openmpi-devel
Requires:       %{name}-openmpi-libs%{?_isa} = %{version}-%{release}
Requires:       cube-libs-devel%{?_isa} >= 4.9
Requires:       otf2-devel%{?_isa} >= 3.1
Requires:       papi-devel%{?_isa}
%description openmpi
%desc

This package was compiled with openmpi.

%package openmpi-libs
Summary:        Score-P openmpi runtime libraries
Requires:       %{name}-openmpi-config%{?_isa} = %{version}-%{release}
%description openmpi-libs
Score-P openmpi runtime libraries.

%package openmpi-config
Summary:        Score-P openmpi configuration files
%description openmpi-config
Score-P openmpi configuration files.

%prep

%setup -q
%patch -P1 -p1 -b .gcc16
# Bundled libs in vendor/
rm -rf vendor/{opari2,otf2,cubew,cubelib}
mkdir bin
# configure expects llvm-config
ln -s %_bindir/llvm-config-%__isa_bits bin/llvm-config
pushd build-gcc-plugin
autoreconf
popd

%build

%define _lto_cflags %{nil}
%global _configure ../configure
%global configure_opts --enable-shared --disable-static --disable-silent-rules --with-libunwind=yes
cp /usr/lib/rpm/redhat/config.{sub,guess} build-config/
mkdir serial
cd serial
%configure %{configure_opts} --without-mpi --without-shmem
find -name Makefile -exec sed -r -i 's,-L%{_libdir}/?( |$),,g;s,-L/usr/lib/../%{_lib} ,,g' {} \;
%make_build V=1
cd -
for mpi in %{mpi_list}
do
  mkdir $mpi
  cd $mpi
  module load mpi/$mpi-%{_arch}
  %configure %{configure_opts} \
    --libdir=%{_libdir}/$mpi/lib \
    --bindir=%{_libdir}/$mpi/bin \
    --sbindir=%{_libdir}/$mpi/sbin \
    --datadir=%{_libdir}/$mpi/share \
    --includedir=%{_includedir}/$mpi-%{_arch} \
    --mandir=%{_libdir}/$mpi/share/man
  find -name Makefile -exec sed -r -i 's,-L%{_libdir}/?( |$),,g;s,-L/usr/lib/../%{_lib} ,,g' {} \;
  sed -i -e 's/HARDCODE_INTO_LIBS"]="1"/HARDCODE_INTO_LIBS"]="0"/' \
      -e "s/hardcode_into_libs='yes'/hardcode_into_libs='no'/" \
      build-backend/config.status
  %make_build V=1
  module purge
  cd -
done
%install
%make_install -C serial
for mpi in %{mpi_list}
do
  module load mpi/$mpi-%{_arch}
  %make_install -C $mpi
  module purge
done
find %{buildroot} -name '*.la' -exec rm -f {} ';'
find %{buildroot} -name '*.a' -delete
chrpath -d %{buildroot}%{_libdir}/*.so.* %{buildroot}%{_bindir}/scorep-score
chrpath -d %{buildroot}%{_libexecdir}/scorep/scorep-library-wrapper-generator
find %{buildroot} -name scorep.summary | xargs sed -i -e "s|\
no, missing plug-in headers, please install|\
yes, using the C++ compiler and -I$(%_bindir/gcc -print-file-name=plugin/include)|"
%ldconfig_scriptlets libs
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%check

%_openmpi_load
OMPI_MCA_rmaps_base_oversubscribe=1 \
make -C openmpi check V=1
%files -f %{oreon_filedir}/main.list
%files -n scorep-doc -f %{oreon_filedir}/scorep-doc.list
%files -n scorep-libs -f %{oreon_filedir}/scorep-libs.list
%files -n scorep-config -f %{oreon_filedir}/scorep-config.list
%files -n scorep-mpich -f %{oreon_filedir}/scorep-mpich.list
%files -n scorep-mpich-libs -f %{oreon_filedir}/scorep-mpich-libs.list
%files -n scorep-mpich-config -f %{oreon_filedir}/scorep-mpich-config.list
%files -n scorep-openmpi -f %{oreon_filedir}/scorep-openmpi.list
%files -n scorep-openmpi-libs -f %{oreon_filedir}/scorep-openmpi-libs.list
%files -n scorep-openmpi-config -f %{oreon_filedir}/scorep-openmpi-config.list

%changelog

%autochangelog
