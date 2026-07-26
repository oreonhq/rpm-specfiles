%global source0_hash 90d6f1dba59417c00f8f4545131c7efd31930cd0e178598980a8210425e3852e

%if 0%{?fedora} >= 42
%global tclver 9.0
%else
%global tclver 8.6
%endif

%global githash 0
%global shorthash %(c=%{githash}; echo ${c:0:10})

Name:           hamlib
Version:        4.6.5
Release:        3%{?dist}
Summary:        Run-time library to control radio transceivers and receivers

License:        GPL-2.0-or-later and LGPL-2.0-or-later
URL:            http://www.hamlib.org
%if "%{githash}" == "0"
Source0:        http://downloads.sourceforge.net/%{name}/%{name}-%{version}.tar.gz
%else
Source0:        https://github.com/Hamlib/Hamlib/archive/%{githash}/%{name}-%{shorthash}.tar.gz
%endif

Patch0:         hamlib-4.0-perl_install.patch
# -lpython is not needed, https://github.com/Hamlib/Hamlib/issues/253
Patch1:         hamlib-4.0-drop-libpython.patch

ExcludeArch:    i686

BuildRequires:  automake autoconf libtool
BuildRequires:  make
BuildRequires:  gcc gcc-c++ %{?swigver}
BuildRequires:  gd-devel
BuildRequires:  doxygen
BuildRequires:  source-highlight
BuildRequires:  boost-devel
BuildRequires:  libtool-ltdl-devel
BuildRequires:  libusb1-devel
BuildRequires:  libxml2-devel
BuildRequires:  pkgconfig
BuildRequires:  python3-devel
BuildRequires:  swig
BuildRequires:  tcl-devel
#for perl
BuildRequires:  perl-devel
BuildRequires:  perl-generators
BuildRequires:  perl(ExtUtils::MakeMaker)

# Filter provides from private libraries.
%{?perl_default_filter}

%description
Hamlib provides a standardized programming interface that applications
can use to send the appropriate commands to a radio.

Also included in the package is a simple radio control program 'rigctl',
which lets one control a radio transceiver or receiver, either from
command line interface or in a text-oriented interactive interface.

%package devel
Summary:        Development library to control radio transceivers and receivers
Requires:       hamlib%{?_isa} = %{version}-%{release}
Requires:       tcl-hamlib%{?_isa} = %{version}-%{release}

%description devel
Hamlib radio control library C development headers and libraries
for building C applications with Hamlib.

%package doc
Summary:        Documentation for the hamlib radio control library
BuildArch:      noarch

%description doc
This package provides the developers documentation for the hamlib radio
control library API.

%package c++
Summary:        Hamlib radio control library C++ binding
Requires:       hamlib%{?_isa} = %{version}-%{release}

%description c++
Hamlib radio control library C++ language binding.

%package c++-devel
Summary:        Hamlib radio control library C++ binding development headers and libraries
Requires:       hamlib-devel%{?_isa} = %{version}-%{release}
Requires:       hamlib-c++%{?_isa} = %{version}-%{release}

%description c++-devel
Hamlib radio control library C++ binding development headers and libraries
for building C++ applications with Hamlib.

%package -n perl-%{name}
Summary:        Hamlib radio control library Perl binding
Requires:       hamlib%{?_isa} = %{version}-%{release}
Obsoletes:      hamlib-perl < 3.0
Provides:       hamlib-perl = %{version}-%{release}

%description -n perl-%{name}
Hamlib PERL Language bindings to allow radio control from PERL scripts.

%package -n python3-%{name}
%{?python_provide:%python_provide python2-%{name}}
Summary:        Hamlib radio control library Python binding
Requires:       hamlib%{?_isa} = %{version}-%{release}, python3

%description -n python3-%{name}
Hamlib Python Language bindings to allow radio control from Python scripts.

%package -n tcl-%{name}
Summary:        Hamlib radio control library TCL binding
Requires:       hamlib%{?_isa} = %{version}-%{release}
Provides:       hamlib-tcl = %{version}-%{release}
  
