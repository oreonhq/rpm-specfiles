%global source0_hash 524b7bf4c678d6b7192caf202533f0d9abe84c59b8ba5e579a47258bb1a62efc
%global upstreamname rocm-core
%global rocm_release 7.1
%global rocm_patch 1
%global rocm_version %{rocm_release}.%{rocm_patch}
%bcond_with compat
%if %{with compat}
%global pkg_libdir lib
%global pkg_prefix %{_prefix}/lib64/rocm/rocm-%{rocm_release}/
%global pkg_suffix -%{rocm_release}
%global pkg_module rocm%{pkg_suffix}
%else
%global pkg_libdir %{_lib}
%global pkg_prefix %{_prefix}
%global pkg_suffix %{nil}
%global pkg_module default
%endif
%if 0%{?suse_version}
%global core_name librocm-core1%{pkg_suffix}
%else
%global core_name rocm-core%{pkg_suffix}
%endif
Name:           %{core_name}
Version:        %{rocm_version}
Release:        1%{?dist}
Summary:        A utility to get the ROCm release version
License:        MIT
URL:            https://github.com/ROCm/rocm-systems
Source0:        https://github.com/ROCm/rocm-systems/releases/download/%{pkg_module}.%{rocm_patch}/%{upstreamname}.tar.gz#/%{name}.%{rocm_patch}.tar.gz
Provides:       rocm-core = %{version}-%{release}
ExclusiveArch:  x86_64
# oreon:deps
BuildRequires:  cmake
BuildRequires:  gcc-c++
# /oreon:deps
%description
%{summary}

%if 0%{?suse_version}
%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig

%endif
%package devel
Summary:        Libraries and headers for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
Provides:       rocm-core%{pkg_suffix}-devel = %{version}-%{release}
%description devel
%{summary}

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1 -n %{upstreamname}

%build

%cmake \
    -DROCM_VERSION=%{rocm_version} \
    -DCMAKE_INSTALL_LIBDIR=%{pkg_libdir} \
    -DCMAKE_INSTALL_PREFIX=%{pkg_prefix}
%cmake_build
%install
%cmake_install
rm -rf %{buildroot}/%{pkg_prefix}/.info
rm -rf %{buildroot}/%{pkg_prefix}/%{pkg_libdir}/rocmmod
rm -f %{buildroot}/%{pkg_prefix}/share/doc/*/LICENSE.md
rm -f %{buildroot}/%{pkg_prefix}/share/doc/*/*/LICENSE.md
mv  %{buildroot}/%{pkg_prefix}/include/rocm-core/*.h %{buildroot}/%{pkg_prefix}/include/
rm -rf %{buildroot}/%{pkg_prefix}/include/rocm-core
find %{buildroot} -type f -name 'runpath_to_rpath.py' -exec rm {} \;
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*

%files -f %{oreon_filedir}/main.list
%files -n rocm-core-7.1-devel -f %{oreon_filedir}/rocm-core-7.1-devel.list

%changelog

%autochangelog
