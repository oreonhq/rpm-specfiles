%global source0_hash none

Summary: Generator Tools for Coding SOAP/XML Web Services in C and C++
Name: gsoap
Version: 2.8.139
Release: 1%{?dist}

# gsoap is licensed both under the gSOAP public license and under GPL version
# 2 or later with an OpenSSL linking exception.
#
# The gSOAP public license is a modified version of the Mozilla Public License.
# Due to the modifications, the gSOAP public license is non-free. You can not
# use gsoap under this license for software that you intend to contribute to
# fedora. If you use gsoap in fedora you must use it under the GPL license,
# possibly using the OpenSSL linking exception. The specific modification that
# makes the license non-free is in section 3.2:
#
# 3.2. Availability of Source Code.
# Any Modification created by You will be provided to the Initial Developer in
# Source Code form and are subject to the terms of the License.
License: GPL-2.0-or-later
URL: https://gsoap2.sourceforge.net/
Source0: https://downloads.sourceforge.net/gsoap2/%{name}_%{version}.zip
Source1: soapcpp2.1
Source2: wsdl2h.1
# Replace top level index.html in the doc package with a version without
# external image, js and css references to https://www.genivia.com/
Source3: index.html
# Fix build with "make --shuffle=reverse"
# https://sourceforge.net/p/gsoap2/patches/186/
Patch0: %{name}-shuffle-reverse.patch
# Fix out-of-source build
# https://sourceforge.net/p/gsoap2/patches/187/
Patch1: %{name}-tree.patch
# Create shared libraries
Patch2: %{name}-libtool.patch
# The custom tabs css does not work with newer doxygen - use default version
Patch3: %{name}-doxygen-tabs.patch

BuildRequires: gcc-c++
BuildRequires: flex
BuildRequires: bison
BuildRequires: dos2unix
BuildRequires: openssl-devel
BuildRequires: zlib-devel
BuildRequires: autoconf
BuildRequires: automake
BuildRequires: libtool
BuildRequires: doxygen
BuildRequires: graphviz
BuildRequires: make

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
# Patches change autoconf and automake files, so we must reconfigure
autoreconf --install --force

%configure --disable-static --enable-ipv6 --enable-samples

# Dependencies are not declared properly -- no parallel build
# Add /usr/share/gsoap to soapcpp2's default import path
%make_build SOAPCPP2_IMPORTPATH='-DSOAPCPP2_IMPORT_PATH="\"%{_datadir}/gsoap/import:%{_datadir}/gsoap\""'

# Regenerete doxygen documentation
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

%check
%make_build check

%files
%doc factsheet.pdf NOTES.txt README.txt
%license LICENSE.txt GPLv2_license.txt
%{_libdir}/libgsoap-*.so
%{_libdir}/libgsoap++-*.so
%{_libdir}/libgsoapck-*.so
%{_libdir}/libgsoapck++-*.so
%{_libdir}/libgsoapssl-*.so
%{_libdir}/libgsoapssl++-*.so

