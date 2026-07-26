%global source0_hash 4fbe2d1e17ad4451bb3a9d9101ac89f7b465205470f1c7ad5e2c1386ac2c87d2

Name: xsd
Version: 4.1.0
Release: 0.19.a11%{?dist}
Summary: W3C XML schema to C++ data binding compiler
# Exceptions permit otherwise GPLv2 incompatible combination with ASL 2.0
# Automatically converted from old format: GPLv2 with exceptions and ASL 2.0 - review is highly recommended.
License: LicenseRef-Callaway-GPLv2-with-exceptions AND Apache-2.0  
URL: https://www.codesynthesis.com/products/xsd/
Source0: https://codesynthesis.com/~boris/tmp/xsd/%{version}.a11/xsd-%{version}.a11+dep.tar.bz2

# Sent suggestion to upstream via e-mail 20090707
# http://anonscm.debian.org/cgit/collab-maint/xsd.git/tree/debian/patches/0001-xsd_xsdcxx-rename.patch
Patch0: %{name}-%{version}-xsdcxx-rename.patch

# Remove tests for character reference values unsupported by Xerces-C++ 3.2
# https://anonscm.debian.org/cgit/collab-maint/xsd.git/diff/debian/patches/0110-xerces-c3.2.patch?id=442e98604d4158dae11056c4f94aaa655cb480fa
Patch1: %{name}-xerces_3-2.patch

BuildRequires: make
BuildRequires: m4, xerces-c-devel, libcutl-devel, gcc-c++

%if 0%{?rhel} >= 8 || 0%{?fedora}
BuildRequires: boost-devel
%else
BuildRequires: boost148-devel
Requires: boost148%{?_isa}
%endif

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

# Split API documentation to -doc subpackage.
mkdir -p apidocdir
mv $RPM_BUILD_ROOT%{_datadir}/doc/xsd/*.{xhtml,css} apidocdir/
mv $RPM_BUILD_ROOT%{_datadir}/doc/xsd/cxx/ apidocdir/
mv $RPM_BUILD_ROOT%{_datadir}/doc/xsd/ docdir/

# Convert to utf-8.
for file in docdir/NEWS; do
    mv $file timestamp
    iconv -f ISO-8859-1 -t UTF-8 -o $file timestamp
    touch -r timestamp $file
done

# Rename binary to xsdcxx to avoid conflicting with mono-web package.
# Sent suggestion to upstream via e-mail 20090707
# they will consider renaming in 4.0.0
mv $RPM_BUILD_ROOT%{_bindir}/xsd $RPM_BUILD_ROOT%{_bindir}/xsdcxx
mv $RPM_BUILD_ROOT%{_mandir}/man1/xsd.1 $RPM_BUILD_ROOT%{_mandir}/man1/xsdcxx.1

# Remove duplicate docs.
rm -rf $RPM_BUILD_ROOT%{_datadir}/doc/libxsd

# Remove Microsoft Visual C++ compiler helper files.
rm -rf $RPM_BUILD_ROOT%{_includedir}/xsd/cxx/compilers

# Remove redundant PostScript files that rpmlint grunts about not being UTF8
# See: https://bugzilla.redhat.com/show_bug.cgi?id=502024#c27
# for Boris Kolpackov's explanation about those
find apidocdir -name "*.ps" | xargs rm -f
# Remove other unwanted crap
find apidocdir -name "*.doxygen" \
            -o -name "makefile" \
            -o -name "*.html2ps" | xargs rm -f

##Test failed on EPEL6 due to "bad" xerces-c
##http://codesynthesis.com/pipermail/xsd-users/2015-October/004696.html
##https://bugzilla.redhat.com/show_bug.cgi?id=1270978
%if 0%{?fedora} || 0%{?rhel} >= 7
%check
make -j 1 test EXTERNAL_LIBCUTL=y BOOST_LINK_SYSTEM=y
%endif

%files
%doc docdir/README docdir/NEWS docdir/FLOSSE
%license docdir/GPLv2 docdir/LICENSE
%{_bindir}/xsdcxx
%{_mandir}/man1/xsdcxx.1*
%{_includedir}/xsd/

%files doc
%doc docdir/README docdir/NEWS docdir/FLOSSE
%license docdir/GPLv2 docdir/LICENSE
%doc apidocdir/*

%changelog
%autochangelog
