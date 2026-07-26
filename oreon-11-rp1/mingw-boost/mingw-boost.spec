%global source0_hash none

%?mingw_package_header

%global name1 boost
Name:           mingw-%{name1}
Version:        1.78.0
Release:        19%{?dist}
Summary:        MinGW Windows port of Boost C++ Libraries

# Replace each . with _ in %%{version}
%global version_enc %{lua:
  local ver = rpm.expand("%{version}")
  ver = ver:gsub("%.", "_")
  print(ver)
}
%global toplev_dirname %{name1}_%{version_enc}

# Automatically converted from old format: Boost - review is highly recommended.
License:        BSL-1.0
URL:            http://www.boost.org
Source0:        https://sourceforge.net/projects/%%{name1}/files/%{name1}/%{version}/%{toplev_dirname}.tar.bz2

# https://bugzilla.redhat.com/show_bug.cgi?id=828856
# https://bugzilla.redhat.com/show_bug.cgi?id=828857
# https://svn.boost.org/trac/boost/ticket/6701
Patch15:        boost-1.58.0-pool.patch

# https://svn.boost.org/trac/boost/ticket/9038
Patch51:        boost-1.58.0-pool-test_linking.patch

# https://bugzilla.redhat.com/show_bug.cgi?id=1541035
Patch105:       boost-1.78.0-build-optflags.patch

# https://bugzilla.redhat.com/show_bug.cgi?id=1318383
Patch106:       boost-1.78.0-no-rpath.patch

# https://lists.boost.org/Archives/boost/2020/04/248812.php
Patch88:        boost-1.73.0-cmakedir.patch

# https://bugzilla.redhat.com/show_bug.cgi?id=1899888
# https://github.com/boostorg/locale/issues/52
Patch94:        boost-1.73-locale-empty-vector.patch

# https://bugzilla.redhat.com/show_bug.cgi?id=1541035
Patch107:       boost-1.78.0-b2-build-flags.patch

# https://github.com/boostorg/random/issues/82
Patch102:       boost-1.76.0-random-test.patch

# PR https://github.com/boostorg/multiprecision/pull/421
# fixes ppc64le issue https://github.com/boostorg/multiprecision/issues/419
Patch103:       boost-1.76.0-fix_multiprecision_issue_419-ppc64le.patch

# PR https://github.com/boostorg/interval/pull/30
# Fixes narrowing conversions for ppc -
#   https://github.com/boostorg/interval/issues/29
Patch104:       boost-1.76.0-fix-narrowing-conversions-for-ppc.patch 

# https://github.com/boostorg/ptr_container/pull/27
Patch108:       boost-1.76.0-ptr_cont-xml.patch

# Fixes missing libboost_fiber.so
#  https://github.com/boostorg/boost/issues/632
Patch109:       boost-1.78.0-fix-b2-staging.patch

# https://github.com/boostorg/python/pull/385
Patch110:       boost-1.76.0-enum_type_object-type-python-3.11.patch

# https://svn.boost.org/trac/boost/ticket/7262
Patch1000:      boost-mingw.patch

# https://github.com/boostorg/serialization/pull/42
Patch1002:      boost-1.78.0-codecvtwchar.patch

BuildArch:      noarch

BuildRequires:  file
BuildRequires:  gcc
BuildRequires:  gcc-c++
BuildRequires:  mingw32-filesystem >= 117
BuildRequires:  mingw32-gcc
BuildRequires:  mingw32-gcc-c++
BuildRequires:  mingw32-binutils
BuildRequires:  mingw32-bzip2
BuildRequires:  mingw32-zlib
BuildRequires:  mingw32-expat
BuildRequires:  mingw32-winpthreads
BuildRequires:  mingw32-icu
#BuildRequires:  mingw32-win-iconv

BuildRequires:  mingw64-filesystem >= 117
BuildRequires:  mingw64-gcc
BuildRequires:  mingw64-gcc-c++
BuildRequires:  mingw64-binutils
BuildRequires:  mingw64-bzip2
BuildRequires:  mingw64-zlib
BuildRequires:  mingw64-expat
BuildRequires:  mingw64-winpthreads
BuildRequires:  mingw64-icu
#BuildRequires:  mingw64-win-iconv

BuildRequires:  perl-interpreter
# These are required by the native package:
#BuildRequires:  mingw32-python
#BuildRequires:  mingw64-python