%files devel
%{_bindir}/soapcpp2
%{_bindir}/wsdl2h
%{_mandir}/man1/soapcpp2.1*
%{_mandir}/man1/wsdl2h.1*
%{_libdir}/libgsoap.so
%{_libdir}/libgsoap++.so
%{_libdir}/libgsoapck.so
%{_libdir}/libgsoapck++.so
%{_libdir}/libgsoapssl.so
%{_libdir}/libgsoapssl++.so
%{_includedir}/stdsoap2.h
%dir %{_datadir}/gsoap
%dir %{_datadir}/gsoap/import
%{_datadir}/gsoap/import/c14n.h
%{_datadir}/gsoap/import/dom.h
%{_datadir}/gsoap/import/ds2.h
%{_datadir}/gsoap/import/ds.h
%{_datadir}/gsoap/import/README.txt
%{_datadir}/gsoap/import/soap12.h
%{_datadir}/gsoap/import/stldeque.h
%{_datadir}/gsoap/import/stl.h
%{_datadir}/gsoap/import/stllist.h
%{_datadir}/gsoap/import/stlset.h
%{_datadir}/gsoap/import/stlvector.h
%{_datadir}/gsoap/import/wsa3.h
%{_datadir}/gsoap/import/wsa4.h
%{_datadir}/gsoap/import/wsa5.h
%{_datadir}/gsoap/import/wsa.h
%{_datadir}/gsoap/import/WS-example.c
%{_datadir}/gsoap/import/WS-example.h
%{_datadir}/gsoap/import/WS-Header.h
%{_datadir}/gsoap/import/wsp.h
%{_datadir}/gsoap/import/wsrp.h
%{_datadir}/gsoap/import/wsse2.h
%{_datadir}/gsoap/import/wsse.h
%{_datadir}/gsoap/import/wsu.h
%{_datadir}/gsoap/import/xlink.h
%{_datadir}/gsoap/import/xmime4.h
%{_datadir}/gsoap/import/xmime5.h
%{_datadir}/gsoap/import/xmime.h
%{_datadir}/gsoap/import/xml.h
%{_datadir}/gsoap/import/xmlmime5.h
%{_datadir}/gsoap/import/xmlmime.h
%{_datadir}/gsoap/import/xop.h
%dir %{_datadir}/gsoap/WS
%{_datadir}/gsoap/WS/README.txt
%{_datadir}/gsoap/WS/WS-Addressing.xsd
%{_datadir}/gsoap/WS/WS-Addressing03.xsd
%{_datadir}/gsoap/WS/WS-Addressing04.xsd
%{_datadir}/gsoap/WS/WS-Addressing05.xsd
%{_datadir}/gsoap/WS/WS-Discovery.wsdl
%{_datadir}/gsoap/WS/WS-Enumeration.wsdl
%{_datadir}/gsoap/WS/WS-Policy.xsd
%{_datadir}/gsoap/WS/WS-Routing.xsd
%{_datadir}/gsoap/WS/WS-typemap.dat
%{_datadir}/gsoap/WS/discovery.xsd
%{_datadir}/gsoap/WS/ds.xsd
%{_datadir}/gsoap/WS/enumeration.xsd
%{_datadir}/gsoap/WS/typemap.dat
%{_datadir}/gsoap/WS/wsse.xsd
%{_datadir}/gsoap/WS/wsu.xsd
%dir %{_datadir}/gsoap/custom
%{_datadir}/gsoap/custom/README.txt
%{_datadir}/gsoap/custom/long_double.c
%{_datadir}/gsoap/custom/long_double.h
%{_datadir}/gsoap/custom/struct_timeval.c
%{_datadir}/gsoap/custom/struct_timeval.h
%{_datadir}/gsoap/custom/struct_tm.c
%{_datadir}/gsoap/custom/struct_tm.h
%dir %{_datadir}/gsoap/plugin
%{_datadir}/gsoap/plugin/README.txt
%{_datadir}/gsoap/plugin/cacerts.c
%{_datadir}/gsoap/plugin/cacerts.h
%{_datadir}/gsoap/plugin/httpda.c
%{_datadir}/gsoap/plugin/httpda.h
%{_datadir}/gsoap/plugin/httpdatest.c
%{_datadir}/gsoap/plugin/httpdatest.h
%{_datadir}/gsoap/plugin/httpform.c
%{_datadir}/gsoap/plugin/httpform.h
%{_datadir}/gsoap/plugin/httpget.c
%{_datadir}/gsoap/plugin/httpget.h
%{_datadir}/gsoap/plugin/httpgettest.c
%{_datadir}/gsoap/plugin/httpgettest.h
%{_datadir}/gsoap/plugin/httpmd5.c
%{_datadir}/gsoap/plugin/httpmd5.h
%{_datadir}/gsoap/plugin/httpmd5test.c
%{_datadir}/gsoap/plugin/httpmd5test.h
%{_datadir}/gsoap/plugin/httppost.c
%{_datadir}/gsoap/plugin/httppost.h
%{_datadir}/gsoap/plugin/logging.c
%{_datadir}/gsoap/plugin/logging.h
%{_datadir}/gsoap/plugin/md5evp.c
%{_datadir}/gsoap/plugin/md5evp.h
%{_datadir}/gsoap/plugin/plugin.c
%{_datadir}/gsoap/plugin/plugin.h
%{_datadir}/gsoap/plugin/smdevp.c
%{_datadir}/gsoap/plugin/smdevp.h
%{_datadir}/gsoap/plugin/threads.c
%{_datadir}/gsoap/plugin/threads.h
%{_datadir}/gsoap/plugin/wsaapi.c
%{_datadir}/gsoap/plugin/wsaapi.h
%{_datadir}/gsoap/plugin/wsse2api.c
%{_datadir}/gsoap/plugin/wsse2api.h
%{_datadir}/gsoap/plugin/wsseapi.c
%{_datadir}/gsoap/plugin/wsseapi.h
%{_libdir}/pkgconfig/gsoapck.pc
%{_libdir}/pkgconfig/gsoapck++.pc
%{_libdir}/pkgconfig/gsoap.pc
%{_libdir}/pkgconfig/gsoap++.pc
%{_libdir}/pkgconfig/gsoapssl.pc
%{_libdir}/pkgconfig/gsoapssl++.pc
# Additions in 2.7.12-1
%{_datadir}/gsoap/WS/WS-ReliableMessaging.wsdl
%{_datadir}/gsoap/WS/WS-ReliableMessaging.xsd
%{_datadir}/gsoap/WS/reference-1.1.xsd
%{_datadir}/gsoap/WS/ws-reliability-1.1.xsd
%{_datadir}/gsoap/import/ref.h
%{_datadir}/gsoap/import/wsrm.h
%{_datadir}/gsoap/import/wsrm4.h
%{_datadir}/gsoap/import/wsrx.h
# Additions in 2.7.13-1
%{_datadir}/gsoap/import/stdstring.h
%{_datadir}/gsoap/import/xsd.h
%{_datadir}/gsoap/plugin/wsseapi.cpp
# Additions in 2.7.16-1
%{_datadir}/gsoap/custom/duration.c
%{_datadir}/gsoap/custom/duration.h
%{_datadir}/gsoap/plugin/httpposttest.c
%{_datadir}/gsoap/plugin/httpposttest.h
%{_datadir}/gsoap/plugin/wsrmapi.c
%{_datadir}/gsoap/plugin/wsrmapi.h
# Additions in 2.7.17-1
%{_datadir}/gsoap/WS/WS-Policy12.xsd
%{_datadir}/gsoap/WS/WS-SecurityPolicy.xsd
%{_datadir}/gsoap/import/wsse11.h
# Additions in 2.8.3-1
%{_datadir}/gsoap/WS/xenc.xsd
%{_datadir}/gsoap/import/xenc.h
%{_datadir}/gsoap/plugin/mecevp.c
%{_datadir}/gsoap/plugin/mecevp.h
# Additions in 2.8.4-1
%{_datadir}/gsoap/import/wsdd.h
%{_datadir}/gsoap/import/wsdx.h
%{_datadir}/gsoap/plugin/wsddapi.c
%{_datadir}/gsoap/plugin/wsddapi.h
# Additions in 2.8.7-1
%{_datadir}/gsoap/import/wsdd10.h
# Additions in 2.8.12-1
%{_datadir}/gsoap/WS/WS-SecureConversation.xsd
%{_datadir}/gsoap/WS/WS-Trust.wsdl
%{_datadir}/gsoap/WS/WS-Trust.xsd
%{_datadir}/gsoap/import/ser.h
%{_datadir}/gsoap/import/wsc.h
%{_datadir}/gsoap/import/wsrm5.h
%{_datadir}/gsoap/import/wsrx5.h
%{_datadir}/gsoap/import/wst.h
%{_datadir}/gsoap/import/wstx.h
# Additions in 2.8.16-1
%{_datadir}/gsoap/import/wsc2.h
%{_datadir}/gsoap/plugin/calcrest.h
# Additions in 2.8.17-1
%{_datadir}/gsoap/plugin/mq.c
%{_datadir}/gsoap/plugin/mq.h
# Additions in 2.8.21-1
%{_datadir}/gsoap/WS/LEGAL.txt
%{_datadir}/gsoap/WS/ws-bpel_abstract_common_base.xsd
%{_datadir}/gsoap/WS/ws-bpel_executable.xsd
%{_datadir}/gsoap/WS/ws-bpel_plnktype.xsd
%{_datadir}/gsoap/WS/ws-bpel_serviceref.xsd
%{_datadir}/gsoap/WS/ws-bpel_varprop.xsd
%{_datadir}/gsoap/import/plnk.h
%{_datadir}/gsoap/import/vprop.h
# Additions in 2.8.22-1
%{_datadir}/gsoap/import/wsdd5.h
%{_datadir}/gsoap/plugin/wsseapi-lite.c
%{_datadir}/gsoap/plugin/wsseapi-lite.h
# Additions in 2.8.28-1
%{_datadir}/gsoap/WS/oasis-sstc-saml-schema-assertion-1.1.xsd
%{_datadir}/gsoap/WS/saml-schema-assertion-2.0.xsd
%{_datadir}/gsoap/custom/chrono_duration.cpp
%{_datadir}/gsoap/custom/chrono_duration.h
%{_datadir}/gsoap/custom/chrono_time_point.cpp
%{_datadir}/gsoap/custom/chrono_time_point.h
%{_datadir}/gsoap/custom/float128.c
%{_datadir}/gsoap/custom/float128.h
%{_datadir}/gsoap/custom/int128.c
%{_datadir}/gsoap/custom/int128.h
%{_datadir}/gsoap/custom/long_time.c
%{_datadir}/gsoap/custom/long_time.h
%{_datadir}/gsoap/custom/struct_tm_date.c
%{_datadir}/gsoap/custom/struct_tm_date.h
%{_datadir}/gsoap/import/saml1.h
%{_datadir}/gsoap/import/saml2.h
# Additions in 2.8.35-1
%{_datadir}/gsoap/custom/qbytearray_base64.cpp
%{_datadir}/gsoap/custom/qbytearray_base64.h
%{_datadir}/gsoap/custom/qbytearray_hex.cpp
%{_datadir}/gsoap/custom/qbytearray_hex.h
%{_datadir}/gsoap/custom/qdate.cpp
%{_datadir}/gsoap/custom/qdate.h
%{_datadir}/gsoap/custom/qdatetime.cpp
%{_datadir}/gsoap/custom/qdatetime.h
%{_datadir}/gsoap/custom/qstring.cpp
%{_datadir}/gsoap/custom/qstring.h
%{_datadir}/gsoap/custom/qtime.cpp
%{_datadir}/gsoap/custom/qtime.h
%{_datadir}/gsoap/import/wsp_appliesto.h
%{_datadir}/gsoap/import/xenc2.h
%{_datadir}/gsoap/plugin/sessions.c
%{_datadir}/gsoap/plugin/sessions.h
%{_datadir}/gsoap/plugin/wstapi.c
%{_datadir}/gsoap/plugin/wstapi.h
# Additions in 2.8.48-1
%{_datadir}/gsoap/plugin/curlapi.c
%{_datadir}/gsoap/plugin/curlapi.h
# Additions in 2.8.75-1
%{_datadir}/gsoap/import/wst2.h
%{_datadir}/gsoap/import/wstx2.h
%{_datadir}/gsoap/plugin/httppipe.c
%{_datadir}/gsoap/plugin/httppipe.h

%files doc
%doc gsoap/doc-build/*
%license LICENSE.txt GPLv2_license.txt

%changelog
%autochangelog
