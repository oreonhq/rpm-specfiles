%global source0_hash 2fe772da383a935645ced07a07b51942ca178d38129df3bf685890bc3c1752cf

Name:           mlpack
Version:        4.6.2
Release:        6%{?dist}
Summary:        Fast, header-only C++ machine learning library

# The source in src/mlpack/core/std_backport/ is available under 
# Apache-2.0 license
# All other code is under BSD-3-Clause
# The stb_image and stb_image_write libraries are (MIT OR Unlicense); since
# header-only libraries are treated as static libraries, they also contribute
# to the license of the binary RPMs.
License:        BSD-3-Clause AND Apache-2.0 AND (MIT OR Unlicense)
URL:            http://www.mlpack.org
Source0:        http://www.mlpack.org/files/%{name}-%{version}.tar.gz

# Drop support for i686
# https://fedoraproject.org/wiki/Changes/EncourageI686LeafRemoval
ExcludeArch:    %{ix86}
# s390 and s390x do not build---maybe worth trying again in a few years?
ExcludeArch:    s390
ExcludeArch:	s390x

BuildRequires:  make
BuildRequires:  gcc-c++
BuildRequires:  cmake >= 3.11

BuildRequires:  armadillo-devel >= 10.8.2
BuildRequires:  ensmallen-devel >= 2.10.0
BuildRequires:  cli11-devel
BuildRequires:  cereal-devel
BuildRequires:  pkg-config

# Header-only libraries (-static is for tracking per guidelines)
# Enforce the the minimum EVR to contain fixes for all of:
# CVE-2021-28021
# CVE-2021-42715
# CVE-2021-42716
# CVE-2022-28041
# CVE-2023-43898
# CVE-2023-45661
# CVE-2023-45662
# CVE-2023-45663
# CVE-2023-45664
# CVE-2023-45666
# CVE-2023-45667
%if 0%{?el7} || 0%{?el8}
%global min_stb_image 2.28-0.39.20231011gitbeebb24
%else
%global min_stb_image 2.28^20231011gitbeebb24-12
%endif
BuildRequires:  stb_image-devel >= %{min_stb_image}
BuildRequires:  stb_image-static
BuildRequires:  stb_image_write-devel
BuildRequires:  stb_image_write-static
BuildRequires:  stb_image_resize2-devel
BuildRequires:  stb_image_resize2-static

# For generating man pages (CMake configuration takes care of this assuming
# txt2man is installed).  It is possible that we could just add all the man
# pages, generated offline, as a patch to this SRPM, but txt2man seems to exist
# in repos.
BuildRequires:  txt2man

# Required for building Python bindings.
BuildRequires: 	python3-devel, python3-Cython, python3-setuptools, python3-numpy
BuildRequires:	python3-pandas, python3-pytest, python3-wheel

%description
mlpack is a C++ machine learning library with emphasis on scalability, speed,
and ease-of-use. Its aim is to make machine learning possible for novice users
by means of a simple, consistent API, while simultaneously exploiting C++
language features to provide maximum performance and maximum flexibility for
expert users. mlpack outperforms competing machine learning libraries by large
margins.

# Licenses and information files
%package licenses
Summary:        Licenses and information files for mlpack (machine learning library)

%description licenses
mlpack is a C++ machine learning library with emphasis on scalability, speed,
and ease-of-use. Its aim is to make machine learning possible for novice users
by means of a simple, consistent API, while simultaneously exploiting C++
language features to provide maximum performance and maximum flexibility for
expert users. mlpack outperforms competing machine learning libraries by large
margins.  This package provides the command-line executables which run mlpack
methods and related documentation.

# Executables.
%package bin
Summary:        Command-line executables for mlpack (machine learning library)
Requires:       %{name}-licenses
Requires:       armadillo

%description bin
mlpack is a C++ machine learning library with emphasis on scalability, speed,
and ease-of-use. Its aim is to make machine learning possible for novice users
by means of a simple, consistent API, while simultaneously exploiting C++
language features to provide maximum performance and maximum flexibility for
expert users. mlpack outperforms competing machine learning libraries by large
margins.  This package provides the command-line executables which run mlpack
methods and related documentation.

# Development headers.
%package devel
Summary:   Development headers for mlpack (C++ machine learning library)
Requires:  %{name}-licenses
Requires:  armadillo-devel >= 10.8.2
Requires:  ensmallen-devel >= 2.10.0
Requires:  cereal-devel
Requires:  lapack-devel
Requires:  pkg-config
Requires:  stb_image-devel%{?_isa} >= %{min_stb_image}
Requires:  stb_image_write-devel%{?_isa}
Provides:  %{name}-static = %{version}-%{release}

