%global source0_hash daf53fe96783043ca33151a3851d054a826fab8d9a173e6bcbbedd4a7eabf5b1

Name:           ensmallen
Version:        2.22.1
Release:        3%{?dist}
Summary:        Header-only C++ library for efficient mathematical optimization

License:        BSD-3-Clause
URL:            https://www.ensmallen.org
Source0:        https://www.ensmallen.org/files/%{name}-%{version}.tar.gz

BuildRequires:  cmake >= 2.8.5
BuildRequires:	gcc-c++
BuildRequires:	armadillo-devel >= 10.8.2
Requires:       armadillo-devel >= 10.8.2

# ensmallen is header-only, and the build just builds the tests, so there's no
# use for a debuginfo package.
%global debug_package %{nil}

%description
ensmallen is a header-only C++ library for efficient mathematical optimization.
It provides a simple set of abstractions for writing an objective function to
optimize. It also provides a large set of standard and cutting-edge optimizers
that can be used for virtually any mathematical optimization task.  These
include full-batch gradient descent techniques, small-batch techniques,
gradient-free optimizers, and constrained optimization.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1

%build
%cmake -DENSMALLEN_CMAKE_DIR=%{_libdir}/cmake/ensmallen/ -DBUILD_TESTS=ON

%cmake_build -t ensmallen_tests

%install
%cmake_install

%check
# Disable the SmallLovaszThetaSdp test---it exposes a bug in one of ensmallen's
# dependencies.  In addition, sometimes the tests may fail, as they are
# probabilistic---so just make sure the test suite passes at least once out of
# five runs.
%ifarch armv7hl
# There's an issue with the tests on armv7hl.
%else
success=0;
cd %{_vpath_builddir};
for i in `seq 1 5`; do
  code=""; # Reset exit code.
  ./ensmallen_tests --rng-seed=time ~SmallLovaszThetaSdp ~BBSBBLogisticRegressionTest || code=$?
  if [ "a$code" == "a" ]; then
    success=1;
    break;
  fi
done
if [ $success -eq 0 ]; then
  false # Force a build error.
fi
cd ..;
%endif

%package devel
Summary:  Header-only C++ library for efficient mathematical optimization
Provides: ensmallen-static = %{version}-%{release}

%description devel
ensmallen is a header-only C++ library for efficient mathematical optimization.
It provides a simple set of abstractions for writing an objective function to
optimize. It also provides a large set of standard and cutting-edge optimizers
that can be used for virtually any mathematical optimization task.  These
include full-batch gradient descent techniques, small-batch techniques,
gradient-free optimizers, and constrained optimization.

%files devel
%license LICENSE.txt
%{_includedir}/ensmallen.hpp
%{_includedir}/ensmallen_bits/
%{_libdir}/cmake/ensmallen/ensmallen-config-version.cmake
%{_libdir}/cmake/ensmallen/ensmallen-config.cmake
%{_libdir}/cmake/ensmallen/ensmallen-targets.cmake

%changelog
%autochangelog
