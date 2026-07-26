%global source0_hash 4c07315f3ca64e368f2228f22c3eb7d603e1317c2c4d73fc6637bb023f849933

# Omit internal libraries from dependency generation. We can omit all
# the provides
%global __provides_exclude_from ^%{python3_sitearch}/pyscf/lib/.*\\.so$
# but since we still need to pick up the dependencies for libcint,
# libxc, etc, we just have to filter out the internal libraries
%global __requires_exclude ^(libao2mo\\.so|libcgto\\.so|libcvhf\\.so|libfci\\.so|libnp_helper\\.so|libpbc\\.so|libdft\\.so).*$

%if 0%{?fedora} >= 33 || 0%{?rhel} >= 9
%global blaslib flexiblas
%global cmake_blas_flags -DBLA_VENDOR=FlexiBLAS
%else
%global blaslib openblas
%global blasvar o
%global cmake_blas_flags -DBLAS_LIBRARIES=%{_libdir}/lib%{blaslib}%{blasvar}.so
%endif

Name:           python-pyscf
Version:        2.12.1
Release:        1%{?dist}
Summary:        Python module for quantum chemistry
# Automatically converted from old format: ASL 2.0 - review is highly recommended.
License:        Apache-2.0
URL:            https://github.com/pyscf/pyscf/
Source0:        https://github.com/pyscf/pyscf/archive/v%{version}/pyscf-%{version}.tar.gz

# Disable rpath
Patch1:         pyscf-2.6.0-rpath.patch
# Need to load libpbc before libdft, https://github.com/pyscf/pyscf/pull/2273
Patch2:         2273.patch

# i686 disabled since this is a leaf package; see
# https://fedoraproject.org/wiki/Changes/EncourageI686LeafRemoval
#
# ppc64 doesn't appear to have floats beyond 64 bits, so ppc64 is
# disabled as per upstream's request as for the libcint package.
ExcludeArch:    %{ix86} %{power64}

BuildRequires:  %{blaslib}-devel
BuildRequires:  python3-devel
BuildRequires:  python3dist(setuptools)
BuildRequires:  python3-numpy
BuildRequires:  python3-scipy
BuildRequires:  python3-h5py
BuildRequires:  libxc-devel
# make sure we are using the newer version
BuildRequires:  libcint-devel >= 5.0.0
BuildRequires:  xcfun-devel
BuildRequires:  cmake
BuildRequires:  gcc-c++

# For tests
BuildRequires:  python3-pytest
BuildRequires:  python3-pytest-cov

%description
Python‐based simulations of chemistry framework (PySCF) is a
general‐purpose electronic structure platform designed from the ground
up to emphasize code simplicity, so as to facilitate new method
development and enable flexible computational workflows. The package
provides a wide range of tools to support simulations of finite‐size
systems, extended systems with periodic boundary conditions,
low‐dimensional periodic systems, and custom Hamiltonians, using
mean‐field and post‐mean‐field methods with standard Gaussian basis
functions. To ensure ease of extensibility, PySCF uses the Python
language to implement almost all of its features, while
computationally critical paths are implemented with heavily optimized
C routines. Using this combined Python/C implementation, the package
is as efficient as the best existing C or Fortran‐based quantum
chemistry programs.

%package -n python3-pyscf
Summary:        Python 3 module for quantum chemistry
# These are needed at runtime
Requires:  python3-numpy
Requires:  python3-scipy
Requires:  python3-h5py

%description -n python3-pyscf
Python‐based simulations of chemistry framework (PySCF) is a
general‐purpose electronic structure platform designed from the ground
up to emphasize code simplicity, so as to facilitate new method
development and enable flexible computational workflows. The package
provides a wide range of tools to support simulations of finite‐size
systems, extended systems with periodic boundary conditions,
low‐dimensional periodic systems, and custom Hamiltonians, using
mean‐field and post‐mean‐field methods with standard Gaussian basis
functions. To ensure ease of extensibility, PySCF uses the Python
language to implement almost all of its features, while
computationally critical paths are implemented with heavily optimized
C routines. Using this combined Python/C implementation, the package
is as efficient as the best existing C or Fortran‐based quantum
chemistry programs.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n pyscf-%{version}
%patch 1 -p1 -b .rpath
%patch 2 -p1 -b .2273

# Remove shebangs
find pyscf -name \*.py -exec sed -i '/#!\/usr\/bin\/env /d' '{}' \;
find pyscf -name \*.py -exec sed -i '/#!\/usr\/bin\/python/d' '{}' \;

%build
cd pyscf/lib
%cmake -DENABLE_LIBXC=ON -DBUILD_LIBXC=OFF -DENABLE_XCFUN=ON -DBUILD_XCFUN=OFF -DBUILD_LIBCINT=OFF %{cmake_blas_flags} -DCMAKE_SKIP_BUILD_RPATH=1
%cmake_build

%install
# Package doesn't have an install command, so we do this by hand.
# Install all python sources
for f in $(find pyscf -name \*.py); do
    install -D -p -m 644 $f %{buildroot}%{python3_sitearch}/$f
done
# Install data files (mostly basis sets)
for f in $(find pyscf -name \*.dat); do
    install -D -p -m 644 $f %{buildroot}%{python3_sitearch}/$f
done
for f in $(find pyscf -name \*.json); do
    install -D -p -m 644 $f %{buildroot}%{python3_sitearch}/$f
done
# Install compiled libraries
for f in $(find pyscf -name \*.so); do
    install -D -p -m 755 $f %{buildroot}%{python3_sitearch}/$f
done

%check
# Use the same test setup as upstream.
# Disabled for now since the tests don't pass; https://github.com/pyscf/pyscf/issues/3021
#bash .github/workflows/run_tests.sh

%files -n python3-pyscf
%license LICENSE
%doc CHANGELOG CONTRIBUTING.md FEATURES NOTICE README.md
%{python3_sitearch}/pyscf/

%changelog
%autochangelog
