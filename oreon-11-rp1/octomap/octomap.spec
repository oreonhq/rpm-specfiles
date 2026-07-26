%global source0_hash 417af6da4e855e9a83b93458aa98b01a2c88f880088baad2b59d323ce162586e

%global soversion 1.9

Name:           octomap
Version:        1.9.8
Release:        10%{?dist}
Summary:        Efficient Probabilistic 3D Mapping Framework Based on Octrees

# octovis is GPLv2, octomap and dynamic-edt-3d are BSD
# Automatically converted from old format: BSD and GPLv2 - review is highly recommended.
License:        LicenseRef-Callaway-BSD AND GPL-2.0-only
URL:            http://octomap.github.io/
Source0:        https://github.com/OctoMap/%{name}/archive/v%{version}/%{name}-%{version}.tar.gz

# This patch moves CMake configuration files from datadir to libdir.
# It also disables -Werror to work around warnings described in #1862718
# Not submitted upstream
Patch0:         %{name}-1.9.8-libdir.patch
BuildRequires:  cmake
BuildRequires:  doxygen
BuildRequires:  gcc-c++
BuildRequires:  libQGLViewer-qt5-devel
BuildRequires:  libXext-devel
BuildRequires:  mesa-libGL-devel
BuildRequires:  mesa-libGLU-devel

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
# TODO: Please submit an issue to upstream (rhbz#2380960)
export CMAKE_POLICY_VERSION_MINIMUM=3.5
%cmake \
  -DCMAKE_BUILD_TYPE=None

%cmake_build
%cmake_build --target docs

%install
%cmake_install

%check
export LD_LIBRARY_PATH=%{buildroot}%{_libdir}
# Color octree comes out to be wrong size on ix86; ignore for now
%ctest --output-on-failure || exit 0

%ldconfig_scriptlets

%ldconfig_scriptlets -n %{name}-octovis

%ldconfig_scriptlets -n dynamic-edt-3d

%files
%license octomap/LICENSE.txt
%doc octomap/README.md octomap/CHANGELOG.txt octomap/AUTHORS.txt
%exclude %{_bindir}/octovis
%{_bindir}/*
%{_libdir}/liboctomap.so.%{version}
%{_libdir}/liboctomap.so.%{soversion}
%{_libdir}/liboctomath.so.%{version}
%{_libdir}/liboctomath.so.%{soversion}
%{_datadir}/%{name}
%{_datadir}/ament_index/resource_index/packages/octomap

%files devel
%{_includedir}/octomap
%{_libdir}/liboctomap.so
%{_libdir}/liboctomath.so
%{_libdir}/pkgconfig/octomap.pc
%{_libdir}/%{name}

%files doc
%license octomap/LICENSE.txt
%doc octomap/doc/html

%files octovis
%license octovis/LICENSE.txt
%doc octovis/README.md
%{_bindir}/octovis
%{_libdir}/liboctovis.so.%{version}
%{_libdir}/liboctovis.so.%{soversion}
%{_datadir}/octovis
%{_datadir}/ament_index/resource_index/packages/octovis

%files octovis-devel
%{_includedir}/octovis
%{_libdir}/liboctovis.so
%{_libdir}/octovis

%files -n dynamic-edt-3d
%license dynamicEDT3D/LICENSE.txt
%doc dynamicEDT3D/README.txt
%{_libdir}/libdynamicedt3d.so.%{version}
%{_libdir}/libdynamicedt3d.so.%{soversion}
%{_datadir}/dynamic_edt_3d
%{_datadir}/ament_index/resource_index/packages/dynamicEDT3D

%files -n dynamic-edt-3d-devel
%{_includedir}/dynamicEDT3D
%{_libdir}/libdynamicedt3d.so
%{_libdir}/pkgconfig/dynamicEDT3D.pc
%{_libdir}/dynamicEDT3D

%changelog
%autochangelog
