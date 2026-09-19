%global source0_hash none

# Warning:
# Anyone editing this spec file please make sure the same spec file
# works on other fedora and epel releases, which are supported by this software.
# No quick Rawhide-only fixes will be allowed.

%if 0%{?fedora} >= 38
# openmpi segmentation fault on i686 bug #2142304
ExcludeArch: %{ix86} s390x
%else
# ga/nwchem most likely does not support s390x
# https://github.com/edoapra/fedpkg/issues/10
ExcludeArch: s390x
%endif

%if 0%{?el6} || 0%{?el7}
need libxc version > 3
%quit
%endif

%global upstream_name nwchem

%{?!major_version: %global major_version 7.3.1}
%{?!git_hash: %global git_hash e2869a2c81445f2edfd25bbae652d099fabb9a92}
%{?!ga_version: %global ga_version 5.8.2-1}

%if 0%{?fedora} >= 33 || 0%{?rhel} >= 9
%global blaslib flexiblas
%else
%global blaslib openblas
%endif

%ifarch %ix86 %arm
%global make64_to_32 0
%global NWCHEM_TARGET LINUX
%else
%global make64_to_32 1
# arch is x86_64
%global NWCHEM_TARGET LINUX64
%endif
# build with python support
%{?!PYTHON_SUPPORT: %global PYTHON_SUPPORT 1}

# static (a) or shared (so) libpython.*
%global BLASOPT -L%{_libdir} -l%{blaslib}
# from https://nwchemgit.github.io/ forum:
# BLAS_SIZE=4 is needed when the Blas library you are using have
# 32-bit integer arguments (de facto default)
%global BLAS_SIZE 4
%global LAPACK_LIB -L%{_libdir} -l%{blaslib}

Name:			nwchem
Version:		%{major_version}
Release:		1%{?dist}
Summary:		Delivering High-Performance Computational Chemistry to Science

# Automatically converted from old format: ECL 2.0 - review is highly recommended.
License:		ECL-2.0
URL:			https://nwchemgit.github.io/
# Nwchem changes naming convention of tarballs very often!
Source0:		https://github.com/nwchemgit/nwchem/archive/%{git_hash}.tar.gz

%global PKG_TOP ${RPM_BUILD_DIR}/%{name}-%{git_hash}

BuildRequires: make
BuildRequires:		patch
BuildRequires:		time

%if 0%{?fedora} >= 29 || 0%{?rhel} >= 9
BuildRequires:		python3-devel
%else
BuildRequires:		python2-devel
%endif

BuildRequires:		gcc-gfortran

BuildRequires:		%{blaslib}-devel
# https://pagure.io/releng/issue/12359
BuildRequires:		environment-modules
# Use openblas-serial instead of openblas-openmp, but it's unavailable on centos stream
# due to https://bugzilla.redhat.com/show_bug.cgi?id=2182460, so use a workaround of export OMP_NUM_THREADS=1
# See https://github.com/edoapra/fedpkg/issues/10#issuecomment-731855285
%if 0%{?fedora} >= 33 || 0%{?rhel} >= 9
BuildRequires:		flexiblas-openblas-openmp
Requires:		flexiblas-openblas-openmp
%endif
BuildRequires:		libxc-devel

%if 0%{?rhel} == 6
BuildRequires:		net-tools
%else
BuildRequires:		hostname
%endif

%if 0%{?fedora}
BuildRequires:		perl-interpreter
%else
BuildRequires:		perl
%endif
%if 0%{?fedora} >= 33
BuildRequires:		perl-File-Basename
%endif

BuildRequires:		openssh-clients

Requires:		openssh-clients
Requires:		%{name}-common = %{version}-%{release}

%global nwchem_desc_base \
NWChem aims to provide its users with computational chemistry tools that are\
scalable both in their ability to treat large scientific computational\
chemistry problems efficiently, and in their use of available parallel\
computing resources from high-performance parallel supercomputers to\
conventional workstation clusters.

