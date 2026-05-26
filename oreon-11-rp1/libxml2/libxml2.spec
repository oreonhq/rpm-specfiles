# oreon source sha256 begin
# URL sources: global sourceN_sha256 = 64-char hex from sha256sum. Omit a sourceN_sha256 line to skip verify for that source.
%global source0_sha256 c3d8c0c34aa39098f66576fe51969db12a5100b956233dc56506f7a8679be995
%global source1_sha256 96151685cec997e1f9f3387e3626d61e6284d4d6e66e0e440c209286c03e9cc7
%global source2_sha256 55e5c08db29946a91ea8e70e8f2418d3fd30d8b6777941dfba7f54726ffd9914
%global source3_sha256 09bdf9f81f381ebf9bc158a9472e498e896f7a02eb7461146e9abe1b9493ca17
%global oreon_verify_sources \
%{?source0_sha256:%(test -z "%{source0_sha256}" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_sha256}" || { echo "oreon: Source0 sha256 mismatch" >&2; exit 1; }; })} \
%{?source1_sha256:%(test -z "%{source1_sha256}" || { f="%{SOURCE1}"; test -f "$f" || { echo "oreon: missing Source1 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source1_sha256}" || { echo "oreon: Source1 sha256 mismatch" >&2; exit 1; }; })} \
%{?source2_sha256:%(test -z "%{source2_sha256}" || { f="%{SOURCE2}"; test -f "$f" || { echo "oreon: missing Source2 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source2_sha256}" || { echo "oreon: Source2 sha256 mismatch" >&2; exit 1; }; })} \
%{?source3_sha256:%(test -z "%{source3_sha256}" || { f="%{SOURCE3}"; test -f "$f" || { echo "oreon: missing Source3 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source3_sha256}" || { echo "oreon: Source3 sha256 mismatch" >&2; exit 1; }; })}
%(true)
# oreon source sha256 end

Name:           libxml2
Version:        2.12.10
Release:        6%{?dist}
Summary:        Library providing XML and HTML support

# list.c, dict.c and few others use ISC-Veillard
# the conformance and test suite data in
# Source1, Source2 and Source3 is covered by W3C
License:        MIT AND ISC-Veillard AND W3C
URL:            https://gitlab.gnome.org/GNOME/libxml2/-/wikis/home
Source0:        https://download.gnome.org/sources/%{name}/2.12/%{name}-%{version}.tar.xz
# https://www.w3.org/XML/Test/xmlconf-20080827.html
Source1:        https://www.w3.org/XML/Test/xmlts20080827.tar.gz
# https://www.w3.org/XML/2004/xml-schema-test-suite/index.html
Source2:        https://www.w3.org/XML/2004/xml-schema-test-suite/xmlschema2002-01-16/xsts-2002-01-16.tar.gz
Source3:        https://www.w3.org/XML/2004/xml-schema-test-suite/xmlschema2004-01-14/xsts-2004-01-14.tar.gz
Patch0:         libxml2-multilib.patch
# Patch from openSUSE.
# See:  https://bugzilla.gnome.org/show_bug.cgi?id=789714
Patch1:         libxml2-2.12.0-python3-unicode-errors.patch

BuildRequires:  cmake-rpm-macros
BuildRequires:  gcc
BuildRequires:  make
BuildRequires:  pkgconfig(zlib)
BuildRequires:  pkgconfig(liblzma)

%description
This library allows to manipulate XML files. It includes support
to read, modify and write XML and HTML files. There is DTDs support
this includes parsing and validation even with complex DtDs, either
at parse time or later once the document has been modified. The output
can be a simple SAX stream or and in-memory DOM like representations.
In this case one can use the built-in XPath and XPointer implementation
to select sub nodes or ranges. A flexible Input/Output mechanism is
available, with existing HTTP and FTP modules and combined to an
URI library.

%package devel
Summary:        Libraries, includes, etc. to develop XML and HTML applications
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       zlib-devel%{?_isa}
Requires:       xz-devel%{?_isa}

