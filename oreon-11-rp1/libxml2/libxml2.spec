%global source0_hash 98087fd181d9070724f3fbc65c7377db03038eb92bd882374daff44940138821
%global source1_hash 96151685cec997e1f9f3387e3626d61e6284d4d6e66e0e440c209286c03e9cc7
%global source2_hash 55e5c08db29946a91ea8e70e8f2418d3fd30d8b6777941dfba7f54726ffd9914
%global source3_hash 09bdf9f81f381ebf9bc158a9472e498e896f7a02eb7461146e9abe1b9493ca17
Name:           libxml2
Version:        2.15.4
Release:        1%{?dist}
Summary:        Library providing XML and HTML support
License:        MIT AND ISC-Veillard AND W3C
URL:            https://gitlab.gnome.org/GNOME/libxml2/-/wikis/home
Source0:        https://download.gnome.org/sources/%{name}/2.15/%{name}-%{version}.tar.xz
Source1:        https://www.w3.org/XML/Test/xmlts20080827.tar.gz
Source2:        https://www.w3.org/XML/2004/xml-schema-test-suite/xmlschema2002-01-16/xsts-2002-01-16.tar.gz
Source3:        https://www.w3.org/XML/2004/xml-schema-test-suite/xmlschema2004-01-14/xsts-2004-01-14.tar.gz
Patch0:         libxml2-multilib.patch
# oreon:deps
BuildRequires:  cmake-rpm-macros
BuildRequires:  gcc
BuildRequires:  make
BuildRequires:  pkgconfig(liblzma)
BuildRequires:  pkgconfig(zlib)
BuildRequires:  python3-devel
# /oreon:deps
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

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
test "%{source1_hash}" = "none" || { f="%{SOURCE1}"; test -f "$f" || { echo "oreon: missing Source1 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source1_hash}" || { echo "oreon: Source1 hash mismatch" >&2; exit 1; }; }
test "%{source2_hash}" = "none" || { f="%{SOURCE2}"; test -f "$f" || { echo "oreon: missing Source2 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source2_hash}" || { echo "oreon: Source2 hash mismatch" >&2; exit 1; }; }
test "%{source3_hash}" = "none" || { f="%{SOURCE3}"; test -f "$f" || { echo "oreon: missing Source3 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source3_hash}" || { echo "oreon: Source3 hash mismatch" >&2; exit 1; }; }
%autosetup -p1
find doc -type f -executable -print -exec chmod 0644 {} ';'

%build

%configure \
    --enable-static \
    --with-legacy \
    --with-ftp \
    --with-python=%{__python3}
%make_build
%install
%make_install
touch -m --reference=%{buildroot}%{_includedir}/libxml2/libxml/parser.h %{buildroot}%{_bindir}/xml2-config
find %{buildroot} -type f -name '*.la' -print -delete
rm -vf %{buildroot}{%{python2_sitearch},%{python3_sitearch}}/*.a
rm -vrf %{buildroot}%{_datadir}/doc/
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/* usr/*/lib*.so.* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%check

tar -xzvf %{SOURCE1}
%make_build check
rm -rf xmlconf
cp %{SOURCE2} %{SOURCE3} xstc/
pushd xstc
mkdir Tests
%make_build tests
popd
(cd doc/examples ; make clean ; rm -rf .deps Makefile)
%ldconfig_scriptlets
%files -f %{oreon_filedir}/main.list
%files -n libxml2-devel -f %{oreon_filedir}/libxml2-devel.list
%files -n libxml2-static -f %{oreon_filedir}/libxml2-static.list
%files -n python3-libxml2 -f %{oreon_filedir}/python3-libxml2.list

%changelog

* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 2.12.10-6
- Prepare for Oreon 11 (RP1)
