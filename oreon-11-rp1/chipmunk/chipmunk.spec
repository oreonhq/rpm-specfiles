%global source0_hash 1e6f093812d6130e45bdf4cb80280cb3c93d1e1833d8cf989d554d7963b7899a

Name:           chipmunk
Version:        7.0.3
Release:        20%{?dist}
Summary:        Physics engine for 2D games

License:        MIT
URL:            https://github.com/slembcke/Chipmunk2D/
Source0:        https://github.com/slembcke/Chipmunk2D/archive/Chipmunk-%{version}.tar.gz
Patch0:         sysctl.patch

BuildRequires: gcc
BuildRequires: gcc-c++
BuildRequires: cmake
BuildRequires: freeglut-devel
BuildRequires: mesa-libGL-devel
BuildRequires: libX11-devel
BuildRequires: libXext-devel
BuildRequires: libXi-devel
BuildRequires: libXmu-devel
BuildRequires: libXrandr-devel

%description
Chipmunk is a 2D rigid body physics library distributed under the MIT license.
Though not yet complete, it is intended to be fast, numerically stable, and 
easy to use.

%package        devel
Summary:        Development tools for programs which will use the chipmunk library
Requires:       %{name} = %{version}-%{release}

%description    devel
Chipmunk is a 2D rigid body physics library distributed under the MIT license.
Though not yet complete, it is intended to be fast, numerically stable, and 
easy to use.

This package contains the header files and  static libraries to develop
programs that will use the chipmunk library.  You should
install this package if you need to develop programs which will use the 
chipmunk library functions.  You'll also need to install the chipmunk package.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -qn Chipmunk2D-Chipmunk-%{version}
%patch -P0 -p0

%build
# TODO: Remove LIB_INSTALL_DIR after https://github.com/slembcke/Chipmunk2D/pull/256 is in
%cmake \
  -DLIB_INSTALL_DIR:PATH=%{_libdir} \
  -DBUILD_SHARED:BOOL=ON \
  -DBUILD_STATIC:BOOL=OFF \
  -DINSTALL_STATIC:BOOL=OFF
%cmake_build

%install
%cmake_install

%files
%license LICENSE.txt
%doc README.textile
%{_libdir}/*.so.*

%files devel
%doc doc/ demo/
%{_includedir}/chipmunk
%{_libdir}/*.so

%changelog
%autochangelog
