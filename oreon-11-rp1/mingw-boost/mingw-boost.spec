%global source0_hash 8681f175d4bdb26c52222665793eef08490d7758529330f98d3b29dd0735bccc
%?mingw_package_header
%global name1 boost
Name:           mingw-%{name1}
Version:        1.78.0
Release:        1%{?dist}
Summary:        MinGW Windows port of Boost C++ Libraries
%global version_enc %{lua:
  local ver = rpm.expand("%{version}")
  ver = ver:gsub("%.", "_")
  print(ver)
}
%global toplev_dirname %{name1}_%{version_enc}
License:        BSL-1.0
URL:            http://www.boost.org
Source0:        https://sourceforge.net/projects/%{name1}/files/%{name1}/%{version}/%{name1}_1_78_0.tar.bz2
Patch15:        boost-1.58.0-pool.patch
Patch51:        boost-1.58.0-pool-test_linking.patch
Patch105:       boost-1.78.0-build-optflags.patch
Patch106:       boost-1.78.0-no-rpath.patch
Patch88:        boost-1.73.0-cmakedir.patch
Patch94:        boost-1.73-locale-empty-vector.patch
Patch107:       boost-1.78.0-b2-build-flags.patch
Patch102:       boost-1.76.0-random-test.patch
Patch103:       boost-1.76.0-fix_multiprecision_issue_419-ppc64le.patch
Patch104:       boost-1.76.0-fix-narrowing-conversions-for-ppc.patch 
Patch108:       boost-1.76.0-ptr_cont-xml.patch
Patch109:       boost-1.78.0-fix-b2-staging.patch
Patch110:       boost-1.76.0-enum_type_object-type-python-3.11.patch
Patch1000:      boost-mingw.patch
Patch1002:      boost-1.78.0-codecvtwchar.patch
BuildArch:      noarch
# oreon:deps
BuildRequires:  file
BuildRequires:  gcc
BuildRequires:  gcc-c++
BuildRequires:  mingw32-binutils
BuildRequires:  mingw32-bzip2
BuildRequires:  mingw32-expat
BuildRequires:  mingw32-filesystem
BuildRequires:  mingw32-gcc
BuildRequires:  mingw32-gcc-c++
BuildRequires:  mingw32-icu
BuildRequires:  mingw32-winpthreads
BuildRequires:  mingw32-zlib
BuildRequires:  mingw64-binutils
BuildRequires:  mingw64-bzip2
BuildRequires:  mingw64-expat
BuildRequires:  mingw64-filesystem
BuildRequires:  mingw64-gcc
BuildRequires:  mingw64-gcc-c++
BuildRequires:  mingw64-icu
BuildRequires:  mingw64-winpthreads
BuildRequires:  mingw64-zlib
BuildRequires:  perl-interpreter
# /oreon:deps
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
%oreon_autofiles mingw32-boost usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles mingw32-boost-static usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles mingw64-boost usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles mingw64-boost-static usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%endif
%files -f %{oreon_filedir}/main.list
%files -n mingw32-boost -f %{oreon_filedir}/mingw32-boost.list
%files -n mingw32-boost-static -f %{oreon_filedir}/mingw32-boost-static.list
%files -n mingw64-boost -f %{oreon_filedir}/mingw64-boost.list
%files -n mingw64-boost-static -f %{oreon_filedir}/mingw64-boost-static.list

%changelog

%autochangelog
