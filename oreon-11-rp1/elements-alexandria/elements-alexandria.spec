%global source0_hash 96f987bf3ad9fe32e65dd8c9b4de87ccb16e11436bae45b9b3099423d1ab4b05
Summary:        A lightweight C++ utility library
Name:           elements-alexandria
Version:        2.33.0
Release:        1%{?dist}
License:        LGPL-3.0-or-later
URL:            https://github.com/astrorama/Alexandria
Source0:        https://github.com/astrorama/Alexandria/archive/%{version}/%{name}-%{version}.tar.gz
Source1:        cppreference-doxygen-web.tag.xml
Patch0:         boost-1.90-headers.patch
%global elements_version 6.3.4
Requires: cmake-filesystem%{?_isa}
%global cmakedir %{_libdir}/cmake/ElementsProject
%global makedir %{_datadir}/Elements/make
%global confdir %{_datadir}/Elements
%global auxdir %{_datadir}/auxdir
%global docdir %{_docdir}/Alexandria
%global python_sitearch %{python2_sitearch}
# oreon:deps
BuildRequires:  CCfits-devel
BuildRequires:  boost-devel
BuildRequires:  cfitsio-devel
BuildRequires:  cmake
BuildRequires:  cppunit-devel
BuildRequires:  doxygen
BuildRequires:  elements-devel
BuildRequires:  elements-doc
BuildRequires:  gcc-c++
BuildRequires:  graphviz
BuildRequires:  log4cpp-devel
BuildRequires:  make
BuildRequires:  python2
BuildRequires:  python2-devel
BuildRequires:  python2-pytest
# /oreon:deps
%description
A lightweight C++ utility library.

%package devel
Summary: The development part of the %{name} package
Requires: %{name}%{?_isa} = %{version}-%{release}
Requires: elements-devel%{?_isa} = %{elements_version}
%description devel
The development part of the %{name} package.

%package doc
Summary: Documentation for package %{name}
License: LGPL-3.0-or-later AND LicenseRef-Callaway-CC-BY-SA
BuildArch: noarch
Requires: elements-doc = %{elements_version}
%description doc
Documentation for package %{name}

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%global oreon_srcdir Alexandria-%{version}
%oreon_prep
%build

export VERBOSE=1
EXTRA_CMAKE_FLAGS="-DUSE_ENV_FLAGS=ON"
EXTRA_CMAKE_FLAGS="${EXTRA_CMAKE_FLAGS} -DPYTHON_EXPLICIT_VERSION=2"
%cmake -B "%{_vpath_builddir}" -DELEMENTS_BUILD_TESTS=ON -DELEMENTS_INSTALL_TESTS=OFF -DSQUEEZED_INSTALL:BOOL=ON -DINSTALL_DOC:BOOL=ON \
    -DUSE_SPHINX=OFF --no-warn-unused-cli \
    -DCMAKE_LIB_INSTALL_SUFFIX=%{_lib} -DUSE_VERSIONED_LIBRARIES=ON ${EXTRA_CMAKE_FLAGS}
mkdir -p "%{_vpath_builddir}/doc/doxygen"
cp -v "%{SOURCE1}" "%{_vpath_builddir}/doc/doxygen"
%make_build -C "%{_vpath_builddir}"
%install
export VERBOSE=1
%make_install -C "%{_vpath_builddir}"
rm -fv "%{buildroot}/%{_libdir}/"*BoostTest.so*
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%check

make test -C "%{_vpath_builddir}"
%files -f %{oreon_filedir}/main.list
%files -n elements-alexandria-devel -f %{oreon_filedir}/elements-alexandria-devel.list
%files -n elements-alexandria-doc -f %{oreon_filedir}/elements-alexandria-doc.list

%changelog

%autochangelog
