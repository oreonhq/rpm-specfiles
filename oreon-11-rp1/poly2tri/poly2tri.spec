%global source0_hash b4f2ee42aa9070f6e7c045347b3551b54ab79933c4637cec191e1758e4a8ca53

Name:           poly2tri
Version:        0.0^20260314gitmaster
Release:        1%{?dist}
Summary:        A 2D constrained Delaunay triangulation library
License:        BSD-3-Clause
URL:            https://github.com/jhasse/poly2tri
Source0:        https://github.com/jhasse/poly2tri/archive/refs/heads/master.tar.gz#/poly2tri-master.tar.gz

BuildRequires: cmake
BuildRequires: gcc-c++

%description
Library based on the paper "Sweep-line algorithm for constrained Delaunay
triangulation" by V. Domiter and B. Zalik.

%package devel
Summary: Development files for %{name}
Requires: %{name}%{?_isa} = %{version}-%{release}

%description devel
Development files for %{name}.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%autosetup -n poly2tri-master

%build
%cmake -DBUILD_TESTING=OFF
%cmake_build

%install
%cmake_install

%files
%{_libdir}/libpoly2tri.so.1.0
%{_libdir}/libpoly2tri.so.1

%files devel
%{_includedir}/poly2tri/
%{_libdir}/libpoly2tri.so
%{_libdir}/libpoly2tri.so.1.0
%{_libdir}/pkgconfig/poly2tri.pc
