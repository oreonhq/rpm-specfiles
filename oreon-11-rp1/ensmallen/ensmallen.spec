%global source0_hash 3606c0d0a06ac75858ddb4eecd0802154bc91d45763aa9521cf53a0e78178d55
Name:           ensmallen
Version:        3.11.1
Release:        1%{?dist}
Summary:        Header-only C++ library for efficient mathematical optimization
License:        BSD-3-Clause
URL:            https://www.ensmallen.org
Source0:        https://www.ensmallen.org/files/%{name}-%{version}.tar.gz
Requires:       armadillo-devel >= 10.8.2
%global debug_package %{nil}
# oreon:deps
BuildRequires:  armadillo-devel
BuildRequires:  cmake
BuildRequires:  gcc-c++
# /oreon:deps
%description
ensmallen is a header-only C++ library for efficient mathematical optimization.
It provides a simple set of abstractions for writing an objective function to
optimize. It also provides a large set of standard and cutting-edge optimizers
that can be used for virtually any mathematical optimization task.  These
include full-batch gradient descent techniques, small-batch techniques,
gradient-free optimizers, and constrained optimization.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%oreon_prep
%build

%cmake -DENSMALLEN_CMAKE_DIR=%{_libdir}/cmake/ensmallen/ -DBUILD_TESTS=ON
%cmake_build -t ensmallen_tests
%install
%cmake_install
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*

%check

%ifarch armv7hl
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

%files -f %{oreon_filedir}/main.list
%files -n ensmallen-devel -f %{oreon_filedir}/ensmallen-devel.list

%changelog

%autochangelog
