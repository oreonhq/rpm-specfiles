%global source0_hash f7e05179df39c45434cad433f5783840bb3788ef322976f9138bc6b72b3a107d
%global lib_version 2608.0.0
Name:           abseil-cpp
Version:        20260817.0
Release:        1%{?dist}
Summary:        C++ Common Libraries
License:        Apache-2.0 AND LicenseRef-Fedora-Public-Domain
URL:            https://abseil.io
Source0:        https://github.com/abseil/abseil-cpp/archive/refs/tags/%{version}.tar.gz#/%{name}-%{version}.tar.gz
Patch:          0001-Omit-the-bind-block-in-test-Test-Mutex-FunctorCondit.patch
Patch:          0002-build-all-testonly-libs-with-TEST_HELPERS.patch
Provides:       bundled(cctz)
%global _lto_cflags %{nil}
%global _smp_mflags -j2
# oreon:deps
BuildRequires:  cmake
BuildRequires:  gcc-c++
BuildRequires:  gmock-devel
BuildRequires:  gtest-devel
BuildRequires:  ninja-build
# /oreon:deps
%description
Abseil is an open-source collection of C++ library code designed to augment
the C++ standard library. The Abseil library code is collected from
Google's own C++ code base, has been extensively tested and used in
production, and is the same code we depend on in our daily coding lives.

In some cases, Abseil provides pieces missing from the C++ standard; in
others, Abseil provides alternatives to the standard for special needs we've
found through usage in the Google code base. We denote those cases clearly
within the library code we provide you.

Abseil is not meant to be a competitor to the standard library; we've just
found that many of these utilities serve a purpose within our code base,
and we now want to provide those resources to the C++ community as a whole.

%package testing
Summary:        Libraries needed for running tests on the installed %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
Provides:       bundled(cctz)
%description testing
%{summary}.

%package devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       %{name}-testing%{?_isa} = %{version}-%{release}
Provides:       bundled(cctz)
%description devel
Development headers for %{name}

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%oreon_prep
%build

%cmake \
  -GNinja \
  -DABSL_USE_EXTERNAL_GOOGLETEST:BOOL=ON \
  -DABSL_FIND_GOOGLETEST:BOOL=ON \
  -DABSL_ENABLE_INSTALL:BOOL=ON \
  -DABSL_BUILD_TESTING:BOOL=OFF \
  -DABSL_BUILD_TEST_HELPERS:BOOL=ON \
  -DCMAKE_BUILD_TYPE:STRING=None \
  -DCMAKE_CXX_STANDARD:STRING=17
%cmake_build
%install
%cmake_install
rm -rf %{buildroot}/usr/lib/debug
%oreon_autofiles abseil-cpp-testing usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles abseil-cpp-devel usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*

%check

:
%files -f %{oreon_filedir}/main.list
%files -n abseil-cpp-testing -f %{oreon_filedir}/abseil-cpp-testing.list
%files -n abseil-cpp-devel -f %{oreon_filedir}/abseil-cpp-devel.list

%changelog

%autochangelog
