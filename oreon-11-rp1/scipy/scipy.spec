# without means enabled
%bcond_with doc

# Pythran is an optional build dependency.
# When used, it makes some modules faster,
# but it is usually not available soon enough for new major Python versions.
%if 0%{?rhel} || 0%{?oreon}
%bcond_with pythran
%bcond_with pooch
%bcond_with tests
%else
%bcond_without pythran
%bcond_without pooch
%bcond_without tests
%endif

# The code is not safe to build with LTO
%global _lto_cflags %{nil}

%ifarch %{ix86}
# On i686, there is a confusion whether Fortran INTEGER should be
# translated as int or long.
# <https://github.com/scipy/scipy/issues/19993>
%global build_type_safety_c 2
%endif

# Set to pre-release version suffix if building pre-release, else %%{nil}
%global rcver %{nil}

%if 0%{?fedora} >= 33 || 0%{?rhel} >= 9 || 0%{?oreon}
%global blaslib flexiblas
%global blasvar %{nil}
%else
%global blaslib openblas
%global blasvar p
%endif

%global build_backend_args %{shrink:
    -Csetup-args=-Dblas=%{blaslib}%{blasvar}
    -Csetup-args=-Dlapack=%{blaslib}%{blasvar}
    %{!?with_pythran:-Csetup-args=-Duse-pythran=false}
}

Summary:    Scientific Tools for Python
Name:       scipy
Version:    1.16.2
Release:    3%{?dist}

# BSD-3-Clause -- whole package except:
# BSD-2-Clause -- scipy/_lib/_pep440.py
#                 scipy/_lib/decorator.py
#                 scipy/optimize/lbfgsb_src
#                 scipy/special/_ellip_harm.pxd
# MIT -- scipy/cluster/_optimal_leaf_ordering.pyx
#        scipy/io/_idl.py
#        scipy/linalg/_basic.py (in part)
#        scipy/optimize/_direct
#        scipy/optimize/_highs
#        scipy/optimize/_lbfgsb_py.py
#        scipy/optimize/_tnc.py
#        scipy/optimize/_trlib
#        scipy/optimize/tnc
#        scipy/special/Faddeeva.{cc,hh}
# BSL-1.0 -- scipy/_lib/boost_math
#            scipy/special/cephes
# Boehm-GC -- scipy/sparse/linalg/_dsolve/SuperLU
# Qhull -- scipy/spatial/qhull_src
# LicenseRef-Public-Domain -- scipy/odr/__odrpack.c
License:    BSD-3-Clause AND BSD-2-Clause AND MIT AND BSL-1.0 AND Boehm-GC AND Qhull AND LicenseRef-Public-Domain
Url:        https://scipy.org/
Source0:    https://github.com/scipy/scipy/releases/download/v%{version}/scipy-%{version}.tar.gz
# oreon url source checksums begin
%global source0_sha256 af029b153d243a80afb6eabe40b0a07f8e35c9adc269c019f364ad747f826a6b
%global source0_file scipy-1.16.2.tar.gz
# oreon url source checksums end

BuildRequires: %{blaslib}-devel
BuildRequires: gcc-gfortran, gcc-c++

BuildRequires:  pybind11-devel
BuildRequires:  python3-devel, python3-numpy-f2py

# for %%pyproject_buildrequires -p:
BuildRequires:  pyproject-rpm-macros >= 1.15

%ifarch %{power64}
# scipy segfaults with netlib/atlas on ppc64le
BuildRequires:  flexiblas-openblas-openmp
%endif

%if %{with doc}
BuildRequires:  python3-sphinx
BuildRequires:  python3-matplotlib
BuildRequires:  python3-numpydoc
%endif

%global _description %{expand:
Scipy is open-source software for mathematics, science, and
engineering. The core library is NumPy which provides convenient and
fast N-dimensional array manipulation. The SciPy library is built to
work with NumPy arrays, and provides many user-friendly and efficient
numerical routines such as routines for numerical integration and
optimization. Together, they run on all popular operating systems, are
quick to install, and are free of charge. NumPy and SciPy are easy to
use, but powerful enough to be depended upon by some of the world's
leading scientists and engineers.}

%description %_description

%package -n python3-scipy
Summary:    Scientific Tools for Python
Requires:   python3-numpy, python3-f2py
%if %{with pooch}
Requires:   python3-pooch
%endif
Provides:   bundled(arpack) = 3.9.1
Provides:   bundled(biasedurn)
Provides:   bundled(boost-math)
Provides:   bundled(coin-or-HiGHS) = 1.2
Provides:   bundled(direct)
Provides:   bundled(Faddeeva)
Provides:   bundled(id)
Provides:   bundled(l-bfgs-b) = 3.0
Provides:   bundled(LAPJVsp)
Provides:   bundled(python3-decorator) = 4.0.5
Provides:   bundled(python3-pep440)
Provides:   bundled(python3-pypocketfft) = bf2c431c21213b7c5e23c2f542009b0bd3ec1445
Provides:   bundled(qhull) = 2019.1
Provides:   bundled(SuperLU) = 5.2.0
Provides:   bundled(unuran) = 1.8.1
%description -n python3-scipy %_description

%if %{with doc}
%package -n python3-scipy-doc
Summary:    Scientific Tools for Python - documentation
Requires:   python3-scipy = %{version}-%{release}
%description -n python3-scipy-doc
HTML documentation for Scipy
%endif

%if %{with tests}
%package -n python3-scipy-tests
Summary:    Scientific Tools for Python - test files
Requires:   python3-scipy = %{version}-%{release}
Requires:   python3-pytest
%description -n python3-scipy-tests
Scipy test files
%endif

