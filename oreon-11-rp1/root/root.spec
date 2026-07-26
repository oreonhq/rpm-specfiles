%global source0_hash 9bcfae0931849658443deecae4f13ff23e9b79de60632c318efa059f9fd2dc6d

# Disable package note flags, since root saves the compiler/linker flags
# used during the build
%undefine _package_note_flags

%global root7 1
%global dataframe 1
%global roofit 1
%global tmvasofieparser 1
%global distrdf %{dataframe}

%global bundlejson 0

%if %{?fedora}%{!?fedora:0} || %{?rhel}%{!?rhel:0} >= 10
%ifarch %{ix86} %{arm}
%global pandas 0
%else
%global pandas 1
%endif
%else
%global pandas 0
%endif

%global rrr 1

%if %{?fedora}%{!?fedora:0} >= 40 || %{?rhel}%{!?rhel:0} >= 10
%global roofitmp 1
%else
%global roofitmp 0
%endif

# Do not generate autoprovides for Python modules
%global __provides_exclude_from ^%{python3_sitearch}/.*/lib.*\\.so$

Name:		root
Version:	6.38.04
%global libversion %(cut -d. -f 1-2 <<< %{version})
Release:	1%{?dist}
Summary:	Numerical data analysis framework

License:	LGPL-2.1-or-later
URL:		https://root.cern/
#		The upstream source is modified to exclude proprietary fonts
#		See Source8 for how to create Source0
Source0:	%{name}-%{version}.tar.xz
#		Input data for the tests
Source1:	%{name}-testfiles.tar.xz
#		Script to generate above source
Source2:	%{name}-testfiles.sh
#		Desktop file and icon
Source3:	%{name}.desktop
Source4:	%{name}.png
#		MIME type file and icon
Source5:	%{name}.xml
Source6:	application-x-root.png
#		Instructions for setting up a python virtual environment
#		for running the JupyROOT notebook on EPEL
Source7:	JupyROOT-on-EPEL
#		Script to generate Source0
Source8:	%{name}-get-src.sh
#		Clad is a source-transformation automatic differentiation (AD)
#		library for C++, implemented as a plugin for the Clang compiler
Source9:	https://github.com/vgvassilev/clad/archive/v2.2/clad-2.2.tar.gz
#		Use system fonts
Patch0:		%{name}-fontconfig.patch
#		Reduce memory usage during linking on ARM and x86 by generating
#		smaller debuginfo for the llvm libraries
#		Fedora builders run out of memory with the default setting
Patch1:		%{name}-memory-arm-x86.patch
#		Don't install minicern static library
Patch2:		%{name}-dont-install-minicern.patch
#		Do not export Python modules in CMake config
Patch3:		%{name}-no-export-python-modules.patch
#		Run some test on 32 bit that upstream has disabled
Patch4:		%{name}-32bit-tests.patch
#		Revert test change that breaks the test
Patch5:		%{name}-Revert-test-Fetch-the-geometries-from-EOS-and-not-fr.patch
#		Preserve memory during parallel build
#		https://github.com/root-project/root/pull/18991
Patch6:		%{name}-Save-memory-Do-not-link-to-LLVM-libraries-in-parallel.patch
#		https://github.com/root-project/root/pull/21604
#		https://github.com/root-project/root/pull/21605
Patch7:		%{name}-Avoid-additional-python-version-file-to-wrong-location.patch

BuildRequires:	gcc-c++
BuildRequires:	gcc-gfortran
BuildRequires:	make
BuildRequires:	cmake >= 3.20
BuildRequires:	libX11-devel
BuildRequires:	libXpm-devel
BuildRequires:	libXft-devel
BuildRequires:	libXext-devel
BuildRequires:	fontconfig-devel
BuildRequires:	freetype-devel
BuildRequires:	fcgi-devel
BuildRequires:	ftgl-devel
BuildRequires:	gl2ps-devel
BuildRequires:	glew-devel
BuildRequires:	pcre2-devel
BuildRequires:	zlib-devel
BuildRequires:	xz-devel
BuildRequires:	lz4-devel
BuildRequires:	xxhash-devel
BuildRequires:	libzstd-devel
BuildRequires:	libtiff-devel
BuildRequires:	libpng-devel
BuildRequires:	giflib-devel
BuildRequires:	libjpeg-devel
BuildRequires:	ncurses-devel
BuildRequires:	libxml2-devel
BuildRequires:	fftw-devel
BuildRequires:	gsl-devel
BuildRequires:	unuran-devel
BuildRequires:	sqlite-devel
BuildRequires:	libGL-devel
BuildRequires:	libGLU-devel
BuildRequires:	libxcrypt-devel
BuildRequires:	python3-devel >= 3.9
BuildRequires:	python3-setuptools
BuildRequires:	python3-numpy
%ifarch %{qt6_qtwebengine_arches}
BuildRequires:	qt6-qtbase-devel
BuildRequires:	qt6-qtwebengine-devel
%endif
BuildRequires:	openssl-devel
BuildRequires:	libtool-ltdl-devel
BuildRequires:	desktop-file-utils
BuildRequires:	dcap-devel
BuildRequires:	xrootd-client-devel >= 1:5.0.0
BuildRequires:	cfitsio-devel
#		Davix version >= 0.6.4, but not between 0.6.8 and 0.7.0
BuildRequires:	davix-devel >= 0.7.1
%if %{rrr}
BuildRequires:	R-Rcpp-devel
BuildRequires:	R-RInside-devel
%endif
BuildRequires:	readline-devel
BuildRequires:	tbb-devel >= 2020
BuildRequires:	libuuid-devel
BuildRequires:	graphviz-devel
BuildRequires:	expat-devel
BuildRequires:	pythia8-devel >= 8.1.80
BuildRequires:	flexiblas-devel
%if ! %{bundlejson}
BuildRequires:	json-devel >= 3.9
%endif
BuildRequires:	liburing-devel
%if %{tmvasofieparser}
BuildRequires:	protobuf-devel >= 3.0
%endif
%ifnarch %{ix86} %{arm}
BuildRequires:	libarrow-devel
%endif
%if %{roofit}
%if %{roofitmp}
#		Required for roofit-multiprocess
#		Requires new zeromq with zmq_ppoll
BuildRequires:	zeromq-devel >= 4.3.5
BuildRequires:	cppzmq-devel
%endif
%endif
%if %{pandas}
BuildRequires:	python3-pandas
%endif
BuildRequires:	perl-generators
BuildRequires:	gtest-devel
BuildRequires:	gmock-devel
#		Fonts
BuildRequires:	font(freesans)
BuildRequires:	font(freeserif)
BuildRequires:	font(freemono)
BuildRequires:	font(standardsymbolsps)
BuildRequires:	font(d050000l)
BuildRequires:	font(z003)
BuildRequires:	font(droidsansfallback)
#		With gdb installed test failures will show backtraces
BuildRequires:	gdb
#		Defines _jsdir
BuildRequires:	web-assets-devel
Requires:	%{name}-core%{?_isa} = %{version}-%{release}
Requires:	%{name}-io%{?_isa} = %{version}-%{release}
Requires:	%{name}-mathcore%{?_isa} = %{version}-%{release}
Requires:	%{name}-multiproc%{?_isa} = %{version}-%{release}
Requires:	%{name}-net%{?_isa} = %{version}-%{release}
Requires:	%{name}-tree%{?_isa} = %{version}-%{release}
Requires:	%{name}-tree-ntuple%{?_isa} = %{version}-%{release}
Requires:	%{name}-tree-player%{?_isa} = %{version}-%{release}
Requires:	hicolor-icon-theme
Obsoletes:	emacs-%{name} < 5.34.28
Obsoletes:	emacs-%{name}-el < 5.34.28

%description
The ROOT system provides a set of object oriented frameworks with all
the functionality needed to handle and analyze large amounts of data
in a very efficient way. Having the data defined as a set of objects,
specialized storage methods are used to get direct access to the
separate attributes of the selected objects, without having to touch
the bulk of the data. Included are histogramming methods in an
arbitrary number of dimensions, curve fitting, function evaluation,
minimization, graphics and visualization classes to allow the easy
setup of an analysis system that can query and process the data
interactively or in batch mode.

Thanks to the built-in C++ interpreter cling, the command, the
scripting and the programming language are all C++. The interpreter
allows for fast prototyping of the macros since it removes the, time
consuming, compile/link cycle. It also provides a good environment to
learn C++. If more performance is needed the interactively developed
macros can be compiled using a C++ compiler via a machine independent
transparent compiler interface called ACliC.

The system has been designed in such a way that it can query its
databases in parallel on clusters of workstations or many-core
machines. ROOT is an open system that can be dynamically extended by
linking external libraries. This makes ROOT a premier platform on
which to build data acquisition, simulation and data analysis systems.

%package icons
Summary:	ROOT icon collection
BuildArch:	noarch
Requires:	%{name}-core = %{version}-%{release}

%description icons
This package contains icons used by the ROOT GUI.

%package font-files
Summary:	ROOT font collection
BuildArch:	noarch
#		STIX version 0.9 only
License:	OFL-1.1
Requires:	%{name}-core = %{version}-%{release}
#		Package renamed
Provides:	%{name}-fonts = %{version}-%{release}
Obsoletes:	%{name}-fonts < 6.36.00-2

%description font-files
This package contains fonts used by ROOT that are not available in Fedora.
In particular it contains STIX version 0.9 that is used by TMathText.

%package tutorial
Summary:	ROOT tutorial scripts and test suite
BuildArch:	noarch
Requires:	%{name} = %{version}-%{release}

%description tutorial
This package contains the tutorial scripts and test suite for ROOT.

%package core
Summary:	ROOT core libraries
License:	LGPL-2.1-or-later AND LGPL-2.0-or-later AND ISC AND MIT AND NCSA
Requires:	%{name}-font-files = %{version}-%{release}
Requires:	%{name}-icons = %{version}-%{release}
#		Dynamic dependencies
Requires:	%{name}-cling%{?_isa} = %{version}-%{release}
Requires:	%{name}-graf-asimage%{?_isa} = %{version}-%{release}
#		Packages providing the libraries listed by "root-config --libs"
#		(Only root-physics and root-multiproc are not dragged in by
#		recursively resolving the dependency on root-graf-asimage
#		above, so it is not that much of a bloat...)
Requires:	%{name}-graf%{?_isa} = %{version}-%{release}
Requires:	%{name}-graf-gpad%{?_isa} = %{version}-%{release}
Requires:	%{name}-graf-postscript%{?_isa} = %{version}-%{release}
Requires:	%{name}-graf3d%{?_isa} = %{version}-%{release}
Requires:	%{name}-hist%{?_isa} = %{version}-%{release}
Requires:	%{name}-io%{?_isa} = %{version}-%{release}
Requires:	%{name}-mathcore%{?_isa} = %{version}-%{release}
Requires:	%{name}-matrix%{?_isa} = %{version}-%{release}
Requires:	%{name}-multiproc%{?_isa} = %{version}-%{release}
Requires:	%{name}-net%{?_isa} = %{version}-%{release}
Requires:	%{name}-physics%{?_isa} = %{version}-%{release}
Requires:	%{name}-tree%{?_isa} = %{version}-%{release}
%if %{dataframe}
Requires:	%{name}-tree-dataframe%{?_isa} = %{version}-%{release}
%endif
Requires:	%{name}-tree-ntuple%{?_isa} = %{version}-%{release}
Requires:	%{name}-tree-ntuple-utils%{?_isa} = %{version}-%{release}
Requires:	%{name}-tree-player%{?_isa} = %{version}-%{release}
Requires:	%{name}-vecops%{?_isa} = %{version}-%{release}
#		To resolve dependency in installed ROOTConfig.cmake
%if %{bundlejson}
Provides:	bundled(json-devel) = 3.10.5
%else
Requires:	json-devel >= 3.9
%endif
#		Fonts
Requires:	xorg-x11-fonts-ISO8859-1-75dpi
Requires:	font(freesans)
Requires:	font(freeserif)
Requires:	font(freemono)
Requires:	font(standardsymbolsps)
Requires:	font(d050000l)
Requires:	font(z003)
Requires:	font(droidsansfallback)
Obsoletes:	%{name}-ruby < 6.00.00
Obsoletes:	%{name}-vdt < 6.10.00
Obsoletes:	%{name}-proof-pq2 < 6.16.00
Obsoletes:	%{name}-proofd < 6.16.00
Obsoletes:	%{name}-rootd < 6.16.00
Obsoletes:	%{name}-geocad < 6.18.00
Obsoletes:	%{name}-graf-qt < 6.18.00
Obsoletes:	%{name}-gui-qt < 6.18.00
Obsoletes:	%{name}-gui-qtgsi < 6.18.00
Obsoletes:	%{name}-io-hdfs < 6.18.00
Obsoletes:	%{name}-io-rfio < 6.18.00
Obsoletes:	%{name}-net-bonjour < 6.18.00
Obsoletes:	%{name}-net-globus < 6.18.00
Obsoletes:	%{name}-net-ldap < 6.18.00
Obsoletes:	%{name}-net-krb5 < 6.18.00
Obsoletes:	%{name}-table < 6.18.00
Obsoletes:	%{name}-xproof < 6.22.08-2
Obsoletes:	%{name}-memstat < 6.26.00
Obsoletes:	%{name}-montecarlo-vmc < 6.26.00
Obsoletes:	%{name}-doc < 6.26.00
Obsoletes:	%{name}-io-gfal < 6.30.00
Obsoletes:	%{name}-roofit-common < 6.30.00
Obsoletes:	%{name}-gui-qt5webdisplay < 6.36.00
Obsoletes:	%{name}-hist-draw < 6.36.00
Obsoletes:	%{name}-html < 6.36.00
Obsoletes:	%{name}-proof < 6.38.00
Obsoletes:	%{name}-proof-bench < 6.38.00
Obsoletes:	%{name}-proof-player < 6.38.00
Obsoletes:	%{name}-proof-sessionviewer < 6.38.00
Obsoletes:	%{name}-sql-mysql < 6.38.00
Obsoletes:	%{name}-sql-odbc < 6.38.00
Obsoletes:	%{name}-sql-pgsql < 6.38.00

%description core
This package contains the core libraries used by ROOT: libCore, libNew,
libRint and libThread.

%package multiproc
Summary:	Multi-processor support for ROOT
Requires:	%{name}-core%{?_isa} = %{version}-%{release}
Requires:	%{name}-io%{?_isa} = %{version}-%{release}
Requires:	%{name}-net%{?_isa} = %{version}-%{release}

%description multiproc
This package provides ROOT's multi-processor support library: libMultiProc.

%package cling
Summary:	Cling C++ interpreter
License:	(NCSA OR LGPL-2.1-only) AND (Apache-2.0 WITH LLVM-exception OR NCSA) AND BSD-2-Clause AND BSD-3-Clause AND MIT
Requires:	%{name}-core%{?_isa} = %{version}-%{release}
Requires:	%{name}-io%{?_isa} = %{version}-%{release}
#		Root's cling interpreter uses a particular git commit of
#		llvm and clang with application specific changes. It does
#		not work with the system libraries. The bundled llvm and
#		clang are compiled using -fvisibility=hidden, and are not
#		visible outside of the libCling module.
Provides:	bundled(clang-libs)
Provides:	bundled(llvm-libs)
Requires:	gcc-c++
Requires:	redhat-rpm-config
Obsoletes:	%{name}-cint7 < 5.26.00c
Obsoletes:	%{name}-cint < 6.00.00
Obsoletes:	%{name}-cintex < 6.00.00
Obsoletes:	%{name}-reflex < 6.00.00

%description cling
Cling is an interactive C++ interpreter, built on top of Clang and
LLVM compiler infrastructure.

%package testsupport
Summary:	Unit test support library for ROOT
Requires:	%{name}-core%{?_isa} = %{version}-%{release}

%description testsupport
This package contains the unit test support library for ROOT.

%package tpython
Summary:	ROOT's TPython interface
Requires:	%{name}-core%{?_isa} = %{version}-%{release}
Requires:	python3-%{name}%{?_isa} = %{version}-%{release}
#		Package split (tpython from Python bindings)
Obsoletes:	python3-%{name} < 6.22.00

%description tpython
This package contains ROOT's TPython interface. It makes it possible
to call Python from ROOT.

%package -n python3-%{name}
Summary:	Python extension for ROOT
%py_provides	python3-%{name}
Provides:	%{name}-python3 = %{version}-%{release}
Obsoletes:	%{name}-python3 < 6.08.00
Requires:	%{name}-core%{?_isa} = %{version}-%{release}
Requires:	%{name}-io%{?_isa} = %{version}-%{release}
Requires:	%{name}-tree%{?_isa} = %{version}-%{release}
#		Package split (tpython from Python bindings)
Obsoletes:	python3-%{name} < 6.22.00
Obsoletes:	python3-jsmva < 6.32.00

%description -n python3-%{name}
This package contains the Python extension for ROOT. It makes it
possible to use ROOT classes in Python.

%package -n python3-jupyroot
Summary:	ROOT Jupyter kernel
BuildArch:	noarch
%py_provides	python3-jupyroot
Requires:	python3-%{name} = %{version}-%{release}
Requires:	%{name}-core = %{version}-%{release}
#		notebook package was merged with JupyROOT package
Provides:	%{name}-notebook = %{version}-%{release}
Obsoletes:	%{name}-notebook < 6.32.00
Requires:	js-jsroot >= 7.10
%if %{?fedora}%{!?fedora:0} || %{?rhel}%{!?rhel:0} >= 10
#		jupyter-notebook not available in RHEL/EPEL
#		some functionality missing
Requires:	jupyter-notebook
#		python-metakernel not available in RHEL/EPEL
#		some functionality missing
Requires:	python3-ipython
Requires:	python3-metakernel
Requires:	python-jupyter-filesystem
%endif

%description -n python3-jupyroot
The Jupyter kernel for the ROOT notebook.

%if %{distrdf}
%package -n python3-distrdf
Summary:	Distributed RDataFrame
BuildArch:	noarch
%py_provides	python3-distrdf
Requires:	python3-%{name} = %{version}-%{release}
Requires:	%{name}-tree-dataframe = %{version}-%{release}

%description -n python3-distrdf
A layer on top of RDataFrame to enable distributed computations. It is
a port of the previously known PyRDF python package.
%endif

%if %{rrr}
%package r
Summary:	R interface for ROOT
Requires:	%{name}-core%{?_isa} = %{version}-%{release}
Requires:	%{name}-matrix%{?_isa} = %{version}-%{release}
Requires:	R-Rcpp-devel
Requires:	R-RInside-devel

%description r
ROOT R is an interface in ROOT to call R functions using an R C++
interface. This interface opens the possibility in ROOT to use the
very large set of mathematical and statistical tools provided by R.
With ROOT R you can perform a conversion from ROOT's C++ objects to
R's objects, transform the returned R objects into ROOT's C++ objects,
then the R functionality can be used directly for statistical studies
in ROOT.

%package r-tools
Summary:	R Tools
Requires:	%{name}-core%{?_isa} = %{version}-%{release}
Requires:	%{name}-mathcore%{?_isa} = %{version}-%{release}
Requires:	%{name}-matrix%{?_isa} = %{version}-%{release}
Requires:	%{name}-r%{?_isa} = %{version}-%{release}

%description r-tools
This package contains a minimizer module for ROOT that uses the ROOT
R interface.
%endif

%package genetic
Summary:	Genetic algorithms for ROOT
Requires:	%{name}-core%{?_isa} = %{version}-%{release}
Requires:	%{name}-mathcore%{?_isa} = %{version}-%{release}
Requires:	%{name}-tmva%{?_isa} = %{version}-%{release}

%description genetic
This package contains a genetic minimizer module for ROOT.

%package geom
Summary:	Geometry library for ROOT
Requires:	%{name}-core%{?_isa} = %{version}-%{release}
Requires:	%{name}-io%{?_isa} = %{version}-%{release}
Requires:	%{name}-mathcore%{?_isa} = %{version}-%{release}
#		Package split (geom-builder and geom-painter from geom)
Obsoletes:	%{name}-geom < 6.28.00

