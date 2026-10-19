%global source0_hash 60946e3d84f16370b5d8a9c8235b2af6c188d0897787afef4cbabc355c2547ff
%global commit 3cb6f2cd61a5d482611d85c47dcb61f8d51d50ba
Name:           OpenMolcas
Version:        26.06
Release:        1%{?dist}
Summary:        A multiconfigurational quantum chemistry software package
License:        LGPL-2.1-only
URL:            https://gitlab.com/Molcas/OpenMolcas
Source0:        https://gitlab.com/Molcas/OpenMolcas/-/archive/v%{version}/%{name}-%{version}.tar.bz2
Patch0:         OpenMolcas-23.06-fedora.patch
Patch1:         OpenMolcas-19.11-pymodule.patch
Patch3:         https://gitlab.com/Molcas/OpenMolcas/-/merge_requests/803.patch
ExclusiveArch:  x86_64 aarch64 ppc64le s390x
Requires:       python3-pyparsing
Requires:       python3-setuptools
Requires:       CheMPS2
# oreon:deps
BuildRequires:  CheMPS2-devel
BuildRequires:  cmake
BuildRequires:  gcc-gfortran
BuildRequires:  hdf5-devel
BuildRequires:  libxc-devel
BuildRequires:  make
BuildRequires:  pkgconfig(flexiblas)
BuildRequires:  python3-devel
BuildRequires:  python3-pyparsing
BuildRequires:  python3-setuptools
# /oreon:deps
%description
OpenMolcas is a quantum chemistry software package developed by
scientists and intended to be used by scientists. It includes programs
to apply many different electronic structure methods to chemical
systems, but its key feature is the multiconfigurational approach,
with methods like CASSCF and CASPT2.

OpenMolcas is not a fork or reimplementation of Molcas, it is a large
part of the Molcas codebase that has been released as free and
open-source software (FOSS) under the Lesser GNU Public License
(LGPL). Some parts of Molcas remain under a different license by
decision of their authors (or impossibility to reach them), and are
therefore not included in OpenMolcas.

%prep

%setup -q -n %{name}-v%{version}-%{commit}
%patch -P0 -p1 -b .fedora
%patch -P1 -p1 -b .pymodule
%patch -P3 -p1 -b .intprocarg

# Name of OpenBLAS library to use is
%if 0%{?__isa_bits} == 64
%endif
%if 0%{?__isa_bits} == 64
sed -i 's|@OPENBLAS_LIBRARY@|openblaso64|g' CMakeLists.txt
%else
sed -i 's|@OPENBLAS_LIBRARY@|openblaso|g' CMakeLists.txt
%endif

# Location python modules are installed
sed -i 's|@MOLCAS_PYTHON@|%{_libdir}/%{name}/python|g' Tools/pymolcas/pymolcas.py
# Fix shebangs
for f in Tools/pymolcas/*.py; do
    sed -i 's|#!/usr/bin/env python|#!/usr/bin/python3|g' $f
done

%build

export CC=gcc
export FC=gfortran
export CFLAGS="%{optflags} -fopenmp -std=gnu99 -fPIC -Wtrampolines"
export FFLAGS="%{optflags} -cpp -fopenmp -fdefault-integer-8 -fPIC -I%{_libdir}/gfortran/modules -Wtrampolines"
%cmake -DCMAKE_INSTALL_PREFIX:PATH=%{_libdir}/%{name}/ \
       -DLINALG=OpenBLAS -DOPENMP=ON -DHDF5=ON -DCHEMPS2=ON \
       -DEXTERNAL_LIBXC=%{_usr} -S . -B %{_host}
%make_build -C %{_host}
%install
%{make_install} -C %{_host}
mkdir -p %{buildroot}%{_sysconfdir}/profile.d
cat > %{buildroot}%{_sysconfdir}/profile.d/%{name}.sh <<EOF
export MOLCAS=%{_libdir}/%{name}
export PATH=\${PATH}:\${MOLCAS}/bin:\${MOLCAS}/sbin
EOF
cat > %{buildroot}%{_sysconfdir}/profile.d/%{name}.csh <<EOF
setenv MOLCAS %{_libdir}/%{name}
export PATH \${PATH}:\${MOLCAS}/bin:\${MOLCAS}/sbin
EOF
mkdir -p %{buildroot}%{_libdir}/%{name}/python
for f in $(cd Tools/pymolcas; ls *.py|grep -v pymolcas.py); do
    cp -p Tools/pymolcas/${f} %{buildroot}%{_libdir}/%{name}/python
done
mkdir -p %{buildroot}%{_bindir} 
cp -p Tools/pymolcas/pymolcas.py %{buildroot}%{_bindir}/pymolcas
%oreon_autofiles main

%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