%global nwchem_desc_cite \
Please cite the following reference when\
publishing results obtained with NWChem:\
M. Valiev, E.J. Bylaska, N. Govind, K. Kowalski, T.P. Straatsma,\
H.J.J. van Dam, D. Wang, J. Nieplocha, E. Apra, T.L. Windus, W.A. de Jong,\
"NWChem: a comprehensive and scalable open-source solution for\
large scale molecular simulations" Comput. Phys. Commun. 181, 1477 (2010)

%description
%{nwchem_desc_base}
%{nwchem_desc_cite}

There is currently no serial version built.

%package openmpi
Summary:		%{upstream_name} - openmpi version
BuildRequires:		openmpi-devel
BuildRequires:		ga-openmpi-devel >= %{ga_version}
Requires:		%{name} = %{version}-%{release}
Requires:		openmpi
%if 0%{?el7} 
Requires:		ga-openmpi
%endif

%description openmpi
%{nwchem_desc_base}
%{nwchem_desc_cite}

This package contains the openmpi version.

%package mpich
Summary:		%{upstream_name} - mpich version
BuildRequires:		mpich-devel
BuildRequires:		ga-mpich-devel >= %{ga_version}
Requires:		%{name} = %{version}-%{release}
Requires:		mpich
%if 0%{?el7} 
Requires:		ga-mpich
%endif

%description mpich
%{nwchem_desc_base}
%{nwchem_desc_cite}

This package contains the mpich version.

%package common
Summary:		%{upstream_name} - common files
BuildArch:		noarch

%description common
%{nwchem_desc_base}
%{nwchem_desc_cite}

This package contains the data files.

%prep
%setup -q -n %{name}-%{git_hash}