%description devel
mlpack is a C++ machine learning library with emphasis on scalability, speed,
and ease-of-use. Its aim is to make machine learning possible for novice users
by means of a simple, consistent API, while simultaneously exploiting C++
language features to provide maximum performance and maximum flexibility for
expert users. mlpack outperforms competing machine learning libraries by large
margins.  This package provides the headers to compile applications against
mlpack.

%package python3
Summary:   Python 3 bindings for mlpack (C++ machine learning library)
Requires:  %{name}-licenses
Requires:  python3
Requires:  python3-numpy
Requires:  python3-pandas
Requires:  python3-Cython

%description python3
mlpack is a C++ machine learning library with emphasis on scalability, speed,
and ease-of-use.  Its aim is to make machine learning possible for novice users
by means of a simple, consistent API, while simultaneously exploiting C++
language features to provide maximum performance and maximum flexibility for
expert users.  mlpack outperforms competing machine learning libraries by large
margins.  This package provides the Python bindings for mlpack.

# For the F20 unversioned documentation change.  This evaluates to
# %%{_pkgdocdir} if on F20 and %%{_docdir}/%%{name}-%%{version} otherwise.
%global our_docdir %{?_pkgdocdir}%{!?_pkgdocdir:%{_docdir}/%{name}-%{version}}

# Disable LTO: it takes too much memory.
%define _lto_cflags %{nil}

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1

%build
# Make sure pip is available.
%{python3} -m ensurepip --upgrade

%{cmake} \
    -D CMAKE_INSTALL_LIBDIR=%{_libdir} \
    -D BUILD_TESTS=OFF \
    -D BUILD_PYTHON_BINDINGS=ON \
    -D PYTHON_EXECUTABLE=%{python3} \
    -D STB_IMAGE_INCLUDE_DIR=%{_includedir} \
    -D USE_SYSTEM_STB=ON

# Try and reduce RAM usage.
%ifarch armv7hl
cmake -B %{__cmake_builddir} \
      -D CMAKE_C_FLAGS="`echo %{optflags} | sed 's/-pipe//g' | sed 's/$/ --param ggc-min-heapsize=32768 --param ggc-min-expand=1/'`" -D CMAKE_CXX_FLAGS="`echo %{optflags} | sed 's/-pipe//g' | sed 's/$/ --param ggc-min-heapsize=32768 --param ggc-min-expand=1/'`" .
%endif

%ifarch i686
cmake -B %{__cmake_builddir} \
      -D CMAKE_C_FLAGS="`echo %{optflags} | sed 's/-pipe//g' | sed 's/$/ --param ggc-min-heapsize=32768 --param ggc-min-expand=1/'`" -D CMAKE_CXX_FLAGS="`echo %{optflags} | sed 's/-pipe//g' | sed 's/$/ --param ggc-min-heapsize=32768 --param ggc-min-expand=1/'`" .
%endif

%ifarch ppc64le
cmake -B %{__cmake_builddir} \
      -D CMAKE_C_FLAGS="`echo %{optflags} | sed 's/-pipe//g' | sed 's/$/ --param ggc-min-heapsize=32768 --param ggc-min-expand=1/'`" -D CMAKE_CXX_FLAGS="`echo %{optflags} | sed 's/-pipe//g' | sed 's/$/ --param ggc-min-heapsize=32768 --param ggc-min-expand=1/'`" .
%endif

# Don't use %make because it could use too much RAM with multiple cores on Koji...
%{cmake_build}

%install
%{cmake_install}

%ldconfig_scriptlets

%files licenses
%license LICENSE.txt
%license COPYRIGHT.txt
%doc CODE_OF_CONDUCT.md
%doc CONTRIBUTING.md
%doc HISTORY.md
%doc GOVERNANCE.md
%doc README.md
%doc UPDATING.txt

