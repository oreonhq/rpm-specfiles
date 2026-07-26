%global source0_hash 08240160b0f28dc3293aa4d61ce65e2d67cd597acf6faca439f2e46625f7e793

# Needed for EPEL 8:
%undefine __cmake_in_source_build

Name:		HepMC3
Version:	3.3.1
Release:	9%{?dist}
Summary:	C++ Event Record for Monte Carlo Generators

#		HepMC3 itself is LGPLv3+
#		The included bxzstr header-only library is MPLv2.0
License:	LGPL-3.0-or-later AND MPL-2.0
URL:		https://hepmc.web.cern.ch/hepmc
Source0:	%{url}/releases/%{name}-%{version}.tar.gz
#		Valgrind suppression file for memory leak in dlopen (EPEL 10)
Source1:	valgrind-epel10.supp
#		https://gitlab.cern.ch/hepmc/HepMC3/-/merge_requests/400
Patch0:		0001-Drop-obsolete-work-around-for-ppc64le-on-EPEL-7.patch

BuildRequires:	cmake
BuildRequires:	make
BuildRequires:	gcc-c++
BuildRequires:	root-core
BuildRequires:	root-hist
BuildRequires:	root-io
BuildRequires:	root-tree
BuildRequires:	json-devel
BuildRequires:	protobuf-devel
BuildRequires:	doxygen
BuildRequires:	graphviz
BuildRequires:	python%{python3_pkgversion}-devel
#		Additional requirements for tests
BuildRequires:	pythia8-devel
BuildRequires:	valgrind
BuildRequires:	zlib-devel
BuildRequires:	bzip2-devel
BuildRequires:	xz-devel
BuildRequires:	libzstd-devel
#		For HepMC2 - HepMC3 conversion tests
BuildRequires:	HepMC-devel

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

%if %{?rhel}%{!?rhel:0} == 10
sed 's!MEMORYCHECK_COMMAND_OPTIONS "!&--suppressions=%{SOURCE1} !' \
    -i test/CMakeLists.txt
%endif

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

%check
%ctest

%files
%{_libdir}/libHepMC3.so.4
%license COPYING
%license include/HepMC3/bxzstr/LICENSE

%files devel
%{_bindir}/HepMC3-config
%{_libdir}/libHepMC3.so
%dir %{_includedir}/%{name}
%dir %{_includedir}/%{name}/bxzstr
%dir %{_includedir}/%{name}/Data
%{_includedir}/%{name}/bxzstr/bxzstr.hpp
%{_includedir}/%{name}/bxzstr/bz_stream_wrapper.hpp
%{_includedir}/%{name}/bxzstr/compression_types.hpp
%{_includedir}/%{name}/bxzstr/config.hpp
%{_includedir}/%{name}/bxzstr/lzma_stream_wrapper.hpp
%{_includedir}/%{name}/bxzstr/stream_wrapper.hpp
%{_includedir}/%{name}/bxzstr/strict_fstream.hpp
%{_includedir}/%{name}/bxzstr/zstd_stream_wrapper.hpp
%{_includedir}/%{name}/bxzstr/z_stream_wrapper.hpp
%{_includedir}/%{name}/AssociatedParticle.h
%{_includedir}/%{name}/Attribute.h
%{_includedir}/%{name}/CompressedIO.h
%{_includedir}/%{name}/Data/GenEventData.h
%{_includedir}/%{name}/Data/GenParticleData.h
%{_includedir}/%{name}/Data/GenRunInfoData.h
%{_includedir}/%{name}/Data/GenVertexData.h
%{_includedir}/%{name}/Errors.h
%{_includedir}/%{name}/FourVector.h
%{_includedir}/%{name}/GenCrossSection.h
%{_includedir}/%{name}/GenCrossSection_fwd.h
%{_includedir}/%{name}/GenEvent.h
%{_includedir}/%{name}/GenHeavyIon.h
%{_includedir}/%{name}/GenHeavyIon_fwd.h
%{_includedir}/%{name}/GenParticle.h
%{_includedir}/%{name}/GenParticle_fwd.h
%{_includedir}/%{name}/GenPdfInfo.h
%{_includedir}/%{name}/GenPdfInfo_fwd.h
%{_includedir}/%{name}/GenRunInfo.h
%{_includedir}/%{name}/GenVertex.h
%{_includedir}/%{name}/GenVertex_fwd.h
%{_includedir}/%{name}/HEPEVT_Helpers.h
%{_includedir}/%{name}/HEPEVT_Wrapper.h
%{_includedir}/%{name}/HEPEVT_Wrapper_Runtime.h
%{_includedir}/%{name}/HEPEVT_Wrapper_Runtime_Static.h
%{_includedir}/%{name}/HEPEVT_Wrapper_Template.h
%{_includedir}/%{name}/HepMC3.h
%{_includedir}/%{name}/LHEF.h
%{_includedir}/%{name}/LHEFAttributes.h
%{_includedir}/%{name}/Print.h
%{_includedir}/%{name}/PrintStreams.h
%{_includedir}/%{name}/Reader.h
%{_includedir}/%{name}/ReaderAscii.h
%{_includedir}/%{name}/ReaderAsciiHepMC2.h
%{_includedir}/%{name}/ReaderFactory.h
%{_includedir}/%{name}/ReaderFactory_fwd.h
%{_includedir}/%{name}/ReaderGZ.h
%{_includedir}/%{name}/ReaderHEPEVT.h
%{_includedir}/%{name}/ReaderLHEF.h
%{_includedir}/%{name}/ReaderMT.h
%{_includedir}/%{name}/ReaderPlugin.h
%{_includedir}/%{name}/Setup.h
%{_includedir}/%{name}/Units.h
%{_includedir}/%{name}/Version.h
%{_includedir}/%{name}/Writer.h
%{_includedir}/%{name}/WriterAscii.h
%{_includedir}/%{name}/WriterAsciiHepMC2.h
%{_includedir}/%{name}/WriterHEPEVT.h
%{_includedir}/%{name}/WriterGZ.h
%{_includedir}/%{name}/WriterPlugin.h
%dir %{_datadir}/%{name}
%dir %{_datadir}/%{name}/cmake
%{_datadir}/%{name}/cmake/HepMC3Config.cmake
%{_datadir}/%{name}/cmake/HepMC3Config-version.cmake
%{_datadir}/%{name}/cmake/HepMC3Targets.cmake
%{_datadir}/%{name}/cmake/HepMC3Targets-release.cmake