%description -n tcl-%{name}
Hamlib TCL Language bindings to allow radio control from TCL scripts.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%if "%{githash}" == "0"
%autosetup -p1
%else
%autosetup -p1 -n Hamlib-%{githash}
%endif

%build
%if 0%{?fedora} || 0%{?rhel} >= 8
export PYTHON=%{__python3}
%else
export PYTHON=%{__python2}
%endif

# Only run if we're working with a git checkout
#if 0%{?githash}
autoreconf -fi
#endif

%configure \
        --disable-static \
        --with-tcl=/usr/%{_lib} \
        --with-tcl-binding \
        --with-perl-binding \
        --with-python-binding \

%make_build

# Build Documentation
make -C doc doc

%install
%make_install

# Install documentation
mkdir -p %{buildroot}%{_docdir}/%{name}/html/search
for f in `find doc/html/ -type f -maxdepth 1`
        do install -D -m 0644 $f %{buildroot}%{_docdir}/%{name}/`echo $f | cut -d '/' -f2`
done
for f in `find doc/html/search -type f -maxdepth 1`
        do install -D -m 0644 $f %{buildroot}%{_docdir}/%{name}/html/`echo $f | cut -d '/' -f3`
 done

# Move installed docs to include them in subpackage via %%doc magic
rm -rf __tmp_doc ; mkdir __tmp_doc
mv %{buildroot}%{_docdir}/%{name}/* __tmp_doc

# Fix permissions
find %{buildroot} -type f -name Hamlib.so -exec chmod 0755 {} ';'

# Remove unneeded files
find %{buildroot} -name \*.la -exec rm -f {} ';'
find %{buildroot} -type f -name pkgIndex.tcl -exec rm -f {} ';'
find %{buildroot} -type f -name .packlist -exec rm -f {} ';'
find %{buildroot} -type f -name Hamlib.bs -exec rm -f {} ';'
find %{buildroot} -type f -name perltest.pl -exec rm -f {} ';'

%check
make V=1 check

%ldconfig_scriptlets

%ldconfig_scriptlets c++

%ldconfig_scriptlets -n tcl-hamlib

%files
%license COPYING
%doc AUTHORS ChangeLog PLAN README THANKS
%{_bindir}/*
%{_libdir}/libhamlib.so.*
%{_mandir}/man?/*

%files devel
%doc README.developer
%{_libdir}/libhamlib.so
%{_libdir}/tcl%{tclver}/Hamlib/hamlibtcl.so
%{_datadir}/aclocal/hamlib.m4
%dir %{_includedir}/hamlib
%{_includedir}/hamlib/ampclass.h
%{_includedir}/hamlib/amplifier.h
%{_includedir}/hamlib/amplist.h
#{_includedir}/hamlib/config.h
%{_includedir}/hamlib/multicast.h
%{_includedir}/hamlib/rig.h
%{_includedir}/hamlib/riglist.h
%{_includedir}/hamlib/rig_dll.h
%{_includedir}/hamlib/rotator.h
%{_includedir}/hamlib/rotlist.h
%{_libdir}/pkgconfig/hamlib.pc

%files doc
%doc __tmp_doc/*

%files c++
%{_libdir}/libhamlib++.so.*

%files c++-devel
%{_libdir}/libhamlib++.so
%{_includedir}/hamlib/rigclass.h
%{_includedir}/hamlib/rotclass.h

%files -n perl-hamlib
%{perl_vendorarch}/*

%files -n python3-%{name}
%if 0%{?fedora} || 0%{?rhel} >= 8
%{python3_sitearch}/*.py*
%{python3_sitearch}/_Hamlib.so
%{python3_sitearch}/__pycache__/Hamlib.*
%else
%{python2_sitearch}/*.py*
%{python2_sitearch}/_Hamlib.so
%endif

%files -n tcl-hamlib
%{_libdir}/tcl%{tclver}/
%exclude %{_libdir}/tcl%{tclver}/Hamlib/hamlibtcl.so

%changelog
%autochangelog
