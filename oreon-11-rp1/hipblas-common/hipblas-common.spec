%global source0_hash 6c00bb9335ad2ad3d4730eb41ebc704b0207162d5f98da1cdce3eea1087c3944
%bcond_with gitcommit
%if %{with gitcommit}
%global commit0 2584e35062ad9c2edb68d93c464cf157bc57e3b0
%global shortcommit0 %(c=%{commit0}; echo ${c:0:7})
%global date0 20250926
%endif
%global upstreamname hipBLAS-common
%global rocm_release 7.1
%global rocm_patch 0
%global rocm_version %{rocm_release}.%{rocm_patch}
%bcond_with compat
%if %{with compat}
%global pkg_libdir lib
%global pkg_prefix %{_prefix}/lib64/rocm/rocm-%{rocm_release}
%global pkg_suffix -%{rocm_release}
%global pkg_module rocm%{pkg_suffix}
%else
%global pkg_libdir %{_lib}
%global pkg_prefix %{_prefix}
%global pkg_suffix %{nil}
%global pkg_module default
%endif
Name:           hipblas-common%{pkg_suffix}
%if %{with gitcommit}
Version:        git%{date0}.%{shortcommit0}
Release:        1%{?dist}
%else
Version:        %{rocm_version}
Release:        1%{?dist}
%endif
Summary:        Common files shared by hipBLAS and hipBLASLt
License:        MIT
%if %{with gitcommit}
Url:            https://github.com/ROCm/rocm-libraries
Source0:        https://github.com/ROCm/%{upstreamname}/archive/%{pkg_module}.%{rocm_patch}.tar.gz#/%{upstreamname}-%{version}.tar.gz
%else
Url:            https://github.com/ROCm/%{upstreamname}
%endif
BuildArch: noarch
ExclusiveArch:  x86_64
%global _smp_mflags %{nil}
# oreon:deps
BuildRequires:  cmake
BuildRequires:  gcc-c++
BuildRequires:  rocm-cmake
# /oreon:deps
%description
%summary

%package devel
Summary:        Libraries and headers for %{name}
Provides:       %{name}-static = %{version}-%{release}
%description devel
%{summary}

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%if %{with gitcommit}
%setup -q -n rocm-libraries-%{commit0}
cd projects/hipblas-common
%else
%autosetup -p1 -n %{upstreamname}-rocm-%{version}
%endif

%build

%if %{with gitcommit}
cd projects/hipblas-common
%endif
%cmake \
    -DCMAKE_INSTALL_LIBDIR=share \
    -DCMAKE_INSTALL_PREFIX=%{pkg_prefix}
%cmake_build
%install
%if %{with gitcommit}
cd projects/hipblas-common
%endif
%cmake_install
rm -f %{buildroot}%{pkg_prefix}/share/doc/hipblas-common/LICENSE.md
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*

%files -f %{oreon_filedir}/main.list
%files -n hipblas-common-devel -f %{oreon_filedir}/hipblas-common-devel.list

%changelog

%autochangelog
