%global source0_hash 3749f48220db78c29c375a373861f4e1f4138e5dbae3c298584e96cfcc556515
Name:           apriltag
Version:        3.4.5
Release:        1%{?dist}
Summary:        Visual fiducial system popular for robotics research
License:        BSD-2-Clause-Views AND MIT
URL:            https://april.eecs.umich.edu/software/apriltag
Source0:        https://github.com/AprilRobotics/apriltag/archive/v%{version}/%{name}-%{version}.tar.gz
Patch0:         %{name}-3.4.2-test-directory.patch
Patch1:         %{name}-3.4.2-cmake-config-directory.patch
# oreon:deps
BuildRequires:  cmake
BuildRequires:  gcc-c++
# /oreon:deps
%description
AprilTag is a visual fiducial system popular in robotics research. This package
contains the most recent version of AprilTag, AprilTag 3, which includes a
faster (>2x) detector, improved detection rate on small tags, flexible tag
layouts, and pose estimation. AprilTag consists of a small C library with
minimal dependencies.

%package devel
Summary:        Development files for %{name}
Requires:       %{name}%{?isa} = %{version}-%{release}
%description devel
Development files for the %{name} package.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%oreon_prep
%build

%cmake \
  -DBUILD_EXAMPLES:BOOL=OFF \
  -DBUILD_TESTING:BOOL=ON \
  -DBUILD_PYTHON_WRAPPER:BOOL=OFF \
  -DCMAKE_C_STANDARD:STRING=99 \
  %{nil}
%cmake_build
%install
%cmake_install
%oreon_autofiles apriltag-devel usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*

%check

%ctest
%files -f %{oreon_filedir}/main.list
%files -n apriltag-devel -f %{oreon_filedir}/apriltag-devel.list

%changelog

%autochangelog
