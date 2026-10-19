%global source0_hash dcf338cc61b636c871ccf370e673bfd380c5ecb71ce49ad50f28e1d4ec9995dc
%global		srcname embree
%global		with_snapshot	0
%global		with_examples	0
%bcond_without	ispc
Name:		%{srcname}3
Version:	4.4.1
Release:        1%{?dist}
Summary:        Collection of high-performance ray tracing kernels
License:	Apache-2.0
URL:		https://embree.github.io
Source0:        https://github.com/%{srcname}/%{srcname}/archive/v%{version}.tar.gz#/%{srcname}-%{version}.tar.gz
Patch:		ace05ce4e3bcee8ff4d6204f4dac835f86f17d4a.patch
Patch:		cda4cf1919bb2a748e78915fbd6e421a1056638d.patch
%if %{with ispc} 
%endif
ExclusiveArch:	aarch64 x86_64
# oreon:deps
BuildRequires:  cmake
BuildRequires:  gcc-c++
BuildRequires:  giflib-devel
BuildRequires:  ispc
BuildRequires:  pkgconfig(glfw3)
BuildRequires:  pkgconfig(glut)
BuildRequires:  pkgconfig(tbb)
BuildRequires:  pkgconfig(xmu)
# /oreon:deps
%description
A collection of high-performance ray tracing kernels intended to graphics 
application engineers that want to improve the performance of their application.

%package	devel
Summary:	Development files for %{name}
Requires:	%{name}%{?_isa} = %{version}-%{release}
%description	devel
The %{name}-devel package contains libraries and header files for
 applications that use %{name}.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1 -n %{srcname}-%{version}%{?prerelease:-%{prerelease}.0}

%build

export CMAKE_POLICY_VERSION_MINIMUM=3.5
%cmake \
	-DCMAKE_BUILD_TYPE=Release \
	-DCMAKE_CXX_FLAGS="%{optflags} -Wl,--as-needed" \
	-DCMAKE_INSTALL_LIBDIR=%{_libdir} \
	-DCMAKE_INSTALL_PREFIX=%{_prefix} \
	-DEMBREE_COMPACT_POLYS=ON \
	-DEMBREE_IGNORE_CMAKE_CXX_FLAGS=OFF \
%if %{with ispc}
        -DEMBREE_ISPC_SUPPORT=ON \
%endif
%ifarch x86_64
	-DEMBREE_ISA_SSE2=ON \
	-DEMBREE_ISA_SSE4=ON \
	-DEMBREE_ISA_AVX=ON \
	-DEMBREE_ISA_AVX2=ON \
%else
	-DEMBREE_ISA_NEON=ON \
%endif
	-DEMBREE_TUTORIALS=OFF 
%cmake_build
%install
%cmake_install
rm %{buildroot}%{_docdir}/%{name}/LICENSE.txt
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*

%files -f %{oreon_filedir}/main.list
%files -n embree3-devel -f %{oreon_filedir}/embree3-devel.list

%changelog

%autochangelog
