%global _docdir_fmt %{name}

%global source0_hash 05826c104b842bcdd1339b86894cb44c84ac2525ac296689d34b38a14bbba0dd

Name: bullet
Version: 3.08
Release: 18%{?dist}
Summary: 3D Collision Detection and Rigid Body Dynamics Library
# Automatically converted from old format: zlib and MIT and BSD and Boost - review is highly recommended.
License: Zlib AND LicenseRef-Callaway-MIT AND LicenseRef-Callaway-BSD AND BSL-1.0
URL: http://www.bulletphysics.com

Source0: https://github.com/bulletphysics/bullet3/archive/refs/tags/%{version}.tar.gz#/%{name}3-%{version}.tar.gz

# Build against system tinyxml
Patch0: %{name}-3.08-tinyxml2.patch

# Fix C++ One Definition Rule violation
Patch1: %{name}-3.08-fix-c++-one-definition-rule-violation.patch

BuildRequires:  gcc
BuildRequires:  gcc-c++
BuildRequires: cmake
BuildRequires: dos2unix
BuildRequires: doxygen
BuildRequires: freeglut-devel
BuildRequires: libICE-devel
BuildRequires: tinyxml2-devel
BuildRequires: libglvnd-devel

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
# Automatically converted from old format: zlib and LGPLv2+ - review is highly recommended.
License: Zlib AND LicenseRef-Callaway-LGPLv2+
Requires: %{name}-extras%{?_isa} = %{version}-%{release}

%description devel-doc
Documentation (PDF) for developing programs that will use %{name}-devel.


%package extras
Summary: Extra libraries for %{name}
# Automatically converted from old format: zlib and LGPLv2+ - review is highly recommended.
License: Zlib AND LicenseRef-Callaway-LGPLv2+

%description extras
Extra libraries for %{name}.


%package extras-devel
Summary: Development files for %{name} extras
# Automatically converted from old format: zlib and LGPLv2+ - review is highly recommended.
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


%files
%license LICENSE.txt
%doc README.md AUTHORS.txt VERSION
%{_libdir}/libBullet3Collision.so.*
%{_libdir}/libBullet3Common.so.*
%{_libdir}/libBullet3Dynamics.so.*
%{_libdir}/libBullet3Geometry.so.*
%{_libdir}/libBullet3OpenCL_clew.so.*
%{_libdir}/libBulletCollision.so.*
%{_libdir}/libBulletDynamics.so.*
%{_libdir}/libBulletInverseDynamics.so.*
%{_libdir}/libBulletSoftBody.so.*
%{_libdir}/libLinearMath.so.*

%files devel
%dir %{_includedir}/%{name}
%{_includedir}/%{name}/*.h
%{_includedir}/%{name}/Bullet3Collision
%{_includedir}/%{name}/Bullet3Common
%{_includedir}/%{name}/Bullet3Dynamics
%{_includedir}/%{name}/Bullet3Geometry
%{_includedir}/%{name}/Bullet3OpenCL
%{_includedir}/%{name}/BulletCollision
%{_includedir}/%{name}/BulletDynamics
%{_includedir}/%{name}/BulletInverseDynamics
%{_includedir}/%{name}/BulletSoftBody
%{_includedir}/%{name}/InverseDynamics
%{_includedir}/%{name}/LinearMath
%{_libdir}/libBullet3Collision.so
%{_libdir}/libBullet3Common.so
%{_libdir}/libBullet3Dynamics.so
%{_libdir}/libBullet3Geometry.so
%{_libdir}/libBullet3OpenCL_clew.so
%{_libdir}/libBulletCollision.so
%{_libdir}/libBulletDynamics.so
%{_libdir}/libBulletInverseDynamics.so
%{_libdir}/libBulletSoftBody.so
%{_libdir}/libLinearMath.so
%{_libdir}/pkgconfig/bullet.pc
%{_libdir}/cmake/%{name}

%files devel-doc
%doc docs/Bullet_User_Manual.pdf
%doc docs/BulletQuickstart.pdf
%doc docs/GPU_rigidbody_using_OpenCL.pdf
%doc html

%files extras
%{_libdir}/libConvexDecomposition.so.*
%{_libdir}/libGIMPACTUtils.so.*
%{_libdir}/libHACD.so.*
%{_libdir}/libBulletFileLoader.so.*
%{_libdir}/libBullet2FileLoader.so.*
%{_libdir}/libBulletInverseDynamicsUtils.so.*
%{_libdir}/libBulletWorldImporter.so.*
%{_libdir}/libBulletXmlWorldImporter.so.*

%files extras-devel
%{_includedir}/%{name}/ConvexDecomposition
%{_includedir}/%{name}/GIMPACTUtils
%{_includedir}/%{name}/HACD
%{_includedir}/%{name}/BulletFileLoader
%{_includedir}/%{name}/Bullet2FileLoader
%{_includedir}/%{name}/BulletWorldImporter
%{_includedir}/%{name}/BulletXmlWorldImporter
%{_libdir}/libConvexDecomposition.so
%{_libdir}/libGIMPACTUtils.so
%{_libdir}/libHACD.so
%{_libdir}/libBulletFileLoader.so
%{_libdir}/libBullet2FileLoader.so
%{_libdir}/libBulletInverseDynamicsUtils.so
%{_libdir}/libBulletWorldImporter.so
%{_libdir}/libBulletXmlWorldImporter.so

%changelog
%autochangelog