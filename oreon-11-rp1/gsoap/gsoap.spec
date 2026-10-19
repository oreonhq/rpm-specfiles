%global source0_hash b981818fbbd4bf9f6f4feac03136800f6e16a7d0b7515924ff7a2661ca26e581
Summary:        Generator Tools for Coding SOAP/XML Web Services in C and C++
Name: gsoap
Version: 2.8.144
Release:        1%{?dist}
License: GPL-2.0-or-later
URL: https://gsoap2.sourceforge.net/
Source0:        https://downloads.sourceforge.net/gsoap2/%{name}_%{version}.zip
Source1: soapcpp2.1
Source2: wsdl2h.1
Source3: index.html
Patch0: %{name}-shuffle-reverse.patch
Patch1: %{name}-tree.patch
Patch2: %{name}-libtool.patch
Patch3: %{name}-doxygen-tabs.patch
# oreon:deps
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  bison
BuildRequires:  dos2unix
BuildRequires:  doxygen
BuildRequires:  flex
BuildRequires:  gcc-c++
BuildRequires:  graphviz
BuildRequires:  libtool
BuildRequires:  make
BuildRequires:  openssl-devel
BuildRequires:  zlib-devel
# /oreon:deps
%description
The gSOAP Web services development toolkit offers an XML to C/C++
language binding to ease the development of SOAP/XML Web services in C
and C/C++.

%package devel
Summary: Devel libraries and headers for linking with gSOAP generated stubs
Requires: %name = %version-%release
%description devel
gSOAP libraries, headers and generators for linking with and creating
gSOAP generated stubs.

%package doc
Summary: Documentation for gSOAP
BuildArch: noarch
%description doc
gSOAP documentation in html.

%prep

%setup -q -n gsoap-2.8
%patch -P0 -p1
%patch -P1 -p1
%patch -P2 -p1
%patch -P3 -p1

# XML files non-executable
find gsoap/samples/autotest/databinding/examples -name '*.xml' \
    -exec chmod a-x {} ';'

# Documentation fonts non-executable
chmod a-x gsoap/doc/fonts/*

# We want all txt files to have unix end-of-line encoding
dos2unix -k README.txt LICENSE.txt NOTES.txt GPLv2_license.txt \
    gsoap/plugin/sessions.c gsoap/plugin/sessions.h

# Remove stuff with gsoap license only - not GPL
rm -rf gsoap/extras gsoap/mod_gsoap gsoap/Symbian
sed 's!$(top_srcdir)/gsoap/extras/\*!!' -i gsoap/Makefile.am
rm -rf gsoap/doc/apache gsoap/doc/wininet gsoap/doc/isapi

# Remove pre-compiled binaries
rm -rf gsoap/bin
rm gsoap/samples/rest/person
rm gsoap/samples/wcf/Basic/TransportSecurity/calculator
rm gsoap/VisualStudio2005/wsdl2h/wsdl2h/soapcpp2.exe

# Remove pre-generated files
rm gsoap/samples/webserver/opt{C.c,H.h,Stub.h}
rm gsoap/VisualStudio2005/wsdl2h/wsdl2h/wsdl{C.cpp,H.h,Stub.h}

# Remove .DS_Store files
find . -name .DS_Store -exec rm {} ';'

%build

autoreconf --install --force
%configure --disable-static --enable-ipv6 --enable-samples
%make_build SOAPCPP2_IMPORTPATH='-DSOAPCPP2_IMPORT_PATH="\"%{_datadir}/gsoap/import:%{_datadir}/gsoap\""'
cp -pr gsoap/doc gsoap/doc-build
pushd gsoap/doc-build
rm -rf */html
for f in */Doxyfile ; do
  ( cd $(dirname $f) ; doxygen Doxyfile )
done
rm README.txt index.html
rm doxygen_footer.html doxygen_header.html
rm guide/index.md guide/stdsoap2.h soapdoc2.html
rm GeniviaLogo2_trans_noslogan.png
rm genivia_content.css genivia_tabs.css
rm */Doxyfile
rm */html/genivia_tabs.css
rm -f */doxygen_sqlite3.db
popd
install -m 644 -p %{SOURCE3} gsoap/doc-build
%install
%make_install
rm -f %{buildroot}/%{_libdir}/*.la
rm %{buildroot}/%{_datadir}/gsoap/custom/*.o
rm %{buildroot}/%{_datadir}/gsoap/plugin/*.o
mkdir -p %{buildroot}/%{_mandir}/man1
install -m 644 -p %{SOURCE1} %{SOURCE2} %{buildroot}/%{_mandir}/man1
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%check

%make_build check
%files -f %{oreon_filedir}/main.list
%files -n gsoap-devel -f %{oreon_filedir}/gsoap-devel.list
%files -n gsoap-doc -f %{oreon_filedir}/gsoap-doc.list

%changelog

%autochangelog