# See bundling discussion at https://github.com/nwchemgit/nwchem/discussions/905
# remove the whole src/libext
mv src/libext/GNUmakefile /tmp/GNUmakefile.libext
rm -rf src/libext/*
mv /tmp/GNUmakefile.libext src/libext/GNUmakefile

# remove bundling of BLAS/LAPACK
mv src/blas/GNUmakefile /tmp/GNUmakefile.blas
mv src/lapack/GNUmakefile /tmp/GNUmakefile.lapack
rm -rf src/blas/* src/lapack/*
mv /tmp/GNUmakefile.blas src/blas/GNUmakefile
mv /tmp/GNUmakefile.lapack src/lapack/GNUmakefile
sed -e 's|CORE_SUBDIRS_EXTRA +=.*|CORE_SUBDIRS_EXTRA +=|g' -i src/config/makefile.h
sed -e 's|CORE_SUBDIRS_EXTRA =.*|CORE_SUBDIRS_EXTRA =|g' -i src/config/makefile.h
sed -e 's|-llapack||g' -i src/config/makefile.h
sed -e 's|-lblas||g' -i src/config/makefile.h
sed -e 's|-lnwclapack||g' -i src/config/makefile.h
sed -e 's|-lnwcblas||g' -i src/config/makefile.h

# remove references to tcsh
rm -f QA/doqm.bat
rm -f src/config/sngl_to_dbl
rm -f src/config/*depend
rm -f src/config/*blas
rm -f src/config/dbl_to_sngl
rm -rf src/tools/ga-*

# remove compiler native arch optimizations, see
# https://bugzilla.redhat.com/show_bug.cgi?id=1347788
# https://bugs.debian.org/cgi-bin/bugreport.cgi?bug=767481
sed -i 's|-march=native||' src/config/makefile.h
sed -i 's|-mtune=native|-mtune=generic|' src/config/makefile.h
sed -i 's|-mfpmath=sse||' src/config/makefile.h
sed -i 's|-msse3||' src/config/makefile.h

# remove slow tests
# https://github.com/nwchemgit/nwchem/issues/895
sed -i '/libxc_waterdimer_bmk/d' QA/dolibxctests.mpi

%build
# base settings
echo "# see https://nwchemgit.github.io/Compiling-NWChem.html" > settings.sh
echo export NWCHEM_TARGET=%{NWCHEM_TARGET} >> settings.sh
echo export CC="'gcc'" >> settings.sh
echo export FC=gfortran >> settings.sh
# https://nwchemgit.github.io/Special_AWCforum/st/id1590/Nwchem-dev.revision26704-src.201....html
%if 0%{?fedora} >= 21 || 0%{?rhel} >= 9
echo export USE_ARUR=TRUE >> settings.sh
%endif
%if 0%{?rhel} >= 7
echo export USE_ARUR=TRUE >> settings.sh
%endif
echo export USE_NOFSCHECK=TRUE >> settings.sh
# https://github.com/nwchemgit/nwchem/issues/272
echo export USE_NOIO=TRUE >> settings.sh
echo export NWCHEM_FSCHECK=N >> settings.sh
echo export LARGE_FILES=TRUE >> settings.sh
echo export MRCC_THEORY=Y >> settings.sh
echo export EACCSD=Y >> settings.sh
echo export IPCCSD=Y >> settings.sh
echo export CCSDTQ=Y >> settings.sh
echo export CCSDTLR=Y >> settings.sh
echo export NWCHEM_LONG_PATHS=Y >> settings.sh
# https://github.com/nwchemgit/nwchem/issues/723
echo unset USE_LIBXC >> settings.sh
echo export LIBXC_LIB="'%{_libdir}'" >> settings.sh
echo export LIBXC_INCLUDE="'%{_includedir}'" >> settings.sh
echo export LIBXC_MODDIR="'%{_libdir}/gfortran/modules'" >> settings.sh
echo export NO_NWPWXC_VDW3A=1 >> settings.sh
# https://github.com/nwchemgit/nwchem/issues/1189
echo export SCALAPACK_SIZE=4 >> settings.sh
echo export USE_HWOPT=n >> settings.sh
#
echo export HAS_BLAS=yes >> settings.sh
echo export BLASOPT="'%{BLASOPT}'" >> settings.sh
echo export BLAS_SIZE="'%{BLAS_SIZE}'" >> settings.sh
echo export LAPACK_LIB="'%{LAPACK_LIB}'" >> settings.sh
echo export MAKE='%{__make}' >> settings.sh
%if 0%{?PYTHON_SUPPORT}
echo '$MAKE nwchem_config NWCHEM_MODULES="all python" 2>&1 | tee ../make_nwchem_config.log' > make.sh
%else
echo '$MAKE nwchem_config NWCHEM_MODULES="all" 2>&1 | tee ../make_nwchem_config.log' > make.sh
%endif
%if 0%{?make64_to_32}
echo '$MAKE 64_to_32 2>&1 | tee ../make_64_to_32.log' >> make.sh
echo 'export MAKEOPTS="USE_64TO32=y"' >> make.sh
%else
echo 'export MAKEOPTS=""' >> make.sh
%endif
# final make (log of ~200MB, don't write it)
echo '$MAKE ${MAKEOPTS} 2>&1' >> make.sh # | tee ../make.log' >> make.sh

# Have to do off-root builds to be able to build many versions at once
mv src src.orig

# To avoid replicated code define a macro
%global dobuild() \
cd src&& \
cp -p ../settings.sh ../compile$MPI_SUFFIX.sh&& \
echo export USE_MPI=y >> ../compile$MPI_SUFFIX.sh&& \
echo export USE_MPIF=y >> ../compile$MPI_SUFFIX.sh&& \
echo export USE_MPIF4=y >> ../compile$MPI_SUFFIX.sh&& \
echo export SCALAPACK="'-L$MPI_LIB -lscalapack'" >> ../compile$MPI_SUFFIX.sh&& \
echo export MPIEXEC=$MPI_BIN/mpiexec >> ../compile$MPI_SUFFIX.sh&& \
echo export LD_LIBRARY_PATH=$MPI_LIB >> ../compile$MPI_SUFFIX.sh&& \
echo export EXTERNAL_GA_PATH=$MPI_HOME >> ../compile$MPI_SUFFIX.sh&& \
cat ../make.sh >> ../compile$MPI_SUFFIX.sh&& \
%{__sed} -i "s|.log|$MPI_SUFFIX.log|g" ../compile$MPI_SUFFIX.sh&& \
cat ../compile$MPI_SUFFIX.sh&& \
sh ../compile$MPI_SUFFIX.sh&& \
mv ../bin/%{NWCHEM_TARGET}/%{name} ../bin/%{NWCHEM_TARGET}/%{name}_binary$MPI_SUFFIX&& \
echo '#!/bin/bash' >  ../bin/%{NWCHEM_TARGET}/%{name}$MPI_SUFFIX&& \
echo 'export FLEXIBLAS=openblas-openmp' >>  ../bin/%{NWCHEM_TARGET}/%{name}$MPI_SUFFIX&& \
echo -n "%{name}_binary$MPI_SUFFIX " >>  ../bin/%{NWCHEM_TARGET}/%{name}$MPI_SUFFIX&& \
echo '"$@"' >>  ../bin/%{NWCHEM_TARGET}/%{name}$MPI_SUFFIX&& \
chmod 755  ../bin/%{NWCHEM_TARGET}/%{name}$MPI_SUFFIX&& \
cat ../bin/%{NWCHEM_TARGET}/%{name}$MPI_SUFFIX&& \
NWCHEM_TARGET=%{NWCHEM_TARGET} %{__make} BLAS_SIZE=%{BLAS_SIZE} USE_INTERNALBLAS=1 USE_MPI=y clean&& \
cd ..

# build openmpi version
cp -rp src.orig src
%{_openmpi_load}
%dobuild
%{_openmpi_unload}

rm -rf src

cp -rp src.orig src
# build mpich version
%{_mpich_load}
%dobuild
%{_mpich_unload}

# leave last src build for debuginfo

rm -f make.sh settings.sh

cat <<EOF > %{PKG_TOP}/%{name}.sh
# NOTE: This is an automatically-generated file!  (generated by the
# %%{name} RPM).  Any changes made here will be lost if the RPM is
# uninstalled or upgraded.

# must end with slash!
PA=%{_datadir}/%{name}/libraries/

case \$NWCHEM_BASIS_LIBRARY in
*\${PA}*);;
*) NWCHEM_BASIS_LIBRARY=\${PA};;
esac
export NWCHEM_BASIS_LIBRARY

# must end with slash!
PA=%{_datadir}/%{name}/libraryps/

case \$NWCHEM_NWPW_LIBRARY in
*\${PA}*);;
*) NWCHEM_NWPW_LIBRARY=\${PA};;
esac
export NWCHEM_NWPW_LIBRARY

EOF

cat <<EOF > %{PKG_TOP}/%{name}.csh
# NOTE: This is an automatically-generated file!  (generated by the
# %%{name} RPM).  Any changes made here will be lost if the RPM is
# uninstalled or upgraded.

# must end with slash!
set PA=%{_datadir}/%{name}/libraries/

if (\$?NWCHEM_BASIS_LIBRARY) then
if ("\$NWCHEM_BASIS_LIBRARY" !~ *\${PA}*) then
	setenv NWCHEM_BASIS_LIBRARY \${PA}
endif
else
setenv NWCHEM_BASIS_LIBRARY \${PA}
endif

unset PA

# must end with slash!
set PA=%{_datadir}/%{name}/libraryps/

if (\$?NWCHEM_NWPW_LIBRARY) then
if ("\$NWCHEM_NWPW_LIBRARY" !~ *\${PA}*) then
	setenv NWCHEM_NWPW_LIBRARY \${PA}
endif
else
setenv NWCHEM_NWPW_LIBRARY \${PA}
endif

unset PA

EOF

# create /etc/nwchemrc
cat <<EOF > %{PKG_TOP}/nwchemrc
# NOTE: This is an automatically-generated file!  (generated by the
# %%{name} RPM).  Any changes made here will be lost if the RPM is
# uninstalled or upgraded.

# data directory names must end with slash!
nwchem_basis_library %{_datadir}/%{name}/libraries/
nwchem_nwpw_library %{_datadir}/%{name}/libraryps/
ffield amber
amber_1 %{_datadir}/%{name}/amber_s/
amber_2 %{_datadir}/%{name}/amber_q/
amber_3 %{_datadir}/%{name}/amber_x/
amber_4 %{_datadir}/%{name}/amber_u/
spce %{_datadir}/%{name}/solvents/spce.rst
charmm_s %{_datadir}/%{name}/charmm_s/
charmm_x %{_datadir}/%{name}/charmm_x/
EOF

%install
mkdir -p $RPM_BUILD_ROOT%{_sysconfdir}

# *.bak files not allowed by rpmlint
for file in `find %{PKG_TOP} -name "*.bak"`; do
rm -f ${file}
done

# To avoid replicated code define a macro
%global doinstall() \
mkdir -p $RPM_BUILD_ROOT/$MPI_BIN&& \
install -p -m 755 %{PKG_TOP}/bin/%{NWCHEM_TARGET}/%{name}_binary$MPI_SUFFIX $RPM_BUILD_ROOT/$MPI_BIN&& \
install -p -m 755 %{PKG_TOP}/bin/%{NWCHEM_TARGET}/%{name}$MPI_SUFFIX $RPM_BUILD_ROOT/$MPI_BIN

# install openmpi version
%{_openmpi_load}
%doinstall
%{_openmpi_unload}

# install mpich version
%{_mpich_load}
%doinstall
%{_mpich_unload}

mkdir -p $RPM_BUILD_ROOT%{_datadir}/%{name}

cp -rp %{PKG_TOP}/src/data/* $RPM_BUILD_ROOT%{_datadir}/%{name}
cp -rp %{PKG_TOP}/src/basis/libraries $RPM_BUILD_ROOT%{_datadir}/%{name}
cp -rp %{PKG_TOP}/src/nwpw/libraryps $RPM_BUILD_ROOT%{_datadir}/%{name}
rm -f $RPM_BUILD_ROOT%{_datadir}/%{name}/libraryps/{*MakeFile,*.fh,*.F,dependencies,include_stamp}

# env scripts
install -p -m 444 %{PKG_TOP}/*.*sh $RPM_BUILD_ROOT%{_datadir}/%{name}
install -p -m 444 %{PKG_TOP}/nwchemrc $RPM_BUILD_ROOT%{_datadir}/%{name}
install -p -m 444 %{PKG_TOP}/nwchemrc $RPM_BUILD_ROOT%{_sysconfdir}
mkdir -p $RPM_BUILD_ROOT%{_sysconfdir}/profile.d
install -p -m 444 %{PKG_TOP}/%{name}*.*sh $RPM_BUILD_ROOT%{_sysconfdir}/profile.d

# To avoid: "Found '/tmp/rpmbuild/build/' in installed files; aborting"
for file in `find %{PKG_TOP} -name "*.log"`; do
%{__sed} -i "s|$RPM_BUILD_ROOT||g" ${file}
done
for file in `find %{PKG_TOP} -name "*.sh"`; do
%{__sed} -i "s|$RPM_BUILD_ROOT||g" ${file}
done

%check
export NWCHEM_TARGET=%{NWCHEM_TARGET}
# data directory names must end with slash!
export NWCHEM_BASIS_LIBRARY=$RPM_BUILD_ROOT%{_datadir}/%{name}/libraries/
export NWCHEM_NWPW_LIBRARY=$RPM_BUILD_ROOT%{_datadir}/%{name}/libraryps/

mv QA QA.orig.orig
cp -rp QA.orig.orig QA.orig

export NPROC=2 # test on 2 cores
export FLEXIBLAS=openblas-openmp

%if 0%{?el6}
export TIMEOUT_OPTS='3600'
%else
export TIMEOUT_OPTS='--preserve-status --kill-after 10 2700'
%endif

# To avoid replicated code define a macro
%global docheck() \
cp -rp QA.orig QA&& \
cd QA&& \
export LD_LIBRARY_PATH=${MPI_LIB}&& \
export PATH=%{PKG_TOP}/bin/$NWCHEM_TARGET:${MPI_BIN}:${PATH}&& \
export MPIRUN_PATH=${MPI_BIN}/mpiexec&& \
export MPIRUN_NPOPT="-np" && \
export USE_LIBXC=True && \
export NWCHEM_EXECUTABLE=%{PKG_TOP}/bin/$NWCHEM_TARGET/nwchem$MPI_SUFFIX&& \
time timeout ${TIMEOUT_OPTS} ./doafewqmtests.mpi ${NPROC} 2>&1 < /dev/null | tee ../doafewqmtests.mpi.${NPROC}$MPI_SUFFIX.log&& \
mv testoutputs ../testoutputs.doafewqmtests.mpi.${NPROC}$MPI_SUFFIX.log&& \
time timeout ${TIMEOUT_OPTS} ./dolibxctests.mpi ${NPROC} 2>&1 < /dev/null | tee ../dolibxctests.mpi.${NPROC}$MPI_SUFFIX.log&& \
mv testoutputs ../testoutputs.dolibxctests.mpi.${NPROC}$MPI_SUFFIX.log&& \
BUILD_LOG=../doafewqmtests.mpi.${NPROC}$MPI_SUFFIX.log&& \
TESTOUTPUTS=../testoutputs.doafewqmtests.mpi.${NPROC}$MPI_SUFFIX.log&& \
ls -al ${TESTOUTPUTS}&& \
for f in $(diff <(grep "Running tests/" ${BUILD_LOG}) <(grep -E "Running tests/|verifying output ... OK" ${BUILD_LOG} | grep "verifying output" -B 1 | grep Running) | grep Running | cut -d' ' -f 4); do printf '#%.0s' {1..80} && echo && NAME=$(basename ${f}) && echo ${TESTOUTPUTS}/${NAME}.out && printf '#%.0s' {1..80} && echo && cat ${TESTOUTPUTS}/${NAME}.out && printf '#%.0s' {1..80} && echo && if test -r ${TESTOUTPUTS}/${NAME}.out.nwparse; then cat ${TESTOUTPUTS}/${NAME}.out.nwparse; else cat ${TESTOUTPUTS}/${NAME}.err; fi; done&& \
BUILD_LOG=../dolibxctests.mpi.${NPROC}$MPI_SUFFIX.log&& \
TESTOUTPUTS=../testoutputs.dolibxctests.mpi.${NPROC}$MPI_SUFFIX.log&& \
ls -al ${TESTOUTPUTS}&& \
for f in $(diff <(grep "Running tests/" ${BUILD_LOG}) <(grep -E "Running tests/|verifying output ... OK" ${BUILD_LOG} | grep "verifying output" -B 1 | grep Running) | grep Running | cut -d' ' -f 4); do printf '#%.0s' {1..80} && echo && NAME=$(basename ${f}) && echo ${TESTOUTPUTS}/${NAME}.out && printf '#%.0s' {1..80} && echo && cat ${TESTOUTPUTS}/${NAME}.out && printf '#%.0s' {1..80} && echo && if test -r ${TESTOUTPUTS}/${NAME}.out.nwparse; then cat ${TESTOUTPUTS}/${NAME}.out.nwparse; else cat ${TESTOUTPUTS}/${NAME}.err; fi; done&& \
cd ..&& \
rm -rf QA

# check openmpi version
%{_openmpi_load}
export OMPI_MCA_btl=^uct
export OMPI_MCA_btl_base_warn_component_unused=0
%docheck
%{_openmpi_unload}

%{_mpich_load}
%docheck
%{_mpich_unload}

# restore QA
mv QA.orig QA

%files

%files common
%doc LICENSE*
%{_datadir}/%{name}
%config(noreplace) %{_sysconfdir}/profile.d/%{name}*.*sh
%config(noreplace) %{_sysconfdir}/nwchemrc

%files openmpi
%{_libdir}/openmpi%{?_opt_cc_suffix}/bin/%{name}_binary_openmpi
%{_libdir}/openmpi%{?_opt_cc_suffix}/bin/%{name}_openmpi

%files mpich
%{_libdir}/mpich%{?_opt_cc_suffix}/bin/%{name}_binary_mpich
%{_libdir}/mpich%{?_opt_cc_suffix}/bin/%{name}_mpich

%changelog
%autochangelog