%description
Boost provides free peer-reviewed portable C++ source libraries.  The
emphasis is on libraries which work well with the C++ Standard
Library, in the hopes of establishing "existing practice" for
extensions and providing reference implementations so that the Boost
libraries are suitable for eventual standardization. (Some of the
libraries have already been proposed for inclusion in the C++
Standards Committee's upcoming C++ Standard Library Technical Report.)

# Win32
%package -n mingw32-boost
Summary:         MinGW Windows Boost C++ library for the win32 target

%description -n mingw32-boost
Boost provides free peer-reviewed portable C++ source libraries.  The
emphasis is on libraries which work well with the C++ Standard
Library, in the hopes of establishing "existing practice" for
extensions and providing reference implementations so that the Boost
libraries are suitable for eventual standardization. (Some of the
libraries have already been proposed for inclusion in the C++
Standards Committee's upcoming C++ Standard Library Technical Report.)

%package -n mingw32-boost-static
Summary:        Static version of the MinGW Windows Boost C++ library
Requires:       mingw32-boost = %{version}-%{release}

%description -n mingw32-boost-static
Static version of the MinGW Windows Boost C++ library.

# Win64
%package -n mingw64-boost
Summary:         MinGW Windows Boost C++ library for the win64 target

%description -n mingw64-boost
Boost provides free peer-reviewed portable C++ source libraries.  The
emphasis is on libraries which work well with the C++ Standard
Library, in the hopes of establishing "existing practice" for
extensions and providing reference implementations so that the Boost
libraries are suitable for eventual standardization. (Some of the
libraries have already been proposed for inclusion in the C++
Standards Committee's upcoming C++ Standard Library Technical Report.)

%package -n mingw64-boost-static
Summary:        Static version of the MinGW Windows Boost C++ library
Requires:       mingw64-boost = %{version}-%{release}

%description -n mingw64-boost-static
Static version of the MinGW Windows Boost C++ library.

%?mingw_debug_package

%prep
%setup -qc
mv %{toplev_dirname} win32

pushd win32
find ./boost -name '*.hpp' -perm /111 | xargs chmod a-x

%patch -P15 -p0
%patch -P51 -p1
%patch -P105 -p1
%patch -P106 -p1
%patch -P107 -p1
%patch -P88 -p1
%patch -P94 -p1
%patch -P102 -p1
%patch -P103 -p2
%patch -P104 -p2
%patch -P108 -p1
%patch -P109 -p1
%patch -P110 -p1

%patch -P1000 -p0 -b .mingw
%patch -P1002 -p1 -b .codecvtwchar
popd

cp -r win32 win64

%build
%if 0%{?mingw_build_win32} == 1
pushd win32
export MINGW32_CXXFLAGS="$MINGW32_CXXFLAGS %{mingw32_cflags}"
export MINGW32_LDFLAGS="$MINGW32_LDFLAGS %{mingw32_ldflags}"
cat >> ./tools/build/src/user-config.jam << "EOF"
import os ;
local MINGW32_CXXFLAGS = [ os.environ MINGW32_CXXFLAGS ] ;
local MINGW32_LDFLAGS = [ os.environ MINGW32_LDFLAGS ] ;

using gcc : : i686-w64-mingw32-g++ : <rc>/usr/bin/i686-w64-mingw32-windres <compileflags>$(MINGW32_CXXFLAGS) <linkflags>$(MINGW32_LDFLAGS) ;
EOF

./bootstrap.sh --with-toolset=gcc --with-icu=%{mingw32_prefix}

echo ============================= build serial ==================
./b2 -d+2 -q %{?_smp_mflags} --layout=tagged \
	--without-mpi --without-graph_parallel --without-python --build-dir=serial \
	variant=release threading=single,multi debug-symbols=on pch=off \
	link=shared,static toolset=gcc target-os=windows address-model=32 stage
popd
%endif
%if 0%{?mingw_build_win64} == 1
pushd win64
export MINGW64_CXXFLAGS="$MINGW64_CXXFLAGS %{mingw64_cflags}"
export MINGW64_LDFLAGS="$MINGW64_LDFLAGS %{mingw64_ldflags}"
cat >> ./tools/build/src/user-config.jam << "EOF"
import os ;
local MINGW64_CXXFLAGS = [ os.environ MINGW64_CXXFLAGS ] ;
local MINGW64_LDFLAGS = [ os.environ MINGW64_LDFLAGS ] ;

using gcc : : x86_64-w64-mingw32-g++ : <rc>/usr/bin/x86_64-w64-mingw32-windres <compileflags>$(MINGW64_CXXFLAGS) <linkflags>$(MINGW64_LDFLAGS) ;
EOF

./bootstrap.sh --with-toolset=gcc --with-icu=%{mingw64_prefix}

echo ============================= build serial ==================
./b2 -d+2 -q %{?_smp_mflags} --layout=tagged \
	--without-mpi --without-graph_parallel --without-python --build-dir=serial \
	variant=release threading=single,multi debug-symbols=on pch=off \
	link=shared,static toolset=gcc target-os=windows address-model=64 stage
popd
%endif

%install
%if 0%{?mingw_build_win32} == 1
pushd win32
echo ============================= install serial ==================
./b2 -d+2 -q %{?_smp_mflags} --layout=tagged \
	--without-mpi --without-graph_parallel --without-python --build-dir=serial \
	--prefix=$RPM_BUILD_ROOT%{mingw32_prefix} \
	--libdir=$RPM_BUILD_ROOT%{mingw32_libdir} \
	variant=release threading=single,multi debug-symbols=on pch=off \
	link=shared,static target-os=windows address-model=32 install
popd
mkdir -p $RPM_BUILD_ROOT%{mingw32_bindir}
mv $RPM_BUILD_ROOT%{mingw32_libdir}/*.dll $RPM_BUILD_ROOT%{mingw32_bindir}
%endif
%if 0%{?mingw_build_win64} == 1
pushd win64
echo ============================= install serial ==================
./b2 -d+2 -q %{?_smp_mflags} --layout=tagged \
	--without-mpi --without-graph_parallel --without-python --build-dir=serial \
	--prefix=$RPM_BUILD_ROOT%{mingw64_prefix} \
	--libdir=$RPM_BUILD_ROOT%{mingw64_libdir} \
	variant=release threading=single,multi debug-symbols=on pch=off \
	link=shared,static target-os=windows address-model=64 install
popd
mkdir -p $RPM_BUILD_ROOT%{mingw64_bindir}
mv $RPM_BUILD_ROOT%{mingw64_libdir}/*.dll $RPM_BUILD_ROOT%{mingw64_bindir}
%endif

# Win32
%files -n mingw32-boost
%doc win32/LICENSE_1_0.txt
%{mingw32_includedir}/boost
%{mingw32_bindir}/libboost_atomic-mt-x32.dll
%{mingw32_bindir}/libboost_chrono-x32.dll
%{mingw32_bindir}/libboost_chrono-mt-x32.dll
%{mingw32_bindir}/libboost_container-x32.dll
%{mingw32_bindir}/libboost_container-mt-x32.dll
%{mingw32_bindir}/libboost_context-mt-x32.dll
%{mingw32_bindir}/libboost_contract-x32.dll
%{mingw32_bindir}/libboost_contract-mt-x32.dll
%{mingw32_bindir}/libboost_coroutine-x32.dll
%{mingw32_bindir}/libboost_coroutine-mt-x32.dll
%{mingw32_bindir}/libboost_date_time-x32.dll
%{mingw32_bindir}/libboost_date_time-mt-x32.dll
%{mingw32_bindir}/libboost_fiber-mt-x32.dll
%{mingw32_bindir}/libboost_filesystem-x32.dll
%{mingw32_bindir}/libboost_filesystem-mt-x32.dll
%{mingw32_bindir}/libboost_graph-x32.dll
%{mingw32_bindir}/libboost_graph-mt-x32.dll
%{mingw32_bindir}/libboost_iostreams-x32.dll
%{mingw32_bindir}/libboost_iostreams-mt-x32.dll
%{mingw32_bindir}/libboost_json-x32.dll
%{mingw32_bindir}/libboost_json-mt-x32.dll
%{mingw32_bindir}/libboost_locale-mt-x32.dll
%{mingw32_bindir}/libboost_log-x32.dll
%{mingw32_bindir}/libboost_log-mt-x32.dll
%{mingw32_bindir}/libboost_log_setup-x32.dll
%{mingw32_bindir}/libboost_log_setup-mt-x32.dll
%{mingw32_bindir}/libboost_math_c99-x32.dll
%{mingw32_bindir}/libboost_math_c99f-x32.dll
%{mingw32_bindir}/libboost_math_c99f-mt-x32.dll
%{mingw32_bindir}/libboost_math_c99l-x32.dll
%{mingw32_bindir}/libboost_math_c99l-mt-x32.dll
%{mingw32_bindir}/libboost_math_c99-mt-x32.dll
%{mingw32_bindir}/libboost_math_tr1-x32.dll
%{mingw32_bindir}/libboost_math_tr1f-x32.dll
%{mingw32_bindir}/libboost_math_tr1f-mt-x32.dll
%{mingw32_bindir}/libboost_math_tr1l-x32.dll
%{mingw32_bindir}/libboost_math_tr1l-mt-x32.dll
%{mingw32_bindir}/libboost_math_tr1-mt-x32.dll
%{mingw32_bindir}/libboost_nowide-x32.dll
%{mingw32_bindir}/libboost_nowide-mt-x32.dll
%{mingw32_bindir}/libboost_prg_exec_monitor-x32.dll
%{mingw32_bindir}/libboost_prg_exec_monitor-mt-x32.dll
%{mingw32_bindir}/libboost_program_options-x32.dll
%{mingw32_bindir}/libboost_program_options-mt-x32.dll
%{mingw32_bindir}/libboost_random-x32.dll
%{mingw32_bindir}/libboost_random-mt-x32.dll
%{mingw32_bindir}/libboost_regex-x32.dll
%{mingw32_bindir}/libboost_regex-mt-x32.dll
%{mingw32_bindir}/libboost_serialization-x32.dll
%{mingw32_bindir}/libboost_serialization-mt-x32.dll
%{mingw32_bindir}/libboost_stacktrace_basic-x32.dll
%{mingw32_bindir}/libboost_stacktrace_basic-mt-x32.dll
%{mingw32_bindir}/libboost_stacktrace_noop-x32.dll
%{mingw32_bindir}/libboost_stacktrace_noop-mt-x32.dll
%{mingw32_bindir}/libboost_system-x32.dll
%{mingw32_bindir}/libboost_system-mt-x32.dll
%{mingw32_bindir}/libboost_thread-mt-x32.dll
%{mingw32_bindir}/libboost_timer-x32.dll
%{mingw32_bindir}/libboost_timer-mt-x32.dll
%{mingw32_bindir}/libboost_type_erasure-x32.dll
%{mingw32_bindir}/libboost_type_erasure-mt-x32.dll
%{mingw32_bindir}/libboost_unit_test_framework-x32.dll
%{mingw32_bindir}/libboost_unit_test_framework-mt-x32.dll
%{mingw32_bindir}/libboost_wave-x32.dll
%{mingw32_bindir}/libboost_wave-mt-x32.dll
%{mingw32_bindir}/libboost_wserialization-x32.dll
%{mingw32_bindir}/libboost_wserialization-mt-x32.dll
%{mingw32_libdir}/libboost_atomic-mt-x32.dll.a
%{mingw32_libdir}/libboost_chrono-x32.dll.a
%{mingw32_libdir}/libboost_chrono-mt-x32.dll.a
%{mingw32_libdir}/libboost_container-x32.dll.a
%{mingw32_libdir}/libboost_container-mt-x32.dll.a
%{mingw32_libdir}/libboost_context-mt-x32.dll.a
%{mingw32_libdir}/libboost_contract-x32.dll.a
%{mingw32_libdir}/libboost_contract-mt-x32.dll.a
%{mingw32_libdir}/libboost_coroutine-x32.dll.a
%{mingw32_libdir}/libboost_coroutine-mt-x32.dll.a
%{mingw32_libdir}/libboost_date_time-x32.dll.a
%{mingw32_libdir}/libboost_date_time-mt-x32.dll.a
%{mingw32_libdir}/libboost_fiber-mt-x32.dll.a
%{mingw32_libdir}/libboost_filesystem-x32.dll.a
%{mingw32_libdir}/libboost_filesystem-mt-x32.dll.a
%{mingw32_libdir}/libboost_graph-x32.dll.a
%{mingw32_libdir}/libboost_graph-mt-x32.dll.a
%{mingw32_libdir}/libboost_iostreams-x32.dll.a
%{mingw32_libdir}/libboost_iostreams-mt-x32.dll.a
%{mingw32_libdir}/libboost_json-x32.dll.a
%{mingw32_libdir}/libboost_json-mt-x32.dll.a
%{mingw32_libdir}/libboost_locale-mt-x32.dll.a
%{mingw32_libdir}/libboost_log-x32.dll.a
%{mingw32_libdir}/libboost_log-mt-x32.dll.a
%{mingw32_libdir}/libboost_log_setup-x32.dll.a
%{mingw32_libdir}/libboost_log_setup-mt-x32.dll.a
%{mingw32_libdir}/libboost_math_c99-x32.dll.a
%{mingw32_libdir}/libboost_math_c99f-x32.dll.a
%{mingw32_libdir}/libboost_math_c99f-mt-x32.dll.a
%{mingw32_libdir}/libboost_math_c99l-x32.dll.a
%{mingw32_libdir}/libboost_math_c99l-mt-x32.dll.a
%{mingw32_libdir}/libboost_math_c99-mt-x32.dll.a
%{mingw32_libdir}/libboost_math_tr1-x32.dll.a
%{mingw32_libdir}/libboost_math_tr1f-x32.dll.a
%{mingw32_libdir}/libboost_math_tr1f-mt-x32.dll.a
%{mingw32_libdir}/libboost_math_tr1l-x32.dll.a
%{mingw32_libdir}/libboost_math_tr1l-mt-x32.dll.a
%{mingw32_libdir}/libboost_math_tr1-mt-x32.dll.a
%{mingw32_libdir}/libboost_nowide-x32.dll.a
%{mingw32_libdir}/libboost_nowide-mt-x32.dll.a
%{mingw32_libdir}/libboost_prg_exec_monitor-x32.dll.a
%{mingw32_libdir}/libboost_prg_exec_monitor-mt-x32.dll.a
%{mingw32_libdir}/libboost_program_options-x32.dll.a
%{mingw32_libdir}/libboost_program_options-mt-x32.dll.a
%{mingw32_libdir}/libboost_random-x32.dll.a
%{mingw32_libdir}/libboost_random-mt-x32.dll.a
%{mingw32_libdir}/libboost_regex-x32.dll.a
%{mingw32_libdir}/libboost_regex-mt-x32.dll.a
%{mingw32_libdir}/libboost_serialization-x32.dll.a
%{mingw32_libdir}/libboost_serialization-mt-x32.dll.a
%{mingw32_libdir}/libboost_stacktrace_basic-x32.dll.a
%{mingw32_libdir}/libboost_stacktrace_basic-mt-x32.dll.a
%{mingw32_libdir}/libboost_stacktrace_noop-x32.dll.a
%{mingw32_libdir}/libboost_stacktrace_noop-mt-x32.dll.a
%{mingw32_libdir}/libboost_system-x32.dll.a
%{mingw32_libdir}/libboost_system-mt-x32.dll.a
%{mingw32_libdir}/libboost_thread-mt-x32.dll.a
%{mingw32_libdir}/libboost_timer-x32.dll.a
%{mingw32_libdir}/libboost_timer-mt-x32.dll.a
%{mingw32_libdir}/libboost_type_erasure-x32.dll.a
%{mingw32_libdir}/libboost_type_erasure-mt-x32.dll.a
%{mingw32_libdir}/libboost_unit_test_framework-x32.dll.a
%{mingw32_libdir}/libboost_unit_test_framework-mt-x32.dll.a
%{mingw32_libdir}/libboost_wave-x32.dll.a
%{mingw32_libdir}/libboost_wave-mt-x32.dll.a
%{mingw32_libdir}/libboost_wserialization-x32.dll.a
%{mingw32_libdir}/libboost_wserialization-mt-x32.dll.a
%{mingw32_libdir}/cmake

%files -n mingw32-boost-static
%{mingw32_libdir}/libboost_atomic-mt-x32.a
%{mingw32_libdir}/libboost_chrono-x32.a
%{mingw32_libdir}/libboost_chrono-mt-x32.a
%{mingw32_libdir}/libboost_container-x32.a
%{mingw32_libdir}/libboost_container-mt-x32.a
%{mingw32_libdir}/libboost_context-mt-x32.a
%{mingw32_libdir}/libboost_contract-x32.a
%{mingw32_libdir}/libboost_contract-mt-x32.a
%{mingw32_libdir}/libboost_coroutine-x32.a
%{mingw32_libdir}/libboost_coroutine-mt-x32.a
%{mingw32_libdir}/libboost_date_time-x32.a
%{mingw32_libdir}/libboost_date_time-mt-x32.a
%{mingw32_libdir}/libboost_fiber-mt-x32.a
%{mingw32_libdir}/libboost_filesystem-x32.a
%{mingw32_libdir}/libboost_filesystem-mt-x32.a
%{mingw32_libdir}/libboost_graph-x32.a
%{mingw32_libdir}/libboost_graph-mt-x32.a
%{mingw32_libdir}/libboost_iostreams-x32.a
%{mingw32_libdir}/libboost_iostreams-mt-x32.a
%{mingw32_libdir}/libboost_json-x32.a
%{mingw32_libdir}/libboost_json-mt-x32.a
%{mingw32_libdir}/libboost_locale-mt-x32.a
%{mingw32_libdir}/libboost_log-x32.a
%{mingw32_libdir}/libboost_log-mt-x32.a
%{mingw32_libdir}/libboost_log_setup-x32.a
%{mingw32_libdir}/libboost_log_setup-mt-x32.a
%{mingw32_libdir}/libboost_math_c99-x32.a
%{mingw32_libdir}/libboost_math_c99f-x32.a
%{mingw32_libdir}/libboost_math_c99f-mt-x32.a
%{mingw32_libdir}/libboost_math_c99l-x32.a
%{mingw32_libdir}/libboost_math_c99l-mt-x32.a
%{mingw32_libdir}/libboost_math_c99-mt-x32.a
%{mingw32_libdir}/libboost_math_tr1-x32.a
%{mingw32_libdir}/libboost_math_tr1f-x32.a
%{mingw32_libdir}/libboost_math_tr1f-mt-x32.a
%{mingw32_libdir}/libboost_math_tr1l-x32.a
%{mingw32_libdir}/libboost_math_tr1l-mt-x32.a
%{mingw32_libdir}/libboost_math_tr1-mt-x32.a
%{mingw32_libdir}/libboost_nowide-x32.a
%{mingw32_libdir}/libboost_nowide-mt-x32.a
%{mingw32_libdir}/libboost_prg_exec_monitor-x32.a
%{mingw32_libdir}/libboost_prg_exec_monitor-mt-x32.a
%{mingw32_libdir}/libboost_program_options-x32.a
%{mingw32_libdir}/libboost_program_options-mt-x32.a
%{mingw32_libdir}/libboost_random-x32.a
%{mingw32_libdir}/libboost_random-mt-x32.a
%{mingw32_libdir}/libboost_regex-x32.a
%{mingw32_libdir}/libboost_regex-mt-x32.a
%{mingw32_libdir}/libboost_serialization-x32.a
%{mingw32_libdir}/libboost_serialization-mt-x32.a
%{mingw32_libdir}/libboost_stacktrace_basic-x32.a
%{mingw32_libdir}/libboost_stacktrace_basic-mt-x32.a
%{mingw32_libdir}/libboost_stacktrace_noop-x32.a
%{mingw32_libdir}/libboost_stacktrace_noop-mt-x32.a
%{mingw32_libdir}/libboost_system-x32.a
%{mingw32_libdir}/libboost_system-mt-x32.a
%{mingw32_libdir}/libboost_thread-mt-x32.a
%{mingw32_libdir}/libboost_timer-x32.a
%{mingw32_libdir}/libboost_timer-mt-x32.a
%{mingw32_libdir}/libboost_type_erasure-x32.a
%{mingw32_libdir}/libboost_type_erasure-mt-x32.a
%{mingw32_libdir}/libboost_unit_test_framework-x32.a
%{mingw32_libdir}/libboost_unit_test_framework-mt-x32.a
%{mingw32_libdir}/libboost_wave-x32.a
%{mingw32_libdir}/libboost_wave-mt-x32.a
%{mingw32_libdir}/libboost_wserialization-x32.a
%{mingw32_libdir}/libboost_wserialization-mt-x32.a
# static only libraries
%{mingw32_libdir}/libboost_exception-x32.a
%{mingw32_libdir}/libboost_exception-mt-x32.a
%{mingw32_libdir}/libboost_test_exec_monitor-x32.a
%{mingw32_libdir}/libboost_test_exec_monitor-mt-x32.a

# Win64
%files -n mingw64-boost
%doc win64/LICENSE_1_0.txt
%{mingw64_includedir}/boost
%{mingw64_bindir}/libboost_atomic-mt-x64.dll
%{mingw64_bindir}/libboost_chrono-x64.dll
%{mingw64_bindir}/libboost_chrono-mt-x64.dll
%{mingw64_bindir}/libboost_container-x64.dll
%{mingw64_bindir}/libboost_container-mt-x64.dll
%{mingw64_bindir}/libboost_context-mt-x64.dll
%{mingw64_bindir}/libboost_contract-x64.dll
%{mingw64_bindir}/libboost_contract-mt-x64.dll
%{mingw64_bindir}/libboost_coroutine-x64.dll
%{mingw64_bindir}/libboost_coroutine-mt-x64.dll
%{mingw64_bindir}/libboost_date_time-x64.dll
%{mingw64_bindir}/libboost_date_time-mt-x64.dll
%{mingw64_bindir}/libboost_fiber-mt-x64.dll
%{mingw64_bindir}/libboost_filesystem-x64.dll
%{mingw64_bindir}/libboost_filesystem-mt-x64.dll
%{mingw64_bindir}/libboost_graph-x64.dll
%{mingw64_bindir}/libboost_graph-mt-x64.dll
%{mingw64_bindir}/libboost_iostreams-x64.dll
%{mingw64_bindir}/libboost_iostreams-mt-x64.dll
%{mingw64_bindir}/libboost_json-x64.dll
%{mingw64_bindir}/libboost_json-mt-x64.dll
%{mingw64_bindir}/libboost_locale-mt-x64.dll
%{mingw64_bindir}/libboost_log-x64.dll
%{mingw64_bindir}/libboost_log-mt-x64.dll
%{mingw64_bindir}/libboost_log_setup-x64.dll
%{mingw64_bindir}/libboost_log_setup-mt-x64.dll
%{mingw64_bindir}/libboost_math_c99-x64.dll
%{mingw64_bindir}/libboost_math_c99f-x64.dll
%{mingw64_bindir}/libboost_math_c99f-mt-x64.dll
%{mingw64_bindir}/libboost_math_c99l-x64.dll
%{mingw64_bindir}/libboost_math_c99l-mt-x64.dll
%{mingw64_bindir}/libboost_math_c99-mt-x64.dll
%{mingw64_bindir}/libboost_math_tr1-x64.dll
%{mingw64_bindir}/libboost_math_tr1f-x64.dll
%{mingw64_bindir}/libboost_math_tr1f-mt-x64.dll
%{mingw64_bindir}/libboost_math_tr1l-x64.dll
%{mingw64_bindir}/libboost_math_tr1l-mt-x64.dll
%{mingw64_bindir}/libboost_math_tr1-mt-x64.dll
%{mingw64_bindir}/libboost_nowide-x64.dll
%{mingw64_bindir}/libboost_nowide-mt-x64.dll
%{mingw64_bindir}/libboost_prg_exec_monitor-x64.dll
%{mingw64_bindir}/libboost_prg_exec_monitor-mt-x64.dll
%{mingw64_bindir}/libboost_program_options-x64.dll
%{mingw64_bindir}/libboost_program_options-mt-x64.dll
%{mingw64_bindir}/libboost_random-x64.dll
%{mingw64_bindir}/libboost_random-mt-x64.dll
%{mingw64_bindir}/libboost_regex-x64.dll
%{mingw64_bindir}/libboost_regex-mt-x64.dll
%{mingw64_bindir}/libboost_serialization-x64.dll
%{mingw64_bindir}/libboost_serialization-mt-x64.dll
%{mingw64_bindir}/libboost_stacktrace_basic-x64.dll
%{mingw64_bindir}/libboost_stacktrace_basic-mt-x64.dll
%{mingw64_bindir}/libboost_stacktrace_noop-x64.dll
%{mingw64_bindir}/libboost_stacktrace_noop-mt-x64.dll
%{mingw64_bindir}/libboost_system-x64.dll
%{mingw64_bindir}/libboost_system-mt-x64.dll
%{mingw64_bindir}/libboost_thread-mt-x64.dll
%{mingw64_bindir}/libboost_timer-x64.dll
%{mingw64_bindir}/libboost_timer-mt-x64.dll
%{mingw64_bindir}/libboost_type_erasure-x64.dll
%{mingw64_bindir}/libboost_type_erasure-mt-x64.dll
%{mingw64_bindir}/libboost_unit_test_framework-x64.dll
%{mingw64_bindir}/libboost_unit_test_framework-mt-x64.dll
%{mingw64_bindir}/libboost_wave-x64.dll
%{mingw64_bindir}/libboost_wave-mt-x64.dll
%{mingw64_bindir}/libboost_wserialization-x64.dll
%{mingw64_bindir}/libboost_wserialization-mt-x64.dll
%{mingw64_libdir}/libboost_atomic-mt-x64.dll.a
%{mingw64_libdir}/libboost_chrono-x64.dll.a
%{mingw64_libdir}/libboost_chrono-mt-x64.dll.a
%{mingw64_libdir}/libboost_container-x64.dll.a
%{mingw64_libdir}/libboost_container-mt-x64.dll.a
%{mingw64_libdir}/libboost_context-mt-x64.dll.a
%{mingw64_libdir}/libboost_contract-x64.dll.a
%{mingw64_libdir}/libboost_contract-mt-x64.dll.a
%{mingw64_libdir}/libboost_coroutine-x64.dll.a
%{mingw64_libdir}/libboost_coroutine-mt-x64.dll.a
%{mingw64_libdir}/libboost_date_time-x64.dll.a
%{mingw64_libdir}/libboost_date_time-mt-x64.dll.a
%{mingw64_libdir}/libboost_fiber-mt-x64.dll.a
%{mingw64_libdir}/libboost_filesystem-x64.dll.a
%{mingw64_libdir}/libboost_filesystem-mt-x64.dll.a
%{mingw64_libdir}/libboost_graph-x64.dll.a
%{mingw64_libdir}/libboost_graph-mt-x64.dll.a
%{mingw64_libdir}/libboost_iostreams-x64.dll.a
%{mingw64_libdir}/libboost_iostreams-mt-x64.dll.a
%{mingw64_libdir}/libboost_json-x64.dll.a
%{mingw64_libdir}/libboost_json-mt-x64.dll.a
%{mingw64_libdir}/libboost_locale-mt-x64.dll.a
%{mingw64_libdir}/libboost_log-x64.dll.a
%{mingw64_libdir}/libboost_log-mt-x64.dll.a
%{mingw64_libdir}/libboost_log_setup-x64.dll.a
%{mingw64_libdir}/libboost_log_setup-mt-x64.dll.a
%{mingw64_libdir}/libboost_math_c99-x64.dll.a
%{mingw64_libdir}/libboost_math_c99f-x64.dll.a
%{mingw64_libdir}/libboost_math_c99f-mt-x64.dll.a
%{mingw64_libdir}/libboost_math_c99l-x64.dll.a
%{mingw64_libdir}/libboost_math_c99l-mt-x64.dll.a
%{mingw64_libdir}/libboost_math_c99-mt-x64.dll.a
%{mingw64_libdir}/libboost_math_tr1-x64.dll.a
%{mingw64_libdir}/libboost_math_tr1f-x64.dll.a
%{mingw64_libdir}/libboost_math_tr1f-mt-x64.dll.a
%{mingw64_libdir}/libboost_math_tr1l-x64.dll.a
%{mingw64_libdir}/libboost_math_tr1l-mt-x64.dll.a
%{mingw64_libdir}/libboost_math_tr1-mt-x64.dll.a
%{mingw64_libdir}/libboost_nowide-x64.dll.a
%{mingw64_libdir}/libboost_nowide-mt-x64.dll.a
%{mingw64_libdir}/libboost_prg_exec_monitor-x64.dll.a
%{mingw64_libdir}/libboost_prg_exec_monitor-mt-x64.dll.a
%{mingw64_libdir}/libboost_program_options-x64.dll.a
%{mingw64_libdir}/libboost_program_options-mt-x64.dll.a
%{mingw64_libdir}/libboost_random-x64.dll.a
%{mingw64_libdir}/libboost_random-mt-x64.dll.a
%{mingw64_libdir}/libboost_regex-x64.dll.a
%{mingw64_libdir}/libboost_regex-mt-x64.dll.a
%{mingw64_libdir}/libboost_serialization-x64.dll.a
%{mingw64_libdir}/libboost_serialization-mt-x64.dll.a
%{mingw64_libdir}/libboost_stacktrace_basic-x64.dll.a
%{mingw64_libdir}/libboost_stacktrace_basic-mt-x64.dll.a
%{mingw64_libdir}/libboost_stacktrace_noop-x64.dll.a
%{mingw64_libdir}/libboost_stacktrace_noop-mt-x64.dll.a
%{mingw64_libdir}/libboost_system-x64.dll.a
%{mingw64_libdir}/libboost_system-mt-x64.dll.a
%{mingw64_libdir}/libboost_thread-mt-x64.dll.a
%{mingw64_libdir}/libboost_timer-x64.dll.a
%{mingw64_libdir}/libboost_timer-mt-x64.dll.a
%{mingw64_libdir}/libboost_type_erasure-x64.dll.a
%{mingw64_libdir}/libboost_type_erasure-mt-x64.dll.a
%{mingw64_libdir}/libboost_unit_test_framework-x64.dll.a
%{mingw64_libdir}/libboost_unit_test_framework-mt-x64.dll.a
%{mingw64_libdir}/libboost_wave-x64.dll.a
%{mingw64_libdir}/libboost_wave-mt-x64.dll.a
%{mingw64_libdir}/libboost_wserialization-x64.dll.a
%{mingw64_libdir}/libboost_wserialization-mt-x64.dll.a
%{mingw64_libdir}/cmake

%files -n mingw64-boost-static
%{mingw64_libdir}/libboost_atomic-mt-x64.a
%{mingw64_libdir}/libboost_chrono-x64.a
%{mingw64_libdir}/libboost_chrono-mt-x64.a
%{mingw64_libdir}/libboost_container-x64.a
%{mingw64_libdir}/libboost_container-mt-x64.a
%{mingw64_libdir}/libboost_context-mt-x64.a
%{mingw64_libdir}/libboost_contract-x64.a
%{mingw64_libdir}/libboost_contract-mt-x64.a
%{mingw64_libdir}/libboost_coroutine-x64.a
%{mingw64_libdir}/libboost_coroutine-mt-x64.a
%{mingw64_libdir}/libboost_date_time-x64.a
%{mingw64_libdir}/libboost_date_time-mt-x64.a
%{mingw64_libdir}/libboost_fiber-mt-x64.a
%{mingw64_libdir}/libboost_filesystem-x64.a
%{mingw64_libdir}/libboost_filesystem-mt-x64.a
%{mingw64_libdir}/libboost_graph-x64.a
%{mingw64_libdir}/libboost_graph-mt-x64.a
%{mingw64_libdir}/libboost_iostreams-x64.a
%{mingw64_libdir}/libboost_iostreams-mt-x64.a
%{mingw64_libdir}/libboost_json-x64.a
%{mingw64_libdir}/libboost_json-mt-x64.a
%{mingw64_libdir}/libboost_locale-mt-x64.a
%{mingw64_libdir}/libboost_log-x64.a
%{mingw64_libdir}/libboost_log-mt-x64.a
%{mingw64_libdir}/libboost_log_setup-x64.a
%{mingw64_libdir}/libboost_log_setup-mt-x64.a
%{mingw64_libdir}/libboost_math_c99-x64.a
%{mingw64_libdir}/libboost_math_c99f-x64.a
%{mingw64_libdir}/libboost_math_c99f-mt-x64.a
%{mingw64_libdir}/libboost_math_c99l-x64.a
%{mingw64_libdir}/libboost_math_c99l-mt-x64.a
%{mingw64_libdir}/libboost_math_c99-mt-x64.a
%{mingw64_libdir}/libboost_math_tr1-x64.a
%{mingw64_libdir}/libboost_math_tr1f-x64.a
%{mingw64_libdir}/libboost_math_tr1f-mt-x64.a
%{mingw64_libdir}/libboost_math_tr1l-x64.a
%{mingw64_libdir}/libboost_math_tr1l-mt-x64.a
%{mingw64_libdir}/libboost_math_tr1-mt-x64.a
%{mingw64_libdir}/libboost_nowide-x64.a
%{mingw64_libdir}/libboost_nowide-mt-x64.a
%{mingw64_libdir}/libboost_prg_exec_monitor-x64.a
%{mingw64_libdir}/libboost_prg_exec_monitor-mt-x64.a
%{mingw64_libdir}/libboost_program_options-x64.a
%{mingw64_libdir}/libboost_program_options-mt-x64.a
%{mingw64_libdir}/libboost_random-x64.a
%{mingw64_libdir}/libboost_random-mt-x64.a
%{mingw64_libdir}/libboost_regex-x64.a
%{mingw64_libdir}/libboost_regex-mt-x64.a
%{mingw64_libdir}/libboost_serialization-x64.a
%{mingw64_libdir}/libboost_serialization-mt-x64.a
%{mingw64_libdir}/libboost_stacktrace_basic-x64.a
%{mingw64_libdir}/libboost_stacktrace_basic-mt-x64.a
%{mingw64_libdir}/libboost_stacktrace_noop-x64.a
%{mingw64_libdir}/libboost_stacktrace_noop-mt-x64.a
%{mingw64_libdir}/libboost_system-x64.a
%{mingw64_libdir}/libboost_system-mt-x64.a
%{mingw64_libdir}/libboost_thread-mt-x64.a
%{mingw64_libdir}/libboost_timer-x64.a
%{mingw64_libdir}/libboost_timer-mt-x64.a
%{mingw64_libdir}/libboost_type_erasure-x64.a
%{mingw64_libdir}/libboost_type_erasure-mt-x64.a
%{mingw64_libdir}/libboost_unit_test_framework-x64.a
%{mingw64_libdir}/libboost_unit_test_framework-mt-x64.a
%{mingw64_libdir}/libboost_wave-x64.a
%{mingw64_libdir}/libboost_wave-mt-x64.a
%{mingw64_libdir}/libboost_wserialization-x64.a
%{mingw64_libdir}/libboost_wserialization-mt-x64.a
# static only libraries
%{mingw64_libdir}/libboost_exception-x64.a
%{mingw64_libdir}/libboost_exception-mt-x64.a
%{mingw64_libdir}/libboost_test_exec_monitor-x64.a
%{mingw64_libdir}/libboost_test_exec_monitor-mt-x64.a

%changelog
%autochangelog
