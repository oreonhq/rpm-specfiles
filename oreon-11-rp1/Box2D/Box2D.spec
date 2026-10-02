%global source0_hash fb6ef914b50f4312d7d921a600eabc12318bb3c55a0b8c0b90608fa4488ef2e4

Name: Box2D
Version:  3.1.1
Release:  1%{?dist}
Summary: A 2D Physics Engine for Games

License: Zlib
URL: http://box2d.org/
Source0:        https://github.com/erincatto/box2d/archive/refs/tags/v%{version}.tar.gz#/%{name}-%{version}.tar.gz
BuildRequires:  gcc
BuildRequires:  gcc-c++
BuildRequires: cmake

%package devel
Summary: Development files for %{name}
Requires: %{name} = %{version}-%{release}

%description
Box2D is an open source C++ engine for simulating rigid bodies in 2D. 
Box2D is developed by Erin Catto and has the zlib license. 
While the zlib license does not require acknowledgement, 
we encourage you to give credit to Box2D in your product. 

%description devel
Box2D is an open source C++ engine for simulating rigid bodies in 2D. 
Box2D is developed by Erin Catto and has the zlib license. 
While the zlib license does not require acknowledgement, 
we encourage you to give credit to Box2D in your product. 

These are the development files.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%setup -qn box2d-%{version}
rm -r extern

%build
%cmake -DBOX2D_INSTALL=ON -DBOX2D_BUILD_SHARED=ON -DBOX2D_BUILD_TESTBED=OFF -DBOX2D_BUILD_UNIT_TESTS=OFF .
%cmake_build

%install
%cmake_install

%files
%license LICENSE
%{_libdir}/*.so.2*

%files devel
%doc README.md docs/
%{_libdir}/*.so
%{_includedir}/box2d
%{_libdir}/cmake/box2d/*.cmake

%changelog
%autochangelog
