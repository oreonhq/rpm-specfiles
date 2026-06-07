%global source0_hash none

#uncomment next line for a release candidate or a beta
#%%global relc rc1

# Simple way to disable tests
%if 0%{?flatpak} || 0%{?rhel} || 0%{?fedora} || (0%{?oreon} >= 11)
%bcond_with tests
%else
%bcond_without tests
%endif

%if 0%{?fedora} >= 33 || 0%{?rhel} >= 9 || (0%{?oreon} >= 11)
%global blaslib flexiblas
%global blasvar %{nil}
%else
%global blaslib openblas
%global blasvar p
%endif

%global modname numpy

Name:           numpy
Version:        2.4.6
Release:        1%{?dist}
Epoch:          1
Summary:        A fast multidimensional array facility for Python

# Everything is BSD-3-Clause except...
# numpy/core/include/numpy/libdivide: Zlib OR BSL-1.0
# numpy/core/src/multiarray/dragon4.*: MIT
# numpy/random/src/mt19937/randomkit.h: MIT
# numpy/random/src/pcg64: MIT AND Apache-2.0
# numpy/random/src/sfc64: MIT
License:        BSD-3-Clause AND MIT AND Apache-2.0 AND (Zlib OR BSL-1.0)
URL:            http://www.numpy.org/
Source0:        https://github.com/%{name}/%{name}/releases/download/v%{version}/%{name}-%{version}.tar.gz
Source1:        https://numpy.org/doc/%(echo 2.4.6 | cut -d. -f1-2)/numpy-html.zip

# Fix FTBFS with GCC 16
# Sent upstream:
# https://github.com/numpy/x86-simd-sort/pull/225
#Patch:          fix-gcc-16-ftbfs.patch

%description
NumPy is a general-purpose array-processing package designed to
efficiently manipulate large multi-dimensional arrays of arbitrary
records without sacrificing too much speed for small multi-dimensional
arrays.  NumPy is built on the Numeric code base and adds features
introduced by numarray as well as an extended C-API and the ability to
create arrays of arbitrary type.

There are also basic facilities for discrete fourier transform,
basic linear algebra and random number generation. Also included in
this package is a version of f2py that works properly with NumPy.


%package -n python3-numpy
Summary:        A fast multidimensional array facility for Python

%{?python_provide:%python_provide python3-numpy}
Provides:       libnpymath-static = %{epoch}:%{version}-%{release}
Provides:       libnpymath-static%{?_isa} = %{epoch}:%{version}-%{release}
Provides:       numpy = %{epoch}:%{version}-%{release}
Provides:       numpy%{?_isa} = %{epoch}:%{version}-%{release}
Obsoletes:      numpy < 1:1.10.1-3

BuildRequires:  python3-devel
BuildRequires:  gcc-gfortran gcc gcc-c++
BuildRequires:  lapack-devel
%if 0%{?fedora} || (0%{?oreon} >= 11)
BuildRequires:  libdivide-devel
%endif
BuildRequires:  ninja-build
%if %{with tests}
BuildRequires:  python3-hypothesis
BuildRequires:  python3-pytest
BuildRequires:  python3-test
BuildRequires:  python3-typing-extensions
%endif
BuildRequires: %{blaslib}-devel
BuildRequires: chrpath
# Upstream does not support splitting out f2py
#  https://github.com/numpy/numpy/issues/28016
#  https://bugzilla.redhat.com/show_bug.cgi?id=2332307
Requires:       python3-numpy-f2py%{?_isa} = %{epoch}:%{version}-%{release}

%if !0%{?fedora} || (0%{?oreon} >= 11)
Provides:       bundled(libdivide) = 3.0
%endif

%description -n python3-numpy
NumPy is a general-purpose array-processing package designed to
efficiently manipulate large multi-dimensional arrays of arbitrary
records without sacrificing too much speed for small multi-dimensional
arrays.  NumPy is built on the Numeric code base and adds features
introduced by numarray as well as an extended C-API and the ability to
create arrays of arbitrary type.

There are also basic facilities for discrete fourier transform,
basic linear algebra and random number generation. Also included in
this package is a version of f2py that works properly with NumPy.

%package -n python3-numpy-f2py
Summary:        f2py for numpy
Requires:       python3-numpy%{?_isa} = %{epoch}:%{version}-%{release}
Suggests:       python3-devel
Provides:       python3-f2py = %{version}-%{release}
Obsoletes:      python3-f2py <= 2.45.241_1927
%{?python_provide:%python_provide python3-numpy-f2py}
Provides:       f2py = %{epoch}:%{version}-%{release}
Provides:       numpy-f2py = %{epoch}:%{version}-%{release}
Obsoletes:      numpy-f2py < 1:1.10.1-3

%description -n python3-numpy-f2py
This package includes a version of f2py that works properly with NumPy.

%package -n python3-numpy-doc
Summary:	Documentation for numpy
Requires:	python3-numpy = %{epoch}:%{version}-%{release}
BuildArch:	noarch

%description -n python3-numpy-doc
This package provides the complete documentation for NumPy.


%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | cut -d' ' -f1); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%autosetup -n %{name}-%{version} -p1

# openblas is provided by flexiblas by default; otherwise,
# Use openblas pthreads as recommended by upstream (see comment in site.cfg.example)
cat >> site.cfg <<EOF
[openblas]
libraries = %{blaslib}%{blasvar}
library_dirs = %{_libdir}
EOF

%if 0%{?fedora} || (0%{?oreon} >= 11)
# Unbundle libdivide
sed -i 's,"numpy/libdivide/libdivide.h",<libdivide.h>,' \
    numpy/_core/src/umath/loops.c.src
