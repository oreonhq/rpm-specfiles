%global source0_hash none

%global		soversion	2.1

Name:		nvidia-texture-tools
Version:	2.1.2
Release:	16%{?dist}
Summary:	Collection of image processing and texture manipulation tools
# Automatically converted from old format: MIT and ASL 2.0 and BSD - review is highly recommended.
License:	LicenseRef-Callaway-MIT AND Apache-2.0 AND LicenseRef-Callaway-BSD
URL:		https://github.com/castano/nvidia-texture-tools/wiki
Source0:	https://github.com/castano/%{name}/archive/%{version}.tar.gz
BuildRequires:  gcc
BuildRequires:  gcc-c++
BuildRequires:	cmake
BuildRequires:	help2man
BuildRequires:	libjpeg-turbo-devel
BuildRequires:	libpng-devel
BuildRequires:	libtiff-devel
BuildRequires:	libGL-devel
BuildRequires:	libGLU-devel

Patch0:		%{name}-libs.patch
Patch1:		%{name}-check.patch
Patch2:		%{name}-docs.patch
# add MIPS support
Patch3:		%{name}-mips.patch
# add S390 support
Patch4:		%{name}-s390.patch
# add PPCLE support
Patch5:		%{name}-ppcle.patch
# add aarch64 support
Patch6:		%{name}-aarch64.patch
# Do not presume SSE is available
Patch7:		%{name}-simd.patch
# Do not force compiler flags
Patch8:		%{name}-flags.patch
# Only implemented for x86
Patch9:		%{name}-debug.patch
# add riscv64
Patch10:	%{name}-riscv64.patch

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
%if 0
%ifarch ppc64 ppc64le
	-DBUILD_SQUISH_WITH_ALTIVEC=ON		\
%endif
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
%check
export LD_LIBRARY_PATH=$RPM_BUILD_ROOT/%{_libdir}:
%ctest
%endif

%ldconfig_scriptlets

%files
%license LICENSE
%doc README.md
%{_bindir}/*
%{_libdir}/lib*.%{version}
%{_libdir}/lib*.%{soversion}
%{_mandir}/man1/*

%files		devel
%doc ChangeLog
%{_includedir}/nvtt
%{_libdir}/lib*.so

%changelog
%autochangelog