%description devel
Libraries, include files, etc you can use to develop XML applications.
This library allows to manipulate XML files. It includes support
to read, modify and write XML and HTML files. There is DTDs support
this includes parsing and validation even with complex DtDs, either
at parse time or later once the document has been modified. The output
can be a simple SAX stream or and in-memory DOM like representations.
In this case one can use the built-in XPath and XPointer implementation
to select sub nodes or ranges. A flexible Input/Output mechanism is
available, with existing HTTP and FTP modules and combined to an
URI library.

%package static
Summary:        Static library for libxml2

%description static
Static library for libxml2 provided for specific uses or shaving a few
microseconds when parsing, do not link to them for generic purpose packages.

%package -n python3-%{name}
Summary:        Python 3 bindings for the libxml2 library
BuildRequires:  python3-devel
Requires:       %{name}%{?_isa} = %{version}-%{release}
Obsoletes:      %{name}-python3 < %{version}-%{release}
Provides:       %{name}-python3 = %{version}-%{release}

%description -n python3-%{name}
The libxml2-python3 package contains a Python 3 module that permits
applications written in the Python programming language, version 3, to use the
interface supplied by the libxml2 library to manipulate XML files.

This library allows to manipulate XML files. It includes support
to read, modify and write XML and HTML files. There is DTDs support
this includes parsing and validation even with complex DTDs, either
at parse time or later once the document has been modified.

%prep
%oreon_verify_sources
%autosetup -p1
find doc -type f -executable -print -exec chmod 0644 {} ';'

%build
# see https://bugzilla.redhat.com/show_bug.cgi?id=2139546 , several
# of these options are needed to (mostly) retain ABI compatibility
# with earlier versions
%configure \
    --enable-static \
    --with-legacy \
    --with-ftp \
    --with-python=%{__python3}
%make_build

%install
%make_install

# multiarch crazyness on timestamp differences or Makefile/binaries for examples
touch -m --reference=%{buildroot}%{_includedir}/libxml2/libxml/parser.h %{buildroot}%{_bindir}/xml2-config

find %{buildroot} -type f -name '*.la' -print -delete
rm -vf %{buildroot}{%{python2_sitearch},%{python3_sitearch}}/*.a
rm -vrf %{buildroot}%{_datadir}/doc/
gzip -9 -c doc/libxml2-api.xml > doc/libxml2-api.xml.gz

%check
# Tests require the XML conformance suite.
tar -xzvf %{SOURCE1}
%make_build check
rm -rf xmlconf
# Schema tests use the schema test suite.
cp %{SOURCE2} %{SOURCE3} xstc/
pushd xstc
mkdir Tests
%make_build tests
popd
# As the directory is copied to the devel subpackage, remove any build
# artifacts.
(cd doc/examples ; make clean ; rm -rf .deps Makefile)

%ldconfig_scriptlets

%files
%license Copyright
%doc NEWS README.md
%{_libdir}/libxml2.so.2*
%{_bindir}/xmlcatalog
%{_bindir}/xmllint
%{_mandir}/man1/xmlcatalog.1*
%{_mandir}/man1/xmllint.1*

%files devel
%doc doc/*.html
%doc doc/tutorial doc/libxml2-api.xml.gz
%doc doc/examples
%dir %{_datadir}/gtk-doc
%dir %{_datadir}/gtk-doc/html
%{_datadir}/aclocal/libxml.m4
%{_datadir}/gtk-doc/html/libxml2/
%{_includedir}/libxml2/
%{_libdir}/libxml2.so
%{_libdir}/pkgconfig/libxml-2.0.pc
%{_libdir}/cmake/libxml2/
%{_bindir}/xml2-config
%{_mandir}/man1/xml2-config.1*

%files static
%license Copyright
%{_libdir}/libxml2.a

%files -n python3-%{name}
%doc doc/*.py
%{python3_sitearch}/libxml2mod.so
%{python3_sitelib}/libxml2.py
%{python3_sitelib}/__pycache__/libxml2.*
%{python3_sitelib}/drv_libxml2.py
%{python3_sitelib}/__pycache__/drv_libxml2.*

%changelog
* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 2.12.10-6
- Prepare for Oreon 11 (RP1)
