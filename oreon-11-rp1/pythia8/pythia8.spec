%global source0_hash none

Name:		pythia8
Version:	8.3.17
Release:	1%{?dist}
Summary:	Pythia Event Generator for High Energy Physics

License:	GPL-2.0-or-later
URL:		https://pythia.org
Source0:	https://pythia.org/download/pythia83/pythia8317.tgz
#		Link plugins to the shared library
#		Remove rpath
Patch0:		%{name}-makefile.patch

BuildRequires:	make
BuildRequires:	gcc-c++
BuildRequires:	lhapdf-devel
BuildRequires:	zlib-devel
BuildRequires:	python3-devel
BuildRequires:	rsync
BuildRequires:	dos2unix
Requires:	%{name}-data = %{version}-%{release}
Obsoletes:	%{name}-hepmcinterface < 8.2
%if %{?rhel}%{!?rhel:0} == 8
Obsoletes:	python2-%{name} < 8.3.12
%endif

%description
PYTHIA is a program for the generation of high-energy physics events, i.e.
for the description of collisions at high energies between elementary
particles such as e⁺, e⁻, p and p̄ in various combinations. It contains
theory and models for a number of physics aspects, including hard and soft
interactions, parton distributions, initial and final-state parton showers,
multiple interactions, fragmentation and decay.

%package devel
Summary:	Pythia 8 Development Files
Requires:	%{name}%{?_isa} = %{version}-%{release}
Obsoletes:	%{name}-hepmcinterface-devel < 8.2

%description devel
This package provides development files for Pythia 8.

%package lhapdf
Summary:	Pythia 8 LHAPDF Interface
Requires:	%{name}%{?_isa} = %{version}-%{release}

%description lhapdf
This package provides the LHAPDF interface for Pythia 8.

%package -n python3-%{name}
Summary:	Pythia 8 Python 3 bindings
%py_provides	python3-%{name}
Requires:	%{name}%{?_isa} = %{version}-%{release}

%description -n python3-%{name}
This package provides the Python 3 bindings for Pythia 8.

%package data
Summary:	Pythia 8 Data Files
BuildArch:	noarch

%description data
This package provides XML data files for Pythia 8.

%package examples
Summary:	Pythia 8 Example Source Files
BuildArch:	noarch

%description examples
This package provides example source files for Pythia 8.

%package doc
Summary:	Pythia 8 Documentation
BuildArch:	noarch

%description doc
This package provides documentation for Pythia 8.

%prep
%setup -q -n pythia8317
%patch -P0 -p1

# Remove DOS end-of-line
dos2unix -k share/Pythia8/htmldoc/pythia.css \
	    share/Pythia8/pdfdata/mrstlostarstar.00.dat

%build
PYTHON_CONFIG=%{__python3}-config \
./configure --prefix=%{_prefix} --prefix-lib=%{_libdir} \
	    --cxx-common="%{build_cxxflags} -fPIC" \
	    --cxx-shared="%{build_ldflags} -shared" \
	    --lib-suffix="-%{version}.so" \
	    --with-lhapdf6 \
	    --with-python \
	    --with-gzip

%make_build PYTHON_EXT_SUFFIX=%{python3_ext_suffix}
ln -s libpythia8-%{version}.so lib/libpythia8.so

%install
%make_install \
     PYTHON_EXT_SUFFIX=%{python3_ext_suffix} \
     PREFIX_BIN=%{buildroot}%{_bindir} \
     PREFIX_INCLUDE=%{buildroot}%{_includedir} \
     PREFIX_LIB=%{buildroot}%{_libdir} \
     PREFIX_SHARE=%{buildroot}%{_datadir}/Pythia8

rm %{buildroot}%{_bindir}/pythia8-config
rm %{buildroot}%{_libdir}/libpythia8.a
rm -rf %{buildroot}%{_datadir}/Pythia8/htmldoc
rm -rf %{buildroot}%{_datadir}/Pythia8/pdfdoc
rm -rf %{buildroot}%{_datadir}/Pythia8/phpdoc
rm %{buildroot}%{_datadir}/Pythia8/AUTHORS
rm %{buildroot}%{_datadir}/Pythia8/COPYING
rm %{buildroot}%{_datadir}/Pythia8/GUIDELINES
rm %{buildroot}%{_datadir}/Pythia8/README
rm %{buildroot}%{_datadir}/Pythia8/examples/Makefile
rm %{buildroot}%{_datadir}/Pythia8/examples/Makefile.inc
rm %{buildroot}%{_datadir}/Pythia8/examples/runmains

touch %{buildroot}%{_datadir}/Pythia8/examples/Makefile.inc

mkdir -p %{buildroot}%{python3_sitearch}
mv %{buildroot}%{_libdir}/pythia8%{python3_ext_suffix} \
	%{buildroot}%{python3_sitearch}
mkdir %{buildroot}%{python3_sitearch}/%{name}-%{version}.dist-info
echo 'Name: %{name}' > \
     %{buildroot}%{python3_sitearch}/%{name}-%{version}.dist-info/METADATA
echo 'Version: %{version}' >> \
     %{buildroot}%{python3_sitearch}/%{name}-%{version}.dist-info/METADATA

%files
%{_libdir}/libpythia8-%{version}.so
%doc AUTHORS GUIDELINES
%license COPYING

%files devel
%{_libdir}/libpythia8.so
%{_includedir}/Pythia8
%{_includedir}/Pythia8Plugins
%doc CODINGSTYLE

%files lhapdf
%{_libdir}/libpythia8lhapdf*.so

%files -n python3-%{name}
%{python3_sitearch}/%{name}-%{version}.dist-info
%{python3_sitearch}/pythia8.*.so

%files data
%dir %{_datadir}/Pythia8
%{_datadir}/Pythia8/pdfdata
%{_datadir}/Pythia8/setups
%{_datadir}/Pythia8/tunes
%{_datadir}/Pythia8/xmldoc
%license COPYING

%files examples
%dir %{_datadir}/Pythia8
%doc %{_datadir}/Pythia8/examples
%license COPYING

%files doc
%doc share/Pythia8/htmldoc
%doc share/Pythia8/pdfdoc
%license COPYING

%changelog
%autochangelog
