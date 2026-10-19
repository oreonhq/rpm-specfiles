%global source0_hash ae1fcf2dbc80ea0786ea8f047b09399c3f7737d1930442f61a031708ed33e88f
%global tclver 8.6
%global githash 0
%global shorthash %(c=%{githash}; echo ${c:0:10})
Name:           hamlib
Version:        4.7.2
Release:        1%{?dist}
Summary:        Run-time library to control radio transceivers and receivers
License:        GPL-2.0-or-later and LGPL-2.0-or-later
URL:            http://www.hamlib.org
%if "%{githash}" == "0"
Source0:        http://downloads.sourceforge.net/%{name}/%{name}-%{version}.tar.gz
%else
%endif
Patch0:         hamlib-4.0-perl_install.patch
Patch1:         hamlib-4.0-drop-libpython.patch
ExcludeArch:    i686
%{?perl_default_filter}
# oreon:deps
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  boost-devel
BuildRequires:  doxygen
BuildRequires:  gcc
BuildRequires:  gcc-c++
BuildRequires:  gd-devel
BuildRequires:  libtool
BuildRequires:  libtool-ltdl-devel
BuildRequires:  libusb1-devel
BuildRequires:  libxml2-devel
BuildRequires:  make
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl-devel
BuildRequires:  perl-generators
BuildRequires:  pkgconfig
BuildRequires:  python3-devel
BuildRequires:  source-highlight
BuildRequires:  swig
BuildRequires:  tcl-devel
# /oreon:deps
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

export PYTHON=%{__python2}
autoreconf -fi
%configure \
        --disable-static \
        --with-tcl=/usr/%{_lib} \
        --with-tcl-binding \
        --with-perl-binding \
        --with-python-binding \
%make_build
make -C doc doc
%install
%make_install
mkdir -p %{buildroot}%{_docdir}/%{name}/html/search
for f in `find doc/html/ -type f -maxdepth 1`
        do install -D -m 0644 $f %{buildroot}%{_docdir}/%{name}/`echo $f | cut -d '/' -f2`
done
for f in `find doc/html/search -type f -maxdepth 1`
        do install -D -m 0644 $f %{buildroot}%{_docdir}/%{name}/html/`echo $f | cut -d '/' -f3`
 done
rm -rf __tmp_doc ; mkdir __tmp_doc
mv %{buildroot}%{_docdir}/%{name}/* __tmp_doc
find %{buildroot} -type f -name Hamlib.so -exec chmod 0755 {} ';'
find %{buildroot} -name \*.la -exec rm -f {} ';'
find %{buildroot} -type f -name pkgIndex.tcl -exec rm -f {} ';'
find %{buildroot} -type f -name .packlist -exec rm -f {} ';'
find %{buildroot} -type f -name Hamlib.bs -exec rm -f {} ';'
find %{buildroot} -type f -name perltest.pl -exec rm -f {} ';'
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%check

make V=1 check
%ldconfig_scriptlets
%ldconfig_scriptlets c++
%ldconfig_scriptlets -n tcl-hamlib
%files -f %{oreon_filedir}/main.list
%files -n hamlib-devel -f %{oreon_filedir}/hamlib-devel.list
%files -n hamlib-doc -f %{oreon_filedir}/hamlib-doc.list
%files -n perl-hamlib -f %{oreon_filedir}/perl-hamlib.list
%files -n python3-hamlib -f %{oreon_filedir}/python3-hamlib.list
%files -n tcl-hamlib -f %{oreon_filedir}/tcl-hamlib.list

%changelog

%autochangelog
