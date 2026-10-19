%global source0_hash 0187336b0285038fab4f4a6b7654f51beaebab040b6aad53c147c917c5ab519b
%global		soversion	2.1
Name:		nvidia-texture-tools
Version:	2.1.2
Release:        1%{?dist}
Summary:        Collection of image processing and texture manipulation tools
License:	LicenseRef-Callaway-MIT AND Apache-2.0 AND LicenseRef-Callaway-BSD
URL:		https://github.com/castano/nvidia-texture-tools/wiki
Source0:        https://github.com/castano/%{name}/archive/%{version}.tar.gz
Patch0:		%{name}-libs.patch
Patch1:		%{name}-check.patch
Patch2:		%{name}-docs.patch
Patch3:		%{name}-mips.patch
Patch4:		%{name}-s390.patch
Patch5:		%{name}-ppcle.patch
Patch6:		%{name}-aarch64.patch
Patch7:		%{name}-simd.patch
Patch8:		%{name}-flags.patch
Patch9:		%{name}-debug.patch
Patch10:	%{name}-riscv64.patch
# oreon:deps
BuildRequires:  cmake
BuildRequires:  gcc
BuildRequires:  gcc-c++
BuildRequires:  help2man
BuildRequires:  libGL-devel
BuildRequires:  libGLU-devel
BuildRequires:  libjpeg-turbo-devel
BuildRequires:  libpng-devel
BuildRequires:  libtiff-devel
# /oreon:deps
%description
The NVIDIA Texture Tools is a collection of image processing and texture
manipulation tools, designed to be integrated in game tools and asset
conditioning pipelines.

The primary features of the library are mipmap and normal map generation,
format conversion and DXT compression.

DXT compression is based on Simon Brown's squish library. The library also
contains an alternative GPU-accelerated compressor that uses CUDA and is
one order of magnitude faster.

%package	devel
Summary:	Development libraries/headers for %{name}
Requires:	%{name}%{?_isa} = %{version}-%{release}
%description	devel
Headers and libraries for development with %{name}.

%prep

%setup -q
%patch -P0 -p0
%patch -P1 -p0
%patch -P2 -p0
%patch -P3 -p0
%patch -P4 -p0
%patch -P5 -p0
%patch -P6 -p0
%patch -P7 -p0
%patch -P8 -p0
%ifnarch %{ix86} x86_64
%patch -P9 -p0
%endif
%patch -P10 -p1

%build

%cmake -DNVTT_SHARED=1 -DCMAKE_SKIP_RPATH=1 -DCMAKE_POLICY_VERSION_MINIMUM=3.5	\
  -DINCLUDE_INSTALL_DIR:PATH=%{_includedir} \
   -DLIB_INSTALL_DIR:PATH=%{_libdir} \
   -DSYSCONF_INSTALL_DIR:PATH=%{_sysconfdir} \
   -DSHARE_INSTALL_PREFIX:PATH=%{_datadir} \
   %if "%{?_lib}" == "lib64"
     %{?_cmake_lib_suffix64} \
   %endif
%ifnarch %{ix86} x86_64
	-DBUILD_SQUISH_WITH_SSE2=OFF		\
%endif
%cmake_build
sed -e 's/\r//' -i LICENSE
%install
%cmake_install
mkdir -p $RPM_BUILD_ROOT/%{_mandir}/man1
pushd $RPM_BUILD_ROOT/%{_bindir}
    export LD_LIBRARY_PATH=$RPM_BUILD_ROOT/%{_libdir}:
    for bin in *; do
	help2man --no-info ./$bin > $RPM_BUILD_ROOT/%{_mandir}/man1/$bin.1
    done
popd
%ifnarch %{ix86}
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*

%check

export LD_LIBRARY_PATH=$RPM_BUILD_ROOT/%{_libdir}:
%ctest
%endif
%ldconfig_scriptlets
%files -f %{oreon_filedir}/main.list
%files -n nvidia-texture-tools-devel -f %{oreon_filedir}/nvidia-texture-tools-devel.list

%changelog

%autochangelog
