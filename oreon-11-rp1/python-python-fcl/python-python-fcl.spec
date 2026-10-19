%global source0_hash 5aac8b9b8ba1b2e94971db7ae9b05649985df3ff099b6c6a2785bef9ff5f9b85
%bcond system_fcl 0
%global libccd_version 2.1
%global fcl_version 0.7.0
Name:           python-python-fcl
Version:        0.7.0.11
Release:        1%{?dist}
Summary:        Python bindings for the Flexible Collision Library
License:        BSD-3-Clause
URL:            https://github.com/BerkeleyAutomation/python-fcl
Source0:        https://github.com/BerkeleyAutomation/python-fcl/archive/v%{version}/python-fcl-%{version}.tar.gz
%global libccd_forgeurl https://github.com/danfis/libccd
Source1:        %{libccd_forgeurl}/archive/v%{libccd_version}/libccd-%{libccd_version}.tar.gz
%global fcl_forgeurl https://github.com/flexible-collision-library/fcl
Source2:        %{fcl_forgeurl}/archive/%{fcl_version}/fcl-%{fcl_version}.tar.gz
ExcludeArch:    %{ix86}
Patch0:         0001-Add-environment-variables-to-control-bundling.patch
Patch1001:      https://src.fedoraproject.org/rpms/libccd/raw/80bc68bb9f9644aec2e8dbf036e3ac84be918eef/f/libccd-2.1-ctest.patch
Patch1002:      https://src.fedoraproject.org/rpms/libccd/raw/80bc68bb9f9644aec2e8dbf036e3ac84be918eef/f/libccd-2.1-py3.patch
Patch1003:      https://github.com/danfis/libccd/pull/82.patch#/libccd-2.1-cmake4.patch
Patch2001:      2001-Directly-include-cassert-wherever-we-use-assert.patch
%if %{with system_fcl}
%else
%ifarch %{valgrind_arches}
%endif
%endif
%global common_description %{expand:
Python-FCL is an (unofficial) Python interface for the Flexible Collision
Library (FCL), an excellent C++ library for performing proximity and collision
queries on pairs of geometric models.
This package supports three types of proximity queries for pairs of geometric
models:
  • Collision Detection: Detecting whether two models overlap (and optionally
    where).
  • Distance Computation: Computing the minimum distance between a pair of
    models.
  • Continuous Collision Detection: Detecting whether two models overlap during
    motion (and optionally the time of contact).
This package also supports most of FCL’s object shapes, including:
  • TriangleP
  • Box
  • Sphere
  • Ellipsoid
  • Capsule
  • Cone
  • Convex
  • Cylinder
  • Half-Space
  • Plane
  • Mesh
  • OcTree}
# oreon:deps
BuildRequires:  cmake
BuildRequires:  eigen3-static
BuildRequires:  gcc-c++
BuildRequires:  ninja-build
BuildRequires:  octomap-devel
BuildRequires:  python3dist(pytest)
# /oreon:deps
%description %{common_description}

%package -n     python3-python-fcl
Summary:        Python bindings for the Flexible Collision Library
%py_provides python3-fcl
%if %{without system_fcl}
Provides:       bundled(libccd) = %{libccd_version}
Provides:       bundled(fcl) = %{fcl_version}
%endif
%description -n python3-python-fcl %{common_description}

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n python-fcl-%{version} -N
%autopatch -M999 -p1
# Compile as C++14 instead of C++11, for compatibility with eigen3 5.0.
sed -r -i 's/(-std=c\+\+)11\b/\114/' setup.py

%if %{without system_fcl}
%setup -q -T -D -b 1 -n python-fcl-%{version}
pushd ../libccd-%{libccd_version}/
%autopatch -m1000 -M1001 -p0
%autopatch -m1002 -M1999 -p1
popd
cp -p ../libccd-%{libccd_version}/BSD-LICENSE libccd-LICENSE

%setup -q -T -D -b 2 -n python-fcl-%{version}
pushd ../fcl-%{fcl_version}/
%autopatch -m2000 -M2999 -p1
# Compile as C++14 instead of C++11, for compatibility with eigen3 5.0.
sed -r -i 's/(-std=c\+\+)11\b/\114/' \
    CMakeModules/CompilerSettings.cmake CMakeLists.txt
