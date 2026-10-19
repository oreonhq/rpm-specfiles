%global source0_hash df2d5874ff183595a4ba404edd04f6bd9b5505c1d7708573f6a6c17489a67563
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
Version:        2.5.3
Release:        1%{?dist}
Epoch:          1
Summary:        A fast multidimensional array facility for Python
License:        BSD-3-Clause AND MIT AND Apache-2.0 AND (Zlib OR BSL-1.0)
URL:            http://www.numpy.org/
Source0:        https://github.com/%{name}/%{name}/releases/download/v%{version}/%{name}-%{version}.tar.gz
Source1:        https://numpy.org/doc/%(echo 2.5.3 | cut -d. -f1-2)/numpy-html.zip
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
BuildRequires:  python3dist(cython) >= 3.1.0
BuildRequires:  python3dist(meson-python) >= 0.18.0
Requires:       python3-numpy = %{version}-%{release}
# /oreon:deps
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
BuildRequires:  python3-meson-python
BuildRequires:  python3-packaging
BuildRequires:  python3-pyproject-rpm-macros
%if %{with tests}
BuildRequires:  python3-hypothesis
BuildRequires:  python3-pytest
BuildRequires:  python3-test
BuildRequires:  python3-typing-extensions
%endif
BuildRequires: %{blaslib}-devel
BuildRequires: chrpath
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

%build

%set_build_flags
%ifarch x86_64
%if 0%{?rhel} > 9 || (0%{?oreon} >= 11)
sed -i '/libdivide\.h/i#define LIBDIVIDE_AVX2' numpy/_core/src/umath/loops.c.src
%else
sed -i '/libdivide\.h/i#define LIBDIVIDE_SSE2' numpy/_core/src/umath/loops.c.src
%endif
%elifarch aarch64
sed -i '/libdivide\.h/i#define LIBDIVIDE_NEON' numpy/_core/src/umath/loops.c.src
%endif
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
mkdir -p %{buildroot}%{_includedir}
ln -s %{python3_sitearch}/%{name}/_core/include/numpy/ %{buildroot}%{_includedir}/numpy
%if 0%{?fedora} || (0%{?oreon} >= 11)
rm %{buildroot}%{python3_sitearch}/numpy/_core/include/numpy/random/libdivide.h
%oreon_autofiles python3-numpy usr/lib/python3*/site-packages/numpy* usr/lib64/python3*/site-packages/numpy* usr/bin/*
%oreon_autofiles python3-numpy-f2py usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles python3-numpy-doc usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles main usr/lib/python3*/site-packages/numpy* usr/lib64/python3*/site-packages/numpy* usr/bin/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%endif
%check

%if %{with tests}
export PYTHONPATH=%{buildroot}%{python3_sitearch}
%ifarch %{ix86}
%global ix86_k and not test_vector_matrix_values and not test_matrix_vector_values and not test_identityless_reduction_huge_array and not (TestKind and test_all)
%endif
%ifarch riscv64
%global riscv64_k and not test_fpclass and not test_fp_noncontiguous and not (TestBoolCmp and test_float)
%endif
%if v"0%{python3_version}" >= v"3.13"
%global py313_k and not test_deprecate_help_indentation and not test_deprecate_preserve_whitespace
%endif
%ifnarch %{ix86}
%{__python3} runtests.py --no-build -- -ra -k 'not test_ppc64_ibm_double_double128 %{?ix86_k} %{?riscv64_k} %{?py313_k}' \
                                  -W "ignore:pkg_resources is deprecated as an API::pkg_resources"
%endif
%endif
%files
%files -n python3-numpy -f %{oreon_filedir}/python3-numpy.list
%files -n python3-numpy-f2py -f %{oreon_filedir}/python3-numpy-f2py.list
%files -n python3-numpy-doc -f %{oreon_filedir}/python3-numpy-doc.list

%changelog

* Mon May 25 2026 Oreon Packaging Team <packaging@oreonhq.com> - 1:2.4.6-1
- Import