%files bin
%{_bindir}/mlpack_adaboost
%{_bindir}/mlpack_approx_kfn
%{_bindir}/mlpack_bayesian_linear_regression
%{_bindir}/mlpack_cf
%{_bindir}/mlpack_dbscan
%{_bindir}/mlpack_decision_tree
%{_bindir}/mlpack_det
%{_bindir}/mlpack_emst
%{_bindir}/mlpack_fastmks
%{_bindir}/mlpack_gmm_generate
%{_bindir}/mlpack_gmm_probability
%{_bindir}/mlpack_gmm_train
%{_bindir}/mlpack_hmm_generate
%{_bindir}/mlpack_hmm_loglik
%{_bindir}/mlpack_hmm_train
%{_bindir}/mlpack_hmm_viterbi
%{_bindir}/mlpack_hoeffding_tree
%{_bindir}/mlpack_image_converter
%{_bindir}/mlpack_kde
%{_bindir}/mlpack_kernel_pca
%{_bindir}/mlpack_kfn
%{_bindir}/mlpack_kmeans
%{_bindir}/mlpack_knn
%{_bindir}/mlpack_krann
%{_bindir}/mlpack_lars
%{_bindir}/mlpack_linear_regression
%{_bindir}/mlpack_linear_svm
%{_bindir}/mlpack_lmnn
%{_bindir}/mlpack_local_coordinate_coding
%{_bindir}/mlpack_logistic_regression
%{_bindir}/mlpack_lsh
%{_bindir}/mlpack_mean_shift
%{_bindir}/mlpack_nbc
%{_bindir}/mlpack_nca
%{_bindir}/mlpack_nmf
%{_bindir}/mlpack_pca
%{_bindir}/mlpack_perceptron
%{_bindir}/mlpack_preprocess_binarize
%{_bindir}/mlpack_preprocess_describe
%{_bindir}/mlpack_preprocess_imputer
%{_bindir}/mlpack_preprocess_one_hot_encoding
%{_bindir}/mlpack_preprocess_scale
%{_bindir}/mlpack_preprocess_split
%{_bindir}/mlpack_radical
%{_bindir}/mlpack_random_forest
%{_bindir}/mlpack_range_search
%{_bindir}/mlpack_softmax_regression
%{_bindir}/mlpack_sparse_coding
%{_mandir}/mlpack_adaboost.1*
%{_mandir}/mlpack_approx_kfn.1*
%{_mandir}/mlpack_bayesian_linear_regression.1*
%{_mandir}/mlpack_cf.1*
%{_mandir}/mlpack_dbscan.1*
%{_mandir}/mlpack_decision_tree.1*
%{_mandir}/mlpack_det.1*
%{_mandir}/mlpack_emst.1*
%{_mandir}/mlpack_fastmks.1*
%{_mandir}/mlpack_gmm_generate.1*
%{_mandir}/mlpack_gmm_probability.1*
%{_mandir}/mlpack_gmm_train.1*
%{_mandir}/mlpack_hmm_generate.1*
%{_mandir}/mlpack_hmm_loglik.1*
%{_mandir}/mlpack_hmm_train.1*
%{_mandir}/mlpack_hmm_viterbi.1*
%{_mandir}/mlpack_hoeffding_tree.1*
%{_mandir}/mlpack_image_converter.1*
%{_mandir}/mlpack_kde.1*
%{_mandir}/mlpack_kernel_pca.1*
%{_mandir}/mlpack_kfn.1*
%{_mandir}/mlpack_kmeans.1*
%{_mandir}/mlpack_knn.1*
%{_mandir}/mlpack_krann.1*
%{_mandir}/mlpack_lars.1*
%{_mandir}/mlpack_linear_regression.1*
%{_mandir}/mlpack_linear_svm.1*
%{_mandir}/mlpack_lmnn.1*
%{_mandir}/mlpack_local_coordinate_coding.1*
%{_mandir}/mlpack_logistic_regression.1*
%{_mandir}/mlpack_lsh.1*
%{_mandir}/mlpack_mean_shift.1*
%{_mandir}/mlpack_nbc.1*
%{_mandir}/mlpack_nca.1*
%{_mandir}/mlpack_nmf.1*
%{_mandir}/mlpack_pca.1*
%{_mandir}/mlpack_perceptron.1*
%{_mandir}/mlpack_preprocess_binarize.1*
%{_mandir}/mlpack_preprocess_describe.1*
%{_mandir}/mlpack_preprocess_imputer.1*
%{_mandir}/mlpack_preprocess_one_hot_encoding.1*
%{_mandir}/mlpack_preprocess_scale.1*
%{_mandir}/mlpack_preprocess_split.1*
%{_mandir}/mlpack_radical.1*
%{_mandir}/mlpack_random_forest.1*
%{_mandir}/mlpack_range_search.1*
%{_mandir}/mlpack_softmax_regression.1*
%{_mandir}/mlpack_sparse_coding.1*

%files devel
%{_includedir}/mlpack.hpp
%{_includedir}/mlpack/
%{_libdir}/pkgconfig/mlpack.pc

%files python3
%{python3_sitearch}/mlpack/
%{python3_sitearch}/mlpack-*.dist-info

%changelog
%autochangelog
