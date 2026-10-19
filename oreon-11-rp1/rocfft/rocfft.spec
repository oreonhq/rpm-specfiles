%global source0_hash 8cd4fcca0b8b730135f76bb34f95965348b1809061af65ff6bfbd4ad2ac85e0d
%bcond_with gitcommit
%if %{with gitcommit}
%global commit0 2584e35062ad9c2edb68d93c464cf157bc57e3b0
%global shortcommit0 %(c=%{commit0}; echo ${c:0:7})
%global date0 20250926
%endif
%global upstreamname rocFFT
%global rocm_release 7.1
%global rocm_patch 0
%global rocm_version %{rocm_release}.%{rocm_patch}
%bcond_with compat
%if %{with compat}
%global pkg_libdir lib
%global pkg_prefix %{_prefix}/lib64/rocm/rocm-%{rocm_release}
%global pkg_suffix -%{rocm_release}
%else
%global pkg_libdir %{_lib}
%global pkg_prefix %{_prefix}
%global pkg_suffix %{nil}
%endif
%if 0%{?suse_version}
%global rocfft_name librocfft0%{pkg_suffix}
%else
%global rocfft_name rocfft%{pkg_suffix}
%endif
%global toolchain rocm
%global build_cxxflags %(echo %{optflags} | sed -e 's/-fstack-protector-strong/-Xarch_host -fstack-protector-strong/' -e 's/-fcf-protection/-Xarch_host-fcf-protection/')
%bcond_with debug
%if %{with debug}
%global build_type DEBUG
%else
%global build_type RelWithDebInfo
%endif
%bcond_with test
%if %{with test}
%global __brp_check_rpaths %{nil}
%global build_test ON
%else
%global build_test OFF
%endif
%bcond check 1
%bcond_with doc
%global _source_payload w7T0.xzdio
%global _binary_payload w7T0.xzdio
%global __strip %rocmllvm_bindir/llvm-strip
%bcond_with ninja
%if %{with ninja}
%global cmake_generator -G Ninja
%else
%global cmake_generator %{nil}
%endif
%global cmake_config \\\
  -DBUILD_CLIENTS_TESTS_OPENMP=OFF \\\
  -DBUILD_CLIENTS_TESTS=%{build_test} \\\
  -DCMAKE_AR=%rocmllvm_bindir/llvm-ar \\\
  -DCMAKE_BUILD_TYPE=%{build_type} \\\
  -DCMAKE_C_COMPILER=%rocmllvm_bindir/amdclang \\\
  -DCMAKE_CXX_COMPILER=%rocmllvm_bindir/amdclang++ \\\
  -DCMAKE_CXX_FLAGS="--rtlib=compiler-rt --unwindlib=libgcc" \\\
  -DCMAKE_INSTALL_LIBDIR=%{pkg_libdir} \\\
  -DCMAKE_INSTALL_PREFIX=%{pkg_prefix} \\\
  -DCMAKE_LINKER=%rocmllvm_bindir/ld.lld \\\
  -DCMAKE_RANLIB=%rocmllvm_bindir/llvm-ranlib \\\
  -DCMAKE_PREFIX_PATH=%{rocmllvm_cmakedir}/.. \\\
  -DROCFFT_BUILD_OFFLINE_TUNER=OFF \\\
  -DROCFFT_KERNEL_CACHE_ENABLE=OFF \\\
  -DROCM_SYMLINK_LIBS=OFF \\\
  -DSQLITE_USE_SYSTEM_PACKAGE=ON
