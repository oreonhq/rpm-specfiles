%global source0_hash 08240160b0f28dc3293aa4d61ce65e2d67cd597acf6faca439f2e46625f7e793
%undefine __cmake_in_source_build
Name:		HepMC3
Version:	3.3.1
Release:        9%{?dist}
Summary:        C++ Event Record for Monte Carlo Generators
License:	LGPL-3.0-or-later AND MPL-2.0
URL:		https://hepmc.web.cern.ch/hepmc
Source0:        https://hepmc.web.cern.ch/hepmc/releases/%{name}-%{version}.tar.gz
Source1:	valgrind-epel10.supp
Patch0:		0001-Drop-obsolete-work-around-for-ppc64le-on-EPEL-7.patch
# oreon:deps
BuildRequires:  HepMC-devel
BuildRequires:  bzip2-devel
BuildRequires:  cmake
BuildRequires:  doxygen
BuildRequires:  gcc-c++
BuildRequires:  graphviz
BuildRequires:  json-devel
BuildRequires:  libzstd-devel
BuildRequires:  make
BuildRequires:  protobuf-devel
BuildRequires:  pythia8-devel
BuildRequires:  python3-devel
BuildRequires:  root-core
BuildRequires:  root-hist
BuildRequires:  root-io
BuildRequires:  root-tree
BuildRequires:  valgrind
BuildRequires:  xz-devel
BuildRequires:  zlib-devel
# /oreon:deps
%description
The HepMC3 package is an object oriented, C++ event record for
High Energy Physics Monte Carlo generators and simulation, described in
A. Buckley et al., "The HepMC3 Event Record Library for Monte Carlo
Event Generators" Comput.Phys.Commun. 260 (2021) 107310, arxiv:1912.08005.
It is a continuation of the HepMC2 by M. Dobbs and J.B. Hansen described
in "The HepMC C++ Monte Carlo event record for High Energy Physics"
(Comput. Phys. Commun. 134 (2001) 41). In version 3 the package
has undergone several modifications and in particular, the latest
HepMC3 series is a completely new re-write using currently available
C++11 techniques, and have out-of-the-box interfaces for the widely
used in HEP community ROOT and Python.

%package devel
Summary:	C++ Event Record for Monte Carlo Generators - development files
Requires:	%{name}%{?_isa} = %{version}-%{release}
%description devel
This package provides development files for %{name}.

%package search
Summary:	C++ Event Record for Monte Carlo Generators - search engine library
Requires:	%{name}%{?_isa} = %{version}-%{release}
%description search
This package provides a library for selecting particles in HepMC3 event
records.

%package search-devel
Summary:	C++ Event Record for Monte Carlo Generators - %{name}-search development files
Requires:	%{name}-search%{?_isa} = %{version}-%{release}
Requires:	%{name}-devel%{?_isa} = %{version}-%{release}
%description search-devel
This package provides development files for %{name}-search.

%package rootIO
Summary:	C++ Event Record for Monte Carlo Generators - ROOT IO
Requires:	%{name}%{?_isa} = %{version}-%{release}
%description rootIO
This package provides a library for ROOT IO support.

%package rootIO-devel
Summary:	C++ Event Record for Monte Carlo Generators - %{name}-rootIO development files
Requires:	%{name}-rootIO%{?_isa} = %{version}-%{release}
Requires:	%{name}-devel%{?_isa} = %{version}-%{release}
%description rootIO-devel
This package provides development files for %{name}-rootIO.

%package protobufIO
Summary:	C++ Event Record for Monte Carlo Generators - protobuf IO
Requires:	%{name}%{?_isa} = %{version}-%{release}
%description protobufIO
This package provides a library for protobuf IO support.

%package protobufIO-devel
Summary:	C++ Event Record for Monte Carlo Generators - %{name}-protobufIO development files
Requires:	%{name}-protobufIO%{?_isa} = %{version}-%{release}
Requires:	%{name}-devel%{?_isa} = %{version}-%{release}
%description protobufIO-devel
This package provides development files for %{name}-protobufIO.

%package interfaces-devel
Summary:	C++ Event Record for Monte Carlo Generators - generator interfaces
License:	LGPL-3.0-or-later AND GPL-3.0-or-later
Requires:	%{name}-devel = %{version}-%{release}
BuildArch:	noarch
%description interfaces-devel
This package provides HepMC3 interfaces to some common Monte Carlo generators.

%package -n python%{python3_pkgversion}-%{name}
Summary:	HepMC3 Python 3 bindings
License:	LGPL-3.0-or-later AND CNRI-Python AND BSD-3-Clause
%py_provides	python%{python3_pkgversion}-%{name}
Requires:	%{name}%{?_isa} = %{version}-%{release}
%description -n python%{python3_pkgversion}-%{name}
This package provides the Python 3 bindings for HepMC3.

