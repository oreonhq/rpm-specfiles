%global source0_hash ddfdc433dd8ad31b5c5819cc4404a8d2127472a3b720d3e744e8c51d79732eab
%global git_long  e8e3d20f20da5ee3e37d347207b01890829a5475
%global git_short e8e3d20
%global snap 20130812
%global baserelease 56
Summary:        A C++ port of Lucene
Name:		clucene
Version:	2.3.3.4
Release:        1%{?dist}
License:	LicenseRef-Callaway-LGPLv2+ OR Apache-2.0
URL:		http://www.sourceforge.net/projects/clucene
Source0:        https://downloads.sourceforge.net/clucene/clucene-core-%{version}.tar.gz
Patch50: clucene-core-2.3.3.4-pkgconfig.patch
Patch51: clucene-core-2.3.3.4-install_contribs_lib.patch  
Patch52: clucene-core-2.3.3.4-CLuceneConfig.patch
Patch53: clucene-core-2.3.3.4-TestIndexSearcher-tests.patch
Patch54: 0001-Fix-missing-include-time.h.patch
Patch55: pkgconfig.patch
# oreon:deps
BuildRequires:  boost-devel
BuildRequires:  cmake
BuildRequires:  gawk
BuildRequires:  gcc-c++
BuildRequires:  make
BuildRequires:  zlib-devel
# /oreon:deps
%description
CLucene is a C++ port of the popular Apache Lucene search engine
(http://lucene.apache.org/java). 
CLucene aims to be a high-speed alternative to Java Lucene, its API is very
similar to that of the Java version. CLucene has recently been brought up to
date with Lucene 2.3.2. It contains most of the same functionality as the Java version.

%package core
Summary:	Core clucene module
Provides:	clucene = %{version}-%{release}
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

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%setup -n %{name}-core-%{version}

%patch -P50 -p1 -b .pkgconfig
%patch -P51 -p1 -b .install_contribs_lib
%patch -P52 -p1 -b .CLuceneConfig
%patch -P53 -p1 -b .testindexsearcher
%patch -P54 -p1 -b .missing-include
%patch -P55 -p1 -b .pkgconfig

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
%oreon_autofiles clucene-core usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles clucene-core-devel usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*
%oreon_autofiles clucene-contribs-lib usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%check

export PKG_CONFIG_PATH=%{buildroot}%{_libdir}/pkgconfig
test "$(pkg-config --modversion libclucene-core)" = "%{version}"
export CTEST_OUTPUT_ON_FAILURE=1
touch src/test/CMakeLists.txt && \
make -C %{_target_platform} cl_test && \
time make -C %{_target_platform} test ARGS="--timeout 300 --output-on-failure" ||:
%ldconfig_scriptlets core
%files -f %{oreon_filedir}/main.list
%files -n clucene-core -f %{oreon_filedir}/clucene-core.list
%files -n clucene-core-devel -f %{oreon_filedir}/clucene-core-devel.list
%files -n clucene-contribs-lib -f %{oreon_filedir}/clucene-contribs-lib.list

%changelog

* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 2.3.3.4-1
- Prepare for Oreon 11 (RP1)