%prep
# oreon verify url source checksums begin
%(f=%{_sourcedir}/scipy-1.16.2.tar.gz; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "af029b153d243a80afb6eabe40b0a07f8e35c9adc269c019f364ad747f826a6b" || { echo "oreon: Source0 SHA256 mismatch for scipy-1.16.2.tar.gz" >&2; exit 1; })
# oreon verify url source checksums end
%autosetup -p1 -n %{name}-%{version}%{?rcver}

%if %{without pythran}
# Remove pythran dependency if not explicitly required
sed -i '/pythran/d' pyproject.toml
%else
# Relax it otherwise
sed -i 's/pythran>=0.14.0,<0.18.0/pythran>=0.14.0/' pyproject.toml
%endif
%if %{without pooch}
sed -i '/pooch/d' pyproject.toml
%endif

rm $(grep -rl '/\* Generated by Cython') PKG-INFO

# Do not do benchmarking, coverage, or timeout testing for RPM builds
sed -Ei '/^[[:blank:]]*"(asv|pytest-cov|pytest-timeout)"/d' pyproject.toml

# No scikit-umfpack in Fedora
sed -i '/^[[:blank:]]*"scikit-umfpack"/d' pyproject.toml

# No pytest-xdist in RHEL
%if 0%{?rhel} || 0%{?oreon}
sed -i '/^[[:blank:]]*"pytest-xdist"/d' pyproject.toml
%endif

# Loosen the upper bound on numpy
sed -i "/numpy/s/,<2\.3//" pyproject.toml

# Loosen the lower bound on array-api-strict
sed -i "/array-api-strict/s/>=2\.3\.1/>=2/" pyproject.toml

# Loosen the upper bound on Cython
sed -i '/Cython/s/,<[0-9.]\+//' pyproject.toml

%generate_buildrequires
%pyproject_buildrequires -p %{?with_tests:-x test} %{build_backend_args}

%build
%pyproject_wheel %{build_backend_args}

%if %{with doc}
for PY in %{python3_version}; do
  pushd doc
  export PYTHONPATH=$(echo ../build/lib.linux-*-$PY/)
  make html SPHINXBUILD=sphinx-build-$PY
  rm -rf build/html/.buildinfo
  mv build build-$PY
  popd
done
%endif

%install
%pyproject_install
%pyproject_save_files scipy

# Some files got ambiguous python shebangs, we fix them after everything else is done
%py3_shebang_fix %{buildroot}%{python3_sitearch}

%check
%if %{with tests}
# check against the reference BLAS/LAPACK
export FLEXIBLAS=netlib

%ifarch %{power64}
# scipy segfaults with netlib/atlas on ppc64le
export FLEXIBLAS=openblas-openmp
%endif

# TestDatasets try to download from the internet
SKIP_ALL="not TestDatasets"
export PYTEST_ADDOPTS="-k '$SKIP_ALL'"

%ifarch aarch64
# TestConstructUtils::test_concatenate_int32_overflow is flaky on aarch64
export PYTEST_ADDOPTS="-k '$SKIP_ALL and \
not test_concatenate_int32_overflow'"
%endif

%ifarch s390x
# https://bugzilla.redhat.com/show_bug.cgi?id=1959353
export PYTEST_ADDOPTS="-k '$SKIP_ALL and \
not test_distance_transform_cdt05'"
%endif

%ifarch x86_64
%if 0%{?rhel} || 0%{?oreon}
# test_minimize_constrained started failing on ELN without any direct changes to scipy
export PYTEST_ADDOPTS="-k '$SKIP_ALL and \
not test_gh7799 and \
not test_minimize_constrained'"
%endif
%endif

%ifarch i686
# https://github.com/scipy/scipy/issues/17213
export PYTEST_ADDOPTS="-k '$SKIP_ALL and \
not test_examples and \
not test_shifts and \
not test_svdp and \
not TestMMIO and \
not test_mmio and \
not test_threadpoolctl and \
not test_gh11389 and \
not test_gh18123 and \
not test_gh_17782_segfault and \
not test_svd_gesdd_nofegfault'"
%endif

%ifarch riscv64
export PYTEST_ADDOPTS="-k '$SKIP_ALL and \
not TestSchur and \
not test_gejsv_general and \
not test_kendall_p_exact_large and \
not test_gejsv_edge_arguments and \
not test_gh12999 and \
not test_propack and \
not test_milp and \
not test_gejsv_NAG'"
%endif

pushd %{buildroot}/%{python3_sitearch}
# Ignoring the datasets tests as we don't have the optional pooch
# dependency on RHEL.
%{pytest} %{!?with_pooch:--ignore=scipy/datasets/tests/test_data.py} scipy %{?!rhel:--numprocesses=auto}
# Remove test remnants
rm -rf gram{A,B}
rm -rf .pytest_cache
popd
%endif

%files -n python3-scipy -f %{pyproject_files}
%license LICENSE.txt LICENSES_bundled.txt
%exclude %{python3_sitearch}/scipy/*/tests/
%exclude %{python3_sitearch}/scipy/*/*/tests/
%exclude %{python3_sitearch}/scipy/*/*/*/tests/
%exclude %{python3_sitearch}/scipy/*/*/*/*/tests/ 

%if %{with tests}
%files -n python3-scipy-tests
%{python3_sitearch}/scipy/*/tests/
%{python3_sitearch}/scipy/*/*/tests/
%{python3_sitearch}/scipy/*/*/*/tests/
%{python3_sitearch}/scipy/*/*/*/*/tests/
%endif

%if %{with doc}
%files -n python3-scipy-doc
%license LICENSE.txt
%doc doc/build-%{python3_version}/html
%endif

%changelog
* Mon May 25 2026 Oreon Packaging Team <packaging@oreonhq.com> - 1.16.2-3
- Import
