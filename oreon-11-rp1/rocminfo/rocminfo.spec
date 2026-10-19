%global source0_hash fdf1e08392d3645d64696c5de7c116a1ea7ff3c70f19c0cb46c9eece7c00062c
%global upstreamname rocminfo
%global rocm_release 7.1
%global rocm_patch 0
%global rocm_version %{rocm_release}.%{rocm_patch}
%bcond_with compat
%if %{with compat}
%global pkg_prefix %{_prefix}/lib64/rocm/rocm-%{rocm_release}
%global pkg_skip_rpath OFF
%global pkg_rpath %{_prefix}/lib64/rocm/rocm-%{rocm_release}/lib
%global pkg_suffix -%{rocm_release}
%else
%global pkg_prefix %{_prefix}
%global pkg_skip_rpath ON
%global pkg_rpath %{nil}
%global pkg_suffix %{nil}
%endif
%global pkg_name rocminfo%{pkg_suffix}
Name:       %{pkg_name}
Version:    %{rocm_version}
Release:        1%{?dist}
Summary:        ROCm system info utility
License:    NCSA
URL:        https://github.com/ROCm/rocminfo
Source0:        https://github.com/ROCm/%{upstreamname}/archive/rocm-%{version}.tar.gz#/%{name}.%{rocm_patch}.tar.gz
Patch0:     0001-adjust-CMAKE_CXX_FLAGS.patch
ExclusiveArch:  x86_64
Requires:       kmod
# oreon:deps
BuildRequires:  cmake
BuildRequires:  gcc-c++
BuildRequires:  make
BuildRequires:  python3-devel
BuildRequires:  rocm-runtime-7.1-devel
# /oreon:deps
%description
ROCm system info utility

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n %{upstreamname}-rocm-%{version} -p1

# suse
sed -i -e 's@/usr/bin/env python3@/usr/bin/python3@' rocm_agent_enumerator

%build

%cmake \
    -DROCM_DIR=%{pkg_prefix} \
    -DCMAKE_INSTALL_PREFIX=%{pkg_prefix} \
    -DCMAKE_INSTALL_RPATH=%{pkg_rpath} \
    -DCMAKE_BUILD_TYPE=RelWithDebInfo \
    -DCMAKE_SKIP_INSTALL_RPATH=%{pkg_skip_rpath}
%cmake_build
%install
%cmake_install
chmod 755 %{buildroot}%{pkg_prefix}/bin/*
rm -f %{buildroot}%{pkg_prefix}/share/doc/*/License.txt
rm -f %{buildroot}%{pkg_prefix}/share/doc/*/*/License.txt
%oreon_autofiles main

%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
