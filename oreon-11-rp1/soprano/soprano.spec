%global source0_hash 64066fbd54e71d7ae4c8a4116997448a72808a2813cff3bb5d2c28f0fce9e0e5

%undefine __cmake_in_source_build

# undef or set to 0 to disable items for a faster build
%global apidocs 1
# upstream says tests busted, maybe to be fixed in some future point release
%global tests 1
%if 0%{?fedora} < 24 && 0%{?rhel} <= 7 || (0%{?oreon} >= 11) 
%global virtuoso 1
%endif

Summary: Qt wrapper API to different RDF storage solutions
Name:    soprano
Version: 2.9.4
Release: 38%{?dist}

# Automatically converted from old format: LGPLv2+ - review is highly recommended.
License: LicenseRef-Callaway-LGPLv2+
URL:     https://quickgit.kde.org/?p=soprano.git
#URL:    http://sourceforge.net/projects/soprano

%if 0%{?snap:1}
# git clone git://anongit.kde.org/soprano ; cd soprano
# git archive --prefix=soprano-%%{version}/ master | bzip2 > soprano-%%{version}-%%{snap}.tar.bz2
Source0:        http://downloads.sf.net/soprano/soprano-%{version}.tar.bz2
%else
Source0:        http://downloads.sf.net/soprano/soprano-%{version}.tar.bz2
%endif

## upstreamable patches
Patch1: soprano-2.9.4-gcc6.patch

## upstream patches

BuildRequires: clucene-core-devel >= 0.9.20-2
BuildRequires: cmake
BuildRequires: kde4-macros(api)
BuildRequires: pkgconfig
BuildRequires: pkgconfig(raptor2)
BuildRequires: pkgconfig(rasqal) >= 0.9.22
BuildRequires: pkgconfig(redland)
BuildRequires: pkgconfig(QtDBus) pkgconfig(QtNetwork) pkgconfig(QtXml) 

%if 0%{?apidocs}
BuildRequires: doxygen
BuildRequires: graphviz
BuildRequires: qt4-doc
%endif

%{?_qt4_version:Requires: qt4%{?_isa} >= %{_qt4_version}}
## If/When backends are packaged separately
#Requires: soprano-backend
## otherwise,
Provides: soprano-backend = %{version}-%{release}
Provides: soprano-backend-redland =  %{version}-%{release}
%if 0%{?virtuoso}
Requires: redland-virtuoso
Provides: soprano-backend-virtuoso = %{version}-%{release}
## nepomuk upstream recommends this be in nepomuk-core, and strictly optional here -- rex
#Recommends: virtuoso-opensource
%endif

%description
%{summary}.

%package devel
Summary: Developer files for %{name}
Requires: %{name}%{?_isa} = %{version}-%{release}
%description devel
%{summary}.

%package backend-redland 
Summary: Redland backend for %{name}
Provides: %{name}-backend = %{version}-%{release}
Requires: %{name}%{?_isa} = %{version}-%{release}
%description backend-redland 
%{summary}.

%if 0%{?virtuoso}
%package backend-virtuoso
Summary: Virtuoso backend for %{name}
BuildRequires: libiodbc-devel
%if 0%{?tests}
BuildRequires: virtuoso-opensource
%endif
Provides: %{name}-backend = %{version}-%{release}
Requires: %{name}%{?_isa} = %{version}-%{release}
## not sure if  this is really needed -- rex
Requires: redland-virtuoso
## nepomuk upstream recommends this be in nepomuk-core, and strictly optional here -- rex
#Recommends: virtuoso-opensource
%description backend-virtuoso 
%{summary}.
%endif

%package apidocs
Summary: Soprano API documentation
Requires: kde-filesystem
BuildArch: noarch
%description apidocs
This package includes the Soprano API documentation in HTML
format for easy browsing.


%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%setup -q -n soprano-%{version}%{?pre:-%{pre}}

%patch -P1 -p1 -b .gcc6


%build
%cmake \
  -DDATA_INSTALL_DIR:PATH=%{_kde4_appsdir} \
  -DQT_DOC_DIR=%{?_qt4_docdir}%{!?_qt4_docdir:%(pkg-config --variable=docdir Qt)} \
  -DSOPRANO_BUILD_API_DOCS:BOOL=%{!?apidocs:0}%{?apidocs} \
  -DSOPRANO_BUILD_TESTS:BOOL=%{?tests:ON}%{!?tests:OFF} \
  -DSOPRANO_DISABLE_SESAME2_BACKEND:BOOL=ON \
  %{!?virtuoso:-DSOPRANO_DISABLE_VIRTUOSO_BACKEND:BOOL=ON}

%cmake_build


%install
%cmake_install

%if 0%{?apidocs}
mkdir -p %{buildroot}%{_kde4_docdir}/HTML/en
cp -a %{_vpath_builddir}/docs/html %{buildroot}%{_kde4_docdir}/HTML/en/soprano-apidocs
# spurious executables, pull in perl dep(s)
find %{buildroot}%{_kde4_docdir}/HTML/en/ -name 'installdox' -exec rm -fv {} ';'
%endif


%check
# verify pkg-config version (notoriously wrong in recent soprano releases)
export PKG_CONFIG_PATH=%{buildroot}%{_datadir}/pkgconfig:%{buildroot}%{_libdir}/pkgconfig
test "$(pkg-config --modversion soprano)" = "%{version}"
%if 0%{?tests:1}
export CTEST_OUTPUT_ON_FAILURE=1
# expect serveral failures, but we care mostly about virtuosobackendtest
time make -C %{_vpath_builddir} test ARGS="--timeout 300 --output-on-failure -R virtuosobackendtest" ||:
%endif


%ldconfig_scriptlets

%files
%doc AUTHORS README TODO
%license COPYING*
%{_bindir}/sopranocmd
%{_bindir}/sopranod
%{_bindir}/onto2vocabularyclass
%{_libdir}/libsoprano.so.4*
%{_libdir}/libsopranoclient.so.1*
%{_libdir}/libsopranoindex.so.1*
%{_libdir}/libsopranoserver.so.1*
%dir %{_datadir}/soprano/
%dir %{_datadir}/soprano/plugins
%{_datadir}/soprano/plugins/*parser.desktop
%{_datadir}/soprano/plugins/*serializer.desktop
%{_datadir}/soprano/rules/
%dir %{_libdir}/soprano/
%{_libdir}/soprano/libsoprano_*parser.so
%{_libdir}/soprano/libsoprano_*serializer.so

#files backend-redland
%{_libdir}/soprano/libsoprano_redlandbackend.so
%{_datadir}/soprano/plugins/redlandbackend.desktop

%if 0%{?virtuoso}
#files backend-virtuoso
%{_libdir}/soprano/libsoprano_virtuosobackend.so
%{_datadir}/soprano/plugins/virtuosobackend.desktop
%endif

%files devel
%{_datadir}/dbus-1/interfaces/org.soprano.*.xml
%{_datadir}/soprano/cmake/
%{_libdir}/libsoprano*.so
%{_libdir}/pkgconfig/soprano.pc
%{_libdir}/pkgconfig/sopranoclient.pc
%{_libdir}/pkgconfig/sopranoindex.pc
%{_libdir}/pkgconfig/sopranoserver.pc
%{_includedir}/soprano/
%{_includedir}/Soprano/

%if 0%{?apidocs}
%files apidocs
%{_kde4_docdir}/HTML/en/soprano-apidocs/
%endif


%changelog
* Mon May 25 2026 Oreon Packaging Team <packaging@oreonhq.com> - 2.9.4-38
- Import
