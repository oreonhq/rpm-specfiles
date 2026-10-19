%global source0_hash 8da2576ec6a0993e8900db7f91083be8682d8397a7be0752c85d1b7dd1b8e992
%global soversion 1.10
Name:           octomap
Version:        1.10.0
Release:        1%{?dist}
Summary:        Efficient Probabilistic 3D Mapping Framework Based on Octrees
License:        LicenseRef-Callaway-BSD AND GPL-2.0-only
URL:            http://octomap.github.io/
Source0:        https://github.com/OctoMap/%{name}/archive/v%{version}/%{name}-%{version}.tar.gz
Patch0:         %{name}-1.9.8-libdir.patch
# oreon:deps
BuildRequires:  cmake
BuildRequires:  doxygen
BuildRequires:  gcc-c++
BuildRequires:  libQGLViewer-qt5-devel
BuildRequires:  libXext-devel
BuildRequires:  mesa-libGL-devel
BuildRequires:  mesa-libGLU-devel
# /oreon:deps
%description
The OctoMap library implements a 3D occupancy grid mapping approach,
providing data structures and mapping algorithms in C++ particularly suited
for robotics. The map implementation is based on an octree.

%package devel
Summary:  Development files and libraries for %name
Requires: %{name}%{?_isa} = %{version}-%{release}
%description devel
This package contains the header files and development libraries
for %{name}. If you like to develop programs using %{name},
you will need to install %{name}-devel.

%package doc
Summary:  HTML Documentation for %{name}
BuildArch: noarch
%description doc
This package contains doxygen-generated API documentation for %{name}

%package octovis
Summary: A visualization tool for Octomap
%description octovis
octovis is visualization tool for the OctoMap library based on Qt and
libQGLViewer
%package octovis-devel
Summary: Development files and libraries for %{name}
Requires: octomap-octovis%{?_isa} = %{version}-%{release}
Requires: octomap-devel%{?_isa} = %{version}-%{release}
%description octovis-devel
This package contains the header files and development libraries
for octovis. If you like to develop programs using octovis,
you will need to install octovis-devel.

%package -n dynamic-edt-3d
Summary:  Dynamic Euclidian Distance Transform Implementation
%description -n dynamic-edt-3d
The dynamicEDT3D library implements an incrementally updatable Euclidean
distance transform (EDT) in 3D. It comes with a wrapper to use the OctoMap
3D representation and hooks into the change detection of the OctoMap library
to propagate changes to the EDT.

%package -n dynamic-edt-3d-devel
Summary:  Development files and libraries for dynamic-edt-3d
Requires: dynamic-edt-3d%{?_isa} = %{version}-%{release}
Requires: octomap-devel%{?_isa} = %{version}-%{release}
%description -n dynamic-edt-3d-devel
This package contains the header files and development libraries
for dynamic-edt-3d. If you like to develop programs using dynamic-edt-3d,
you will need to install dynamic-edt-3d-devel.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q
%patch -P0 -p0 -b .libdir
# Remove bundled QGLViewer
rm -fr octovis/src/extern/

%build

export CMAKE_POLICY_VERSION_MINIMUM=3.5
%cmake \
  -DCMAKE_BUILD_TYPE=None
%cmake_build
%cmake_build --target docs
%install
%cmake_install
%oreon_autofiles dynamic-edt-3d usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles dynamic-edt-3d-devel usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*

%check

export LD_LIBRARY_PATH=%{buildroot}%{_libdir}
%ctest --output-on-failure || exit 0
%ldconfig_scriptlets
%ldconfig_scriptlets -n %{name}-octovis
%ldconfig_scriptlets -n dynamic-edt-3d
%files -f %{oreon_filedir}/main.list
%files -n octomap-devel -f %{oreon_filedir}/octomap-devel.list
%files -n octomap-doc -f %{oreon_filedir}/octomap-doc.list
%files -n octomap-octovis -f %{oreon_filedir}/octomap-octovis.list
%files -n octomap-octovis-devel -f %{oreon_filedir}/octomap-octovis-devel.list
%files -n dynamic-edt-3d -f %{oreon_filedir}/dynamic-edt-3d.list
%files -n dynamic-edt-3d-devel -f %{oreon_filedir}/dynamic-edt-3d-devel.list

%changelog

%autochangelog