%description geom
This package contains a library for defining geometries in ROOT.

%package geom-builder
Summary:	Geometry builder library for ROOT
Requires:	%{name}-core%{?_isa} = %{version}-%{release}
Requires:	%{name}-geom%{?_isa} = %{version}-%{release}
Requires:	%{name}-graf-gpad%{?_isa} = %{version}-%{release}
Requires:	%{name}-gui%{?_isa} = %{version}-%{release}
Requires:	%{name}-gui-ged%{?_isa} = %{version}-%{release}
#		Package split (geom-builder and geom-painter from geom)
Obsoletes:	%{name}-geom < 6.28.00

%description geom-builder
This package contains a library for building geometries in ROOT.

%package geom-checker
Summary:	Geometry checker library for ROOT
Requires:	%{name}-core%{?_isa} = %{version}-%{release}
Requires:	%{name}-geom%{?_isa} = %{version}-%{release}
Requires:	%{name}-graf-gpad%{?_isa} = %{version}-%{release}
Requires:	%{name}-graf3d%{?_isa} = %{version}-%{release}
Requires:	%{name}-hist%{?_isa} = %{version}-%{release}
Requires:	%{name}-io%{?_isa} = %{version}-%{release}
Requires:	%{name}-mathcore%{?_isa} = %{version}-%{release}
Requires:	%{name}-tree%{?_isa} = %{version}-%{release}

%description geom-checker
This package contains a library for checking geometries in ROOT.

%package geom-painter
Summary:	Geometry painter library for ROOT
Requires:	%{name}-core%{?_isa} = %{version}-%{release}
Requires:	%{name}-geom%{?_isa} = %{version}-%{release}
Requires:	%{name}-graf-gpad%{?_isa} = %{version}-%{release}
Requires:	%{name}-graf3d%{?_isa} = %{version}-%{release}
Requires:	%{name}-hist%{?_isa} = %{version}-%{release}
#		Package split (geom-builder and geom-painter from geom)
Obsoletes:	%{name}-geom < 6.28.00

%description geom-painter
This package contains a library for drawing geometries in ROOT.

%package gdml
Summary:	GDML import/export for ROOT geometries
Requires:	%{name}-core%{?_isa} = %{version}-%{release}
Requires:	%{name}-geom%{?_isa} = %{version}-%{release}
Requires:	%{name}-hist%{?_isa} = %{version}-%{release}
Requires:	%{name}-io-xml%{?_isa} = %{version}-%{release}

%description gdml
This package contains an import/export module for ROOT geometries.

%package graf
Summary:	2D graphics library for ROOT
Requires:	%{name}-core%{?_isa} = %{version}-%{release}
Requires:	%{name}-hist%{?_isa} = %{version}-%{release}
Requires:	%{name}-io%{?_isa} = %{version}-%{release}
Requires:	%{name}-mathcore%{?_isa} = %{version}-%{release}

%description graf
This package contains the 2-dimensional graphics library for ROOT.

%package graf-asimage
Summary:	AfterImage graphics renderer for ROOT
Requires:	%{name}-core%{?_isa} = %{version}-%{release}
Requires:	%{name}-graf%{?_isa} = %{version}-%{release}
Requires:	%{name}-graf-gpad%{?_isa} = %{version}-%{release}
Requires:	%{name}-graf-postscript%{?_isa} = %{version}-%{release}
Requires:	%{name}-gui%{?_isa} = %{version}-%{release}
Requires:	%{name}-hist%{?_isa} = %{version}-%{release}
Requires:	%{name}-io%{?_isa} = %{version}-%{release}
Requires:	%{name}-mathcore%{?_isa} = %{version}-%{release}

%description graf-asimage
This package contains the AfterImage renderer for ROOT, which allows
you to store output graphics in many formats, including JPEG, PNG and
TIFF.

%package graf-fitsio
Summary:	ROOT interface for the Flexible Image Transport System (FITS)
Requires:	%{name}-core%{?_isa} = %{version}-%{release}
Requires:	%{name}-graf%{?_isa} = %{version}-%{release}
Requires:	%{name}-graf-gpad%{?_isa} = %{version}-%{release}
Requires:	%{name}-hist%{?_isa} = %{version}-%{release}
Requires:	%{name}-matrix%{?_isa} = %{version}-%{release}

%description graf-fitsio
This package contains a library for using the Flexible Image Transport
System (FITS) data format in root.

%package graf-gpad
Summary:	Canvas and pad library for ROOT
Requires:	%{name}-core%{?_isa} = %{version}-%{release}
Requires:	%{name}-graf%{?_isa} = %{version}-%{release}
Requires:	%{name}-hist%{?_isa} = %{version}-%{release}
Requires:	%{name}-io%{?_isa} = %{version}-%{release}
Requires:	%{name}-mathcore%{?_isa} = %{version}-%{release}
#		Dynamic dependency
Requires:	%{name}-graf-postscript%{?_isa} = %{version}-%{release}

%description graf-gpad
This package contains a library for canvas and pad manipulations.

%package graf-gviz
Summary:	Graphviz 2D library for ROOT
Requires:	%{name}-core%{?_isa} = %{version}-%{release}
Requires:	%{name}-graf%{?_isa} = %{version}-%{release}
Requires:	%{name}-hist%{?_isa} = %{version}-%{release}

%description graf-gviz
This package contains the 2-dimensional graphviz library for ROOT.

%package graf-postscript
Summary:	Postscript/PDF renderer library for ROOT
Requires:	%{name}-core%{?_isa} = %{version}-%{release}
Requires:	%{name}-graf%{?_isa} = %{version}-%{release}

%description graf-postscript
This package contains a library for ROOT, which allows rendering
postscript and PDF output.

%package graf-x11
Summary:	X window system renderer for ROOT
Requires:	%{name}-core%{?_isa} = %{version}-%{release}
Requires:	%{name}-graf%{?_isa} = %{version}-%{release}

%description graf-x11
This package contains the X11 renderer for ROOT, which allows using an
X display for showing graphics.

%package graf3d
Summary:	Basic 3D shapes library for ROOT
Requires:	%{name}-core%{?_isa} = %{version}-%{release}
Requires:	%{name}-graf%{?_isa} = %{version}-%{release}
Requires:	%{name}-graf-gpad%{?_isa} = %{version}-%{release}
Requires:	%{name}-hist%{?_isa} = %{version}-%{release}
Requires:	%{name}-mathcore%{?_isa} = %{version}-%{release}

%description graf3d
This library contains the basic 3D shapes and classes for ROOT. For
a more full-blown geometry library, see the root-geom package.

%package graf3d-csg
Summary:	Constructive solid geometry
Requires:	%{name}-core%{?_isa} = %{version}-%{release}

%description graf3d-csg
This library is used to generate composite shapes.

%package graf3d-eve
Summary:	Event display library for ROOT
Requires:	%{name}-core%{?_isa} = %{version}-%{release}
Requires:	%{name}-geom%{?_isa} = %{version}-%{release}
Requires:	%{name}-graf%{?_isa} = %{version}-%{release}
Requires:	%{name}-graf-gpad%{?_isa} = %{version}-%{release}
Requires:	%{name}-graf3d%{?_isa} = %{version}-%{release}
Requires:	%{name}-graf3d-gl%{?_isa} = %{version}-%{release}
Requires:	%{name}-gui%{?_isa} = %{version}-%{release}
Requires:	%{name}-gui-ged%{?_isa} = %{version}-%{release}
Requires:	%{name}-hist%{?_isa} = %{version}-%{release}
Requires:	%{name}-io%{?_isa} = %{version}-%{release}
Requires:	%{name}-mathcore%{?_isa} = %{version}-%{release}
Requires:	%{name}-montecarlo-eg%{?_isa} = %{version}-%{release}
Requires:	%{name}-physics%{?_isa} = %{version}-%{release}
Requires:	%{name}-tree%{?_isa} = %{version}-%{release}
Requires:	%{name}-tree-player%{?_isa} = %{version}-%{release}

%description graf3d-eve
This package contains a library for defining event displays in ROOT.

%package graf3d-gl
Summary:	GL renderer for ROOT
Requires:	%{name}-core%{?_isa} = %{version}-%{release}
Requires:	%{name}-graf%{?_isa} = %{version}-%{release}
Requires:	%{name}-graf-asimage%{?_isa} = %{version}-%{release}
Requires:	%{name}-graf-gpad%{?_isa} = %{version}-%{release}
Requires:	%{name}-graf3d%{?_isa} = %{version}-%{release}
Requires:	%{name}-graf3d-csg%{?_isa} = %{version}-%{release}
Requires:	%{name}-gui%{?_isa} = %{version}-%{release}
Requires:	%{name}-gui-ged%{?_isa} = %{version}-%{release}
Requires:	%{name}-hist%{?_isa} = %{version}-%{release}
Requires:	%{name}-mathcore%{?_isa} = %{version}-%{release}
Requires:	%{name}-tree%{?_isa} = %{version}-%{release}

%description graf3d-gl
This package contains the GL renderer for ROOT. This library provides
3D rendering of volumes and shapes defined in ROOT, as well as 3D
rendering of histograms, and similar. Included is also a high quality
3D viewer for ROOT defined geometries.

%package graf3d-gviz3d
Summary:	Graphviz 3D library for ROOT
Requires:	%{name}-core%{?_isa} = %{version}-%{release}
Requires:	%{name}-geom%{?_isa} = %{version}-%{release}
Requires:	%{name}-graf-gpad%{?_isa} = %{version}-%{release}
Requires:	%{name}-graf3d%{?_isa} = %{version}-%{release}
Requires:	%{name}-graf3d-gl%{?_isa} = %{version}-%{release}
Requires:	%{name}-gui%{?_isa} = %{version}-%{release}
Requires:	%{name}-gui-ged%{?_isa} = %{version}-%{release}

%description graf3d-gviz3d
This package contains the 3-dimensional graphviz library for ROOT.

%package graf3d-x3d
Summary:	X 3D renderer for ROOT
Requires:	%{name}-core%{?_isa} = %{version}-%{release}
Requires:	%{name}-graf3d%{?_isa} = %{version}-%{release}
Requires:	%{name}-gui%{?_isa} = %{version}-%{release}

%description graf3d-x3d
This package contains the X 3D renderer for ROOT. This library provides
3D rendering of volumes and shapes defined in ROOT. Included is also
a low quality 3D viewer for ROOT defined geometries.

%package gui
Summary:	GUI library for ROOT
Requires:	%{name}-core%{?_isa} = %{version}-%{release}
Requires:	%{name}-graf%{?_isa} = %{version}-%{release}
Requires:	%{name}-graf-gpad%{?_isa} = %{version}-%{release}
Requires:	%{name}-io%{?_isa} = %{version}-%{release}
Requires:	%{name}-mathcore%{?_isa} = %{version}-%{release}
Requires:	%{name}-tree-ntuple%{?_isa} = %{version}-%{release}
Requires:	%{name}-tree-ntuple-browse%{?_isa} = %{version}-%{release}
#		Dynamic dependencies
Requires:	%{name}-graf-x11%{?_isa} = %{version}-%{release}
Requires:	%{name}-gui-ged%{?_isa} = %{version}-%{release}
#		Package split (gui-html from gui)
Obsoletes:	%{name}-gui < 6.14.00

%description gui
This package contains a library for defining graphical user interfaces.

%package gui-html
Summary:	HTML GUI library for ROOT
Requires:	%{name}-core%{?_isa} = %{version}-%{release}
Requires:	%{name}-graf%{?_isa} = %{version}-%{release}
Requires:	%{name}-gui%{?_isa} = %{version}-%{release}
Requires:	%{name}-net%{?_isa} = %{version}-%{release}
#		Package split (gui-html from gui)
Obsoletes:	%{name}-gui < 6.14.00

%description gui-html
This package contains a library for defining HTML graphical user interfaces.

%package gui-fitpanel
Summary:	GUI element for fits in ROOT
Requires:	%{name}-core%{?_isa} = %{version}-%{release}
Requires:	%{name}-graf-gpad%{?_isa} = %{version}-%{release}
Requires:	%{name}-gui%{?_isa} = %{version}-%{release}
Requires:	%{name}-hist%{?_isa} = %{version}-%{release}
Requires:	%{name}-mathcore%{?_isa} = %{version}-%{release}
Requires:	%{name}-tree%{?_isa} = %{version}-%{release}
Requires:	%{name}-tree-player%{?_isa} = %{version}-%{release}

%description gui-fitpanel
This package contains a library to show a pop-up dialog when fitting
various kinds of data.

%package gui-ged
Summary:	GUI element for editing various ROOT objects
Requires:	%{name}-core%{?_isa} = %{version}-%{release}
Requires:	%{name}-graf%{?_isa} = %{version}-%{release}
Requires:	%{name}-graf-gpad%{?_isa} = %{version}-%{release}
Requires:	%{name}-gui%{?_isa} = %{version}-%{release}
Requires:	%{name}-hist%{?_isa} = %{version}-%{release}
Requires:	%{name}-tree%{?_isa} = %{version}-%{release}
#		Dynamic dependency
Requires:	%{name}-tree-player%{?_isa} = %{version}-%{release}

%description gui-ged
This package contains a library to show a pop-up window for editing
various ROOT objects.

%package gui-builder
Summary:	GUI editor library for ROOT
Requires:	%{name}-core%{?_isa} = %{version}-%{release}
Requires:	%{name}-graf%{?_isa} = %{version}-%{release}
Requires:	%{name}-gui%{?_isa} = %{version}-%{release}
Requires:	%{name}-mathcore%{?_isa} = %{version}-%{release}
#		Package renamed
Provides:	%{name}-guibuilder = %{version}-%{release}
Provides:	%{name}-guibuilder%{?_isa} = %{version}-%{release}
Obsoletes:	%{name}-guibuilder < 6.14.00

%description gui-builder
This package contains a library for editing graphical user interfaces
in ROOT.

%package gui-recorder
Summary:	Interface for recording and replaying events in ROOT
Requires:	%{name}-core%{?_isa} = %{version}-%{release}
Requires:	%{name}-graf-gpad%{?_isa} = %{version}-%{release}
Requires:	%{name}-gui%{?_isa} = %{version}-%{release}
Requires:	%{name}-io%{?_isa} = %{version}-%{release}
Requires:	%{name}-tree%{?_isa} = %{version}-%{release}

%description gui-recorder
This library provides interface for recording and replaying events in ROOT.
Recorded events are:
 - Commands typed by user in command line ('new TCanvas')
 - GUI events (mouse movement, button clicks, ...)
All the recorded events from one session are stored in one TFile
and can be replayed again anytime.

%package gui-treemap
Summary:	GUI element for tree maps in ROOT
Requires:	%{name}-core%{?_isa} = %{version}-%{release}
Requires:	%{name}-graf%{?_isa} = %{version}-%{release}

%description gui-treemap
This package contains a library to show tree maps in the ROOT GUI.

%package hbook
Summary:	Hbook library for ROOT
Requires:	%{name}-core%{?_isa} = %{version}-%{release}
Requires:	%{name}-hist%{?_isa} = %{version}-%{release}
Requires:	%{name}-io%{?_isa} = %{version}-%{release}
Requires:	%{name}-tree%{?_isa} = %{version}-%{release}

%description hbook
This package contains the Hbook library for ROOT, allowing you to
access legacy Hbook files (NTuples and Histograms from PAW).

%package hist
Summary:	Histogram library for ROOT
Requires:	%{name}-core%{?_isa} = %{version}-%{release}
Requires:	%{name}-io%{?_isa} = %{version}-%{release}
Requires:	%{name}-mathcore%{?_isa} = %{version}-%{release}
Requires:	%{name}-matrix%{?_isa} = %{version}-%{release}
#		Dynamic dependency
Requires:	%{name}-hist-painter%{?_isa} = %{version}-%{release}

%description hist
This package contains a library for histogramming in ROOT.

%package hist-painter
Summary:	Histogram painter plugin for ROOT
Requires:	%{name}-core%{?_isa} = %{version}-%{release}
Requires:	%{name}-graf%{?_isa} = %{version}-%{release}
Requires:	%{name}-graf-gpad%{?_isa} = %{version}-%{release}
Requires:	%{name}-hist%{?_isa} = %{version}-%{release}
Requires:	%{name}-mathcore%{?_isa} = %{version}-%{release}
Requires:	%{name}-matrix%{?_isa} = %{version}-%{release}

%description hist-painter
This package contains a painter of histograms for ROOT.

%package spectrum
Summary:	Spectra analysis library for ROOT
Requires:	%{name}-core%{?_isa} = %{version}-%{release}
Requires:	%{name}-hist%{?_isa} = %{version}-%{release}

%description spectrum
This package contains the Spectrum library for ROOT.

%package spectrum-painter
Summary:	Spectrum painter plugin for ROOT
Requires:	%{name}-core%{?_isa} = %{version}-%{release}
Requires:	%{name}-graf%{?_isa} = %{version}-%{release}
Requires:	%{name}-hist%{?_isa} = %{version}-%{release}

%description spectrum-painter
This package contains a painter of spectra for ROOT.

%package io
Summary:	Input/output of ROOT objects
Requires:	%{name}-core%{?_isa} = %{version}-%{release}
Requires:	liburing-devel

%description io
This package provides I/O routines for ROOT objects.

%package io-dcache
Summary:	dCache input/output library for ROOT
Requires:	%{name}-core%{?_isa} = %{version}-%{release}
Requires:	%{name}-io%{?_isa} = %{version}-%{release}

%description io-dcache
This package contains the dCache extension for ROOT.

%package io-sql
Summary:	SQL input/output library for ROOT
Requires:	%{name}-core%{?_isa} = %{version}-%{release}
Requires:	%{name}-io%{?_isa} = %{version}-%{release}
Requires:	%{name}-net%{?_isa} = %{version}-%{release}

%description io-sql
This package contains the SQL extension for ROOT, that allows
transparent access to files data via an SQL database, using ROOT's
TFile interface.

%package io-xml
Summary:	XML reader library for ROOT
Requires:	%{name}-core%{?_isa} = %{version}-%{release}
Requires:	%{name}-io%{?_isa} = %{version}-%{release}
#		Package split (io-xmlparser from io-xml)
Obsoletes:	%{name}-io-xml < 6.14.00

%description io-xml
This package contains the XML reader library for ROOT.

%package io-xmlparser
Summary:	XML parser library for ROOT
Requires:	%{name}-core%{?_isa} = %{version}-%{release}
#		Package split (io-xmlparser from io-xml)
Obsoletes:	%{name}-io-xml < 6.14.00

%description io-xmlparser
This package contains the XML parser library for ROOT.

%package foam
Summary:	A Compact Version of the Cellular Event Generator
Requires:	%{name}-core%{?_isa} = %{version}-%{release}
Requires:	%{name}-hist%{?_isa} = %{version}-%{release}
Requires:	%{name}-mathcore%{?_isa} = %{version}-%{release}

%description foam
The general-purpose self-adapting Monte Carlo (MC) event
generator/simulator mFOAM (standing for mini-FOAM) is a new compact
version of the FOAM program, with a slightly limited functionality
with respect to its parent version. On the other hand, mFOAM is
easier to use for the average user.

%package fftw
Summary:	FFTW library for ROOT
License:	GPL-2.0-or-later
Requires:	%{name}-core%{?_isa} = %{version}-%{release}

%description fftw
This package contains the Fast Fourier Transform extension for ROOT.
It uses the very fast fftw (version 3) library.

%package fumili
Summary:	Fumili library for ROOT
Requires:	%{name}-core%{?_isa} = %{version}-%{release}
Requires:	%{name}-hist%{?_isa} = %{version}-%{release}
Requires:	%{name}-mathcore%{?_isa} = %{version}-%{release}

%description fumili
This package contains the fumili library for ROOT. This provides an
alternative fitting algorithm for ROOT.

%package genvector
Summary:	Generalized vector library for ROOT
Requires:	%{name}-core%{?_isa} = %{version}-%{release}

%description genvector
This package contains the Genvector library for ROOT. This provides
a generalized vector library.