popd
cp -p ../fcl-%{fcl_version}/LICENSE fcl-LICENSE
%endif

%build -p

%if %{without system_fcl}
BUNDLEROOT="%{_vpath_builddir}/_bundled"
mkdir -p "${BUNDLEROOT}"
pushd "${BUNDLEROOT}"
BUNDLEROOT="${PWD}"
popd
pushd ../libccd-%{libccd_version}/
%cmake -GNinja \
    -DBUILD_SHARED_LIBS:BOOL=OFF \
    -DBUILD_STATIC_LIBS:BOOL=ON \
    -DCMAKE_POSITION_INDEPENDENT_CODE:BOOL=ON \
    -DBUILD_TESTING:BOOL=ON \
    -DENABLE_DOUBLE_PRECISION:BOOL=ON
%cmake_build
DESTDIR="${BUNDLEROOT}" %__cmake --install "%{_vpath_builddir}"
popd
pushd ../fcl-%{fcl_version}/
%cmake -GNinja \
    -DCCD_LIBRARY:PATH="${BUNDLEROOT}%{_libdir}/libccd.a" \
    -DCCD_INCLUDE_DIR:PATH="${BUNDLEROOT}%{_includedir}" \
    -DCMAKE_POSITION_INDEPENDENT_CODE:BOOL=ON \
    -DFCL_STATIC_LIBRARY:BOOL=ON \
    -DFCL_NO_DEFAULT_RPATH:BOOL=OFF \
    -DFCL_USE_HOST_NATIVE_ARCH:BOOL=OFF \
    -DFCL_USE_X64_SSE:BOOL=OFF
%cmake_build
DESTDIR="${BUNDLEROOT}" %__cmake --install "%{_vpath_builddir}"
popd
export PYTHON_FCL_EXTRA_INCLUDE_DIRS="${BUNDLEROOT}%{_includedir}"
XO="${XO-}${XO+ }${BUNDLEROOT}%{_libdir}/libfcl.a"
XO="${XO-}${XO+ }${BUNDLEROOT}%{_libdir}/libccd.a"
export PYTHON_FCL_EXTRA_OBJECTS="${XO-}"
export PYTHON_FCL_OMIT_LIBRARIES='fcl'
%endif
%install
%pyproject_install
find '%{buildroot}%{python3_sitearch}' -type f -name '*.cpp' -print -delete
sed -r -i '/\.cpp$/d' %{pyproject_files}
%oreon_autofiles python3-python-fcl usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%check

%if %{without system_fcl}
pushd ../libccd-%{libccd_version}/
skips='^($.'
%ifnarch %{valgrind_arches}
skips="${skips}|.*-valgrind.*"
%endif
skips="${skips})$"
%ctest --exclude-regex "${skips}"
popd
pushd ../fcl-%{fcl_version}/
for exe in %{_vpath_builddir}/test/test_*
do
  unset filter
  case "$(basename "${exe}")" in
  test_fcl_capsule_capsule)
%ifarch %{arm64} %{power64}
    filter="${filter--}${filter+:}CapsuleCapsuleSegmentTest/1.NominalSeparatedCase"
%endif
%ifarch %{arm64} %{power64}
    filter="${filter--}${filter+:}CapsuleCapsuleSegmentTest/0.OverlappingCenterLines"
%endif
    ;;
  test_gjk_libccd-inl_gjk_doSimplex2)
%ifarch %{arm64} %{power64}
    filter="${filter--}${filter+:}DoSimplex2Test.NeedMoreComputing"
    filter="${filter--}${filter+:}DoSimplex2Test.OriginInSimplex"
%endif
    ;;
  test_gjk_libccd-inl_epa)
%ifarch %{arm64} %{power64} s390x
    filter="${filter--}${filter+:}FCL_GJK_EPA.ComputeVisiblePatchColinearNewVertex"
%endif
    ;;
  test_fcl_math)
%ifarch s390x
    filter="${filter--}${filter+:}FCL_MATH.rss_conversion"
%endif
    ;;
  esac
  "${exe}" --gtest_filter="${filter}"
done
popd
%endif
rm -rvf fcl
%pytest --verbose
%files -f %{oreon_filedir}/main.list
%files -n python3-python-fcl -f %{oreon_filedir}/python3-python-fcl.list

%changelog

%autochangelog
