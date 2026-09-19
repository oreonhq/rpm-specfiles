%global source0_hash fae086c84be930fde8a354247259604859fdc4d99db9edaa7c5aa1dec79eb595

##
# Original RPM Specification file from the Dries repository:
#   http://svn.rpmforge.net/svn/trunk/rpms/wsdlpull/wsdlpull.spec
# Original author: Dries Verachtert <dries@ulyssis.org>
##
#
%global mydocs __tmp_docdir
#
Name: wsdlpull
Version: 1.23
Release: 34%{?dist}

Summary: C++ Web Services client library

License: LGPL-2.0-or-later AND MIT
URL: http://%{name}.sourceforge.net

Source0: http://downloads.sourceforge.net/%{name}/%{name}-%{version}.tar.bz2
%{?el5:BuildRoot: %(mktemp -ud %{_tmppath}/%{name}-%{version}-%{release}-XXXXXX)}
# That patch will be submitted upstream
Patch0: wsdlpull-%{version}-fix-gcc43-compatibility.patch
# That patch will be submitted upstream
Patch1: wsdlpull-%{version}-add-man-pages.patch
# That patch will be submitted upstream
Patch2: wsdlpull-%{version}-fix-gnu-autotools-compatibility.patch

%description
%{name} is a C++ web services client library. It includes a WSDL
Parser, a XSD Schema Parser and Validator and XML Parser and serializer
and an API and command line tool for dynamic WSDL inspection and
invocation.

%{name} comes with a generic web service client. Using %{name} tools,
you can invoke most Web services from command line without writing any
code. See http://wsdlpull.sourceforge.net for usage.

%package devel
Summary: Header files, libraries and development documentation for %{name}
Requires: %{name} = %{version}-%{release}

%description devel
This package contains the header files, static libraries and development
documentation for %{name}. If you like to develop programs using %{name},
you will need to install %{name}-devel.

%package doc
Summary: HTML documentation for the %{name} library
%if 0%{?fedora} >= 10
BuildArch: noarch
%endif
BuildRequires: make
BuildRequires:  gcc-c++
BuildRequires: doxygen

%description doc
This package contains the documentation in the HTML format of the %{name}
library. The documentation is the same as at the %{name} web page.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q

# Apply the g++ 4.3 compatibility patch
%patch -P0 -p1

# Create a directory for man pages
%{__mkdir} man

# Apply the man page patch
%patch -P1 -p1

# Remove any CVS sub-directory (they should not be delivered with the tar-ball)
find . -name 'CVS' -print | xargs -r %{__rm} -rf

# Remove any a.out binary (they should not be delivered with the tar-ball)
find . -name 'a.out' -print | xargs -r %{__rm} -f

# Remove the generated HTML documentation (it should not be delivered
# with the tar-ball, as it is generated)
if [ -d docs/html ]; then
  %{__rm} -rf docs/html
fi

# Adapt a little bit the structure, so as to be more compliant with
# GNU Autotools
%{__mkdir} config
%{__mv} config.guess config.sub depcomp install-sh ltmain.sh missing config
%{__mv} config.h.in src

# Rename the standard documentation files
%{__mv} AUTHORS.txt AUTHORS
sed -i -e 's/\r$//' AUTHORS
%{__mv} CHANGES.txt CHANGES
%{__mv} COPYING.txt COPYING
%{__mv} README.txt README

# Apply the GNU Autotools compatibility patch
%patch -P2 -p1

%build
%configure --disable-static
make %{?_smp_mflags}

%install
%{__rm} -rf $RPM_BUILD_ROOT
make install DESTDIR=$RPM_BUILD_ROOT

# Remove unpackaged files from the buildroot
%{__rm} -f $RPM_BUILD_ROOT%{_libdir}/lib*.la
%{__rm} -rf %{mydocs} && %{__mkdir_p} %{mydocs}
%{__mv} $RPM_BUILD_ROOT%{_docdir}/%{name}-%{version}/html %{mydocs}

%ldconfig_scriptlets

%files
%doc AUTHORS CHANGES COPYING README
%{_bindir}/%{name}
%{_bindir}/%{name}-schema
%{_libdir}/lib*.so.*
%{_mandir}/man1/%{name}.1.*
%{_mandir}/man1/%{name}-config.1.*
%{_mandir}/man1/%{name}-schema.1.*
%{_datadir}/%{name}

%files devel
%{_includedir}/schemaparser
%{_includedir}/wsdlparser
%{_includedir}/xmlpull
%{_libdir}/lib*.so

%files doc
%doc AUTHORS CHANGES COPYING README
%doc %{mydocs}/html

%changelog
%autochangelog
