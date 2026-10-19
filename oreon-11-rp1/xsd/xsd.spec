%global source0_hash 4fbe2d1e17ad4451bb3a9d9101ac89f7b465205470f1c7ad5e2c1386ac2c87d2
Name: xsd
Version: 4.2.0
Release:        1%{?dist}
Summary:        W3C XML schema to C++ data binding compiler
License: LicenseRef-Callaway-GPLv2-with-exceptions AND Apache-2.0  
URL: https://www.codesynthesis.com/products/xsd/
Source0:        https://codesynthesis.com/~boris/tmp/xsd/%{version}.a11/xsd-%{version}.a11+dep.tar.bz2
Patch0: %{name}-%{version}-xsdcxx-rename.patch
Patch1: %{name}-xerces_3-2.patch
Requires: boost148%{?_isa}
# oreon:deps
BuildRequires:  boost148-devel
BuildRequires:  gcc-c++
BuildRequires:  ghostscript
BuildRequires:  libcutl-devel
BuildRequires:  m4
BuildRequires:  make
BuildRequires:  xerces-c-devel
# /oreon:deps
%description
CodeSynthesis XSD is an open-source, cross-platform W3C XML Schema to
C++ data binding compiler. Provided with an XML instance specification
(XML Schema), it generates C++ classes that represent the given
vocabulary as well as parsing and serialization code.
You can then access the data stored in XML using types and functions
that semantically correspond to your application domain rather than
dealing with intricacies of reading and writing XML.

%package   doc
BuildArch: noarch
BuildRequires: ghostscript
Summary:   API documentation files for %{name}
%description    doc
This package contains API documentation for %{name}.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p0 -n xsd-%{version}.a11+dep

##Unbundle libcutl
rm -rf libcutl

%build

%make_build verbose=1 CXX=g++ CC=gcc CXXFLAGS="$RPM_OPT_FLAGS -std=c++14 -fPIC -pie -Wl,-z,now" LDFLAGS="%{__global_ldflags} -fPIC -pie -Wl,-z,now" BOOST_LINK_SYSTEM=y EXTERNAL_LIBCUTL=y
%install
rm -rf apidocdir
%make_install LDFLAGS="%{__global_ldflags}" install_prefix=$RPM_BUILD_ROOT%{_prefix} \
 install_bin_dir=$RPM_BUILD_ROOT%{_bindir} install_man_dir=$RPM_BUILD_ROOT%{_mandir} EXTERNAL_LIBCUTL=y BOOST_LINK_SYSTEM=y
mkdir -p apidocdir
mv $RPM_BUILD_ROOT%{_datadir}/doc/xsd/*.{xhtml,css} apidocdir/
mv $RPM_BUILD_ROOT%{_datadir}/doc/xsd/cxx/ apidocdir/
mv $RPM_BUILD_ROOT%{_datadir}/doc/xsd/ docdir/
for file in docdir/NEWS; do
    mv $file timestamp
    iconv -f ISO-8859-1 -t UTF-8 -o $file timestamp
    touch -r timestamp $file
done
mv $RPM_BUILD_ROOT%{_bindir}/xsd $RPM_BUILD_ROOT%{_bindir}/xsdcxx
mv $RPM_BUILD_ROOT%{_mandir}/man1/xsd.1 $RPM_BUILD_ROOT%{_mandir}/man1/xsdcxx.1
rm -rf $RPM_BUILD_ROOT%{_datadir}/doc/libxsd
rm -rf $RPM_BUILD_ROOT%{_includedir}/xsd/cxx/compilers
find apidocdir -name "*.ps" | xargs rm -f
find apidocdir -name "*.doxygen" \
            -o -name "makefile" \
            -o -name "*.html2ps" | xargs rm -f
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%files -f %{oreon_filedir}/main.list
%files -n xsd-doc -f %{oreon_filedir}/xsd-doc.list

%changelog

%autochangelog