%package -n python%{python3_pkgversion}-%{name}-search
Summary:	HepMC3 search module Python 3 bindings
License:	LGPL-3.0-or-later AND CNRI-Python AND BSD-3-Clause
%py_provides	python%{python3_pkgversion}-%{name}-search
Requires:	%{name}-search%{?_isa} = %{version}-%{release}
Requires:	%{name}%{?_isa} = %{version}-%{release}
Requires:	python%{python3_pkgversion}-%{name}%{?_isa} = %{version}-%{release}
%description -n python%{python3_pkgversion}-%{name}-search
This package provides the Python 3 bindings for HepMC3 search module.

%package -n python%{python3_pkgversion}-%{name}-rootIO
Summary:	HepMC3 ROOT I/O module Python 3 bindings
License:	LGPL-3.0-or-later AND CNRI-Python AND BSD-3-Clause
%py_provides	python%{python3_pkgversion}-%{name}-rootIO
Requires:	%{name}-rootIO%{?_isa} = %{version}-%{release}
Requires:	%{name}%{?_isa} = %{version}-%{release}
Requires:	python%{python3_pkgversion}-%{name}%{?_isa} = %{version}-%{release}
%description -n python%{python3_pkgversion}-%{name}-rootIO
This package provides the Python 3 bindings for HepMC3 ROOT I/O module.

%package -n python%{python3_pkgversion}-%{name}-protobufIO
Summary:	HepMC3 protobuf I/O module Python 3 bindings
License:	LGPL-3.0-or-later AND CNRI-Python AND BSD-3-Clause
%py_provides	python%{python3_pkgversion}-%{name}-protobufIO
Requires:	%{name}-protobufIO%{?_isa} = %{version}-%{release}
Requires:	%{name}%{?_isa} = %{version}-%{release}
Requires:	python%{python3_pkgversion}-%{name}%{?_isa} = %{version}-%{release}
%description -n python%{python3_pkgversion}-%{name}-protobufIO
This package provides the Python 3 bindings for HepMC3 protobuf I/O module.

%package doc
Summary:	C++ Event Record for Monte Carlo Generators - documentation
BuildArch:	noarch
%description doc
This package provides HepMC manuals and examples.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q
%patch -P0 -p1

%build

%cmake \
	-DHEPMC3_ENABLE_ROOTIO:BOOL=ON \
	-DHEPMC3_ROOTIO_INSTALL_LIBDIR:PATH=%{_libdir}/root \
	-DHEPMC3_ENABLE_PROTOBUFIO:BOOL=ON \
	-DHEPMC3_ENABLE_TEST:BOOL=ON \
	-DHEPMC3_INSTALL_INTERFACES:BOOL=ON \
	-DHEPMC3_INSTALL_EXAMPLES:BOOL=ON \
	-DHEPMC3_PYTHON_VERSIONS=%python3_version \
	-DHEPMC3_BUILD_DOCS:BOOL=ON \
	-DHEPMC3_BUILD_STATIC_LIBS:BOOL=OFF \
	-DHEPMC3_TEST_VALGRIND:BOOL=ON \
	-DCMAKE_INSTALL_DOCDIR:PATH=%{_pkgdocdir} \
	-DCMAKE_SKIP_INSTALL_RPATH:BOOL=ON
%cmake_build
%install
%cmake_install
rm %{buildroot}%{_includedir}/%{name}/bxzstr/LICENSE
%oreon_autofiles HepMC3-devel usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*
%oreon_autofiles HepMC3-search usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles HepMC3-search-devel usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*
%oreon_autofiles HepMC3-rootIO usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles HepMC3-rootIO-devel usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*
%oreon_autofiles HepMC3-protobufIO usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles HepMC3-protobufIO-devel usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*
%oreon_autofiles HepMC3-interfaces-devel usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*
%oreon_autofiles python3-HepMC3 usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles python3-HepMC3-search usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles python3-HepMC3-rootIO usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles python3-HepMC3-protobufIO usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles HepMC3-doc usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/* usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%check

%ctest
%files -f %{oreon_filedir}/main.list
%files -n HepMC3-devel -f %{oreon_filedir}/HepMC3-devel.list
%files -n HepMC3-search -f %{oreon_filedir}/HepMC3-search.list
%files -n HepMC3-search-devel -f %{oreon_filedir}/HepMC3-search-devel.list
%files -n HepMC3-rootIO -f %{oreon_filedir}/HepMC3-rootIO.list
%files -n HepMC3-rootIO-devel -f %{oreon_filedir}/HepMC3-rootIO-devel.list
%files -n HepMC3-protobufIO -f %{oreon_filedir}/HepMC3-protobufIO.list
%files -n HepMC3-protobufIO-devel -f %{oreon_filedir}/HepMC3-protobufIO-devel.list
%files -n HepMC3-interfaces-devel -f %{oreon_filedir}/HepMC3-interfaces-devel.list
%files -n python3-HepMC3 -f %{oreon_filedir}/python3-HepMC3.list
%files -n python3-HepMC3-search -f %{oreon_filedir}/python3-HepMC3-search.list
%files -n python3-HepMC3-rootIO -f %{oreon_filedir}/python3-HepMC3-rootIO.list
%files -n python3-HepMC3-protobufIO -f %{oreon_filedir}/python3-HepMC3-protobufIO.list
%files -n HepMC3-doc -f %{oreon_filedir}/HepMC3-doc.list

%changelog

%autochangelog
