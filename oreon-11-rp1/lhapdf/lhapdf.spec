%global source3_hash 177f1f21d88e889aec1f7ad6800ecf19895a4a03d3e1e7cebad90ff2164be4d1
%global source2_hash 98ec0541e80e223785bb6029ebf81e93ca5111da41d6565b3b5c4aa86d59bb5d
%global source1_hash 2b8489b521b06d2b18a7903c0e4eac102b22025f9349eeb942acdfae07002b92
%global source0_hash 6b8b7e38dc26a977a24f5a321215b7054c14a4469d04134d70cb93a860eeeea7
Name:		lhapdf
Version:	6.5.6
Release:        2%{?dist}
Summary:        Les Houches Accord PDF Interface
License:	GPL-3.0-only
URL:		https://lhapdf.hepforge.org/
Source0:        https://lhapdf.hepforge.org/downloads/?f=LHAPDF-%{version}.tar.gz#/LHAPDF-%{version}.tar.gz
Source1:	https://lhapdfsets.web.cern.ch/current/CT10nlo.tar.gz
Source2:	https://lhapdfsets.web.cern.ch/current/MSTW2008nlo68cl.tar.gz
Source3:	https://lhapdfsets.web.cern.ch/current/NNPDF31_lo_as_0130.tar.gz
Source4:	testunc.py
Obsoletes:	octave-lhapdf < 6
Obsoletes:	lhapdf-pdfsets-minimal < 6
# oreon:deps
BuildRequires:  doxygen
BuildRequires:  gcc-c++
BuildRequires:  make
BuildRequires:  python3-Cython
BuildRequires:  python3-devel
BuildRequires:  yaml-cpp-devel
# /oreon:deps
%description
LHAPDF is a general purpose C++ interpolator, used for evaluating PDFs
from discretized data files. Previous versions of LHAPDF were written
in Fortran 77/90 and are documented at http://lhapdf.hepforge.org/lhapdf5/.

LHAPDF6 vastly reduces the memory overhead of the Fortran LHAPDF (from
gigabytes to megabytes!), entirely removes restrictions on numbers of
concurrent PDFs, allows access to single PDF members without needing
to load whole sets, and separates a new standardized PDF data format
from the code library so that new PDF sets may be created and released
easier and faster. The C++ LHAPDF6 also permits arbitrary parton
contents via the standard PDG ID code scheme, is computationally more
efficient (particularly if only one or two flavors are required at
each phase space point, as in PDF reweighting), and uses a flexible
metadata system which fixes many fundamental metadata and concurrency
bugs in LHAPDF5.

Compatibility routines are provided as standard for existing C++ and
Fortran codes using the LHAPDF5 and PDFLIB legacy interfaces, so you
can keep using your existing codes. But the new interface is much more
powerful and pleasant to work with, so we think you'll want to switch
once you've used it!

LHAPDF6 is documented in more detail in http://arxiv.org/abs/1412.7420

%package devel
Summary:	Les Houches Accord PDF Interface - development files
Requires:	%{name}%{?_isa} = %{version}-%{release}
%description devel
This package provides development files of LHAPDF, including C++ bindings.

%package -n python%{python3_pkgversion}-%{name}
Summary:	Les Houches Accord PDF Interface - Python 3 module
%py_provides	python%{python3_pkgversion}-%{name}
Requires:	%{name}%{?_isa} = %{version}-%{release}
%description -n python%{python3_pkgversion}-%{name}
This package provides Python 3 bindings for LHAPDF.
This package also provides a script called "lhapdf" which can be used
to query the catalog of PDF sets and to install and update them from
the command line. It accepts commands "list", "update", "install" and
"upgrade". Please run "lhapdf help" for full usage instructions.

%package doc
Summary:	Les Houches Accord PDF Interface - documentation
BuildArch:	noarch
%description doc
This package provides API documentation and examples for LHAPDF.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n LHAPDF-%{version}

mkdir tests/SETS
tar -z -x -f %{SOURCE1} -C tests/SETS
tar -z -x -f %{SOURCE2} -C tests/SETS
tar -z -x -f %{SOURCE3} -C tests/SETS

cp -p %{SOURCE4} tests

# Remove bundled yaml-cpp
rm -rf src/yamlcpp/

# Fix shebangs
sed 's!/usr/bin/env python3!%{__python3}!' -i bin/lhapdf
sed 's!/usr/bin/env python!%{__python3}!' -i examples/*.py
sed 's!/usr/bin/env bash!/bin/bash!' -i bin/lhapdf-config.in

%build

%configure \
	--disable-static \
	--with-yaml-cpp \
	--enable-librelease \
	--docdir=%{_pkgdocdir} \
	PYTHON=%{__python3}
rm wrappers/python/lhapdf.cpp
%make_build
%make_build doxy
%install
%make_install
mkdir %{buildroot}%{python3_sitearch}/%{name}-%{version}.dist-info
cat << EOF > %{buildroot}%{python3_sitearch}/%{name}-%{version}.dist-info/METADATA
Name: %{name}
Version: %{version}
EOF
rm %{buildroot}%{_libdir}/libLHAPDF.la
find %{buildroot}%{_pkgdocdir}/examples -type f -a '!' -name '*.*' -delete
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%check

cp -p pdfsets.index tests/SETS
cp -p lhapdf.conf tests/SETS
export PYTHONPATH=$PWD/wrappers/python/build
export LD_LIBRARY_PATH=$PWD/src/.libs
%make_build check
%files -f %{oreon_filedir}/main.list
%files -n lhapdf-devel -f %{oreon_filedir}/lhapdf-devel.list
%files -n python3-lhapdf -f %{oreon_filedir}/python3-lhapdf.list
%files -n lhapdf-doc -f %{oreon_filedir}/lhapdf-doc.list

%changelog

%autochangelog
