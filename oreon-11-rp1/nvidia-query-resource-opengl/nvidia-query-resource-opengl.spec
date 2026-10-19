%global source0_hash d348430e3aa1aceaffa273b397fee9f6fe6bd9087b2e7f80fd0f7021603d6d18
%undefine _hardened_build
Name:           nvidia-query-resource-opengl
Version:        1.0.0
Release:        1%{?dist}
Summary:        Querying OpenGL resource usage of applications using the NVIDIA OpenGL driver
License:        LicenseRef-Callaway-BSD
URL:            https://github.com/NVIDIA/nvidia-query-resource-opengl/
Source0:        https://github.com/NVIDIA/%{name}//archive/v%{version}/%{name}-%{version}.tar.gz
Requires:       %{name}-lib%{?_isa} = %{version}-%{release}
# oreon:deps
BuildRequires:  cmake
BuildRequires:  gcc
BuildRequires:  gcc-c++
BuildRequires:  libGL-devel
BuildRequires:  libX11-devel
# /oreon:deps
%description
A tool for querying OpenGL resource usage of applications using the NVIDIA
OpenGL driver. Requires NVIDIA 387 or later.

%package        lib
Summary:        Library for %{name}
%description    lib
This package contains library for %{name}.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%oreon_prep
%build

export CMAKE_POLICY_VERSION_MINIMUM=3.5
%cmake
%cmake_build
%install
mkdir -p %{buildroot}%{_bindir}
mkdir -p %{buildroot}%{_libdir}/%{name}
find . -name %{name} -exec mv {} %{buildroot}%{_bindir} ';'
find . -name libnvidia-query-resource-opengl-preload.so -exec mv {} \
  %{buildroot}%{_libdir}/%{name}/lib%{name}-preload.so ';'
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%files -f %{oreon_filedir}/main.list
%files -n nvidia-query-resource-opengl-lib -f %{oreon_filedir}/nvidia-query-resource-opengl-lib.list

%changelog

%autochangelog
