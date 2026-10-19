%global source0_hash d1761b06c0c1c4e8aa17704d71cb3a4445fb856ab60680bd64e93684a5c923b0
Name:           SimGear
Version:        2024.1.7
Release:        1%{?dist}
License:        GPL-2.0-or-later
Summary:        Simulation library components
URL:            https://gitlab.com/flightgear/simgear
Source0:        https://gitlab.com/flightgear/fgmeta/-/jobs/12799933767/artifacts/raw/sgbuild/simgear-%{version}.tar.bz2
Patch:          0001-check-to-be-sure-that-n-is-not-being-set-as-format-t.patch
Patch:          0002-fix-support-for-aarch64.patch
# oreon:deps
BuildRequires:  OpenSceneGraph-devel
BuildRequires:  boost-devel
BuildRequires:  c-ares-devel
BuildRequires:  cmake
BuildRequires:  expat-devel
BuildRequires:  gcc-c++
BuildRequires:  libXext-devel
BuildRequires:  libXi-devel
BuildRequires:  libXmu-devel
BuildRequires:  libXt-devel
BuildRequires:  libcurl-devel
BuildRequires:  libjpeg-devel
BuildRequires:  mesa-libEGL-devel
BuildRequires:  mesa-libGLU-devel
BuildRequires:  openal-soft-devel
BuildRequires:  xz-devel
BuildRequires:  zlib-devel
# /oreon:deps
%description
SimGear is a set of open-source libraries designed to be used as building
blocks for quickly assembling 3d simulations, games, and visualization
applications.

%package devel
Summary: Development libraries and headers for SimGear
Requires: %{name} = %{version}-%{release}
Requires: plib-devel, libjpeg-devel, zlib-devel, libGL-devel
Requires: libX11-devel, expat-devel
%description devel
Development headers and libraries for building applications against 
SimGear.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1 -n simgear-%{version}

# makes rpmlint happy
find -name \*.cxx -o -name \*.hxx | xargs chmod -x

# expat covers most of the files in simgear/xml, except for the custom ones (easyxml.*))
rm -rf simgear/xml/*.h simgear/xml/*.c

%build

%cmake \
    -DCMAKE_BUILD_TYPE=Release \
    -DENABLE_TESTS=OFF \
    -DSIMGEAR_SHARED=ON \
    -DSYSTEM_EXPAT=ON
%cmake_build
%install
%cmake_install
%ldconfig_scriptlets
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*

%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