%package mathcore
Summary:	Core mathematics library for ROOT
Requires:	%{name}-core%{?_isa} = %{version}-%{release}
#		Dynamic dependencies
Requires:	%{name}-mathmore%{?_isa} = %{version}-%{release}
Requires:	%{name}-minuit2%{?_isa} = %{version}-%{release}

%description mathcore
This package contains the MathCore library for ROOT.

%package mathmore
Summary:	GSL interface library for ROOT
License:	GPL-2.0-or-later
Requires:	%{name}-core%{?_isa} = %{version}-%{release}
Requires:	%{name}-mathcore%{?_isa} = %{version}-%{release}

%description mathmore
This package contains the MathMore library for ROOT. This provides
a partial GNU Scientific Library interface for ROOT.
While the rest of root is licensed under LGPLv2+ this optional library
is licensed under GPLv2+ due to its use of GSL.

%package matrix
Summary:	Matrix library for ROOT
Requires:	%{name}-core%{?_isa} = %{version}-%{release}
Requires:	%{name}-mathcore%{?_isa} = %{version}-%{release}

%description matrix
This package contains the Matrix library for ROOT.

%package minuit
Summary:	Minuit library for ROOT
Requires:	%{name}-core%{?_isa} = %{version}-%{release}
Requires:	%{name}-hist%{?_isa} = %{version}-%{release}
Requires:	%{name}-mathcore%{?_isa} = %{version}-%{release}
Requires:	%{name}-matrix%{?_isa} = %{version}-%{release}

%description minuit
This package contains the MINUIT library for ROOT. This provides a
fitting algorithm for ROOT.

%package minuit2
Summary:	Minuit version 2 library for ROOT
Requires:	%{name}-core%{?_isa} = %{version}-%{release}
Requires:	%{name}-hist%{?_isa} = %{version}-%{release}
Requires:	%{name}-mathcore%{?_isa} = %{version}-%{release}

%description minuit2
This package contains the MINUIT version 2 library for ROOT. This
provides an fitting algorithm for ROOT.

%package mlp
Summary:	Multi-layer perceptron extension for ROOT
Requires:	%{name}-core%{?_isa} = %{version}-%{release}
Requires:	%{name}-graf%{?_isa} = %{version}-%{release}
Requires:	%{name}-graf-gpad%{?_isa} = %{version}-%{release}
Requires:	%{name}-hist%{?_isa} = %{version}-%{release}
Requires:	%{name}-mathcore%{?_isa} = %{version}-%{release}
Requires:	%{name}-matrix%{?_isa} = %{version}-%{release}
Requires:	%{name}-tree%{?_isa} = %{version}-%{release}
Requires:	%{name}-tree-player%{?_isa} = %{version}-%{release}

%description mlp
This package contains the mlp library for ROOT. This library provides
a multi-layer perceptron neural network package for ROOT.

%package physics
Summary:	Physics library for ROOT
Requires:	%{name}-core%{?_isa} = %{version}-%{release}
Requires:	%{name}-mathcore%{?_isa} = %{version}-%{release}
Requires:	%{name}-matrix%{?_isa} = %{version}-%{release}

%description physics
This package contains the physics library for ROOT.

%package quadp
Summary:	QuadP library for ROOT
Requires:	%{name}-core%{?_isa} = %{version}-%{release}
Requires:	%{name}-matrix%{?_isa} = %{version}-%{release}

%description quadp
This package contains the QuadP library for ROOT. This provides the a
framework in which to do Quadratic Programming. The quadratic
programming problem involves minimization of a quadratic function
subject to linear constraints.

%package smatrix
Summary:	Sparse matrix library for ROOT
Requires:	%{name}-core%{?_isa} = %{version}-%{release}

%description smatrix
This package contains the Smatrix library for ROOT.

%package splot
Summary:	Splot library for ROOT
Requires:	%{name}-core%{?_isa} = %{version}-%{release}
Requires:	%{name}-hist%{?_isa} = %{version}-%{release}
Requires:	%{name}-matrix%{?_isa} = %{version}-%{release}
Requires:	%{name}-tree%{?_isa} = %{version}-%{release}
Requires:	%{name}-tree-player%{?_isa} = %{version}-%{release}

%description splot
A common method used in High Energy Physics to perform measurements
is the maximum Likelihood method, exploiting discriminating variables
to disentangle signal from background. The crucial point for such an
analysis to be reliable is to use an exhaustive list of sources of
events combined with an accurate description of all the Probability
Density Functions (PDF).

To assess the validity of the fit, a convincing quality check is to
explore further the data sample by examining the distributions of
control variables. A control variable can be obtained for instance by
removing one of the discriminating variables before performing again
the maximum Likelihood fit: this removed variable is a control
variable. The expected distribution of this control variable, for
signal, is to be compared to the one extracted, for signal, from the
data sample. In order to be able to do so, one must be able to unfold
from the distribution of the whole data sample.

The SPlot method allows to reconstruct the distributions for the
control variable, independently for each of the various sources of
events, without making use of any a priori knowledge on this
variable. The aim is thus to use the knowledge available for the
discriminating variables to infer the behavior of the individual
sources of events with respect to the control variable.

SPlot is optimal if the control variable is uncorrelated with the
discriminating variables.

%package unuran
Summary:	Random number generator library
License:	GPL-2.0-or-later
Requires:	%{name}-core%{?_isa} = %{version}-%{release}
Requires:	%{name}-hist%{?_isa} = %{version}-%{release}
Requires:	%{name}-mathcore%{?_isa} = %{version}-%{release}

%description unuran
Contains universal (also called automatic or black-box) algorithms
that can generate random numbers from large classes of continuous or
discrete distributions, and also from practically all standard
distributions.

To generate random numbers the user must supply some information
about the desired distribution, especially a C-function that computes
the density and - depending on the chosen methods - some additional
information (like the borders of the domain, the mode, the derivative
of the density ...). After a user has given this information an
init-program computes all tables and constants necessary for the
random variate generation. The sample program can then generate
variates from the desired distribution.

%package vecops
Summary:	Vector operation extension for ROOT
Requires:	%{name}-core%{?_isa} = %{version}-%{release}
#		Library split (tree-dataframe and vecops from tree-player)
Obsoletes:	%{name}-tree-player < 6.14.00

%description vecops
This package contains a vector operation extension for ROOT.

%package montecarlo-eg
Summary:	Event generator library for ROOT
Requires:	%{name}-core%{?_isa} = %{version}-%{release}
Requires:	%{name}-graf%{?_isa} = %{version}-%{release}
Requires:	%{name}-graf-gpad%{?_isa} = %{version}-%{release}
Requires:	%{name}-graf3d%{?_isa} = %{version}-%{release}
Requires:	%{name}-mathcore%{?_isa} = %{version}-%{release}

%description montecarlo-eg
This package contains an event generator library for ROOT.

%package montecarlo-pythia8
Summary:	Pythia version 8 plugin for ROOT
Requires:	%{name}-core%{?_isa} = %{version}-%{release}
Requires:	%{name}-montecarlo-eg%{?_isa} = %{version}-%{release}

%description montecarlo-pythia8
This package contains the Pythia version 8 plug-in for ROOT. This
package provides the ROOT user with transparent interface to the Pythia
(version 8) event generators for hadronic interactions. If the term
"hadronic" does not ring any bells, this package is not for you.

%package net
Summary:	Net library for ROOT
Requires:	%{name}-core%{?_isa} = %{version}-%{release}
Requires:	%{name}-io%{?_isa} = %{version}-%{release}

%description net
This package contains the ROOT networking library.

%package net-rpdutils
Summary:	Authentication utilities used by rootd
Requires:	%{name}-core%{?_isa} = %{version}-%{release}
Requires:	%{name}-net%{?_isa} = %{version}-%{release}

%description net-rpdutils
This package contains authentication utilities used by rootd.

%package net-auth
Summary:	Authentication extension for ROOT
Requires:	%{name}-core%{?_isa} = %{version}-%{release}
Requires:	%{name}-net%{?_isa} = %{version}-%{release}

%description net-auth
This package contains the basic authentication algorithms used by ROOT.

%package net-davix
Summary:	Davix extension for ROOT
Requires:	davix-libs%{?_isa} >= 0.7.1
Requires:	%{name}-core%{?_isa} = %{version}-%{release}
Requires:	%{name}-io%{?_isa} = %{version}-%{release}

%description net-davix
This package contains the davix extension for ROOT, that provides
access to http based storage such as webdav and S3.

%package net-http
Summary:	HTTP server extension for ROOT
#		The system civetweb is not compiled with websocket support
Provides:	bundled(civetweb)
Requires:	%{name}-core%{?_isa} = %{version}-%{release}
Requires:	%{name}-io%{?_isa} = %{version}-%{release}
Requires:	js-jsroot >= 7.10
#		Library split (net-httpsniff from net-http)
Obsoletes:	%{name}-net-http < 6.14.00

%description net-http
This package contains the HTTP server extension for ROOT. It provides
an http interface to arbitrary ROOT applications.

%package net-httpsniff
Summary:	HTTP sniffer extension for ROOT
Requires:	%{name}-core%{?_isa} = %{version}-%{release}
Requires:	%{name}-graf%{?_isa} = %{version}-%{release}
Requires:	%{name}-graf-gpad%{?_isa} = %{version}-%{release}
Requires:	%{name}-hist%{?_isa} = %{version}-%{release}
Requires:	%{name}-io%{?_isa} = %{version}-%{release}
Requires:	%{name}-io-xml%{?_isa} = %{version}-%{release}
Requires:	%{name}-net-http%{?_isa} = %{version}-%{release}
Requires:	%{name}-tree%{?_isa} = %{version}-%{release}
#		Library split (net-httpsniff from net-http)
Obsoletes:	%{name}-net-http < 6.14.00

%description net-httpsniff
This package contains the HTTP sniffer extension for ROOT.

%package netx
Summary:	NetX extension for ROOT
Requires:	%{name}-core%{?_isa} = %{version}-%{release}
Requires:	%{name}-io%{?_isa} = %{version}-%{release}
Requires:	%{name}-net%{?_isa} = %{version}-%{release}

%description netx
This package contains the NetX extension for ROOT, i.e. a client for
the xrootd server. Only the new (NetXNG) version is provided.

%if %{roofit}
%package roofit
Summary:	ROOT extension for modeling expected distributions - toolkit
License:	BSD-2-Clause
Requires:	%{name}-core%{?_isa} = %{version}-%{release}
Requires:	%{name}-hist%{?_isa} = %{version}-%{release}
Requires:	%{name}-io%{?_isa} = %{version}-%{release}
Requires:	%{name}-mathcore%{?_isa} = %{version}-%{release}
Requires:	%{name}-matrix%{?_isa} = %{version}-%{release}
Requires:	%{name}-roofit-batchcompute%{?_isa} = %{version}-%{release}
Requires:	%{name}-roofit-core%{?_isa} = %{version}-%{release}
Requires:	%{name}-tree%{?_isa} = %{version}-%{release}
#		Package split / Library split (from roofit)
Obsoletes:	%{name}-roofit < 6.20.00

%description roofit
The RooFit packages provide a toolkit for modeling the expected
distribution of events in a physics analysis. Models can be used to
perform likelihood fits, produce plots, and generate "toy Monte
Carlo" samples for various studies. The RooFit tools are integrated
with the object-oriented and interactive ROOT graphical environment.

RooFit has been developed for the BaBar collaboration, a high energy
physics experiment at the Stanford Linear Accelerator Center, and is
primarily targeted to the high-energy physicists using the ROOT
analysis environment, but the general nature of the package make it
suitable for adoption in different disciplines as well.

This package contains the RooFit toolkit classes.

%package roofit-core
Summary:	ROOT extension for modeling expected distributions - core
License:	BSD-2-Clause
Requires:	%{name}-core%{?_isa} = %{version}-%{release}
Requires:	%{name}-foam%{?_isa} = %{version}-%{release}
Requires:	%{name}-graf%{?_isa} = %{version}-%{release}
Requires:	%{name}-hist%{?_isa} = %{version}-%{release}
Requires:	%{name}-io%{?_isa} = %{version}-%{release}
Requires:	%{name}-mathcore%{?_isa} = %{version}-%{release}
Requires:	%{name}-matrix%{?_isa} = %{version}-%{release}
Requires:	%{name}-minuit2%{?_isa} = %{version}-%{release}
Requires:	%{name}-roofit-batchcompute%{?_isa} = %{version}-%{release}
%if %{roofitmp}
Requires:	%{name}-roofit-multiprocess%{?_isa} = %{version}-%{release}
Requires:	%{name}-roofit-zmq%{?_isa} = %{version}-%{release}
%endif
Requires:	%{name}-tree%{?_isa} = %{version}-%{release}
#		Package split / Library split (from roofit)
Obsoletes:	%{name}-roofit < 6.20.00
#		Dataframe helpers are now part of core
Obsoletes:	%{name}-roofit-dataframe-helpers < 6.34.00

%description roofit-core
The RooFit packages provide a toolkit for modeling the expected
distribution of events in a physics analysis. Models can be used to
perform likelihood fits, produce plots, and generate "toy Monte
Carlo" samples for various studies. The RooFit tools are integrated
with the object-oriented and interactive ROOT graphical environment.

RooFit has been developed for the BaBar collaboration, a high energy
physics experiment at the Stanford Linear Accelerator Center, and is
primarily targeted to the high-energy physicists using the ROOT
analysis environment, but the general nature of the package make it
suitable for adoption in different disciplines as well.

This package contains the core RooFit classes.

%package roofit-more
Summary:	ROOT extension for modeling expected distributions - more
License:	BSD-2-Clause
Requires:	%{name}-core%{?_isa} = %{version}-%{release}
Requires:	%{name}-mathcore%{?_isa} = %{version}-%{release}
Requires:	%{name}-mathmore%{?_isa} = %{version}-%{release}
Requires:	%{name}-roofit-core%{?_isa} = %{version}-%{release}
#		Package split / Library split (from roofit)
Obsoletes:	%{name}-roofit < 6.20.00

%description roofit-more
The RooFit packages provide a toolkit for modeling the expected
distribution of events in a physics analysis. Models can be used to
perform likelihood fits, produce plots, and generate "toy Monte
Carlo" samples for various studies. The RooFit tools are integrated
with the object-oriented and interactive ROOT graphical environment.

RooFit has been developed for the BaBar collaboration, a high energy
physics experiment at the Stanford Linear Accelerator Center, and is
primarily targeted to the high-energy physicists using the ROOT
analysis environment, but the general nature of the package make it
suitable for adoption in different disciplines as well.

This package contains RooFit classes that use the mathmore library.

%package roofit-batchcompute
Summary:	Optimized computation functions for PDFs
License:	BSD-2-Clause
Requires:	%{name}-core%{?_isa} = %{version}-%{release}

%description roofit-batchcompute
While fitting, a significant amount of time and processing power is
spent on computing the probability function for every event and PDF
involved in the fitting model. To speed up this process, roofit can
use the computation functions provided in this library. The functions
provided here process whole data arrays (batches) instead of a single
event at a time, as in the legacy evaluate() function in roofit. In
addition, the code is written in a manner that allows for compiler
optimizations, notably auto-vectorization. This library is compiled
multiple times for different vector instruction set architectures and
the optimal code is executed during runtime, as a result of an
automatic hardware detection mechanism that this library contains.

%package roofit-hs3
Summary:	RooFit HS3
License:	BSD-2-Clause
Requires:	%{name}-core%{?_isa} = %{version}-%{release}
Requires:	%{name}-hist%{?_isa} = %{version}-%{release}
Requires:	%{name}-hist-factory%{?_isa} = %{version}-%{release}
Requires:	%{name}-matrix%{?_isa} = %{version}-%{release}
Requires:	%{name}-roofit%{?_isa} = %{version}-%{release}
Requires:	%{name}-roofit-core%{?_isa} = %{version}-%{release}
Requires:	%{name}-roofit-jsoninterface%{?_isa} = %{version}-%{release}

%description roofit-hs3
When using RooFit, statistical models can be conveniently handled and
stored as a RooWorkspace. However, for the sake of interoperability
with other statistical frameworks, and also ease of manipulation, it
may be useful to store statistical models in text form. This library
sets out to achieve exactly that, exporting to and importing from JSON
and YML.

%package roofit-jsoninterface
Summary:	JSON interface to RooFit
License:	BSD-2-Clause
Requires:	%{name}-core%{?_isa} = %{version}-%{release}

%description roofit-jsoninterface
The RooFit packages provide a toolkit for modeling the expected
distribution of events in a physics analysis. Models can be used to
perform likelihood fits, produce plots, and generate "toy Monte
Carlo" samples for various studies. The RooFit tools are integrated
with the object-oriented and interactive ROOT graphical environment.

RooFit has been developed for the BaBar collaboration, a high energy
physics experiment at the Stanford Linear Accelerator Center, and is
primarily targeted to the high-energy physicists using the ROOT
analysis environment, but the general nature of the package make it
suitable for adoption in different disciplines as well.

This package contains the JSON interface to RooFit.

%package roofit-codegen
Summary:	Code generation support for RooFit
License:	BSD-2-Clause
Requires:	%{name}-core%{?_isa} = %{version}-%{release}
Requires:	%{name}-hist-factory%{?_isa} = %{version}-%{release}
Requires:	%{name}-roofit%{?_isa} = %{version}-%{release}
Requires:	%{name}-roofit-core%{?_isa} = %{version}-%{release}

%description roofit-codegen
This package contains a library providing classes that implement
code generation support for RooFit.

%if %{roofitmp}
%package roofit-multiprocess
Summary:	Multi-process support for RooFit
License:	BSD-2-Clause
Requires:	%{name}-core%{?_isa} = %{version}-%{release}
Requires:	%{name}-hist%{?_isa} = %{version}-%{release}
Requires:	%{name}-roofit-zmq%{?_isa} = %{version}-%{release}

%description roofit-multiprocess
This package contains a library providing classes that implement
mult-process support for RooFit.

%package roofit-zmq
Summary:	ZeroMQ interface library for RooFit
License:	BSD-2-Clause

%description roofit-zmq
This package contains a helper library used by RooFit::MultiProcess to
interface to the ZeroMQ library.
%endif

%package roostats
Summary:	Statistical tools built on top of RooFit
Requires:	%{name}-core%{?_isa} = %{version}-%{release}
Requires:	%{name}-graf%{?_isa} = %{version}-%{release}
Requires:	%{name}-graf-gpad%{?_isa} = %{version}-%{release}
Requires:	%{name}-hist%{?_isa} = %{version}-%{release}
Requires:	%{name}-io%{?_isa} = %{version}-%{release}
Requires:	%{name}-mathcore%{?_isa} = %{version}-%{release}
Requires:	%{name}-matrix%{?_isa} = %{version}-%{release}
Requires:	%{name}-minuit%{?_isa} = %{version}-%{release}
Requires:	%{name}-roofit%{?_isa} = %{version}-%{release}
Requires:	%{name}-roofit-core%{?_isa} = %{version}-%{release}
Requires:	%{name}-tree%{?_isa} = %{version}-%{release}
#		Package split / Library split (from roofit)
Obsoletes:	%{name}-roofit < 6.20.00

%description roostats
RooStats is a package containing statistical tools built on top of
RooFit.

%package hist-factory
Summary:	RooFit PDFs from ROOT histograms
Requires:	%{name}-core%{?_isa} = %{version}-%{release}
Requires:	%{name}-hist%{?_isa} = %{version}-%{release}
Requires:	%{name}-io%{?_isa} = %{version}-%{release}
Requires:	%{name}-io-xmlparser%{?_isa} = %{version}-%{release}
Requires:	%{name}-roofit%{?_isa} = %{version}-%{release}
Requires:	%{name}-roofit-core%{?_isa} = %{version}-%{release}
Requires:	%{name}-roostats%{?_isa} = %{version}-%{release}

%description hist-factory
Create RooFit probability density functions from ROOT histograms.

