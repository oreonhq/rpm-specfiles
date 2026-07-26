%global source0_hash 80724ee337d3d48af559342ee090d883c90662d2d60a1c5219a6a18c9bd32d6c

Name:           mrchem
Version:        1.1.4
Release:        9%{?dist}
Summary:        A numerical real-space code for molecular electronic structure calculations
License:        LGPL-3.0-or-later
URL:            https://github.com/MRChemSoft/mrchem/
Source0:        https://github.com/MRChemSoft/mrchem/archive/v%{version}/%{name}-%{version}.tar.gz

# Relax Eigen3 version check, https://github.com/MRChemSoft/mrcpp/issues/186
Patch0:         mrchem-1.0.2-eigen3.patch
# The Python module is installed in the system directory in Fedora
Patch1:         mrchem-1.0.2-pythonpath.patch
# Disable use of rpath
Patch2:         mrchem-1.1.0-rpath.patch
# Re-enable creation of shared library
Patch3:         mrchem-1.1.2-object.patch
# Patch out bundled pyparsing
Patch4:         mrchem-1.1.4-pyparsing.patch
# Namespace fix
Patch5:         mrchem-1.1.4-ompnamespace.patch

# mrcpp doesn't build on s390x which is not supported by upstream (BZ#2035671)
ExcludeArch:    s390x
# mrcpp compile fails on ppc64le on RHEL and gives wrong results on Fedora 44 rawhide
ExcludeArch:    ppc64le

# We need the data files
Requires:       %{name}-data = %{version}-%{release}

BuildRequires:  make
BuildRequires:  cmake
BuildRequires:  gcc-c++
BuildRequires:  json-devel
BuildRequires:  eigen3-devel
BuildRequires:  python3-devel
BuildRequires:  xcfun-devel
BuildRequires:  mrcpp-devel
BuildRequires:  catch2-devel
BuildRequires:  python3-pyparsing

# Eigen3 is a header-only library; this is for dependency tracking
BuildRequires:  eigen3-static

# Due to removal of bundled library
Requires:       python3-pyparsing

%description
MRChem is a numerical real-space code for molecular electronic
structure calculations within the self-consistent field (SCF)
approximations of quantum chemistry (Hartree-Fock and Density
Functional Theory).

%package devel
Summary:        Development headers and libraries for mrchem
Provides:       %{name}-static%{?_isa} = %{version}-%{release}
# For license file
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
# For license file and to ensure data doesn't linger when main package is erased
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
# Move the python library to the correct location
mkdir -p %{buildroot}%{python3_sitelib}
mv %{buildroot}/usr/lib/python/mrchem %{buildroot}%{python3_sitelib}

%check
# Tests use OpenMP so we only want to run them one at a time
%global _smp_mflags "-j1"
# Where to find the python library
export PYTHONPATH=$PWD/python/
# Generate dummy config module for ctest
cat > $PYTHONPATH/mrchem/config.py <<EOF
MRCHEM_VERSION = "%{version}"
MRCHEM_EXECUTABLE = "$PWD/redhat-linux-build/bin/mrchem.x"
MRCHEM_MODULE = "$PYTHONPATH"
EOF
%ctest

%files
%license LICENSE
%doc CHANGELOG.md CONTRIBUTING.md README.md VERSION
%{python3_sitelib}/mrchem/
%{_bindir}/mrchem
%{_bindir}/mrchem.x

%files devel
%{_includedir}/MRChem/
%{_libdir}/libmrchem.a

%files data
%{_datadir}/MRChem/

%changelog
%autochangelog
