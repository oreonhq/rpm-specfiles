%global source0_hash none

# git commit appears in the directory name of the tarball...
%global commit 3cb6f2cd61a5d482611d85c47dcb61f8d51d50ba

Name:           OpenMolcas
Version:        26.02
Release:        1%{?dist}
Summary:        A multiconfigurational quantum chemistry software package
License:        LGPL-2.1-only
URL:            https://gitlab.com/Molcas/OpenMolcas
Source0:        https://gitlab.com/Molcas/OpenMolcas/-/archive/v%{version}/%{name}-%{version}.tar.bz2

# Fedora patches
Patch0:         OpenMolcas-23.06-fedora.patch
# Read python modules from system directory
Patch1:         OpenMolcas-19.11-pymodule.patch
# Disable trampoline code that causes FTBFS in Fedora rawhide (f34)
Patch3:         https://gitlab.com/Molcas/OpenMolcas/-/merge_requests/803.patch

# OpenMolcas is only supported on 64-bit architectures
ExclusiveArch:  x86_64 aarch64 ppc64le s390x

BuildRequires:  make
BuildRequires:  cmake
BuildRequires:  gcc-gfortran
%if 0%{?fedora} >= 33
BuildRequires:  pkgconfig(flexiblas)
%else
BuildRequires:  openblas-devel
%endif
BuildRequires:  libxc-devel
BuildRequires:  hdf5-devel
BuildRequires:  CheMPS2-devel

# Required by runtime
%if 0%{?rhel} == 7
BuildRequires:  python2-devel
Requires:       pyparsing
%else
BuildRequires:  python3-devel
BuildRequires:  python3-setuptools
BuildRequires:  python3-pyparsing
Requires:       python3-pyparsing
Requires:       python3-setuptools
%endif

# CheMPS2 support at runtime (not linked, calls binary)
Requires:       CheMPS2

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
%if 0%{?fedora} >= 33
%if 0%{?__isa_bits} == 64
sed -i 's|@OPENBLAS_LIBRARY@|flexiblas64|g' CMakeLists.txt
%else
sed -i 's|@OPENBLAS_LIBRARY@|flexiblas|g' CMakeLists.txt
%endif
%else
%if 0%{?__isa_bits} == 64
sed -i 's|@OPENBLAS_LIBRARY@|openblaso64|g' CMakeLists.txt
%else
sed -i 's|@OPENBLAS_LIBRARY@|openblaso|g' CMakeLists.txt
%endif
%endif

# Location python modules are installed
sed -i 's|@MOLCAS_PYTHON@|%{_libdir}/%{name}/python|g' Tools/pymolcas/pymolcas.py
# Fix shebangs
%if 0%{?rhel} == 7
for f in Tools/pymolcas/*.py; do
    sed -i 's|#!/usr/bin/env python|#!/usr/bin/python2|g' $f
done
%else
for f in Tools/pymolcas/*.py; do
    sed -i 's|#!/usr/bin/env python|#!/usr/bin/python3|g' $f
done
%endif

%build
export CC=gcc
export FC=gfortran

export CFLAGS="%{optflags} -fopenmp -std=gnu99 -fPIC -Wtrampolines"
export FFLAGS="%{optflags} -cpp -fopenmp -fdefault-integer-8 -fPIC -I%{_libdir}/gfortran/modules -Wtrampolines"

# GCC10 compatibility
%if 0%{?fedora} > 31
export FFLAGS="$FFLAGS -fallow-argument-mismatch"
%endif

%cmake -DCMAKE_INSTALL_PREFIX:PATH=%{_libdir}/%{name}/ \
       -DLINALG=OpenBLAS -DOPENMP=ON -DHDF5=ON -DCHEMPS2=ON \
       -DEXTERNAL_LIBXC=%{_usr} -S . -B %{_host}
%make_build -C %{_host}

%install
%{make_install} -C %{_host}

mkdir -p %{buildroot}%{_sysconfdir}/profile.d
cat > %{buildroot}%{_sysconfdir}/profile.d/%{name}.sh <<EOF
# OpenMolcas root is
export MOLCAS=%{_libdir}/%{name}
export PATH=\${PATH}:\${MOLCAS}/bin:\${MOLCAS}/sbin
EOF
cat > %{buildroot}%{_sysconfdir}/profile.d/%{name}.csh <<EOF
# OpenMolcas root is
setenv MOLCAS %{_libdir}/%{name}
export PATH \${PATH}:\${MOLCAS}/bin:\${MOLCAS}/sbin
EOF

# Install the wrapper and its requirements
mkdir -p %{buildroot}%{_libdir}/%{name}/python

for f in $(cd Tools/pymolcas; ls *.py|grep -v pymolcas.py); do
    cp -p Tools/pymolcas/${f} %{buildroot}%{_libdir}/%{name}/python
done
mkdir -p %{buildroot}%{_bindir} 
cp -p Tools/pymolcas/pymolcas.py %{buildroot}%{_bindir}/pymolcas

%files
%license LICENSE
%doc CONTRIBUTORS.md
%{_sysconfdir}/profile.d/%{name}.*
%{_libdir}/%{name}
%{_bindir}/pymolcas

%changelog
%autochangelog
