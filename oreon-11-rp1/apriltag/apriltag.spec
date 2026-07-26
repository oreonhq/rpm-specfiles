%global source0_hash 7e021bab89f136aa3cf736f772a635aaa353f93f6f8859495f4bd8c519be4805

Name:           apriltag
Version:        3.4.2
Release:        6%{?dist}
Summary:        Visual fiducial system popular for robotics research

# The entire source code BSD-2-Clause-Views except common/pthreads_cross.{cpp,h} which is MIT
License:        BSD-2-Clause-Views AND MIT
URL:            https://april.eecs.umich.edu/software/apriltag
Source0:        https://github.com/AprilRobotics/apriltag/archive/v%{version}/%{name}-%{version}.tar.gz

# Merged upstream as https://github.com/AprilRobotics/apriltag/pull/360
Patch0:         %{name}-3.4.2-test-directory.patch
# Merged upstream as https://github.com/AprilRobotics/apriltag/pull/364
Patch1:         %{name}-3.4.2-cmake-config-directory.patch

BuildRequires:  cmake
BuildRequires:  gcc-c++

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

%autosetup -p1

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

%check
%ctest

%files
%license LICENSE.md
%doc README.md
%{_libdir}/lib%{name}.so.3*

%files devel
%{_includedir}/apriltag/
%{_libdir}/lib%{name}.so
%{_libdir}/pkgconfig/%{name}.pc
%{_libdir}/%{name}/

%changelog
%autochangelog
