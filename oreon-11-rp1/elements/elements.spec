%global source0_hash 61f973f8044730b0eba3ae560f4457da5453fddf061129c9a93a1b13ca83cc8c
Summary:        A C++/Python build framework
Name:           elements
Version:        6.3.7
Release:        1%{?dist}
License:        LGPL-3.0-or-later
Source0:        https://github.com/astrorama/Elements/archive/%{version}/%{name}-%{version}.tar.gz
Source1:        cppreference-doxygen-web.tag.xml
URL:            https://github.com/degauden/Elements.git
Patch0:         0000-Remove-examples.patch
Patch2:         0001-Disable-PDF-documentation.patch
Patch3:         0002-Do-not-rely-on-distutils.patch
Patch4:         elements-boost_filesystem.patch
Requires: cmake-filesystem%{?_isa}
%global cmakedir %{_libdir}/cmake/ElementsProject
%global makedir %{_datadir}/Elements/make
%global confdir %{_datadir}/conf
%global auxdir %{_datadir}/auxdir
%global docdir %{_docdir}/Elements
# oreon:deps
BuildRequires:  CCfits-devel
BuildRequires:  boost-devel
BuildRequires:  cfitsio-devel
BuildRequires:  cmake
BuildRequires:  cppunit-devel
BuildRequires:  doxygen
BuildRequires:  fftw-devel
BuildRequires:  gcc-c++
BuildRequires:  gmock-devel
BuildRequires:  graphviz
BuildRequires:  gtest-devel
BuildRequires:  log4cpp-devel
BuildRequires:  python3
BuildRequires:  python3-devel
BuildRequires:  python3-pytest
BuildRequires:  python3-sphinx
BuildRequires:  swig
BuildRequires:  wcslib-devel
# /oreon:deps
%description
Elements is a C++/Python build framework. It helps to organize
the software into modules which are gathered into projects.

%package devel
Summary: The development part of the %{name} package
Requires: %{name}%{?_isa} = %{version}-%{release}
%description devel
The development part of the %{name} package.

%package doc
Summary: Documentation for package %{name}
License: LGPLv3+ and CC-BY-SA
BuildArch: noarch
%description doc
Documentation for package %{name}

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%global oreon_srcdir Elements-%{version}
%oreon_prep
%build

export VERBOSE=1
%cmake -DELEMENTS_BUILD_TESTS=ON -DINSTALL_TESTS=OFF -DSQUEEZED_INSTALL:BOOL=ON -DINSTALL_DOC:BOOL=ON \
    -DUSE_SPHINX=OFF --no-warn-unused-cli \
    -DPYTHON_EXPLICIT_VERSION=3 -DCMAKE_POLICY_DEFAULT_CMP0148=OLD \
    -DCMAKE_LIB_INSTALL_SUFFIX=%{_lib} -DUSE_VERSIONED_LIBRARIES=ON \
    -DUSE_ENV_FLAGS=ON
mkdir -p "%{_vpath_builddir}/doc/doxygen"
cp -v "%{SOURCE1}" "%{_vpath_builddir}/doc/doxygen"
%cmake_build
%install
export VERBOSE=1
%cmake_install
rm -rfv "%{buildroot}/%{confdir}/ElementsServices/testdata"
rm -fv "%{buildroot}/%{_bindir}/"*_test
rm -fv "%{buildroot}/%{_includedir}/"*BoostTest_export.h
rm -fv "%{buildroot}/%{_libdir}/"*BoostTest.so*
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%check

export ELEMENTS_CONF_PATH="%{_builddir}/ElementsKernel/auxdir/"
%ctest
%files -f %{oreon_filedir}/main.list
%files -n elements-devel -f %{oreon_filedir}/elements-devel.list
%files -n elements-doc -f %{oreon_filedir}/elements-doc.list

%changelog

%autochangelog
