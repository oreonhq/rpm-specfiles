%global source0_hash 80724ee337d3d48af559342ee090d883c90662d2d60a1c5219a6a18c9bd32d6c
Name:           mrchem
Version:        1.1.4
Release:        1%{?dist}
Summary:        A numerical real-space code for molecular electronic structure calculations
License:        LGPL-3.0-or-later
URL:            https://github.com/MRChemSoft/mrchem/
Source0:        https://github.com/MRChemSoft/mrchem/archive/v%{version}/%{name}-%{version}.tar.gz
Patch0:         mrchem-1.0.2-eigen3.patch
Patch1:         mrchem-1.0.2-pythonpath.patch
Patch2:         mrchem-1.1.0-rpath.patch
Patch3:         mrchem-1.1.2-object.patch
Patch4:         mrchem-1.1.4-pyparsing.patch
Patch5:         mrchem-1.1.4-ompnamespace.patch
ExcludeArch:    s390x
ExcludeArch:    ppc64le
Requires:       %{name}-data = %{version}-%{release}
Requires:       python3-pyparsing
# oreon:deps
BuildRequires:  catch2-devel
BuildRequires:  cmake
BuildRequires:  eigen3-devel
BuildRequires:  eigen3-static
BuildRequires:  gcc-c++
BuildRequires:  json-devel
BuildRequires:  make
BuildRequires:  mrcpp-devel
BuildRequires:  python3-devel
BuildRequires:  python3-pyparsing
BuildRequires:  xcfun-devel
# /oreon:deps
%description
MRChem is a numerical real-space code for molecular electronic
structure calculations within the self-consistent field (SCF)
approximations of quantum chemistry (Hartree-Fock and Density
Functional Theory).

%package devel
Summary:        Development headers and libraries for mrchem
Provides:       %{name}-static%{?_isa} = %{version}-%{release}
Requires:       %{name}%{?_isa} = %{version}-%{release}
%description devel
MRChem is a numerical real-space code for molecular electronic
structure calculations within the self-consistent field (SCF)
approximations of quantum chemistry (Hartree-Fock and Density
Functional Theory).

This package contains the development headers and libraries.

%package data
Summary:        Data files for MRchem
Requires:       %{name} = %{version}-%{release}
BuildArch:      noarch
Requires:       %{name} = %{version}-%{release}
%description data
MRChem is a numerical real-space code for molecular electronic
structure calculations within the self-consistent field (SCF)
approximations of quantum chemistry (Hartree-Fock and Density
Functional Theory).

This package contains the data files for MRChem.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q
# EPEL9 doesn't support the new patch syntax
%patch -P0 -p1 -b .eigen3
%patch -P1 -p1 -b .pythonpath
%patch -P2 -p1 -b .rpath
%patch -P3 -p1 -b .object
%patch -P4 -p1 -b .pyparsing
%patch -P5 -p1 -b .ompnamespace
# Remove bundled catch
rm -rf external/catch/
# Remove bundled pyparsing
rm -rf python/mrchem/input_parser/plumbing/pyparsing/

%build

export CXXFLAGS="%{optflags} -I/usr/include/catch2"
%cmake -DENABLE_ARCH_FLAGS=OFF -DENABLE_OPENMP=ON
%cmake_build
%install
%cmake_install
mkdir -p %{buildroot}%{python3_sitelib}
mv %{buildroot}/usr/lib/python/mrchem %{buildroot}%{python3_sitelib}
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%check

%global _smp_mflags "-j1"
export PYTHONPATH=$PWD/python/
cat > $PYTHONPATH/mrchem/config.py <<EOF
MRCHEM_VERSION = "%{version}"
MRCHEM_EXECUTABLE = "$PWD/redhat-linux-build/bin/mrchem.x"
MRCHEM_MODULE = "$PYTHONPATH"
EOF
%ctest
%files -f %{oreon_filedir}/main.list
%files -n mrchem-devel -f %{oreon_filedir}/mrchem-devel.list
%files -n mrchem-data -f %{oreon_filedir}/mrchem-data.list

%changelog

%autochangelog
