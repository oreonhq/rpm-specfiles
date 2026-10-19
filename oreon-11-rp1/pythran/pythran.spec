%global source0_hash c4a716d775d4cc1821fecd44278df79115a0e2bf140f823b7e4990c700b9e7ae
Name:           pythran
Version:        0.19.0
Release:        1%{?dist}
Summary:        Ahead of Time Python compiler for numeric kernels
License:        BSD-3-Clause AND (MIT OR NCSA)
Provides:       bundled(libcxx) = 3
Provides:       bundled(python3dist(networkx)) = 2.6.1
%py_provides    python3-%{name}
URL:            https://github.com/serge-sans-paille/pythran
Source0:        https://github.com/serge-sans-paille/%{name}/archive/%{version}/%{name}-%{version}.tar.gz
Patch: https://github.com/serge-sans-paille/pythran/pull/2375.patch
Patch: https://github.com/serge-sans-paille/pythran/pull/2402.patch
Patch: https://github.com/serge-sans-paille/pythran/pull/2403.patch
Patch: https://github.com/serge-sans-paille/pythran/pull/2404.patch
%global debug_package %{nil}
Requires:       flexiblas-devel
Requires:       gcc-c++
Requires:       python3-devel
Requires:       boost-devel
Requires:       xsimd-devel >= 8
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
BuildRequires:  python3dist(setuptools) < 60
BuildRequires:  python3dist(setuptools) >= 62
Requires:       python3-pythran = %{version}-%{release}
# /oreon:deps
%package -n       python3-pythran+doc
Summary:        Metapackage for python3-pythran doc extras
Requires:       python3-pythran = %{version}-%{release}
Provides:       python3dist(pythran[doc]) = %{version}-%{release}

%description -n python3-pythran+doc
Metapackage for python3-pythran doc extras.

%package -n       python3-pythran+test
Summary:        Metapackage for python3-pythran test extras
Requires:       python3-pythran = %{version}-%{release}
Provides:       python3dist(pythran[test]) = %{version}-%{release}

%description -n python3-pythran+test
Metapackage for python3-pythran test extras.

%description
Pythran is an ahead of time compiler for a subset of the Python language, with
a focus on scientific computing. It takes a Python module annotated with a few
interface description and turns it into a native Python module with the same
interface, but (hopefully) faster. It is meant to efficiently compile
scientific programs, and takes advantage of multi-cores and SIMD
instruction units.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1 -n %{name}-%{version}
find -name '*.hpp' -exec chmod -x {} +
sed -i '1{/#!/d}' pythran/run.py

# Remove bundled header libs and use the ones from system
rm -r pythran/boost pythran/xsimd

# Use FlexiBLAS
sed -i 's|blas=blas|blas=flexiblas|' pythran/pythran-linux*.cfg
sed -i 's|include_dirs=|include_dirs=/usr/include/flexiblas|' pythran/pythran-linux*.cfg

# This test explicitly tests with OpenBLAS
# But we want to avoid OpenBLAS dependency to verify everything works with FlexiBLAS
# https://github.com/serge-sans-paille/pythran/pull/2244#issuecomment-2441215988
sed -i 's/openblas/flexiblas/' pythran/tests/test_distutils/pythran.rc

# not yet available in Fedora
sed -i '/guzzle_sphinx_theme/d' docs/conf.py
sed -i 's/, "guzzle_sphinx_theme"//' pyproject.toml
sed -i 's/, "nbval"//' pyproject.toml

# The tests have some cflags in them
# We need to adapt the flags to play nicely with other Fedora's flags
# E.g. fortify source implies at least -O1
sed -i -e 's/-O0/-O1/g' -e 's/-Werror/-w/g' pythran/tests/__init__.py

%build

%pyproject_wheel
PYTHONPATH=$PWD make -C docs html
rm -rf docs/_build/html/.{doctrees,buildinfo}
%install
%pyproject_install
%oreon_autofiles main

%check

k=""
%if 0%{?__isa_bits} == 32
for t in test_fftn_{8,11,15,16,17,20,22} \
    test_{h,ih,ir}fft_{8,14} \
    test_{,i}fft_3d{,_axis,f64_axis,int64_axis} \
    test_numpy_random_bytes1 \
    test_convolve_2b
do
  k="${k:+$k and }not $t"
done
%endif
%if 0%{?__isa_bits} != 32
%global use_pytest_xdist 1
%endif
%pytest %{?use_pytest_xdist:-n auto} ${k:+-k "$k"}
%files

%changelog

%autochangelog