%global gpu_list %{rocm_gpu_list_default}
%global _gpu_list gfx1100
Name:           rocfft%{pkg_suffix}
%if %{with gitcommit}
Version:        git%{date0}.%{shortcommit0}
Release:        1%{?dist}
%else
Version:        %{rocm_version}
Release:        1%{?dist}
%endif
Summary:        ROCm Fast Fourier Transforms (FFT) library
License:        MIT
%if %{with gitcommit}
Url:            https://github.com/ROCm/rocm-libraries
Source0:        https://github.com/ROCm/%{upstreamname}/archive/%{toolchain}-%{version}.tar.gz#/%{upstreamname}-%{toolchain}-%{version}.tar.gz
%else
Url:            https://github.com/ROCm/%{upstreamname}
%endif
%if %{with test}
%if 0%{?suse_version}
%else
%endif
Requires:  rocm-hip%{pkg_suffix}-devel >= %{rocm_release}
%endif
%if %{with doc}
%if 0%{?suse_version}
%else
%endif
%endif
%if %{with ninja}
%if 0%{?suse_version}
%define __builder ninja
%endif
%endif
Provides:       rocfft%{pkg_suffix} = %{version}-%{release}
ExclusiveArch:  x86_64
Patch0: 0001-cmake-use-gnu-installdirs.patch
# oreon:deps
BuildRequires:  boost-devel
BuildRequires:  cmake
BuildRequires:  fftw-devel
BuildRequires:  gcc-c++
BuildRequires:  gtest-devel
BuildRequires:  hiprand-7.1-devel
BuildRequires:  pkgconfig(sqlite3)
BuildRequires:  python3dist(sphinx)
BuildRequires:  rocm-cmake-7.1
BuildRequires:  rocm-comgr-7.1-devel
BuildRequires:  rocm-compilersupport-7.1-macros
BuildRequires:  rocm-hip-7.1-devel
BuildRequires:  rocm-rpm-macros-7.1
BuildRequires:  rocm-runtime-7.1-devel
BuildRequires:  rocrand-7.1-devel
# /oreon:deps
%description
A library for computing Fast Fourier Transforms (FFT), part of ROCm.

%if 0%{?suse_version}
%package -n %{rocfft_name}
Summary:        Shared libraries for %{name}
%description -n %{rocfft_name}
%{summary}

%ldconfig_scriptlets -n %{rocfft_name}
%endif

%package devel
Summary:        The rocFFT development package
Requires:       %{rocfft_name}%{?_isa} = %{version}-%{release}
Requires:       rocm-hip%{pkg_suffix}-devel
%description devel
The rocFFT development package.

%if %{with test}
%package test
Summary:        Tests for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
%description test
%{summary}
%endif

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%if %{with gitcommit}
%setup -q -n rocm-libraries-%{commit0}
cd projects/rocfft
%else
%autosetup -n %{upstreamname}-rocm-%{version} -p 1
%endif

# Do not care so much about the sqlite version
sed -i -e 's@SQLite3 3.50.2 @SQLite3 @' cmake/sqlite.cmake

%build

%if %{with gitcommit}
cd projects/rocfft
%endif
export LDFLAGS="${LDFLAGS} -pie"
%cmake %{cmake_generator} %{cmake_config} \
    -DGPU_TARGETS=%{gpu_list}
%cmake_build
%install
%if %{with gitcommit}
cd projects/rocfft
%endif
%cmake_install
find %{buildroot} -type f -name "rocfft_rtc_helper" -print0 | xargs -0 -I {} /usr/bin/rm -rf "{}"
rm -rf %{buildroot}/%{pkg_prefix}/.info
rm -f %{buildroot}%{pkg_prefix}/share/doc/rocfft/LICENSE.md
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%check

%if %{with test}
%if %{with check}
%if 0%{?suse_version}
%{__builddir}/clients/staging/rocfft-test
%else
%{_vpath_builddir}/clients/staging/rocfft-test
%endif
%endif
%endif
%if 0%{?suse_version}
%files -f %{oreon_filedir}/main.list
%files -n rocfft-7.1-devel -f %{oreon_filedir}/rocfft-7.1-devel.list
%files -n rocfft-7.1-test -f %{oreon_filedir}/rocfft-7.1-test.list

%changelog

%autochangelog
%endif
