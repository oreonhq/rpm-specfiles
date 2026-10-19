%global source0_hash dcf338cc61b636c871ccf370e673bfd380c5ecb71ce49ad50f28e1d4ec9995dc
%bcond          ispc    1
Name:           embree
Version:        4.4.1
Release:        1%{?dist}
Summary:        High-performance ray tracing kernels
License:        Apache-2.0
URL:            https://embree.github.io
%global         with_snapshot   0
Source0:        https://github.com/%{name}/%{name}/archive/v%{version}/%{name}-%{version}.tar.gz
%if %{with ispc} 
%endif
ExclusiveArch:  aarch64 x86_64
# oreon:deps
BuildRequires:  cmake
BuildRequires:  gcc-c++
BuildRequires:  giflib-devel
BuildRequires:  ispc
BuildRequires:  pkgconfig(OpenImageIO)
BuildRequires:  pkgconfig(glfw3)
BuildRequires:  pkgconfig(glut)
BuildRequires:  pkgconfig(libjpeg)
BuildRequires:  pkgconfig(libpng)
BuildRequires:  pkgconfig(tbb)
BuildRequires:  pkgconfig(xmu)
# /oreon:deps
%description
Embree provides high-performance ray tracing kernels optimized for modern CPUs,
targeting graphics application engineers seeking to accelerate their rendering
workloads.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
%description    devel
The %{name}-devel package contains libraries and header files for
applications that use %{name}.

%prep
%global oreon_srcdir %{name}-%{version}
%oreon_prep
%build

%cmake \
        -DCMAKE_BUILD_TYPE=Release \
        -DCMAKE_CXX_FLAGS="%{optflags} -Wl,--as-needed" \
        -DCMAKE_INSTALL_LIBDIR=%{_libdir} \
        -DCMAKE_INSTALL_PREFIX=%{_prefix} \
        -DCMAKE_SKIP_RPATH=ON \
        -DEMBREE_COMPACT_POLYS=ON \
        -DEMBREE_IGNORE_CMAKE_CXX_FLAGS=OFF \
%if %{with ispc}
        -DEMBREE_ISPC_SUPPORT=ON \
%endif
        -DEMBREE_MAX_ISA=NONE \
%ifarch x86_64
        -DEMBREE_ISA_SSE2=ON \
        -DEMBREE_ISA_SSE4=ON \
        -DEMBREE_ISA_AVX=ON \
        -DEMBREE_ISA_AVX2=ON \
%else
        -DEMBREE_ARM=ON \
        -DEMBREE_ISA_NEON=ON \
%endif
        -DEMBREE_TUTORIALS=ON \
        -DEMBREE_TESTING=ON \
        -DEMBREE_STATIC_LIB=OFF
%cmake_build
%check

%ctest --output-on-failure
%install
%cmake_install
rm -fv %{buildroot}%{_prefix}/%{name}-vars.{csh,sh}
rm -frv %{buildroot}%{_prefix}/src \
        %{buildroot}%{_bindir}/models \
        %{buildroot}%{_bindir}/embree_*_tests
mv %{buildroot}%{_docdir}/%{name}4 %{buildroot}%{_docdir}/%{name}
rm %{buildroot}%{_docdir}/%{name}/LICENSE.txt
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*

%files -f %{oreon_filedir}/main.list
%files -n embree-devel -f %{oreon_filedir}/embree-devel.list

%changelog

%autochangelog
