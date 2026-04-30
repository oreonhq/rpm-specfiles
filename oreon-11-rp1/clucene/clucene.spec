
%global git_long  e8e3d20f20da5ee3e37d347207b01890829a5475
%global git_short e8e3d20
%global snap 20130812

# rpmdev-bumpspec / releng automation compatible
%global baserelease 56

Summary:	A C++ port of Lucene
Name:		clucene
Version:	2.3.3.4
Release:	%{baserelease}.%{snap}.%{git_short}git%{?dist}
# Automatically converted from old format: LGPLv2+ or ASL 2.0 - review is highly recommended.
License:	LicenseRef-Callaway-LGPLv2+ OR Apache-2.0
URL:		http://www.sourceforge.net/projects/clucene
# Release tag still records the old snapshot ids; sources are the upstream release tarball
# (avoids vendoring clucene-core-2.3.3.4-e8e3d20.tar.xz in distgit; spectool can fetch this URL).
Source0:	https://downloads.sourceforge.net/project/clucene/clucene-core-unstable/2.3/clucene-core-%{version}.tar.gz

BuildRequires:	boost-devel
BuildRequires:	cmake
BuildRequires:	gawk
BuildRequires:	gcc-c++
BuildRequires:	zlib-devel
BuildRequires: make

## upstreamable patches
# include LUCENE_SYS_INCLUDES in pkgconfig --cflags output
# https://bugzilla.redhat.com/748196
# and
# https://sourceforge.net/tracker/?func=detail&aid=3461512&group_id=80013&atid=558446
# pkgconfig file is missing clucene-shared
Patch50: clucene-core-2.3.3.4-pkgconfig.patch
# https://bugzilla.redhat.com/794795
# https://sourceforge.net/tracker/index.php?func=detail&aid=3392466&group_id=80013&atid=558446
# contribs-lib is not built and installed even with config
Patch51: clucene-core-2.3.3.4-install_contribs_lib.patch  
# Don't install CLuceneConfig.cmake twice
Patch52: clucene-core-2.3.3.4-CLuceneConfig.patch
# Fix tests for undefined usleep
Patch53: clucene-core-2.3.3.4-usleep.patch
# Upstream at <https://sourceforge.net/p/clucene/bugs/232/> "Patches for
# TestIndexSearcher failures":
Patch54: 0001-Make-sure-to-return-value-from-non-void-function.patch
Patch55: 0002-Avoid-deadlock-in-TestIndexSearcher.patch
# Upstream at <https://sourceforge.net/p/clucene/code/merge-requests/3/> "Fix
# missing #include <time.h>":
Patch56: 0001-Fix-missing-include-time.h.patch
Patch57: pkgconfig.patch

%description
CLucene is a C++ port of the popular Apache Lucene search engine
(http://lucene.apache.org/java). 
CLucene aims to be a high-speed alternative to Java Lucene, its API is very
similar to that of the Java version. CLucene has recently been brought up to
date with Lucene 2.3.2. It contains most of the same functionality as the Java version.

%package core
Summary:	Core clucene module
Provides:	clucene = %{version}-%{release}
#Requires: %%{name} = %%{version}-%%{release}
%description core
CLucene is a C++ port of the popular Apache Lucene search engine
(http://lucene.apache.org/java).
CLucene aims to be a high-speed alternative to Java Lucene, its API is very
similar to that of the Java version. CLucene has recently been brought up to
date with Lucene 2.3.2. It contains most of the same functionality as the Java version.

%package core-devel
Summary:	Headers for developing programs that will use %{name}
Requires:	%{name}-core%{?_isa} = %{version}-%{release}
Requires:	%{name}-contribs-lib%{?_isa} = %{version}-%{release}
%description core-devel
This package contains the libraries and header files needed for
developing with clucene

%package contribs-lib
Summary:	Language specific text analyzers for %{name}
Requires:	%{name}-core%{?_isa} = %{version}-%{release}
%description contribs-lib
%{summary}.


%prep
%setup -n %{name}-core-%{version}

%patch -P50 -p1 -b .pkgconfig
%patch -P51 -p1 -b .install_contribs_lib
%patch -P52 -p1 -b .CLuceneConfig
%patch -P53 -p1 -b .usleep
%patch -P54 -p1 -b .return-value
%patch -P55 -p1 -b .avoid-deadlock
%patch -P56 -p1 -b .missing-include
%patch -P57 -p1 -b .pkgconfig

# nuke bundled code
rm -rfv src/ext/{boost/,zlib/}


%build
%cmake \
   -DINCLUDE_INSTALL_DIR:PATH=%{_includedir} \
   -DLIB_INSTALL_DIR:PATH=%{_libdir} \
   -DSYSCONF_INSTALL_DIR:PATH=%{_sysconfdir} \
   -DSHARE_INSTALL_PREFIX:PATH=%{_datadir} \
   %if "%{?_lib}" == "lib64"
     %{?_cmake_lib_suffix64} \
   %endif
  -DBUILD_CONTRIBS_LIB:BOOL=ON \
  -DLIB_DESTINATION:PATH=%{_libdir} \
  -DLUCENE_SYS_INCLUDES:PATH=%{_libdir} \
  -DCMAKE_POLICY_VERSION_MINIMUM=3.5

%cmake_build


%install
%cmake_install


%check
export PKG_CONFIG_PATH=%{buildroot}%{_libdir}/pkgconfig
test "$(pkg-config --modversion libclucene-core)" = "%{version}"
# FIXME: make tests non-fatal for ppc and s390 (big endian 32 bit archs) until we have a proper fix
#ifnarch ppc s390
export CTEST_OUTPUT_ON_FAILURE=1
# needing the 'touch' here seems an odd workaroudn for missing dependency, race condition or cache requirement
touch src/test/CMakeLists.txt && \
make -C %{_target_platform} cl_test && \
time make -C %{_target_platform} test ARGS="--timeout 300 --output-on-failure" ||:
#endif

%ldconfig_scriptlets core

%files core
%doc AUTHORS ChangeLog README
%license APACHE.license COPYING LGPL.license
%{_libdir}/libclucene-core.so.1*
%{_libdir}/libclucene-core.so.%{version}
%{_libdir}/libclucene-shared.so.1*
%{_libdir}/libclucene-shared.so.%{version}

%ldconfig_scriptlets contribs-lib

%files contribs-lib
%{_libdir}/libclucene-contribs-lib.so.1*
%{_libdir}/libclucene-contribs-lib.so.%{version}

%files core-devel
%dir %{_libdir}/CLucene
%{_includedir}/CLucene/
%{_includedir}/CLucene.h
%{_libdir}/libclucene*.so
%{_libdir}/CLucene/clucene-config.h
%{_libdir}/CLucene/CLuceneConfig.cmake
%{_libdir}/pkgconfig/libclucene-core.pc


%changelog
* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 2.3.3.4-1
- Prepare for Oreon 11 (RP1)