%package xroofit
Summary:	Extra tools for RooFit projects
License:	BSD-2-Clause
Requires:	%{name}-core%{?_isa} = %{version}-%{release}
Requires:	%{name}-graf%{?_isa} = %{version}-%{release}
Requires:	%{name}-graf-gpad%{?_isa} = %{version}-%{release}
Requires:	%{name}-gui%{?_isa} = %{version}-%{release}
Requires:	%{name}-gui-fitpanel%{?_isa} = %{version}-%{release}
Requires:	%{name}-gui-ged%{?_isa} = %{version}-%{release}
Requires:	%{name}-hist%{?_isa} = %{version}-%{release}
Requires:	%{name}-hist-factory%{?_isa} = %{version}-%{release}
Requires:	%{name}-io%{?_isa} = %{version}-%{release}
Requires:	%{name}-mathcore%{?_isa} = %{version}-%{release}
Requires:	%{name}-matrix%{?_isa} = %{version}-%{release}
Requires:	%{name}-roofit%{?_isa} = %{version}-%{release}
Requires:	%{name}-roofit-core%{?_isa} = %{version}-%{release}
Requires:	%{name}-roofit-hs3%{?_isa} = %{version}-%{release}
Requires:	%{name}-roostats%{?_isa} = %{version}-%{release}
Requires:	%{name}-tree%{?_isa} = %{version}-%{release}

%description xroofit
The RooFit packages provide a toolkit for modeling the expected
distribution of events in a physics analysis. Models can be used to
perform likelihood fits, produce plots, and generate "toy Monte
Carlo" samples for various studies. The RooFit tools are integrated
with the object-oriented and interactive ROOT graphical environment.

RooFit has been developed for the BaBar collaboration, a high energy
physics experiment at the Stanford Linear Accelerator Center, and is
primarily targeted to the high-energy physicists using the ROOT
analysis environment, but the general nature of the package make it
suitable for adoption in different disciplines as well.

This package contains extra tools for RooFit projects.
%endif

%package sql-sqlite
Summary:	Sqlite client plugin for ROOT
Requires:	%{name}-core%{?_isa} = %{version}-%{release}
Requires:	%{name}-net%{?_isa} = %{version}-%{release}

%description sql-sqlite
This package contains the sqlite plugin for ROOT. This plugin
provides a thin client (interface) to sqlite servers. Using this
client, one can obtain information from a sqlite database into the
ROOT environment.

%package tmva
Summary:	Toolkit for multivariate data analysis
License:	BSD-3-Clause
Requires:	%{name}-core%{?_isa} = %{version}-%{release}
Requires:	%{name}-graf%{?_isa} = %{version}-%{release}
Requires:	%{name}-graf-gpad%{?_isa} = %{version}-%{release}
Requires:	%{name}-hist%{?_isa} = %{version}-%{release}
Requires:	%{name}-io%{?_isa} = %{version}-%{release}
Requires:	%{name}-io-xml%{?_isa} = %{version}-%{release}
Requires:	%{name}-mathcore%{?_isa} = %{version}-%{release}
Requires:	%{name}-matrix%{?_isa} = %{version}-%{release}
Requires:	%{name}-minuit%{?_isa} = %{version}-%{release}
Requires:	%{name}-mlp%{?_isa} = %{version}-%{release}
Requires:	%{name}-multiproc%{?_isa} = %{version}-%{release}
Requires:	%{name}-net%{?_isa} = %{version}-%{release}
Requires:	%{name}-tree%{?_isa} = %{version}-%{release}
Requires:	%{name}-tree-player%{?_isa} = %{version}-%{release}
#		Library split (tmva-utils from tmva)
Obsoletes:	%{name}-tmva < 6.28.08

%description tmva
The Toolkit for Multivariate Analysis (TMVA) provides a
ROOT-integrated environment for the parallel processing and
evaluation of MVA techniques to discriminate signal from background
samples. It presently includes (ranked by complexity):

  * Rectangular cut optimization
  * Correlated likelihood estimator (PDE approach)
  * Multi-dimensional likelihood estimator (PDE - range-search approach)
  * Fisher (and Mahalanobis) discriminant
  * H-Matrix (chi-squared) estimator
  * Artificial Neural Network (two different implementations)
  * Boosted Decision Trees

The TMVA package includes an implementation for each of these
discrimination techniques, their training and testing (performance
evaluation). In addition all these methods can be tested in parallel,
and hence their performance on a particular data set may easily be
compared.

%if %{dataframe}
%package tmva-utils
Summary:	Toolkit for multivariate data analysis (dataframe utilities)
License:	BSD-3-Clause
Requires:	%{name}-core%{?_isa} = %{version}-%{release}
Requires:	%{name}-io%{?_isa} = %{version}-%{release}
#		Library split (tmva-utils from tmva)
Obsoletes:	%{name}-tmva < 6.28.08

%description tmva-utils
TMVA utilities using dataframe.
%endif

%package tmva-python
Summary:	Toolkit for multivariate data analysis (Python)
License:	BSD-3-Clause
Requires:	%{name}-core%{?_isa} = %{version}-%{release}
Requires:	%{name}-tmva%{?_isa} = %{version}-%{release}
Requires:	%{name}-tmva-sofie%{?_isa} = %{version}-%{release}
Requires:	%{name}-tree%{?_isa} = %{version}-%{release}
Requires:	python3-numpy

%description tmva-python
Python integration with TMVA.

%if %{rrr}
%package tmva-r
Summary:	Toolkit for multivariate data analysis (R)
License:	BSD-3-Clause
Requires:	%{name}-core%{?_isa} = %{version}-%{release}
Requires:	%{name}-matrix%{?_isa} = %{version}-%{release}
Requires:	%{name}-r%{?_isa} = %{version}-%{release}
Requires:	%{name}-tmva%{?_isa} = %{version}-%{release}

%description tmva-r
R integration with TMVA.
%endif

%package tmva-sofie
Summary:	ROOT/TMVA SOFIE (System for Optimized Fast Inference code Emit)
License:	BSD-3-Clause
Requires:	%{name}-core%{?_isa} = %{version}-%{release}
Requires:	%{name}-io%{?_isa} = %{version}-%{release}

%description tmva-sofie
ROOT/TMVA SOFIE (System for Optimized Fast Inference code Emit)
generates C++ functions easily invokable for the fast inference of
trained neural network models. It takes ONNX model files as inputs and
produces C++ header files that can be included and utilized in a
"plug-and-go" style.

%if %{tmvasofieparser}
%package tmva-sofie-parser
Summary:	ROOT/TMVA SOFIE Parsers
License:	BSD-3-Clause AND MIT
Requires:	%{name}-core%{?_isa} = %{version}-%{release}
Requires:	%{name}-tmva-sofie%{?_isa} = %{version}-%{release}

%description tmva-sofie-parser
Parsers for ROOT/TMVA SOFIE
%endif

%package tmva-gui
Summary:	Toolkit for multivariate data analysis GUI
License:	BSD-3-Clause
Requires:	%{name}-core%{?_isa} = %{version}-%{release}
Requires:	%{name}-graf%{?_isa} = %{version}-%{release}
Requires:	%{name}-graf-gpad%{?_isa} = %{version}-%{release}
Requires:	%{name}-gui%{?_isa} = %{version}-%{release}
Requires:	%{name}-hist%{?_isa} = %{version}-%{release}
Requires:	%{name}-io%{?_isa} = %{version}-%{release}
Requires:	%{name}-io-xml%{?_isa} = %{version}-%{release}
Requires:	%{name}-matrix%{?_isa} = %{version}-%{release}
Requires:	%{name}-tmva%{?_isa} = %{version}-%{release}
Requires:	%{name}-tree%{?_isa} = %{version}-%{release}
Requires:	%{name}-tree-viewer%{?_isa} = %{version}-%{release}

%description tmva-gui
GUI for the Toolkit for Multivariate Analysis (TMVA)

%package tree
Summary:	Tree library for ROOT
Requires:	%{name}-core%{?_isa} = %{version}-%{release}
Requires:	%{name}-io%{?_isa} = %{version}-%{release}
Requires:	%{name}-net%{?_isa} = %{version}-%{release}

%description tree
This package contains the Tree library for ROOT.

%if %{dataframe}
%package tree-dataframe
Summary:	A high level interface to ROOT trees
Requires:	%{name}-core%{?_isa} = %{version}-%{release}
Requires:	%{name}-hist%{?_isa} = %{version}-%{release}
Requires:	%{name}-io%{?_isa} = %{version}-%{release}
Requires:	%{name}-mathcore%{?_isa} = %{version}-%{release}
Requires:	%{name}-tree%{?_isa} = %{version}-%{release}
Requires:	%{name}-tree-ntuple%{?_isa} = %{version}-%{release}
Requires:	%{name}-tree-player%{?_isa} = %{version}-%{release}
Requires:	%{name}-vecops%{?_isa} = %{version}-%{release}
#		Library split (tree-dataframe and vecops from tree-player)
Obsoletes:	%{name}-tree-player < 6.14.00

%description tree-dataframe
This package contains a high level interface to ROOT trees.
%endif

%package tree-player
Summary:	Library to loop over a ROOT tree
Requires:	%{name}-core%{?_isa} = %{version}-%{release}
Requires:	%{name}-graf%{?_isa} = %{version}-%{release}
Requires:	%{name}-graf-gpad%{?_isa} = %{version}-%{release}
Requires:	%{name}-graf3d%{?_isa} = %{version}-%{release}
Requires:	%{name}-hist%{?_isa} = %{version}-%{release}
Requires:	%{name}-io%{?_isa} = %{version}-%{release}
Requires:	%{name}-mathcore%{?_isa} = %{version}-%{release}
Requires:	%{name}-multiproc%{?_isa} = %{version}-%{release}
Requires:	%{name}-net%{?_isa} = %{version}-%{release}
Requires:	%{name}-tree%{?_isa} = %{version}-%{release}
#		Library split (tree-dataframe and vecops from tree-player)
Obsoletes:	%{name}-tree-player < 6.14.00

%description tree-player
This package contains a plugin to loop over a ROOT tree.

%package tree-viewer
Summary:	GUI to browse a ROOT tree
Requires:	%{name}-core%{?_isa} = %{version}-%{release}
Requires:	%{name}-graf%{?_isa} = %{version}-%{release}
Requires:	%{name}-graf-gpad%{?_isa} = %{version}-%{release}
Requires:	%{name}-gui%{?_isa} = %{version}-%{release}
Requires:	%{name}-gui-ged%{?_isa} = %{version}-%{release}
Requires:	%{name}-hist%{?_isa} = %{version}-%{release}
Requires:	%{name}-io%{?_isa} = %{version}-%{release}
Requires:	%{name}-mathcore%{?_isa} = %{version}-%{release}
Requires:	%{name}-tree%{?_isa} = %{version}-%{release}
Requires:	%{name}-tree-player%{?_isa} = %{version}-%{release}

%description tree-viewer
This package contains a plugin for browsing a ROOT tree in ROOT.

%package tree-webviewer
Summary:	ROOT tree web viewer library for ROOT
Requires:	%{name}-core%{?_isa} = %{version}-%{release}
Requires:	%{name}-gui-webdisplay%{?_isa} = %{version}-%{release}
Requires:	%{name}-hist%{?_isa} = %{version}-%{release}
Requires:	%{name}-io%{?_isa} = %{version}-%{release}
Requires:	%{name}-tree%{?_isa} = %{version}-%{release}

%description tree-webviewer
This package contains a plugin for browsing a ROOT tree in a web GUI.

%package unfold
Summary:	Distribution unfolding
Requires:	%{name}-core%{?_isa} = %{version}-%{release}
Requires:	%{name}-hist%{?_isa} = %{version}-%{release}
Requires:	%{name}-io-xmlparser%{?_isa} = %{version}-%{release}
Requires:	%{name}-matrix%{?_isa} = %{version}-%{release}

%description unfold
An algorithm to unfold distributions from detector to truth level.

%package cli
Summary:	ROOT command line utilities
BuildArch:	noarch
Requires:	python3-%{name} = %{version}-%{release}

%description cli
The ROOT command line utilities is a set of scripts for common tasks
written in python.

%package gui-webdisplay
Summary:	Web display for ROOT
Requires:	%{name}-core%{?_isa} = %{version}-%{release}
Requires:	%{name}-io%{?_isa} = %{version}-%{release}
Requires:	%{name}-mathcore%{?_isa} = %{version}-%{release}
Requires:	%{name}-net%{?_isa} = %{version}-%{release}
Requires:	%{name}-net-http%{?_isa} = %{version}-%{release}

%description gui-webdisplay
This package contains a web display extension for ROOT.

%ifarch %{qt6_qtwebengine_arches}
%package gui-qt6webdisplay
Summary:	Qt6 Web display
Requires:	%{name}-core%{?_isa} = %{version}-%{release}
Requires:	%{name}-gui-webdisplay%{?_isa} = %{version}-%{release}
Requires:	%{name}-net-http%{?_isa} = %{version}-%{release}

%description gui-qt6webdisplay
This package contains a Qt6 web display extension for ROOT.
%endif

%package gui-webgui6
Summary:	Web based GUI for ROOT
Requires:	%{name}-core%{?_isa} = %{version}-%{release}
Requires:	%{name}-graf%{?_isa} = %{version}-%{release}
Requires:	%{name}-graf-gpad%{?_isa} = %{version}-%{release}
Requires:	%{name}-gui-webdisplay%{?_isa} = %{version}-%{release}
Requires:	%{name}-hist%{?_isa} = %{version}-%{release}
Requires:	%{name}-io%{?_isa} = %{version}-%{release}
Requires:	%{name}-net-http%{?_isa} = %{version}-%{release}

%description gui-webgui6
This package provides a Web based GUI for ROOT.

%package gui-browsable
Summary:	ROOT GUI browsable providers
Requires:	%{name}-core%{?_isa} = %{version}-%{release}
Requires:	%{name}-geom%{?_isa} = %{version}-%{release}
Requires:	%{name}-gui-treemap%{?_isa} = %{version}-%{release}
Requires:	%{name}-hist%{?_isa} = %{version}-%{release}
Requires:	%{name}-io%{?_isa} = %{version}-%{release}
Requires:	%{name}-tree%{?_isa} = %{version}-%{release}
Requires:	%{name}-tree-ntuple%{?_isa} = %{version}-%{release}
Requires:	%{name}-tree-ntuple-browse%{?_isa} = %{version}-%{release}
#		Package split (gui-browsable-v7 from gui-browsable)
Obsoletes:	%{name}-gui-browsable < 6.32.06

%description gui-browsable
This package contains ROOT GUI browsable providers.

%package gui-browserv7
Summary:	ROOT file browser and browser widgets
Requires:	%{name}-core%{?_isa} = %{version}-%{release}
Requires:	%{name}-geom%{?_isa} = %{version}-%{release}
Requires:	%{name}-geom-webviewer%{?_isa} = %{version}-%{release}
Requires:	%{name}-graf-gpad%{?_isa} = %{version}-%{release}
Requires:	%{name}-gui-browsable%{?_isa} = %{version}-%{release}
Requires:	%{name}-gui-webdisplay%{?_isa} = %{version}-%{release}
Requires:	%{name}-gui-webgui6%{?_isa} = %{version}-%{release}
Requires:	%{name}-io%{?_isa} = %{version}-%{release}
Requires:	%{name}-tree%{?_isa} = %{version}-%{release}
Requires:	%{name}-tree-webviewer%{?_isa} = %{version}-%{release}
#		Package split (gui-browserv7-v7 from gui-browserv7)
Obsoletes:	%{name}-gui-browserv7 < 6.32.06

%description gui-browserv7
This package contains the ROOT file browser (RBrowser) and browser widgets.

%package geom-webviewer
Summary:	Geometry web viewer library for ROOT
Requires:	%{name}-core%{?_isa} = %{version}-%{release}
Requires:	%{name}-geom%{?_isa} = %{version}-%{release}
Requires:	%{name}-geom-painter%{?_isa} = %{version}-%{release}
Requires:	%{name}-graf3d-csg%{?_isa} = %{version}-%{release}
Requires:	%{name}-gui-webdisplay%{?_isa} = %{version}-%{release}
Requires:	%{name}-io%{?_isa} = %{version}-%{release}

%description geom-webviewer
This package contains a library for viewing geometries in a web GUI.

%package tree-ntuple
Summary:	The new ROOT n-tuple class
Requires:	%{name}-core%{?_isa} = %{version}-%{release}
Requires:	%{name}-io%{?_isa} = %{version}-%{release}

%description tree-ntuple
This package contains the new ROOT n-tuple class (RNTuple).

%package tree-ntuple-browse
Summary:	N-Tuple browsing library for ROOT
Requires:	%{name}-core%{?_isa} = %{version}-%{release}
Requires:	%{name}-graf%{?_isa} = %{version}-%{release}
Requires:	%{name}-graf-gpad%{?_isa} = %{version}-%{release}
Requires:	%{name}-gui-treemap%{?_isa} = %{version}-%{release}
Requires:	%{name}-hist%{?_isa} = %{version}-%{release}
Requires:	%{name}-io%{?_isa} = %{version}-%{release}
Requires:	%{name}-tree-ntuple%{?_isa} = %{version}-%{release}
Requires:	%{name}-tree-ntuple-utils%{?_isa} = %{version}-%{release}

%description tree-ntuple-browse
This package contains a library for browsing n-tuples.

%package tree-ntuple-utils
Summary:	Ntuple utility library
Requires:	%{name}-core%{?_isa} = %{version}-%{release}
Requires:	%{name}-hist%{?_isa} = %{version}-%{release}
Requires:	%{name}-io%{?_isa} = %{version}-%{release}
Requires:	%{name}-tree%{?_isa} = %{version}-%{release}
Requires:	%{name}-tree-ntuple%{?_isa} = %{version}-%{release}

%description tree-ntuple-utils
This package contains utility functions for ntuples.

%if %{root7}
%package graf-gpadv7
Summary:	Canvas and pad library for ROOT (ROOT 7)
Requires:	%{name}-core%{?_isa} = %{version}-%{release}

%description graf-gpadv7
This package contains a library for canvas and pad manipulations.

%package graf-primitives
Summary:	Graphics primitives (ROOT 7)
Requires:	%{name}-core%{?_isa} = %{version}-%{release}
Requires:	%{name}-graf-gpadv7%{?_isa} = %{version}-%{release}

%description graf-primitives
This package contains graphics primitives for ROOT 7

%package graf3d-eve7
Summary:	Event display library for ROOT (ROOT 7)
Requires:	%{name}-core%{?_isa} = %{version}-%{release}
Requires:	%{name}-geom%{?_isa} = %{version}-%{release}
Requires:	%{name}-geom-webviewer%{?_isa} = %{version}-%{release}
Requires:	%{name}-graf%{?_isa} = %{version}-%{release}
Requires:	%{name}-graf3d%{?_isa} = %{version}-%{release}
Requires:	%{name}-graf3d-csg%{?_isa} = %{version}-%{release}
Requires:	%{name}-gui-webdisplay%{?_isa} = %{version}-%{release}
Requires:	%{name}-hist%{?_isa} = %{version}-%{release}
Requires:	%{name}-io%{?_isa} = %{version}-%{release}
Requires:	%{name}-mathcore%{?_isa} = %{version}-%{release}
Requires:	%{name}-montecarlo-eg%{?_isa} = %{version}-%{release}
Requires:	%{name}-net-http%{?_isa} = %{version}-%{release}
Requires:	%{name}-physics%{?_isa} = %{version}-%{release}
Requires:	%{name}-tree%{?_isa} = %{version}-%{release}
Requires:	%{name}-tree-player%{?_isa} = %{version}-%{release}

%description graf3d-eve7
This package contains a library for defining event displays in ROOT 7.

%package gui-browsable-v7
Summary:	Additional ROOT GUI browsable providers (ROOT 7)
Requires:	%{name}-core%{?_isa} = %{version}-%{release}
Requires:	%{name}-graf-gpadv7%{?_isa} = %{version}-%{release}
Requires:	%{name}-gui-browsable%{?_isa} = %{version}-%{release}
Requires:	%{name}-gui-treemap%{?_isa} = %{version}-%{release}
Requires:	%{name}-hist%{?_isa} = %{version}-%{release}
Requires:	%{name}-tree%{?_isa} = %{version}-%{release}
Requires:	%{name}-tree-ntuple%{?_isa} = %{version}-%{release}
Requires:	%{name}-tree-ntuple-browse%{?_isa} = %{version}-%{release}
#		Package split (gui-browsable-v7 from gui-browsable)
Obsoletes:	%{name}-gui-browsable < 6.32.06

