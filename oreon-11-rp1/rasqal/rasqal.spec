Name:           rasqal
Version:        0.9.33
Release:        32%{?dist}
Summary:        RDF Query Library

License:        LGPL-2.1-or-later OR Apache-2.0
URL:            http://librdf.org/rasqal/
Source:         http://download.librdf.org/source/%{name}-%{version}.tar.gz

BuildRequires: make
BuildRequires:  gcc-c++
BuildRequires:  libxml2-devel
BuildRequires:  mpfr-devel
BuildRequires:  raptor2-devel
BuildRequires:  libgcrypt-devel
# for the testsuite
BuildRequires:  perl(Pod::Usage)
BuildRequires:  perl(XML::DOM)

# Upstream PR: https://github.com/dajobe/rasqal/pull/11
Patch1: define-printf.patch
Patch2: rasqal-configure-c99-2.patch

%description
Rasqal is a library providing full support for querying Resource
Description Framework (RDF) including parsing query syntaxes, constructing
the queries, executing them and returning result formats.  It currently
handles the RDF Data Query Language (RDQL) and SPARQL Query language.

%package        devel
Summary:        Development files for the Rasqal RDF libraries
Requires:       %{name}%{?_isa} = %{version}-%{release}
%description    devel
Libraries, includes etc to develop with the Rasqal RDF query language library.


%prep
%setup -q
%patch -P1 -p1 -b .printf
%patch -P2 -p1

# hack to nuke rpaths
%if "%{_libdir}" != "/usr/lib"
sed -i -e 's|"/lib /usr/lib|"/%{_lib} %{_libdir}|' configure
%endif


%build
%configure \
  --with-digest-library=gcrypt\
  --disable-pcre \
  --disable-static\
  --enable-release

%make_build


%install
%make_install

# unpackaged files
rm -fv $RPM_BUILD_ROOT%{_libdir}/lib*.la


%check
export PKG_CONFIG_PATH=%{buildroot}%{_datadir}/pkgconfig:%{buildroot}%{_libdir}/pkgconfig
test "$(pkg-config --modversion rasqal)" = "%{version}"
if [ -x %{_bindir}/rapper ]; then
%ifarch ppc64 s390x
make -k check ||:
%else
make -k check
%endif
else
echo "WARNING: %{_bindir}/rapper not present in buildroot, 'make check' skipped"
fi


%ldconfig_scriptlets

%files
%license COPYING COPYING.LIB
%license LICENSE.txt LICENSE-2.0.txt
%doc AUTHORS ChangeLog NEWS NOTICE README
%doc RELEASE.html
%{_bindir}/roqet
%{_libdir}/librasqal.so.3*
%{_mandir}/man1/roqet.1*

%files devel
%doc docs/README.html
%{_bindir}/rasqal-config
%{_includedir}/rasqal/
%{_libdir}/librasqal.so
%{_libdir}/pkgconfig/rasqal.pc
%{_mandir}/man1/rasqal-config.1*
%{_mandir}/man3/librasqal.3*
%{_datadir}/gtk-doc/


%changelog
* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 0.9.33-32
- Prepare for Oreon 11 (RP1)