%files search
%{_libdir}/libHepMC3search.so.5

%files search-devel
%{_libdir}/libHepMC3search.so
%{_includedir}/%{name}/AttributeFeature.h
%{_includedir}/%{name}/Feature.h
%{_includedir}/%{name}/Filter.h
%{_includedir}/%{name}/FilterAttribute.h
%{_includedir}/%{name}/Relatives.h
%{_includedir}/%{name}/Selector.h
%{_datadir}/%{name}/cmake/HepMC3searchTargets.cmake
%{_datadir}/%{name}/cmake/HepMC3searchTargets-release.cmake

%files rootIO
%{_libdir}/root/libHepMC3rootIO.so.3
# unversioned symlink is used at runtime when library is used as a ROOT plugin
%{_libdir}/root/libHepMC3rootIO.so
%{_libdir}/root/libHepMC3rootIO_rdict.pcm
%{_libdir}/root/libHepMC3rootIO.rootmap

%files rootIO-devel
%{_includedir}/%{name}/ReaderRoot.h
%{_includedir}/%{name}/ReaderRootTree.h
%{_includedir}/%{name}/WriterRoot.h
%{_includedir}/%{name}/WriterRootTree.h
%{_datadir}/%{name}/cmake/HepMC3rootIOTargets.cmake
%{_datadir}/%{name}/cmake/HepMC3rootIOTargets-release.cmake

%files protobufIO
%{_libdir}/libHepMC3protobufIO.so.1

%files protobufIO-devel
%{_libdir}/libHepMC3protobufIO.so
%{_includedir}/%{name}/protobufUtils.h
%{_includedir}/%{name}/HepMC3.pb.h
%{_includedir}/%{name}/Readerprotobuf.h
%{_includedir}/%{name}/Writerprotobuf.h
%{_datadir}/%{name}/cmake/HepMC3protobufIOTargets.cmake
%{_datadir}/%{name}/cmake/HepMC3protobufIOTargets-release.cmake
%dir %{_datadir}/%{name}/protobufIO
%{_datadir}/%{name}/protobufIO/HepMC3.proto

%files interfaces-devel
%{_datadir}/%{name}/interfaces

%files -n python%{python3_pkgversion}-%{name}
%dir %{python3_sitearch}/pyHepMC3
%{python3_sitearch}/pyHepMC3/__init__.py
%{python3_sitearch}/pyHepMC3/__pycache__
%{python3_sitearch}/pyHepMC3/pyHepMC3.so
%{python3_sitearch}/pyHepMC3-*.egg-info
%license python/include/LICENSE

%files -n python%{python3_pkgversion}-%{name}-search
%dir %{python3_sitearch}/pyHepMC3/search
%{python3_sitearch}/pyHepMC3/search/__init__.py
%{python3_sitearch}/pyHepMC3/search/__pycache__
%{python3_sitearch}/pyHepMC3/search/pyHepMC3search.so
%{python3_sitearch}/pyHepMC3.search-*.egg-info

%files -n python%{python3_pkgversion}-%{name}-rootIO
%dir %{python3_sitearch}/pyHepMC3/rootIO
%{python3_sitearch}/pyHepMC3/rootIO/__init__.py
%{python3_sitearch}/pyHepMC3/rootIO/__pycache__
%{python3_sitearch}/pyHepMC3/rootIO/pyHepMC3rootIO.so
%{python3_sitearch}/pyHepMC3.rootIO-*.egg-info

%files -n python%{python3_pkgversion}-%{name}-protobufIO
%dir %{python3_sitearch}/pyHepMC3/protobufIO
%{python3_sitearch}/pyHepMC3/protobufIO/__init__.py
%{python3_sitearch}/pyHepMC3/protobufIO/__pycache__
%{python3_sitearch}/pyHepMC3/protobufIO/pyHepMC3protobufIO.so
%{python3_sitearch}/pyHepMC3.protobufIO-*.egg-info

%files doc
%dir %{_pkgdocdir}
%{_pkgdocdir}/examples
%{_pkgdocdir}/html
%license COPYING

%changelog
%autochangelog