%description gui-browsable-v7
This package contains additional ROOT GUI browsable providers for ROOT 7.

%package gui-browserv7-v7
Summary:	Additional ROOT browser widgets (ROOT 7)
Requires:	%{name}-core%{?_isa} = %{version}-%{release}
Requires:	%{name}-graf-gpadv7%{?_isa} = %{version}-%{release}
Requires:	%{name}-gui-browsable%{?_isa} = %{version}-%{release}
Requires:	%{name}-gui-browserv7%{?_isa} = %{version}-%{release}
#		Package split (gui-browserv7-v7 from gui-browserv7)
Obsoletes:	%{name}-gui-browserv7 < 6.32.06

%description gui-browserv7-v7
This package contains additional ROOT browser widgets for ROOT 7.

%package gui-canvaspainter
Summary:	Canvas painter (ROOT 7)
Requires:	%{name}-core%{?_isa} = %{version}-%{release}
Requires:	%{name}-graf-gpadv7%{?_isa} = %{version}-%{release}
Requires:	%{name}-gui-webdisplay%{?_isa} = %{version}-%{release}
Requires:	%{name}-io%{?_isa} = %{version}-%{release}

%description gui-canvaspainter
This package contains a canvas painter extension for ROOT 7

%package gui-fitpanelv7
Summary:	GUI element for fits in ROOT (ROOT 7)
Requires:	%{name}-core%{?_isa} = %{version}-%{release}
Requires:	%{name}-graf-gpad%{?_isa} = %{version}-%{release}
Requires:	%{name}-graf-gpadv7%{?_isa} = %{version}-%{release}
Requires:	%{name}-gui-webdisplay%{?_isa} = %{version}-%{release}
Requires:	%{name}-hist%{?_isa} = %{version}-%{release}
Requires:	%{name}-io%{?_isa} = %{version}-%{release}
Requires:	%{name}-mathcore%{?_isa} = %{version}-%{release}

%description gui-fitpanelv7
This package contains a library to show a pop-up dialog when fitting
various kinds of data.

%package histv7
Summary:	Histogram library for ROOT 7
Requires:	%{name}-core%{?_isa} = %{version}-%{release}

%description histv7
This package contains a library for histogramming in ROOT 7.
%endif

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -a 1 -a 9

%patch -P0 -p1
%patch -P1 -p1
%patch -P2 -p1
%patch -P3 -p1
%patch -P4 -p1
%patch -P5 -p1
%patch -P6 -p1
%patch -P7 -p1

