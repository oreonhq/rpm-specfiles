%global _docdir_fmt %{name}
%global source0_hash 05826c104b842bcdd1339b86894cb44c84ac2525ac296689d34b38a14bbba0dd
Name: bullet
Version: 3.08
Release:        19%{?dist}
Summary:        3D Collision Detection and Rigid Body Dynamics Library
License: Zlib AND LicenseRef-Callaway-MIT AND LicenseRef-Callaway-BSD AND BSL-1.0
URL: http://www.bulletphysics.com
Source0:        https://github.com/bulletphysics/bullet3/archive/refs/tags/%{version}.tar.gz#/%{name}3-%{version}.tar.gz
Patch0: %{name}-3.08-tinyxml2.patch
Patch1: %{name}-3.08-fix-c++-one-definition-rule-violation.patch
# oreon:deps
BuildRequires:  cmake
BuildRequires:  dos2unix
BuildRequires:  doxygen
BuildRequires:  freeglut-devel
BuildRequires:  gcc
BuildRequires:  gcc-c++
BuildRequires:  libICE-devel
BuildRequires:  libglvnd-devel
BuildRequires:  tinyxml2-devel
# /oreon:deps
%description
Bullet is a 3D Collision Detection and Rigid Body Dynamics Library for games
and animation.

%package devel
Summary: Development files for %{name}
Requires: %{name}%{?_isa} = %{version}-%{release}
Requires: cmake
%description devel
Development headers and libraries for %{name}.

%package devel-doc
Summary: Documentation for developing programs that will use %{name}-devel
License: Zlib AND LicenseRef-Callaway-LGPLv2+
Requires: %{name}-extras%{?_isa} = %{version}-%{release}
%description devel-doc
Documentation (PDF) for developing programs that will use %{name}-devel.

%package extras
Summary: Extra libraries for %{name}
License: Zlib AND LicenseRef-Callaway-LGPLv2+
%description extras
Extra libraries for %{name}.

%package extras-devel
Summary: Development files for %{name} extras
License: Zlib AND LicenseRef-Callaway-LGPLv2+
Requires: %{name}-extras%{?_isa} = %{version}-%{release}
Requires: %{name}-devel%{?_isa} = %{version}-%{release}
%description extras-devel
Development headers and libraries for %{name} extra libraries.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%setup -q -n %{name}3-%{version}
rm -rf build3/*.bat build3/*.exe build3/xcode* build3/*osx* build3/premake* data examples/ThirdPartyLibs
%patch -P0 -p1 -b .tinyxml
%patch -P1 -p1 -b .fix-odr
# The examples directory isn't needed for building
rm -r examples

# Fix the pkg-config module so it doesn't list the prefix twice in the include install dir.
sed -i 's|${prefix}/@INCLUDE_INSTALL_DIR@|@INCLUDE_INSTALL_DIR@|' bullet.pc.cmake

# BulletRobotics, BulletRoboticsGUI and obj2sdf require several bundled libs not yet packaged in the distribution
sed -i 's|BulletRoboticsGUI BulletRobotics||' Extras/CMakeLists.txt
sed -i 's|obj2sdf||' Extras/CMakeLists.txt

# Fix up file permissions and formats
dos2unix README.md
chmod -x src/BulletDynamics/ConstraintSolver/btSliderConstraint.h
chmod -x src/BulletDynamics/ConstraintSolver/btSliderConstraint.cpp

%build

%cmake \
  -DCMAKE_POLICY_VERSION_MINIMUM=3.5 \
  -DINSTALL_LIBS=ON \
  -DCLSOCKET_DEP_ONLY=ON \
  -DBUILD_BULLET2_DEMOS=OFF \
  -DBUILD_EXTRAS=ON \
  -DBUILD_OPENGL_DEMOS=OFF \
  -DBUILD_CPU_DEMOS=OFF \
  -DBUILD_UNIT_TESTS=OFF \
  -DINSTALL_EXTRA_LIBS=ON \
  -DCMAKE_BUILD_TYPE=RelWithDebInfo \
  -DOpenGL_GL_PREFERENCE=GLVND \
  -DINCLUDE_INSTALL_DIR=%{_includedir}/bullet/
%cmake_build
doxygen Doxyfile
%install
%cmake_install
%ldconfig_scriptlets
%ldconfig_scriptlets extras
%oreon_autofiles bullet-devel usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*
%oreon_autofiles bullet-devel-doc usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles bullet-extras usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles bullet-extras-devel usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*

%files -f %{oreon_filedir}/main.list
%files -n bullet-devel -f %{oreon_filedir}/bullet-devel.list
%files -n bullet-devel-doc -f %{oreon_filedir}/bullet-devel-doc.list
%files -n bullet-extras -f %{oreon_filedir}/bullet-extras.list
%files -n bullet-extras-devel -f %{oreon_filedir}/bullet-extras-devel.list

%changelog

%autochangelog
