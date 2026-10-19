%global source0_hash e954d2c0c96ab1fc428c50c49cac7ce2dc5eab0e3120bff217ff6d2a8d288ada
Name:           poly2tri
Version:        0.0^20260314gitmaster
Release:        1%{?dist}
Summary:        A 2D constrained Delaunay triangulation library
License:        BSD-3-Clause
URL:            https://github.com/jhasse/poly2tri
Source0:        https://github.com/jhasse/poly2tri/archive/refs/heads/master.tar.gz#/poly2tri-master.tar.gz
Source1:        poly2tri-Makefile
# oreon:deps
BuildRequires:  gcc-c++
BuildRequires:  make
# /oreon:deps
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
cp %{SOURCE1} poly2tri/Makefile

%build

cd poly2tri
CFLAGS="%{optflags}" LDFLAGS="%{build_ldflags}" %{make_build}
cd -
%install
install -Dpm0755 poly2tri/libpoly2tri.so.1.0 %{buildroot}%{_libdir}/libpoly2tri.so.1.0
ln -s libpoly2tri.so.1.0 %{buildroot}%{_libdir}/libpoly2tri.so.1
ln -s libpoly2tri.so.1.0 %{buildroot}%{_libdir}/libpoly2tri.so
for H in poly2tri/*/*.h poly2tri/*.h; do
  install -Dpm0644 "$H" %{buildroot}%{_includedir}/"$H"
done
%ldconfig_scriptlets
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*

%files -f %{oreon_filedir}/main.list
%files -n poly2tri-devel -f %{oreon_filedir}/poly2tri-devel.list