# Remove bundled sources in order to be sure they are not used
#  * afterimage
rm -rf graf2d/asimage/src/libAfterImage/{libjpeg,libpng,libungif,zlib}
sed '/zlib\/zlib.h/d' -i graf2d/asimage/src/libAfterImage/.depend
#  * ftgl
rm -rf graf3d/ftgl/src graf3d/ftgl/inc
#  * freetype
rm -rf graf2d/freetype/src
#  * glew, lz4, nlohmann, pcre, xxhash, zlib, zstd
rm -rf builtins/glew
rm -rf builtins/lz4
%if ! %{bundlejson}
rm -rf builtins/nlohmann
%endif
rm -rf builtins/pcre
rm -rf builtins/xxhash
rm -rf builtins/zlib
rm -rf builtins/zstd
#  * lzma
rm core/lzma/src/*.tar.gz
#  * gl2ps
rm graf3d/gl/src/gl2ps.cxx graf3d/gl/src/gl2ps/gl2ps.h
#  * unuran
rm math/unuran/src/*.tar.gz
#  * x11 extension headers
rm -rf graf2d/x11/inc/X11
#  * jsroot
rm -rf js/[^f]* js/files/draw.htm js/files/online.htm

# Additional documentation
install -p -m 644 %{SOURCE7} bindings/jupyroot

%build
%if %{?rhel}%{!?rhel:0} == 10
# This package triggers a fault in LLVM when LTO is enabled.  Until LLVM
# is analyzed and fixed, disable LTO
%define _lto_cflags %{nil}
%endif

unset QTDIR
unset QTLIB
unset QTINC

%cmake -DCMAKE_BUILD_TYPE=RelWithDebInfo \
       -DCMAKE_INSTALL_PREFIX:PATH=%{_prefix} \
       -DCMAKE_INSTALL_LIBDIR:PATH=%{_libdir}/%{name} \
       -DCMAKE_INSTALL_PYTHONDIR:PATH=%{python3_sitearch} \
       -DCMAKE_INSTALL_SYSCONFDIR:PATH=%{_datadir}/%{name} \
       -DCMAKE_INSTALL_DOCDIR:PATH=%{_pkgdocdir} \
       -DCMAKE_SKIP_INSTALL_RPATH:BOOL=ON \
       -DPython3_EXECUTABLE:PATH=%{__python3} \
       -Dgnuinstall:BOOL=ON \
       -Dbuiltin_cfitsio:BOOL=OFF \
       -Dbuiltin_civetweb:BOOL=ON \
       -Dbuiltin_clang:BOOL=ON \
       -Dbuiltin_cling:BOOL=ON \
       -Dbuiltin_cppzmq:BOOL=OFF \
       -Dbuiltin_davix:BOOL=OFF \
       -Dbuiltin_fftw3:BOOL=OFF \
       -Dbuiltin_freetype:BOOL=OFF \
       -Dbuiltin_ftgl:BOOL=OFF \
       -Dbuiltin_gif:BOOL=OFF \
       -Dbuiltin_gl2ps:BOOL=OFF \
       -Dbuiltin_glew:BOOL=OFF \
       -Dbuiltin_gsl:BOOL=OFF \
       -Dbuiltin_gtest:BOOL=OFF \
       -Dbuiltin_jpeg:BOOL=OFF \
       -Dbuiltin_llvm:BOOL=ON \
       -Dbuiltin_lz4:BOOL=OFF \
       -Dbuiltin_lzma:BOOL=OFF \
%if %{bundlejson}
       -Dbuiltin_nlohmannjson:BOOL=ON \
%else
       -Dbuiltin_nlohmannjson:BOOL=OFF \
%endif
       -Dbuiltin_openssl:BOOL=OFF \
       -Dbuiltin_openui5:BOOL=ON \
       -Dbuiltin_pcre:BOOL=OFF \
       -Dbuiltin_png:BOOL=OFF \
       -Dbuiltin_tbb:BOOL=OFF \
       -Dbuiltin_unuran:BOOL=OFF \
       -Dbuiltin_vc:BOOL=OFF \
       -Dbuiltin_vdt:BOOL=OFF \
       -Dbuiltin_veccore:BOOL=OFF \
       -Dbuiltin_xrootd:BOOL=OFF \
       -Dbuiltin_xxhash:BOOL=OFF \
       -Dbuiltin_zeromq:BOOL=OFF \
       -Dbuiltin_zlib:BOOL=OFF \
       -Dbuiltin_zstd:BOOL=OFF \
%ifnarch %{ix86} %{arm}
       -Darrow:BOOL=ON \
%else
       -Darrow:BOOL=OFF \
%endif
       -Dasimage:BOOL=ON \
       -Dasimage_tiff:BOOL=ON \
       -Dccache:BOOL=OFF \
       -Ddistcc:BOOL=OFF \
       -Dcefweb:BOOL=OFF \
       -Dcheck_connection:BOOL=OFF \
       -Dclad:BOOL=ON \
       -DCLAD_SOURCE_DIR:PATH=${PWD}/clad-2.2 \
       -Dcocoa:BOOL=OFF \
       -Dcuda:BOOL=OFF \
       -Ddaos:BOOL=OFF \
%if %{dataframe}
       -Ddataframe:BOOL=ON \
%else
       -Ddataframe:BOOL=OFF \
%endif
       -Ddavix:BOOL=ON \
       -Ddcache:BOOL=ON \
       -Ddev:BOOL=OFF \
       -Dexperimental_adaptivecpp=OFF \
       -Dexperimental_genvectorx=OFF \
       -Dfcgi:BOOL=ON \
       -Dfftw3:BOOL=ON \
       -DFIREFOX_EXECUTABLE:PATH=/usr/bin/firefox \
       -Dfitsio:BOOL=ON \
       -Dfortran:BOOL=ON \
       -Dgdml:BOOL=ON \
       -Dgeom:BOOL=ON \
       -Dgeombuilder:BOOL=ON \
       -Dgviz:BOOL=ON \
       -Dhttp:BOOL=ON \
       -Dimt:BOOL=ON \
       -Dlibcxx:BOOL=OFF \
       -Dmathmore:BOOL=ON \
       -Dmemory_termination:BOOL=OFF \
       -Dminuit2_mpi:BOOL=OFF \
       -Dminuit2_omp:BOOL=ON \
       -Dmpi:BOOL=OFF \
       -Dopengl:BOOL=ON \
       -Dpyroot:BOOL=ON \
       -Dpythia8:BOOL=ON \
%ifarch %{qt6_qtwebengine_arches}
       -Dqt6web:BOOL=ON \
%else
       -Dqt6web:BOOL=OFF \
%endif
%if %{rrr}
       -Dr:BOOL=ON \
%else
       -Dr:BOOL=OFF \
%endif
%if %{roofit}
       -Droofit:BOOL=ON \
%if %{roofitmp}
       -Droofit_multiprocess:BOOL=ON \
%else
       -Droofit_multiprocess:BOOL=OFF \
%endif
%else
       -Droofit:BOOL=OFF \
       -Droofit_multiprocess:BOOL=OFF \
%endif
       -Droofit_hs3_ryml:BOOL=OFF \
%if %{root7}
       -Droot7:BOOL=ON \
%else
       -Droot7:BOOL=OFF \
%endif
       -Druby:BOOL=OFF \
       -Druntime_cxxmodules:BOOL=OFF \
       -Dshadowpw:BOOL=ON \
       -Dshared:BOOL=ON \
       -Dsoversion:BOOL=ON \
       -Dspectrum:BOOL=ON \
       -Dsqlite:BOOL=ON \
       -Dssl:BOOL=ON \
       -Dthisroot_scripts:BOOL=OFF \
       -Dtmva:BOOL=ON \
       -Dtmva-cpu:BOOL=ON \
       -Dtmva-cudnn:BOOL=OFF \
       -Dtmva-gpu:BOOL=OFF \
       -Dtmva-pymva:BOOL=ON \
%if %{rrr}
       -Dtmva-rmva:BOOL=ON \
%else
       -Dtmva-rmva:BOOL=OFF \
%endif
%if %{tmvasofieparser}
       -Dtmva-sofie:BOOL=ON \
%else
       -Dtmva-sofie:BOOL=OFF \
%endif
       -Dtpython:BOOL=ON \
       -Dunfold:BOOL=ON \
       -Dunuran:BOOL=ON \
       -During:BOOL=ON \
       -Dvc:BOOL=OFF \
       -Dvdt:BOOL=OFF \
       -Dveccore:BOOL=OFF \
       -Dvecgeom:BOOL=OFF \
       -Dwebgui:BOOL=ON \
       -Dx11:BOOL=ON \
       -Dxml:BOOL=ON \
       -Dxrootd:BOOL=ON \
       -Dfail-on-missing:BOOL=ON \
       -Dtesting:BOOL=ON \
       -Dtestsupport:BOOL=ON \
       -Dtest_distrdf_pyspark:BOOL=OFF \
       -Dtest_distrdf_dask:BOOL=OFF \
       -Dclingtest:BOOL=OFF \
       -Dcoverage:BOOL=OFF \
       -Droottest:BOOL=OFF \
       -Drootbench:BOOL=OFF \
       -Dasan:BOOL=OFF
%cmake_build

%install
%cmake_install

# Let rpm redo the python byte compilation
find %{buildroot}%{python3_sitearch} -depth -type d -name __pycache__ -exec rm -r {} ';'

# Install desktop entry and icon
mkdir -p %{buildroot}%{_datadir}/applications
mkdir -p %{buildroot}%{_datadir}/icons/hicolor/48x48/apps
desktop-file-install --dir=%{buildroot}%{_datadir}/applications %{SOURCE3}
install -p -m 644 %{SOURCE4} %{buildroot}%{_datadir}/icons/hicolor/48x48/apps

# Install mime type and icon
mkdir -p %{buildroot}%{_datadir}/mime/packages
mkdir -p %{buildroot}%{_datadir}/icons/hicolor/48x48/mimetypes
install -p -m 644 %{SOURCE5} %{buildroot}%{_datadir}/mime/packages
install -p -m 644 %{SOURCE6} \
    %{buildroot}%{_datadir}/icons/hicolor/48x48/mimetypes

# Move python cli helper to its own directory
mkdir -p %{buildroot}%{_datadir}/%{name}/cli
mv %{buildroot}%{python3_sitearch}/cmdLineUtils.py \
   %{buildroot}%{_datadir}/%{name}/cli
sed -e '/^\#!/d' -i %{buildroot}%{_datadir}/%{name}/cli/cmdLineUtils.py

# Install GDB pretty printers to auto load safe path
mkdir -p %{buildroot}%{_datadir}/gdb/auto-load%{_libdir}/%{name}
mv %{buildroot}%{_libdir}/%{name}/*-gdb.py \
   %{buildroot}%{_datadir}/gdb/auto-load%{_libdir}/%{name}

# Fix python extension suffix
mv %{buildroot}%{python3_sitearch}/ROOT/libROOTPythonizations.so \
   %{buildroot}%{python3_sitearch}/ROOT/libROOTPythonizations%{python3_ext_suffix}
mv %{buildroot}%{python3_sitearch}/cppyy/libcppyy.so \
   %{buildroot}%{python3_sitearch}/cppyy/libcppyy%{python3_ext_suffix}

# Move noarch python modules to sitelib
if [ "%{python3_sitelib}" != "%{python3_sitearch}" ] ; then
mkdir -p %{buildroot}%{python3_sitelib}
mv %{buildroot}%{python3_sitearch}/JupyROOT %{buildroot}%{python3_sitelib}
%if %{distrdf}
mv %{buildroot}%{python3_sitearch}/DistRDF %{buildroot}%{python3_sitelib}
%endif
fi

# Create .dist-info files so that rpm auto-generates provides
mkdir %{buildroot}%{python3_sitearch}/ROOT-%{version}.dist-info
echo 'Name: ROOT' > \
    %{buildroot}%{python3_sitearch}/ROOT-%{version}.dist-info/METADATA
echo 'Version: %{version}' >> \
    %{buildroot}%{python3_sitearch}/ROOT-%{version}.dist-info/METADATA
mkdir %{buildroot}%{python3_sitelib}/JupyROOT-%{version}.dist-info
echo 'Name: JupyROOT' > \
    %{buildroot}%{python3_sitelib}/JupyROOT-%{version}.dist-info/METADATA
echo 'Version: %{version}' >> \
    %{buildroot}%{python3_sitelib}/JupyROOT-%{version}.dist-info/METADATA
%if %{distrdf}
mkdir %{buildroot}%{python3_sitelib}/DistRDF-%{version}.dist-info
echo 'Name: DistRDF' > \
    %{buildroot}%{python3_sitelib}/DistRDF-%{version}.dist-info/METADATA
echo 'Version: %{version}' >> \
    %{buildroot}%{python3_sitelib}/DistRDF-%{version}.dist-info/METADATA
%endif

# Put jupyter stuff in the right places
mkdir -p %{buildroot}%{_datadir}/jupyter/kernels

cp -pr %{buildroot}%{_datadir}/%{name}/notebook/kernels/root \
   %{buildroot}%{_datadir}/jupyter/kernels/python3-jupyroot
sed -e 's!python[0-9]*\.[0-9]*!%{__python3}!' \
    -i %{buildroot}%{_datadir}/jupyter/kernels/python3-jupyroot/kernel.json
sed -e '/^\#!/d' \
    -i %{buildroot}%{python3_sitelib}/JupyROOT/kernel/rootkernel.py

rm -rf %{buildroot}%{_datadir}/%{name}/notebook/custom
rm -rf %{buildroot}%{_datadir}/%{name}/notebook/html
rm -rf %{buildroot}%{_datadir}/%{name}/notebook/kernels
rm     %{buildroot}%{_datadir}/%{name}/notebook/jupyter_notebook_config.py
rmdir  %{buildroot}%{_datadir}/%{name}/notebook

# Replace the rootnb.exe wrapper with a simpler one
cat > %{buildroot}%{_bindir}/rootnb.exe << EOF
#! /bin/sh
if [ -z "\$(type jupyter 2>/dev/null)" ] ; then
   echo jupyter not found in path. Exiting.
   exit 1
fi
if [ -z "\$(type jupyter-notebook 2>/dev/null)" ] ; then
   echo jupyter-notebook not found in path. Exiting.
   exit 1
fi
jupyter notebook "\$@"
EOF

# Avoid /usr/bin/env shebangs (and adapt cli to cmdLineUtils location)
sed -e 's!/usr/bin/env bash!/bin/bash!' \
    -i %{buildroot}%{_bindir}/root-config \
       %{buildroot}%{_bindir}/rootssh
sed -e 's!/usr/bin/env python3!%{__python3}!' \
    -e '/import sys/d' \
    -e '/import cmdLineUtils/iimport sys' \
    -e '/import cmdLineUtils/isys.path.insert(0, "%{_datadir}/%{name}/cli")' \
    -i %{buildroot}%{_bindir}/rootbrowse \
       %{buildroot}%{_bindir}/rootcp \
       %{buildroot}%{_bindir}/rooteventselector \
       %{buildroot}%{_bindir}/rootls \
       %{buildroot}%{_bindir}/rootmkdir \
       %{buildroot}%{_bindir}/rootmv \
       %{buildroot}%{_bindir}/rootprint \
       %{buildroot}%{_bindir}/rootrm \
       %{buildroot}%{_bindir}/rootslimtree
sed -e 's!/usr/bin/env python3!%{__python3}!' \
    -i %{buildroot}%{_bindir}/rootdrawtree
sed -e 's!/usr/bin/env python!%{__python3}!' \
    -i %{buildroot}%{_datadir}/%{name}/dictpch/makepch.py
sed -e 's!/usr/bin/python!%{__python3}!' \
    -i %{buildroot}%{_datadir}/%{name}/pdg_table_update.py

# Remove some junk
rm %{buildroot}%{_datadir}/%{name}/root.desktop
rm %{buildroot}%{_pkgdocdir}/INSTALL
rm %{buildroot}%{_pkgdocdir}/README.CXXMODULES.md
rm -rf %{buildroot}%{_datadir}/%{name}/html

# Only used on Windows
rm %{buildroot}%{_datadir}/%{name}/macros/fileopen.C

# Remove plugin definitions for non-built and obsolete plugins
pushd %{buildroot}%{_datadir}/%{name}/plugins
%if ! %{rrr}
rm ROOT@@Math@@Minimizer/P090_RMinimizer.C
%endif
rm TGLManager/P020_TGWin32GLManager.C
rm TGLManager/P030_TGOSXGLManager.C
rm TVirtualGeoConverter/P010_TGeoVGConverter.C
rm TVirtualGLImp/P020_TGWin32GL.C
rm TVirtualX/P030_TGWin32.C
rm TVirtualX/P050_TGQuartz.C
rmdir TVirtualGeoConverter
popd

# Replace bundled jsroot with symlinks to system version
for x in build img mathjax modules scripts files/draw.htm files/online.htm ; do
    ln -nrs %{buildroot}%{_jsdir}/jsroot/$x \
	    %{buildroot}%{_datadir}/%{name}/js/$x
done

# Create ldconfig configuration
mkdir -p %{buildroot}%{_sysconfdir}/ld.so.conf.d
echo %{_libdir}/%{name} > \
     %{buildroot}%{_sysconfdir}/ld.so.conf.d/%{name}-%{_arch}.conf

# Make ROOTConfig-targets.cmake not error on missing files to work better with
# subpackages
sed -e 's/FATAL_ERROR \(.*imported\)/WARNING \1/' \
    -e '/Possible reasons include/i\
but this file does not exist.\
If this target is used you need to install the package that provides this\
file using \\"dnf install\\".\
If this target is not used this warning can be ignored.'$'\x22'')' \
    -e '/Possible reasons include/,/)/d' \
    -i %{buildroot}%{_datadir}/%{name}/cmake/ROOTConfig-targets.cmake

# Create includelist files ...
for f in `find %{_vpath_builddir} -name cmake_install.cmake -a '!' -path '*/llvm-project/*'` ; do
    l=`sed 's!%{_vpath_builddir}/\(.*\)/cmake_install.cmake!includelist-\1!' <<< $f`
    l=`tr / - <<< $l`
    tmpdir=`mktemp -d`
    DESTDIR=$tmpdir cmake -DCMAKE_INSTALL_COMPONENT=headers -P $f > /dev/null
    ( cd $tmpdir ; find . -type f) | sort | sed 's!^\.!!' > $l
    rm -rf $tmpdir
done

# ... and merge some of them
cat includelist-core-{[^mw],m[^au]}* > includelist-core
cat includelist-graf2d-x11ttf >> includelist-graf2d-x11
cat includelist-graf3d-rglew >> includelist-graf3d-gl

# Do python byte compilation (for non-standard paths)
%py_byte_compile %{__python3} %{buildroot}%{_datadir}/%{name}/cli
%py_byte_compile %{__python3} %{buildroot}%{_datadir}/gdb/auto-load%{_libdir}/%{name}

%check
pushd %{_vpath_builddir}
pushd test
ln -s ../../files files
popd
pushd runtutorials
ln -s ../../files files
ln -s ../../files/tutorials/df014_CsvDataSource_MuRun2010B.csv CsvDataSource_MuRun2010B.csv
ln -s ../../files/usa.root usa.root
popd
popd

# Exclude some tests that can not be run
#
# - test-stressIOPlugins-*
#   requires network access (by design since they test the remote file IO)
#
# - tutorial-analysis-dataframe-df101_h1Analysis
# - tutorial-analysis-tree-run_h1analysis
# - tutorial-legacy-multicore-mp104_processH1
#   requires network access: http://root.cern.ch/files/h1/
#
# - tutorial-io-tree-imt_parTreeProcessing
#   requires input data: http://root.cern.ch/files/tp_process_imt.root (707 MB)
#
# - tutorial-analysis-dataframe-df###_SQlite*
#   reads sqlite data over network:
#   http://root.cern.ch/files/root_download_stats.sqlite
#
# - tutorial-analysis-dataframe-df033_Describe-py
# - tutorial-analysis-dataframe-df102_NanoAODDimuonAnalysis(-py)?
#   reads input data over network:
#   root://eospublic.cern.ch//eos/opendata/cms/derived-data/
#   AOD2NanoAODOutreachTool/Run2012BC_DoubleMuParked_Muons.root
#
# - gtest-tree-treeplayer-treeprocessormt-remotefiles
# - tutorial-analysis-dataframe-df103_NanoAODHiggsAnalysis(-py)?
#   reads input data over network:
#   root://eospublic.cern.ch//eos/root-eos/cms_opendata_2012_nanoaod/
#
# - tutorial-analysis-dataframe-df104_HiggsToTwoPhotons-py
# - tutorial-analysis-dataframe-df105_WBosonAnalysis-py
# - tutorial-analysis-dataframe-df106_HiggsToFourLeptons(-py)
# - tutorial-analysis-dataframe-df107_SingleTopAnalysis-py
# - tutorial-visualisation-rcanvas-df104-py
# - tutorial-visualisation-rcanvas-df105-py
#   reads input data over network:
#   root://eospublic.cern.ch//eos/opendata/atlas/OutreachDatasets/2020-01-22/
#
# - tutorial-io-ntuple-ntpl004_dimuon
#   reads input data over network
#   http://root.cern.ch/files/NanoAOD_DoubleMuon_CMS2011OpenData.root (1.5 GB)
#
# - tutorial-io-ntuple-ntpl008_import
#   reads input data over network
#   http://root.cern.ch/files/HiggsTauTauReduced/GluGluToHToTauTau.root (20 MB)
#
# - tutorial-io-ntuple-ntpl011_global_temperatures
#   reads input data over network
#   http://root.cern.ch/files/tutorials/GlobalLandTemperaturesByCity.csv
#
# - gtest-net-davix-RRawFileDavix
#   reads input file over network
#   http://root.cern.ch/files/davix.test
#
# - gtest-net-netxng-RRawFileNetXNG
#   reads input file over network
#   root://eospublic.cern.ch/eos/root-eos/xrootd.test
#
# - gtest-net-netxng-TNetXNGFileTest
# - tutorial-analysis-parallel-mp_processSelector
#   reads input file over network
#   root://eospublic.cern.ch/eos/root-eos/h1/dstarmb.root
#
# - tutorial-machine_learning-tmva100_DataPreparation-py
#   reads input data over network
#   root://eospublic.cern.ch/eos/root-eos/cms_opendata_2012_nanoaod/SMHiggsToZZTo4L.root
#
# - test-webgui-ping
#   error: Cannot display window in native
#
# - test-stressgraphics-firefox-skip3d:
#   requires firefox...
#
# - test-stressgraphics-svg
#   Font metric differences
#
# - tutorial-visualisation-webcanv-fonts_ttf.cxx:
#   Requires web graphics
excluded="\
test-stressIOPlugins|\
tutorial-analysis-dataframe-df101_h1Analysis|\
tutorial-analysis-tree-run_h1analysis|\
tutorial-legacy-multicore-mp104_processH1|\
tutorial-io-tree-imt_parTreeProcessing|\
tutorial-analysis-dataframe-df..._SQlite|\
tutorial-analysis-dataframe-df033_Describe-py|\
tutorial-analysis-dataframe-df102_NanoAODDimuonAnalysis|\
gtest-tree-treeplayer-treeprocessormt-remotefiles|\
tutorial-analysis-dataframe-df103_NanoAODHiggsAnalysis|\
tutorial-analysis-dataframe-df104_HiggsToTwoPhotons-py|\
tutorial-analysis-dataframe-df105_WBosonAnalysis-py|\
tutorial-analysis-dataframe-df106_HiggsToFourLeptons|\
tutorial-analysis-dataframe-df107_SingleTopAnalysis-py|\
tutorial-visualisation-rcanvas-df104-py|\
tutorial-visualisation-rcanvas-df105-py|\
tutorial-io-ntuple-ntpl004_dimuon|\
tutorial-io-ntuple-ntpl008_import|\
tutorial-io-ntuple-ntpl011_global_temperatures|\
gtest-net-davix-RRawFileDavix|\
gtest-net-netxng-RRawFileNetXNG|\
gtest-net-netxng-TNetXNGFileTest|\
tutorial-analysis-parallel-mp_processSelector|\
tutorial-machine_learning-tmva100_DataPreparation-py|\
test-webgui-ping|\
test-stressgraphics-firefox-skip3d|\
test-stressgraphics-svg|\
tutorial-visualisation-webcanv-fonts_ttf.cxx"

%ifarch %{ix86}
# - gtest-hist-hist-TFormulaGradientTests
#   out of memory
#
# - tmva-sofie-test-TestCustomModelsFromONNX
#   Expected equality of these values:
#     output.size()
#       Which is: 1000
#     sizeof(Slice_Neg::output) / sizeof(float)
#       Which is: 900
excluded="${excluded}|\
gtest-hist-hist-TFormulaGradientTests|\
tmva-sofie-test-TestCustomModelsFromONNX\$\$"
%endif

%ifarch %{power64}
%if %{?fedora}%{!?fedora:0} >= 42
# - gtest-tree-ntuple-ntuple-emulated
# - gtest-tree-ntuple-ntuple-evolution-shape
#   waitpid() failed
excluded="${excluded}|\
gtest-tree-ntuple-ntuple-emulated|\
gtest-tree-ntuple-ntuple-evolution-shape"
%endif
%endif

%ifarch s390x
# - gtest-roofit-roofitcore-testNaNPacker
# - gtest-roofit-roofitcore-testLikelihoodGradientJob
#   Uses "Packed NaN" feature, not implemented for big endian.
excluded="${excluded}|\
gtest-roofit-roofitcore-testNaNPacker|\
gtest-roofit-roofitcore-testLikelihoodGradientJob"

# - gtest-core-dictgen-dictgen-base
# - gtest-tree-dataframe-dataframe-concurrency
# - gtest-tree-dataframe-dataframe-snapshot-ntuple
# - gtest-tree-dataframe-dataframe-unified-constructor
# - gtest-tree-dataframe-dataframe-vary
# - gtest-tree-dataframe-datasource-ntuple
# - gtest-tree-ntuple-ntuple-basics
# - gtest-tree-ntuple-ntuple-bulk
# - gtest-tree-ntuple-ntuple-cast
# - gtest-tree-ntuple-ntuple-compat
# - gtest-tree-ntuple-ntuple-evolution-type
# - gtest-tree-ntuple-ntuple-extended
# - gtest-tree-ntuple-ntuple-join-table
# - gtest-tree-ntuple-ntuple-largefile2
# - gtest-tree-ntuple-ntuple-merger
# - gtest-tree-ntuple-ntuple-metrics
# - gtest-tree-ntuple-ntuple-model
# - gtest-tree-ntuple-ntuple-modelext
# - gtest-tree-ntuple-ntuple-multi-column
# - gtest-tree-ntuple-ntuple-packing
# - gtest-tree-ntuple-ntuple-parallel-writer
# - gtest-tree-ntuple-ntuple-processor
# - gtest-tree-ntuple-ntuple-processor-chain
# - gtest-tree-ntuple-ntuple-processor-join
# - gtest-tree-ntuple-ntuple-project
# - gtest-tree-ntuple-ntuple-show
# - gtest-tree-ntuple-ntuple-storage
# - gtest-tree-ntuple-ntuple-storage-daos
# - gtest-tree-ntuple-ntuple-types
# - gtest-tree-ntuple-ntuple-view
# - gtest-tree-ntuple-rfield-class
# - gtest-tree-ntuple-rfield-streamer
# - gtest-tree-ntuple-rfield-variant
# - gtest-tree-ntuple-rfield-vector
# - gtest-tree-ntupleutil-ntuple-importer
# - gtest-tree-ntupleutil-ntuple-inspector
# - gtest-tree-tree-testTTreeRegressions
#   https://github.com/root-project/root/issues/12426
#
# - pyunittests-bindings-distrdf-backend-distrdf-unit-backend-graph-caching
# - pyunittests-bindings-pyroot-pythonizations-pyroot-pyz-rtensor
# - pyunittests-bindings-pyroot-pythonizations-pyroot-pyz-stl-vector
# - pyunittests-io-io-rfile-py
# - tmva-sofie-test-TestCustomModelsFromONNX
# - tutorial-analysis-dataframe-df006_ranges-py
# - tutorial-hist-hist007_TH1_liveupdate-py
# - tutorial-math-exampleFunction-py
# - tutorial-math-fit-combinedFit-py
# - tutorial-math-fit-NumericalMinimization-py
# - tutorial-visualisation-rcanvas-rbox-py
#   https://github.com/root-project/root/issues/12429
#
# - test-stresshistofit
# - test-stresshistofit-interpreted
# - test-stresshistogram
# - test-stresshistogram-interpreted
excluded="${excluded}|\
gtest-core-dictgen-dictgen-base|\
gtest-tree-dataframe-dataframe-concurrency|\
gtest-tree-dataframe-dataframe-snapshot-ntuple|\
gtest-tree-dataframe-dataframe-unified-constructor|\
gtest-tree-dataframe-dataframe-vary|\
gtest-tree-dataframe-datasource-ntuple|\
gtest-tree-ntuple-ntuple-basics|\
gtest-tree-ntuple-ntuple-bulk|\
gtest-tree-ntuple-ntuple-cast|\
gtest-tree-ntuple-ntuple-compat|\
gtest-tree-ntuple-ntuple-evolution-type|\
gtest-tree-ntuple-ntuple-extended|\
gtest-tree-ntuple-ntuple-join-table|\
gtest-tree-ntuple-ntuple-largefile2|\
gtest-tree-ntuple-ntuple-merger|\
gtest-tree-ntuple-ntuple-metrics|\
gtest-tree-ntuple-ntuple-model\$\$|\
gtest-tree-ntuple-ntuple-modelext|\
gtest-tree-ntuple-ntuple-multi-column|\
gtest-tree-ntuple-ntuple-packing|\
gtest-tree-ntuple-ntuple-parallel-writer|\
gtest-tree-ntuple-ntuple-processor\$\$|\
gtest-tree-ntuple-ntuple-processor-chain|\
gtest-tree-ntuple-ntuple-processor-join|\
gtest-tree-ntuple-ntuple-project|\
gtest-tree-ntuple-ntuple-show|\
gtest-tree-ntuple-ntuple-storage\$\$|\
gtest-tree-ntuple-ntuple-storage-daos|\
gtest-tree-ntuple-ntuple-types|\
gtest-tree-ntuple-ntuple-view|\
gtest-tree-ntuple-rfield-class|\
gtest-tree-ntuple-rfield-streamer|\
gtest-tree-ntuple-rfield-variant|\
gtest-tree-ntuple-rfield-vector|\
gtest-tree-ntupleutil-ntuple-importer|\
gtest-tree-ntupleutil-ntuple-inspector|\
gtest-tree-tree-testTTreeRegressions|\
pyunittests-bindings-distrdf-backend-distrdf-unit-backend-graph-caching|\
pyunittests-bindings-pyroot-pythonizations-pyroot-pyz-rtensor|\
pyunittests-bindings-pyroot-pythonizations-pyroot-pyz-stl-vector|\
pyunittests-io-io-rfile-py|\
tmva-sofie-test-TestCustomModelsFromONNX|\
tutorial-analysis-dataframe-df006_ranges-py|\
tutorial-hist-hist007_TH1_liveupdate-py|\
tutorial-math-exampleFunction-py|\
tutorial-math-fit-combinedFit-py|\
tutorial-math-fit-NumericalMinimization-py|\
tutorial-visualisation-rcanvas-rbox-py|\
test-stresshistofit\$\$|\
test-stresshistofit-interpreted|\
test-stresshistogram\$\$|\
test-stresshistogram-interpreted"

# The zlib-ng library is compiled with hardware acceleration support on s390x
# in Fedora 43 and later and RHEL 10.1 and later
# This means that some tests that compare the size of compressed data fail.
# - test-stress
# - gtest-tree-readspeed-readspeed-general
# - gtest-tree-tree-testTBranch
%if %{?fedora}%{!?fedora:0} >= 43 || %{?rhel}%{!?rhel:0} >= 10
excluded="${excluded}|\
test-stress\$\$|\
gtest-tree-readspeed-readspeed-general|\
gtest-tree-tree-testTBranch"
%endif
%endif

# Fails with gcc 14 on aarch64, ppc64le and s390x (on EPEL 10 also x86_64)
# https://github.com/root-project/root/issues/14446
# - gtest-math-matrix-testMatrixTSparse
%if %{?fedora}%{!?fedora:0} >= 40
%ifarch aarch64 %{power64} s390x
excluded="${excluded}|\
gtest-math-matrix-testMatrixTSparse"
%endif
%endif
%if %{?rhel}%{!?rhel:0} >= 10
excluded="${excluded}|\
gtest-math-matrix-testMatrixTSparse"
%endif

# Test failures with GCC 16 on AArch64
# https://bugzilla.redhat.com/show_bug.cgi?id=2440537
# https://github.com/root-project/root/issues/21565
%if %{?fedora}%{!?fedora:0} >= 44
%ifarch aarch64
excluded="${excluded}|\
gtest-tree-ntuple-ntuple-cast|\
gtest-tree-ntuple-ntuple-join-table|\
gtest-tree-ntuple-ntuple-packing|\
gtest-tree-ntuple-ntuple-show|\
gtest-tree-ntuple-ntuple-types|\
gtest-tree-ntuple-ntuple-view|\
gtest-tree-ntupleutil-ntuple-importer"
%endif
%endif

# Filter out parts of tests that require remote network access
# RNTuple.StdAtomic fails on ix86 (different alignment 64 bit (non)atomic)
# InterpreterTest.Evaluate fails on s390x
# TClingDataMemberInfo.Offset fails on s390x
# https://github.com/root-project/root/issues/14512
# TTreeRegressions.PrintClustersRounding
# relies on specific versions of compression libraries
# https://github.com/root-project/root/issues/18995
export GTEST_FILTER=-\
%ifarch %{ix86}
RNTuple.StdAtomic:\
%endif
%ifarch s390x
InterpreterTest.Evaluate:\
TClingDataMemberInfo.Offset:\
TTreeReaderBasic.LorentzVector32:\
%endif
RCsvDS.Remote:\
RFile.RemoteRead:\
RNTuple.OpenHTTP:\
RRawFile.Remote:\
RSqliteDS.Davix:\
TChainParsing.DoubleSlash:\
TChainParsing.RemoteGlob:\
TFile.ReadWithoutGlobalRegistrationNet:\
TFile.ReadWithoutGlobalRegistrationWeb:\
TTreeRegressions.PrintClustersRounding
%ctest -- -E "${excluded}"

%pretrans net-http -p <lua>
path = "%{_datadir}/%{name}/js"
st = posix.stat(path)
if st and st.type == "link" then
    os.remove(path)
end

%post net-http
# Replace bundled jsroot with symlinks to system version
for x in build img mathjax modules scripts files/draw.htm files/online.htm ; do
    ln -fnrs %{_jsdir}/jsroot/$x %{_datadir}/%{name}/js/$x
done

%pre -n python3-%{name}
if [ -r /var/lib/alternatives/libPyROOT.so ] ; then
    for alt in `grep python3.*/.*.so /var/lib/alternatives/libPyROOT.so` ; do
	%{_sbindir}/update-alternatives --remove libPyROOT.so $alt
    done
fi

%post -n python3-jupyroot
mkdir -p /etc/jupyter
if [ -e /etc/jupyter/jupyter_notebook_config.py ] ; then
    sed '/Extra static paths for JupyROOT - start/','/Extra static paths for JupyROOT - end/'d -i /etc/jupyter/jupyter_notebook_config.py
fi
cat << EOF >> /etc/jupyter/jupyter_notebook_config.py
# Extra static paths for JupyROOT - start - do not remove this line
c.NotebookApp.extra_static_paths.append('%{_jsdir}/jsroot')
# Extra static paths for JupyROOT - end - do not remove this line
EOF
if [ -e /etc/jupyter/jupyter_server_config.py ] ; then
    sed '/Extra static paths for JupyROOT - start/','/Extra static paths for JupyROOT - end/'d -i /etc/jupyter/jupyter_server_config.py
fi
cat << EOF >> /etc/jupyter/jupyter_server_config.py
# Extra static paths for JupyROOT - start - do not remove this line
c.ServerApp.extra_static_paths.append('%{_jsdir}/jsroot')
# Extra static paths for JupyROOT - end - do not remove this line
EOF

%postun -n python3-jupyroot
if [ $1 -eq 0 ] ; then
    if [ -e /etc/jupyter/jupyter_notebook_config.py ] ; then
	sed '/Extra static paths for JupyROOT - start/','/Extra static paths for JupyROOT - end/'d -i /etc/jupyter/jupyter_notebook_config.py
	if [ ! -s /etc/jupyter/jupyter_notebook_config.py ] ; then
	    rm /etc/jupyter/jupyter_notebook_config.py
	    rmdir /etc/jupyter 2>/dev/null || :
	fi
    fi
    if [ -e /etc/jupyter/jupyter_server_config.py ] ; then
	sed '/Extra static paths for JupyROOT - start/','/Extra static paths for JupyROOT - end/'d -i /etc/jupyter/jupyter_server_config.py
	if [ ! -s /etc/jupyter/jupyter_server_config.py ] ; then
	    rm /etc/jupyter/jupyter_server_config.py
	    rmdir /etc/jupyter 2>/dev/null || :
	fi
    fi
fi

%post core -p /sbin/ldconfig
%postun core -p /sbin/ldconfig

%files
%{_bindir}/hadd
%{_bindir}/root
%{_bindir}/root.exe
%{_bindir}/rootbrowse
%{_bindir}/rootls
%{_bindir}/rootn.exe
%{_bindir}/rootreadspeed
%{_bindir}/roots
%{_bindir}/roots.exe
%{_bindir}/rootssh
%{_mandir}/man1/hadd.1*
%{_mandir}/man1/root.1*
%{_mandir}/man1/root.exe.1*
%{_mandir}/man1/rootn.exe.1*
%{_mandir}/man1/roots.exe.1*
%{_datadir}/applications/root.desktop
%{_datadir}/icons/hicolor/48x48/apps/root.png
%{_datadir}/icons/hicolor/48x48/mimetypes/application-x-root.png
%{_datadir}/mime/packages/root.xml

%files icons
%{_datadir}/%{name}/icons

%files font-files
%{_datadir}/%{name}/fonts

%files tutorial
%doc %{_pkgdocdir}/tutorials

%files core -f includelist-core
%{_bindir}/rmkdepend
%{_bindir}/root-config
%{_mandir}/man1/rmkdepend.1*
%{_mandir}/man1/root-config.1*
%dir %{_libdir}/%{name}
%{_libdir}/%{name}/libCore.*
%{_libdir}/%{name}/libImt.*
%{_libdir}/%{name}/libNew.*
%{_libdir}/%{name}/libRint.*
%{_libdir}/%{name}/libThread.*
%{_libdir}/%{name}/lib*Dict.*
%dir %{_datadir}/gdb/auto-load%{_libdir}/%{name}
%{_datadir}/gdb/auto-load%{_libdir}/%{name}/libCore.*
%dir %{_datadir}/gdb/auto-load%{_libdir}/%{name}/__pycache__
%{_datadir}/gdb/auto-load%{_libdir}/%{name}/__pycache__/libCore.*
%dir %{_datadir}/%{name}
%{_datadir}/%{name}/allDict.cxx.pch
%{_datadir}/%{name}/class.rules
%{_datadir}/%{name}/gdb-backtrace.sh
%{_datadir}/%{name}/gitinfo.txt
%{_datadir}/%{name}/helgrind-root.supp
%{_datadir}/%{name}/lsan-root.supp
%{_datadir}/%{name}/Makefile.arch
%{_datadir}/%{name}/root.mimes
%{_datadir}/%{name}/system.rootauthrc
%{_datadir}/%{name}/system.rootdaemonrc
%{_datadir}/%{name}/system.rootrc
%{_datadir}/%{name}/valgrind-root.supp
%{_datadir}/%{name}/valgrind-root-python.supp
%{_mandir}/man1/system.rootdaemonrc.1*
%dir %{_datadir}/%{name}/cmake
%{_datadir}/%{name}/cmake/*.cmake
%dir %{_datadir}/%{name}/cmake/modules
%{_datadir}/%{name}/cmake/modules/*.cmake
%dir %{_datadir}/%{name}/macros
%{_datadir}/%{name}/macros/Dialogs.C
%dir %{_datadir}/%{name}/plugins
%dir %{_datadir}/%{name}/plugins/*
%dir %{_includedir}/%{name}
%if %{bundlejson}
%dir %{_includedir}/%{name}/nlohmann
%{_includedir}/%{name}/nlohmann/json.hpp
%endif
%{_includedir}/%{name}/RConfigOptions.h
%{_includedir}/%{name}/RConfigure.h
%{_includedir}/%{name}/ROOT.modulemap
%{_includedir}/%{name}/compiledata.h
%dir %{_includedir}/%{name}/Math
%dir %{_includedir}/%{name}/ROOT
%config(noreplace) %{_sysconfdir}/ld.so.conf.d/%{name}-%{_arch}.conf
%dir %{_pkgdocdir}
# CREDITS and LICENSE are used at runtime by the .credits and .license commands
# They therefore should not be marked doc.
%{_pkgdocdir}/CREDITS
%{_pkgdocdir}/LICENSE
%doc %{_pkgdocdir}/DEVELOPMENT.md
%doc %{_pkgdocdir}/ReleaseNotes
%doc %{_pkgdocdir}/root_citation.bib
%license LICENSE LGPL2_1.txt

%files multiproc -f includelist-core-multiproc
%{_libdir}/%{name}/libMultiProc.*

%files cling
%{_bindir}/genreflex
%{_bindir}/rootcint
%{_bindir}/rootcling
%{_mandir}/man1/rootcling.1*
%{_libdir}/%{name}/libCling.*
%{_datadir}/%{name}/cling
%{_datadir}/%{name}/dictpch
%doc interpreter/cling/CREDITS.txt
%doc interpreter/cling/README.md
%license interpreter/cling/LICENSE.TXT

%files testsupport
%{_includedir}/%{name}/ROOT/TestSupport.hxx
%{_libdir}/%{name}/TestSupport
%doc core/testsupport/README.md

%files tpython -f includelist-bindings-tpython
%{_libdir}/%{name}/libROOTTPython.*
%{_libdir}/%{name}/libROOTTPython_rdict.pcm

%files -n python3-%{name} -f includelist-bindings-pyroot
%{python3_sitearch}/cppyy
%{python3_sitearch}/ROOT
%{python3_sitearch}/ROOT-*.dist-info
%{_libdir}/%{name}/libCPyCppyy.*
%dir %{_includedir}/%{name}/CPyCppyy

%files -n python3-jupyroot
%{python3_sitelib}/JupyROOT
%{python3_sitelib}/JupyROOT-*.dist-info
%{_datadir}/jupyter/kernels/python3-jupyroot
%{_bindir}/rootnb.exe
%doc bindings/jupyroot/README.md
%doc bindings/jupyroot/JupyROOT-on-EPEL

%if %{distrdf}
%files -n python3-distrdf
%{python3_sitelib}/DistRDF
%{python3_sitelib}/DistRDF-*.dist-info
%endif

%if %{rrr}
%files r -f includelist-bindings-r
%{_libdir}/%{name}/libRInterface.*
%{_libdir}/%{name}/libRInterface_rdict.pcm
%doc bindings/r/doc/users-guide/*.md

%files r-tools -f includelist-math-rtools
%{_libdir}/%{name}/libRtools.*
%{_libdir}/%{name}/libRtools_rdict.pcm
%{_datadir}/%{name}/plugins/ROOT@@Math@@Minimizer/P090_RMinimizer.C
%endif

%files genetic -f includelist-math-genetic
%{_libdir}/%{name}/libGenetic.*
%{_libdir}/%{name}/libGenetic_rdict.pcm
%{_datadir}/%{name}/plugins/ROOT@@Math@@Minimizer/P080_GeneticMinimizer.C

%files geom -f includelist-geom-geom
%{_libdir}/%{name}/libGeom.*
%{_libdir}/%{name}/libGeom_rdict.pcm
%{_datadir}/%{name}/RadioNuclides.txt

%files geom-builder -f includelist-geom-geombuilder
%{_libdir}/%{name}/libGeomBuilder.*
%{_libdir}/%{name}/libGeomBuilder_rdict.pcm
%{_datadir}/%{name}/plugins/TGeoManagerEditor/P010_TGeoManagerEditor.C

%files geom-painter -f includelist-geom-geompainter
%{_libdir}/%{name}/libGeomPainter.*
%{_libdir}/%{name}/libGeomPainter_rdict.pcm
%{_datadir}/%{name}/plugins/TVirtualGeoPainter/P010_TGeoPainter.C

%files gdml -f includelist-geom-gdml
%{_libdir}/%{name}/libGdml.*
%{_libdir}/%{name}/libGdml_rdict.pcm

%files graf -f includelist-graf2d-graf
%{_libdir}/%{name}/libGraf.*
%{_libdir}/%{name}/libGraf_rdict.pcm
%{_datadir}/%{name}/plugins/TMinuitGraph/P010_TGraph.C

%files graf-asimage -f includelist-graf2d-asimage
%{_libdir}/%{name}/libASImage.*
%{_libdir}/%{name}/libASImage_rdict.pcm
%{_libdir}/%{name}/libASImageGui.*
%{_libdir}/%{name}/libASImageGui_rdict.pcm
%{_datadir}/%{name}/plugins/TImage/P010_TASImage.C
%{_datadir}/%{name}/plugins/TImagePlugin/P010_TASPluginGS.C
%{_datadir}/%{name}/plugins/TPaletteEditor/P010_TASPaletteEditor.C

%files graf-fitsio -f includelist-graf2d-fitsio
%{_libdir}/%{name}/libFITSIO.*
%{_libdir}/%{name}/libFITSIO_rdict.pcm

%files graf-gpad -f includelist-graf2d-gpad
%{_libdir}/%{name}/libGpad.*
%{_libdir}/%{name}/libGpad_rdict.pcm
%{_datadir}/%{name}/plugins/TVirtualPad/P010_TPad.C

%files graf-gviz -f includelist-graf2d-gviz
%{_libdir}/%{name}/libGviz.*
%{_libdir}/%{name}/libGviz_rdict.pcm

%files graf-postscript -f includelist-graf2d-postscript
%{_libdir}/%{name}/libPostscript.*
%{_libdir}/%{name}/libPostscript_rdict.pcm
%{_datadir}/%{name}/plugins/TVirtualPS/P010_TPostScript.C
%{_datadir}/%{name}/plugins/TVirtualPS/P020_TSVG.C
%{_datadir}/%{name}/plugins/TVirtualPS/P030_TPDF.C
%{_datadir}/%{name}/plugins/TVirtualPS/P040_TImageDump.C
%{_datadir}/%{name}/plugins/TVirtualPS/P050_TTeXDump.C

%files graf-x11 -f includelist-graf2d-x11
%{_libdir}/%{name}/libGX11.*
%{_libdir}/%{name}/libGX11_rdict.pcm
%{_libdir}/%{name}/libGX11TTF.*
%{_libdir}/%{name}/libGX11TTF_rdict.pcm
%{_datadir}/%{name}/plugins/TVirtualX/P010_TGX11.C
%{_datadir}/%{name}/plugins/TVirtualX/P020_TGX11TTF.C

%files graf3d -f includelist-graf3d-g3d
%{_libdir}/%{name}/libGraf3d.*
%{_libdir}/%{name}/libGraf3d_rdict.pcm
%{_datadir}/%{name}/plugins/TView/P010_TView3D.C

%files graf3d-csg -f includelist-graf3d-csg
%{_libdir}/%{name}/libRCsg.*
%{_libdir}/%{name}/libRCsg_rdict.pcm

%files graf3d-eve -f includelist-graf3d-eve
%{_libdir}/%{name}/libEve.*
%{_libdir}/%{name}/libEve_rdict.pcm

%files graf3d-gl -f includelist-graf3d-gl
%{_libdir}/%{name}/libRGL.*
%{_libdir}/%{name}/libRGL_rdict.pcm
%{_datadir}/%{name}/plugins/TGLHistPainter/P010_TGLHistPainter.C
%{_datadir}/%{name}/plugins/TGLManager/P010_TX11GLManager.C
%{_datadir}/%{name}/plugins/TVirtualGLImp/P010_TX11GL.C
%{_datadir}/%{name}/plugins/TVirtualPadPainter/P010_TGLPadPainter.C
%{_datadir}/%{name}/plugins/TVirtualViewer3D/P020_TGLSAViewer.C
%{_datadir}/%{name}/plugins/TVirtualViewer3D/P030_TGLViewer.C

%files graf3d-gviz3d -f includelist-graf3d-gviz3d
%{_libdir}/%{name}/libGviz3d.*
%{_libdir}/%{name}/libGviz3d_rdict.pcm

%files graf3d-x3d -f includelist-graf3d-x3d
%{_libdir}/%{name}/libX3d.*
%{_libdir}/%{name}/libX3d_rdict.pcm
%{_datadir}/%{name}/plugins/TViewerX3D/P010_TViewerX3D.C
%{_datadir}/%{name}/plugins/TVirtualViewer3D/P010_TVirtualViewerX3D.C

%files gui -f includelist-gui-gui
%{_libdir}/%{name}/libGui.*
%{_libdir}/%{name}/libGui_rdict.pcm
%{_datadir}/%{name}/plugins/TBrowserImp/P010_TRootBrowser.C
%{_datadir}/%{name}/plugins/TBrowserImp/P020_TRootBrowserLite.C
%{_datadir}/%{name}/plugins/TGPasswdDialog/P010_TGPasswdDialog.C
%{_datadir}/%{name}/plugins/TGuiFactory/P010_TRootGuiFactory.C

%files gui-html -f includelist-gui-guihtml
%{_libdir}/%{name}/libGuiHtml.*
%{_libdir}/%{name}/libGuiHtml_rdict.pcm

%files gui-fitpanel -f includelist-gui-fitpanel
%{_libdir}/%{name}/libFitPanel.*
%{_libdir}/%{name}/libFitPanel_rdict.pcm
%{_datadir}/%{name}/plugins/TFitEditor/P010_TFitEditor.C

%files gui-ged -f includelist-gui-ged
%{_libdir}/%{name}/libGed.*
%{_libdir}/%{name}/libGed_rdict.pcm
%{_datadir}/%{name}/plugins/TVirtualPadEditor/P010_TGedEditor.C

%files gui-builder -f includelist-gui-guibuilder
%{_libdir}/%{name}/libGuiBld.*
%{_libdir}/%{name}/libGuiBld_rdict.pcm
%{_datadir}/%{name}/plugins/TGuiBuilder/P010_TRootGuiBuilder.C
%{_datadir}/%{name}/plugins/TVirtualDragManager/P010_TGuiBldDragManager.C

%files gui-recorder -f includelist-gui-recorder
%{_libdir}/%{name}/libRecorder.*
%{_libdir}/%{name}/libRecorder_rdict.pcm

%files gui-treemap -f includelist-gui-treemap
%{_libdir}/%{name}/libROOTTreeMap.*
%{_libdir}/%{name}/libROOTTreeMap_rdict.pcm

%files hbook -f includelist-hist-hbook
%{_bindir}/g2root
%{_bindir}/h2root
%{_mandir}/man1/g2root.1*
%{_mandir}/man1/h2root.1*
%{_libdir}/%{name}/libHbook.*
%{_libdir}/%{name}/libHbook_rdict.pcm

%files hist -f includelist-hist-hist
%{_libdir}/%{name}/libHist.*
%{_libdir}/%{name}/libHist_rdict.pcm
%dir %{_includedir}/%{name}/v5

%files hist-painter -f includelist-hist-histpainter
%{_libdir}/%{name}/libHistPainter.*
%{_libdir}/%{name}/libHistPainter_rdict.pcm
%{_datadir}/%{name}/plugins/TVirtualHistPainter/P010_THistPainter.C
%{_datadir}/%{name}/plugins/TVirtualGraphPainter/P010_TGraphPainter.C

%files spectrum -f includelist-hist-spectrum
%{_libdir}/%{name}/libSpectrum.*
%{_libdir}/%{name}/libSpectrum_rdict.pcm

%files spectrum-painter -f includelist-hist-spectrumpainter
%{_libdir}/%{name}/libSpectrumPainter.*
%{_libdir}/%{name}/libSpectrumPainter_rdict.pcm

%files io -f includelist-io-io
%{_libdir}/%{name}/libRIO.*
%{_datadir}/%{name}/plugins/TArchiveFile/P010_TZIPFile.C
%{_datadir}/%{name}/plugins/TVirtualStreamerInfo/P010_TStreamerInfo.C

%files io-dcache -f includelist-io-dcache
%{_libdir}/%{name}/libDCache.*
%{_libdir}/%{name}/libDCache_rdict.pcm
%{_datadir}/%{name}/plugins/TFile/P040_TDCacheFile.C
%{_datadir}/%{name}/plugins/TSystem/P020_TDCacheSystem.C

%files io-sql -f includelist-io-sql
%{_libdir}/%{name}/libSQLIO.*
%{_libdir}/%{name}/libSQLIO_rdict.pcm

%files io-xml -f includelist-io-xml
%{_libdir}/%{name}/libXMLIO.*
%{_libdir}/%{name}/libXMLIO_rdict.pcm
%{_datadir}/%{name}/plugins/TFile/P080_TXMLFile.C

%files io-xmlparser -f includelist-io-xmlparser
%{_libdir}/%{name}/libXMLParser.*
%{_libdir}/%{name}/libXMLParser_rdict.pcm

%files foam -f includelist-math-foam
%{_libdir}/%{name}/libFoam.*
%{_libdir}/%{name}/libFoam_rdict.pcm
%{_datadir}/%{name}/plugins/ROOT@@Math@@DistSampler/P020_TFoamSampler.C

%files fftw -f includelist-math-fftw
%{_libdir}/%{name}/libFFTW.*
%{_libdir}/%{name}/libFFTW_rdict.pcm
%{_datadir}/%{name}/plugins/TVirtualFFT/P010_TFFTComplex.C
%{_datadir}/%{name}/plugins/TVirtualFFT/P020_TFFTComplexReal.C
%{_datadir}/%{name}/plugins/TVirtualFFT/P030_TFFTRealComplex.C
%{_datadir}/%{name}/plugins/TVirtualFFT/P040_TFFTReal.C

%files fumili -f includelist-math-fumili
%{_libdir}/%{name}/libFumili.*
%{_libdir}/%{name}/libFumili_rdict.pcm
%{_datadir}/%{name}/plugins/ROOT@@Math@@Minimizer/P070_TFumiliMinimizer.C
%{_datadir}/%{name}/plugins/TVirtualFitter/P020_TFumili.C

%files genvector -f includelist-math-genvector
%{_libdir}/%{name}/libGenVector.*
%{_libdir}/%{name}/libGenVector_rdict.pcm
%{_libdir}/%{name}/libGenVector32.rootmap
%{_libdir}/%{name}/libGenVector_G__GenVector32_rdict.pcm
%dir %{_includedir}/%{name}/Math/GenVector

%files mathcore -f includelist-math-mathcore
%{_libdir}/%{name}/libMathCore.*
%{_libdir}/%{name}/libMathCore_rdict.pcm
%dir %{_includedir}/%{name}/Fit

%files mathmore -f includelist-math-mathmore
%{_libdir}/%{name}/libMathMore.*
%{_libdir}/%{name}/libMathMore_rdict.pcm
%{_datadir}/%{name}/plugins/ROOT@@Math@@IRootFinderMethod/P010_Brent.C
%{_datadir}/%{name}/plugins/ROOT@@Math@@IRootFinderMethod/P020_Bisection.C
%{_datadir}/%{name}/plugins/ROOT@@Math@@IRootFinderMethod/P030_FalsePos.C
%{_datadir}/%{name}/plugins/ROOT@@Math@@IRootFinderMethod/P040_Newton.C
%{_datadir}/%{name}/plugins/ROOT@@Math@@IRootFinderMethod/P050_Secant.C
%{_datadir}/%{name}/plugins/ROOT@@Math@@IRootFinderMethod/P060_Steffenson.C
%{_datadir}/%{name}/plugins/ROOT@@Math@@Minimizer/P030_GSLMinimizer.C
%{_datadir}/%{name}/plugins/ROOT@@Math@@Minimizer/P040_GSLNLSMinimizer.C
%{_datadir}/%{name}/plugins/ROOT@@Math@@Minimizer/P050_GSLSimAnMinimizer.C
%{_datadir}/%{name}/plugins/ROOT@@Math@@VirtualIntegrator/P010_GSLIntegrator.C
%{_datadir}/%{name}/plugins/ROOT@@Math@@VirtualIntegrator/P020_GSLMCIntegrator.C

%files matrix -f includelist-math-matrix
%{_libdir}/%{name}/libMatrix.*
%{_libdir}/%{name}/libMatrix_rdict.pcm

%files minuit -f includelist-math-minuit
%{_libdir}/%{name}/libMinuit.*
%{_libdir}/%{name}/libMinuit_rdict.pcm
%{_datadir}/%{name}/plugins/ROOT@@Math@@Minimizer/P020_TMinuitMinimizer.C
%{_datadir}/%{name}/plugins/ROOT@@Math@@Minimizer/P060_TLinearMinimizer.C
%{_datadir}/%{name}/plugins/TVirtualFitter/P010_TFitter.C

%files minuit2 -f includelist-math-minuit2
%{_libdir}/%{name}/libMinuit2.*
%{_libdir}/%{name}/libMinuit2_rdict.pcm
%dir %{_includedir}/%{name}/Minuit2
%{_datadir}/%{name}/plugins/ROOT@@Math@@Minimizer/P010_Minuit2Minimizer.C

%files mlp -f includelist-math-mlp
%{_libdir}/%{name}/libMLP.*
%{_libdir}/%{name}/libMLP_rdict.pcm

%files physics -f includelist-math-physics
%{_libdir}/%{name}/libPhysics.*
%{_libdir}/%{name}/libPhysics_rdict.pcm

%files quadp -f includelist-math-quadp
%{_libdir}/%{name}/libQuadp.*
%{_libdir}/%{name}/libQuadp_rdict.pcm

%files smatrix -f includelist-math-smatrix
%{_libdir}/%{name}/libSmatrix.*
%{_libdir}/%{name}/libSmatrix_rdict.pcm
%{_libdir}/%{name}/libSmatrix32.rootmap
%{_libdir}/%{name}/libSmatrix_G__Smatrix32_rdict.pcm

%files splot -f includelist-math-splot
%{_libdir}/%{name}/libSPlot.*
%{_libdir}/%{name}/libSPlot_rdict.pcm

%files unuran -f includelist-math-unuran
%{_libdir}/%{name}/libUnuran.*
%{_libdir}/%{name}/libUnuran_rdict.pcm
%{_datadir}/%{name}/plugins/ROOT@@Math@@DistSampler/P010_TUnuranSampler.C

%files vecops -f includelist-math-vecops
%{_libdir}/%{name}/libROOTVecOps.*
%{_libdir}/%{name}/libROOTVecOps_rdict.pcm

%files montecarlo-eg -f includelist-montecarlo-eg
%{_libdir}/%{name}/libEG.*
%{_libdir}/%{name}/libEG_rdict.pcm
%{_datadir}/%{name}/pdg_table.txt
%{_datadir}/%{name}/pdg_table_update.py
%doc %{_pkgdocdir}/cfortran.doc

%files montecarlo-pythia8 -f includelist-montecarlo-pythia8
%{_libdir}/%{name}/libEGPythia8.*
%{_libdir}/%{name}/libEGPythia8_rdict.pcm

%files net -f includelist-net-net
%{_libdir}/%{name}/libNet.*
%{_libdir}/%{name}/libNet_rdict.pcm
%{_datadir}/%{name}/plugins/TApplication/P010_TApplicationRemote.C
%{_datadir}/%{name}/plugins/TApplication/P020_TApplicationServer.C
%{_datadir}/%{name}/plugins/TFile/P010_TWebFile.C
%{_datadir}/%{name}/plugins/TFile/P120_TNetFile.C
%{_datadir}/%{name}/plugins/TFile/P150_TS3WebFile.C
%{_datadir}/%{name}/plugins/TFileStager/P020_TNetFileStager.C
%{_datadir}/%{name}/plugins/TSystem/P050_TWebSystem.C
%{_datadir}/%{name}/plugins/TSystem/P070_TNetSystem.C
%{_datadir}/%{name}/plugins/TVirtualMonitoringWriter/P020_TSQLMonitoringWriter.C

%files net-rpdutils
%{_libdir}/%{name}/libSrvAuth.*

%files net-auth -f includelist-net-auth
%{_libdir}/%{name}/libRootAuth.*
%{_libdir}/%{name}/libRootAuth_rdict.pcm
%{_datadir}/%{name}/plugins/TVirtualAuth/P010_TRootAuth.C
%doc %{_pkgdocdir}/README.AUTH

%files net-davix -f includelist-net-davix
%{_libdir}/%{name}/libRDAVIX.*
%{_libdir}/%{name}/libRDAVIX_rdict.pcm
%{_datadir}/%{name}/plugins/TFile/P130_TDavixFile.C
%{_datadir}/%{name}/plugins/TSystem/P045_TDavixSystem.C
%{_datadir}/%{name}/plugins/ROOT@@Internal@@RRawFile/P010_RRawFileDavix.C

%files net-http -f includelist-net-http
%{_libdir}/%{name}/libRHTTP.*
%{_libdir}/%{name}/libRHTTP_rdict.pcm
%dir %{_datadir}/%{name}/js
%dir %{_datadir}/%{name}/js/files
%{_datadir}/%{name}/js/files/canv_batch.htm
%{_datadir}/%{name}/js/files/geom_batch.htm
%{_datadir}/%{name}/js/files/web.config
%{_datadir}/%{name}/js/files/wslist.htm
%ghost %{_datadir}/%{name}/js/build
%ghost %{_datadir}/%{name}/js/img
%ghost %{_datadir}/%{name}/js/mathjax
%ghost %{_datadir}/%{name}/js/modules
%ghost %{_datadir}/%{name}/js/scripts
%ghost %{_datadir}/%{name}/js/files/draw.htm
%ghost %{_datadir}/%{name}/js/files/online.htm
%doc net/http/README.txt net/http/civetweb/*.md

%files net-httpsniff -f includelist-net-httpsniff
%{_libdir}/%{name}/libRHTTPSniff.*
%{_libdir}/%{name}/libRHTTPSniff_rdict.pcm

%files netx -f includelist-net-netxng
%{_libdir}/%{name}/libNetxNG.*
%{_libdir}/%{name}/libNetxNG_rdict.pcm
%{_datadir}/%{name}/plugins/TFile/P100_TXNetFile.C
%{_datadir}/%{name}/plugins/TFileStager/P010_TXNetFileStager.C
%{_datadir}/%{name}/plugins/TSystem/P040_TXNetSystem.C
%{_datadir}/%{name}/plugins/ROOT@@Internal@@RRawFile/P020_RRawFileNetXNG.C

%if %{roofit}
%files roofit -f includelist-roofit-roofit
%{_libdir}/%{name}/libRooFit.*
%{_libdir}/%{name}/libRooFit_rdict.pcm

%files roofit-core -f includelist-roofit-roofitcore
%{_libdir}/%{name}/libRooFitCore.*
%{_libdir}/%{name}/libRooFitCore_rdict.pcm
%dir %{_includedir}/%{name}/RooFit
%dir %{_includedir}/%{name}/RooFit/Detail
%dir %{_includedir}/%{name}/RooFit/TestStatistics
%dir %{_includedir}/%{name}/RooFitLegacy
%{_datadir}/gdb/auto-load%{_libdir}/%{name}/libRooFitCore.*
%{_datadir}/gdb/auto-load%{_libdir}/%{name}/__pycache__/libRooFitCore.*

%files roofit-more -f includelist-roofit-roofitmore
%{_libdir}/%{name}/libRooFitMore.*
%{_libdir}/%{name}/libRooFitMore_rdict.pcm

%files roofit-batchcompute
%{_libdir}/%{name}/libRooBatchCompute.*
%{_libdir}/%{name}/libRooBatchCompute_*

%files roofit-hs3 -f includelist-roofit-hs3
%{_libdir}/%{name}/libRooFitHS3.*
%{_libdir}/%{name}/libRooFitHS3_rdict.pcm
%dir %{_includedir}/%{name}/RooFitHS3

%files roofit-jsoninterface -f includelist-roofit-jsoninterface
%{_libdir}/%{name}/libRooFitJSONInterface.*
%{_libdir}/%{name}/libRooFitJSONInterface_rdict.pcm
%dir %{_includedir}/%{name}/RooFit

%files roofit-codegen -f includelist-roofit-codegen
%{_libdir}/%{name}/libRooFitCodegen.*
%{_libdir}/%{name}/libRooFitCodegen_rdict.pcm

%if %{roofitmp}
%files roofit-multiprocess -f includelist-roofit-multiprocess
%{_libdir}/%{name}/libRooFitMultiProcess.*
%dir %{_includedir}/%{name}/RooFit
%dir %{_includedir}/%{name}/RooFit/MultiProcess

%files roofit-zmq
%{_libdir}/%{name}/libRooFitZMQ.*
%endif

%files roostats -f includelist-roofit-roostats
%{_libdir}/%{name}/libRooStats.*
%{_libdir}/%{name}/libRooStats_rdict.pcm
%dir %{_includedir}/%{name}/RooStats

%files hist-factory -f includelist-roofit-histfactory
%{_bindir}/hist2workspace
%{_bindir}/prepareHistFactory
%{_mandir}/man1/hist2workspace.1*
%{_mandir}/man1/prepareHistFactory.1*
%{_libdir}/%{name}/libHistFactory.*
%{_libdir}/%{name}/libHistFactory_rdict.pcm
%{_datadir}/%{name}/HistFactorySchema.dtd
%dir %{_includedir}/%{name}/RooStats/HistFactory
%dir %{_includedir}/%{name}/RooStats/HistFactory/Detail
%doc roofit/histfactory/doc/README

%files xroofit -f includelist-roofit-xroofit
%{_libdir}/%{name}/libRooFitXRooFit.*
%{_libdir}/%{name}/libRooFitXRooFit_rdict.pcm
%dir %{_includedir}/%{name}/RooFit/xRooFit
%endif

%files sql-sqlite -f includelist-sql-sqlite
%{_libdir}/%{name}/libRSQLite.*
%{_libdir}/%{name}/libRSQLite_rdict.pcm
%{_datadir}/%{name}/plugins/TSQLServer/P060_TSQLiteServer.C

%files tmva -f includelist-tmva-tmva
%{_libdir}/%{name}/libTMVA.*
%{_libdir}/%{name}/libTMVA_rdict.pcm
%dir %{_includedir}/%{name}/TMVA
%dir %{_includedir}/%{name}/TMVA/DNN
%dir %{_includedir}/%{name}/TMVA/DNN/Architectures
%dir %{_includedir}/%{name}/TMVA/DNN/Architectures/Cpu
%dir %{_includedir}/%{name}/TMVA/DNN/Architectures/Reference
%dir %{_includedir}/%{name}/TMVA/DNN/CNN
%dir %{_includedir}/%{name}/TMVA/DNN/RNN
%license tmva/doc/LICENSE
%exclude %{_includedir}/%{name}/TMVA/RBDT.hxx
%exclude %{_includedir}/%{name}/TMVA/RInferenceUtils.hxx
%exclude %{_includedir}/%{name}/TMVA/RReader.hxx
%exclude %{_includedir}/%{name}/TMVA/RSofieReader.hxx
%exclude %{_includedir}/%{name}/TMVA/RStandardScaler.hxx
%exclude %{_includedir}/%{name}/TMVA/RTensorUtils.hxx
%exclude %{_includedir}/%{name}/TMVA/BatchGenerator/RBatchGenerator.hxx
%exclude %{_includedir}/%{name}/TMVA/BatchGenerator/RBatchLoader.hxx
%exclude %{_includedir}/%{name}/TMVA/BatchGenerator/RChunkConstructor.hxx
%exclude %{_includedir}/%{name}/TMVA/BatchGenerator/RChunkLoader.hxx

%if %{dataframe}
%files tmva-utils
%{_libdir}/%{name}/libTMVAUtils.*
%{_libdir}/%{name}/libTMVAUtils_rdict.pcm
%dir %{_includedir}/%{name}/TMVA
%{_includedir}/%{name}/TMVA/RBDT.hxx
%{_includedir}/%{name}/TMVA/RInferenceUtils.hxx
%{_includedir}/%{name}/TMVA/RReader.hxx
%{_includedir}/%{name}/TMVA/RSofieReader.hxx
%{_includedir}/%{name}/TMVA/RStandardScaler.hxx
%{_includedir}/%{name}/TMVA/RTensorUtils.hxx
%dir %{_includedir}/%{name}/TMVA/BatchGenerator
%{_includedir}/%{name}/TMVA/BatchGenerator/RBatchGenerator.hxx
%{_includedir}/%{name}/TMVA/BatchGenerator/RBatchLoader.hxx
%{_includedir}/%{name}/TMVA/BatchGenerator/RChunkConstructor.hxx
%{_includedir}/%{name}/TMVA/BatchGenerator/RChunkLoader.hxx
%endif

%files tmva-python -f includelist-tmva-pymva
%{_libdir}/%{name}/libPyMVA.*
%{_libdir}/%{name}/libPyMVA_rdict.pcm

%if %{rrr}
%files tmva-r -f includelist-tmva-rmva
%{_libdir}/%{name}/libRMVA.*
%{_libdir}/%{name}/libRMVA_rdict.pcm
%endif

%files tmva-sofie -f includelist-tmva-sofie
%{_libdir}/%{name}/libROOTTMVASofie.*
%{_libdir}/%{name}/libROOTTMVASofie_rdict.pcm
%doc tmva/sofie/README.md

%if %{tmvasofieparser}
%files tmva-sofie-parser -f includelist-tmva-sofie_parsers
%{_libdir}/%{name}/libROOTTMVASofieParser.*
%{_libdir}/%{name}/libROOTTMVASofieParser_rdict.pcm
%endif

%files tmva-gui -f includelist-tmva-tmvagui
%{_libdir}/%{name}/libTMVAGui.*
%{_libdir}/%{name}/libTMVAGui_rdict.pcm

%files tree -f includelist-tree-tree
%{_libdir}/%{name}/libTree.*
%{_libdir}/%{name}/libTree_rdict.pcm
%doc %{_pkgdocdir}/README.SELECTOR

%if %{dataframe}
%files tree-dataframe -f includelist-tree-dataframe
%{_libdir}/%{name}/libROOTDataFrame.*
%{_libdir}/%{name}/libROOTDataFrame_rdict.pcm
%endif

%files tree-player -f includelist-tree-treeplayer
%{_libdir}/%{name}/libTreePlayer.*
%{_libdir}/%{name}/libTreePlayer_rdict.pcm
%{_datadir}/%{name}/plugins/TFileDrawMap/P010_TFileDrawMap.C
%{_datadir}/%{name}/plugins/TVirtualTreePlayer/P010_TTreePlayer.C

%files tree-viewer -f includelist-tree-treeviewer
%{_libdir}/%{name}/libTreeViewer.*
%{_libdir}/%{name}/libTreeViewer_rdict.pcm
%{_datadir}/%{name}/plugins/TVirtualTreeViewer/P010_TTreeViewer.C

%files tree-webviewer -f includelist-tree-webviewer
%{_libdir}/%{name}/libROOTTreeViewer.*
%{_libdir}/%{name}/libROOTTreeViewer_rdict.pcm
%{_datadir}/%{name}/plugins/TVirtualTreeViewer/P020_RTreeViewer.C

%files unfold -f includelist-hist-unfold
%{_libdir}/%{name}/libUnfold.*
%{_libdir}/%{name}/libUnfold_rdict.pcm

%files cli
%{_bindir}/rootcp
%{_bindir}/rootdrawtree
%{_bindir}/rooteventselector
%{_bindir}/rootmkdir
%{_bindir}/rootmv
%{_bindir}/rootprint
%{_bindir}/rootrm
%{_bindir}/rootslimtree
%{_datadir}/%{name}/cli

%files gui-webdisplay -f includelist-gui-webdisplay
%{_libdir}/%{name}/libROOTWebDisplay.*
%{_libdir}/%{name}/libROOTWebDisplay_rdict.pcm
%{_datadir}/%{name}/runfirefox.sh
%{_datadir}/%{name}/ui5

%ifarch %{qt6_qtwebengine_arches}
%files gui-qt6webdisplay
%{_libdir}/%{name}/libROOTQt6WebDisplay.*
%endif

%files gui-webgui6 -f includelist-gui-webgui6
%{_libdir}/%{name}/libWebGui6.*
%{_libdir}/%{name}/libWebGui6_rdict.pcm
%{_datadir}/%{name}/plugins/TCanvasImp/P010_TWebCanvas.C
%{_datadir}/%{name}/plugins/TControlBarImp/P010_TWebControlBar.C

%files gui-browsable -f includelist-gui-browsable
%{_libdir}/%{name}/libROOTBrowsable.*
%{_libdir}/%{name}/libROOTBrowsable_rdict.pcm
%{_libdir}/%{name}/libROOTBranchBrowseProvider.*
%{_libdir}/%{name}/libROOTGeoBrowseProvider.*
%{_libdir}/%{name}/libROOTLeafDraw6Provider.*
%{_libdir}/%{name}/libROOTNTupleBrowseProvider.*
%{_libdir}/%{name}/libROOTNTupleDraw6Provider.*
%{_libdir}/%{name}/libROOTObjectDraw6Provider.*

%files gui-browserv7 -f includelist-gui-browserv7
%{_libdir}/%{name}/libROOTBrowserv7.*
%{_libdir}/%{name}/libROOTBrowserv7_rdict.pcm
%{_libdir}/%{name}/libROOTBrowserGeomWidget.*
%{_libdir}/%{name}/libROOTBrowserTCanvasWidget.*
%{_libdir}/%{name}/libROOTBrowserTreeWidget.*
%{_libdir}/%{name}/libROOTBrowserWidgets.*
%{_datadir}/%{name}/plugins/TBrowserImp/P030_RWebBrowserImp.C

%files geom-checker -f includelist-geom-geomchecker
%{_libdir}/%{name}/libGeomChecker.*
%{_libdir}/%{name}/libGeomChecker_rdict.pcm
%{_datadir}/%{name}/plugins/TVirtualGeoChecker/P010_TGeoChecker.C

%files geom-webviewer -f includelist-geom-webviewer
%{_libdir}/%{name}/libROOTGeomViewer.*
%{_libdir}/%{name}/libROOTGeomViewer_rdict.pcm
%{_datadir}/%{name}/plugins/TVirtualGeoPainter/P020_RGeoPainter.C

%files tree-ntuple -f includelist-tree-ntuple
%{_libdir}/%{name}/libROOTNTuple.*
%{_libdir}/%{name}/libROOTNTuple_rdict.pcm
%dir %{_includedir}/%{name}/ROOT/libdaos_mock

%files tree-ntuple-browse -f includelist-tree-ntuplebrowse
%{_libdir}/%{name}/libROOTNTupleBrowse.*
%{_libdir}/%{name}/libROOTNTupleBrowse_rdict.pcm

%files tree-ntuple-utils -f includelist-tree-ntupleutil
%{_libdir}/%{name}/libROOTNTupleUtil.*
%{_libdir}/%{name}/libROOTNTupleUtil_rdict.pcm

%if %{root7}
%files graf-gpadv7 -f includelist-graf2d-gpadv7
%{_libdir}/%{name}/libROOTGpadv7.*
%{_libdir}/%{name}/libROOTGpadv7_rdict.pcm

%files graf-primitives -f includelist-graf2d-primitivesv7
%{_libdir}/%{name}/libROOTGraphicsPrimitives.*
%{_libdir}/%{name}/libROOTGraphicsPrimitives_rdict.pcm

%files graf3d-eve7 -f includelist-graf3d-eve7
%{_libdir}/%{name}/libROOTEve.*
%{_libdir}/%{name}/libROOTEve_rdict.pcm

%files gui-browsable-v7
%{_libdir}/%{name}/libROOTLeafDraw7Provider.*
%{_libdir}/%{name}/libROOTNTupleDraw7Provider.*
%{_libdir}/%{name}/libROOTObjectDraw7Provider.*

%files gui-browserv7-v7
%{_libdir}/%{name}/libROOTBrowserRCanvasWidget.*

%files gui-canvaspainter
%{_libdir}/%{name}/libROOTCanvasPainter.*

%files gui-fitpanelv7 -f includelist-gui-fitpanelv7
%{_libdir}/%{name}/libROOTFitPanelv7.*
%{_libdir}/%{name}/libROOTFitPanelv7_rdict.pcm

%files histv7 -f includelist-hist-histv7
%{_libdir}/%{name}/libROOTHist.*
%{_libdir}/%{name}/libROOTHist_rdict.pcm
%endif

%changelog
%autochangelog
