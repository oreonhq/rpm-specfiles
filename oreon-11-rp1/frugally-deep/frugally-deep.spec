%global source0_hash 79a1f400523d629a5f7545f23c152f5b2ba17668a0e07edf8949658ee4066002
%bcond_with test
%global debug_package %{nil}
Summary:        Header-only library for using Keras (TensorFlow) models in C++
Name:           frugally-deep
License:        MIT
Version:        0.20.0
Release:        1%{?dist}
URL:            https://github.com/Dobiasd/frugally-deep
Source0:        https://github.com/Dobiasd/%{name}/archive/v%{version}.tar.gz#/%{name}-%{version}.tar.gz
%if 0%{?suse_version}
%else
%endif
# oreon:deps
BuildRequires:  cmake
BuildRequires:  eigen3-devel
BuildRequires:  fplus-devel
BuildRequires:  gcc-c++
BuildRequires:  json-devel
# /oreon:deps
%description
Would you like to build/train a model using Keras/Python? And would
you like to run the prediction (forward pass) on your model in C++
without linking your application against TensorFlow? Then
frugally-deep is exactly for you.

frugally-deep

* is a small header-only library written in modern and pure C++.
* is very easy to integrate and use.
* depends only on FunctionalPlus, Eigen and json - also header-only
  libraries.
* supports inference (model.predict) not only for sequential models
  but also for computational graphs with a more complex topology,
  created with the functional API.
* re-implements a (small) subset of TensorFlow, i.e., the operations
  needed to support prediction.
* results in a much smaller binary size than linking against TensorFlow.
* works out-of-the-box also when compiled into a 32-bit executable.
  (Of course, 64 bit is fine too.)
* avoids temporarily allocating (potentially large chunks of)
  additional RAM during convolutions (by not materializing the im2col
  input matrix).
* utterly ignores even the most powerful GPU in your system and uses
  only one CPU core per prediction. ;-)
* but is quite fast on one CPU core, and you can run multiple
  predictions in parallel, thus utilizing as many CPUs as you like
  to improve the overall prediction throughput of your
  application/pipeline.

%package devel
Summary:        Header-only library for using Keras (TensorFlow) models in C++
Provides:       %{name}-static = %{version}-%{release}
%description devel
Would you like to build/train a model using Keras/Python? And would
you like to run the prediction (forward pass) on your model in C++
without linking your application against TensorFlow? Then
frugally-deep is exactly for you.

frugally-deep

* is a small header-only library written in modern and pure C++.
* is very easy to integrate and use.
* depends only on FunctionalPlus, Eigen and json - also header-only
  libraries.
* supports inference (model.predict) not only for sequential models
  but also for computational graphs with a more complex topology,
  created with the functional API.
* re-implements a (small) subset of TensorFlow, i.e., the operations
  needed to support prediction.
* results in a much smaller binary size than linking against TensorFlow.
* works out-of-the-box also when compiled into a 32-bit executable.
  (Of course, 64 bit is fine too.)
* avoids temporarily allocating (potentially large chunks of)
  additional RAM during convolutions (by not materializing the im2col
  input matrix).
* utterly ignores even the most powerful GPU in your system and uses
  only one CPU core per prediction. ;-)
* but is quite fast on one CPU core, and you can run multiple
  predictions in parallel, thus utilizing as many CPUs as you like
  to improve the overall prediction throughput of your
  application/pipeline.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1 -n %{name}-%{version}

# cmake changed
sed -i -e 's@cmake_minimum_required(VERSION 3.2)@cmake_minimum_required(VERSION 3.5)@' CMakeLists.txt

%build

%cmake 
%cmake_build
%if %{with test}
%check

%ctest
%endif
%install
%cmake_install
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*

%files -f %{oreon_filedir}/main.list
%files -n frugally-deep-devel -f %{oreon_filedir}/frugally-deep-devel.list

%changelog

%autochangelog