%endif

%generate_buildrequires
%pyproject_buildrequires -R -Csetup-args=-Dblas=flexiblas -Csetup-args=-Dlapack=lapack

%build
%set_build_flags
# Allow libdivide to use vector instructions where possible
%ifarch x86_64
%if 0%{?rhel} > 9 || (0%{?oreon} >= 11)
# x86_64-v3
sed -i '/libdivide\.h/i#define LIBDIVIDE_AVX2' numpy/_core/src/umath/loops.c.src
%else
# x86_64-v1 or x86_64-v2
sed -i '/libdivide\.h/i#define LIBDIVIDE_SSE2' numpy/_core/src/umath/loops.c.src
%endif
%elifarch aarch64
sed -i '/libdivide\.h/i#define LIBDIVIDE_NEON' numpy/_core/src/umath/loops.c.src
%endif

#fix flags for ELN ppc64le
%if 0%{?rhel} >= 10 || (0%{?oreon} >= 11)
%ifarch ppc64le
find . -type f -print0 | xargs -0 sed -i s/mcpu=power8/mcpu=power9/
%endif
%endif

%pyproject_wheel -Csetup-args=-Dcpu-baseline="none" -Csetup-args=-Dblas=flexiblas -Csetup-args=-Dlapack=lapack -Ccompile-args=-v

%install
mkdir docs
pushd docs
unzip %{SOURCE1}
popd

%pyproject_install
pushd %{buildroot}%{_bindir} &> /dev/null
ln -s f2py f2py3
ln -s f2py f2py%{python3_version}
ln -s f2py3 f2py.numpy
popd &> /dev/null

#symlink for includes, BZ 185079
mkdir -p %{buildroot}%{_includedir}
ln -s %{python3_sitearch}/%{name}/_core/include/numpy/ %{buildroot}%{_includedir}/numpy

%if 0%{?fedora} || (0%{?oreon} >= 11)
rm %{buildroot}%{python3_sitearch}/numpy/_core/include/numpy/random/libdivide.h
%endif

%check
%if %{with tests}
export PYTHONPATH=%{buildroot}%{python3_sitearch}
# test_ppc64_ibm_double_double128 is unnecessary now that ppc64le has switched long doubles to IEEE format.
# https://github.com/numpy/numpy/issues/21094
%ifarch %{ix86}
# Weird RuntimeWarnings on i686, similar to https://github.com/numpy/numpy/issues/13173
# Some tests also overflow on 32bit
%global ix86_k and not test_vector_matrix_values and not test_matrix_vector_values and not test_identityless_reduction_huge_array and not (TestKind and test_all)
%endif
%ifarch riscv64
# These two tests will always fail in RISC-V
# See https://github.com/numpy/numpy/pull/25246
# Patch from http://fedora.riscv.rocks:3000/rpms/numpy/commit/b34bc42e3455b5b070d96e041ef0a5303bdc8f6c
%global riscv64_k and not test_fpclass and not test_fp_noncontiguous and not (TestBoolCmp and test_float)
%endif
# test_deprecate_... fail on Python 3.13+ due to docstrings being dedented
# Upstream has removed the tests in git HEAD.
%if v"0%{python3_version}" >= v"3.13"
%global py313_k and not test_deprecate_help_indentation and not test_deprecate_preserve_whitespace
%endif
%ifnarch %{ix86}
%{__python3} runtests.py --no-build -- -ra -k 'not test_ppc64_ibm_double_double128 %{?ix86_k} %{?riscv64_k} %{?py313_k}' \
                                  -W "ignore:pkg_resources is deprecated as an API::pkg_resources"
%endif

%endif


%files -n python3-numpy
%license LICENSE.txt
%doc THANKS.txt
%{python3_sitearch}/%{name}/__pycache__
%{_bindir}/numpy-config
%dir %{python3_sitearch}/%{name}
%{python3_sitearch}/%{name}/*.py*
%{python3_sitearch}/%{name}/char
%{python3_sitearch}/%{name}/ctypeslib
%{python3_sitearch}/%{name}/core
%{python3_sitearch}/%{name}/doc
%{python3_sitearch}/%{name}/fft
%{python3_sitearch}/%{name}/lib
%{python3_sitearch}/%{name}/linalg
%{python3_sitearch}/%{name}/ma
%{python3_sitearch}/%{name}/random
%{python3_sitearch}/%{name}/rec
%{python3_sitearch}/%{name}/strings
%{python3_sitearch}/%{name}/testing
%{python3_sitearch}/%{name}/tests
%{python3_sitearch}/%{name}/matrixlib
%{python3_sitearch}/%{name}/polynomial
%{python3_sitearch}/%{name}-*.dist-info
%{_includedir}/numpy
%{python3_sitearch}/%{name}/__init__.pxd
%{python3_sitearch}/%{name}/__init__.cython-30.pxd
%{python3_sitearch}/%{name}/py.typed
%{python3_sitearch}/%{name}/typing/
%{python3_sitearch}/%{name}/_core/
%{python3_sitearch}/%{name}/_pyinstaller/
%{python3_sitearch}/%{name}/_typing/
%{python3_sitearch}/%{name}/_utils/

%files -n python3-numpy-f2py
%{_bindir}/f2py
%{_bindir}/f2py3
%{_bindir}/f2py.numpy
%{_bindir}/f2py%{python3_version}
%{python3_sitearch}/%{name}/f2py

%files -n python3-numpy-doc
%doc docs/*


%changelog
* Mon May 25 2026 Oreon Packaging Team <packaging@oreonhq.com> - 1:2.4.6-1
- Import
