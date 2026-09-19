%global source0_hash d348430e3aa1aceaffa273b397fee9f6fe6bd9087b2e7f80fd0f7021603d6d18

# This project doesn't work with hardened as it relies on lazzy symbol resolution
# like others Xorg modules
%undefine _hardened_build

Name:           nvidia-query-resource-opengl
Version:        1.0.0
Release:        23%{?dist}
Summary:        Querying OpenGL resource usage of applications using the NVIDIA OpenGL driver

# Automatically converted from old format: BSD - review is highly recommended.
License:        LicenseRef-Callaway-BSD
URL:            https://github.com/NVIDIA/nvidia-query-resource-opengl/
Source0:        %{url}/archive/v%{version}/%{name}-%{version}.tar.gz

BuildRequires:  gcc
BuildRequires:  gcc-c++
BuildRequires:  cmake
BuildRequires:  libX11-devel
BuildRequires:  libGL-devel

Requires:       %{name}-lib%{?_isa} = %{version}-%{release}
%if 0%{?fedora} || 0%{?rhel} > 7
%ifarch x86_64
Suggests:       (%{name}-libs(x86-32) = %{?epoch}:%{version}-%{release} if libGL(x86-32))
%endif
%endif

%description
A tool for querying OpenGL resource usage of applications using the NVIDIA
OpenGL driver. Requires NVIDIA 387 or later.

%package        lib
Summary:        Library for %{name}

%description    lib
This package contains library for %{name}.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1

%build
# TODO: Please submit an issue to upstream (rhbz#2380955)
export CMAKE_POLICY_VERSION_MINIMUM=3.5
%cmake

%cmake_build

%install
mkdir -p %{buildroot}%{_bindir}
mkdir -p %{buildroot}%{_libdir}/%{name}

find . -name %{name} -exec mv {} %{buildroot}%{_bindir} ';'

find . -name libnvidia-query-resource-opengl-preload.so -exec mv {} \
  %{buildroot}%{_libdir}/%{name}/lib%{name}-preload.so ';'

%files
%license LICENSE
%doc README.md
%{_bindir}/%{name}

%files lib
%dir %{_libdir}/%{name}
%{_libdir}/%{name}/lib%{name}-preload.so

%changelog
%autochangelog
