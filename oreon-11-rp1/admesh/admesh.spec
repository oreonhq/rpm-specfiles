%global source0_hash 0d7994bfa587c4e958b2ac7c7d2fb90dfb6c5463d32513ada169cf710a438535
Name:           admesh
Version:        0.98.5
Release:        1%{?dist}
Summary:        Diagnose and/or repair problems with STereo Lithography files
License:        GPL-2.0-or-later
URL:            http://github.com/admesh/admesh/
Source0:        http://github.com/admesh/admesh/releases/download/v%{version}/admesh-%{version}.tar.gz
Requires:       %{name}-libs%{?_isa} = %{version}-%{release}
%if 0%{?fedora} >= 42 || 0%{?rhel} >= 11 || 0%{?oreon} >= 11
ExcludeArch:    %{ix86}
%endif
# oreon:deps
BuildRequires:  gcc
BuildRequires:  make
# /oreon:deps
%description
ADMesh is a program for diagnosing and/or repairing commonly encountered
problems with STL (STereo Lithography) data files. It can remove degenerate
and unconnected facets, connect nearby facets, fill holes by adding facets,
and repair facet normals. Simple transformations such as scaling,
translation and rotation are also supported. ADMesh can read both
ASCII and binary format STL files, while the output can be in
AutoCAD DXF, Geomview OFF, STL, or VRML format.

%package devel
Summary:        Development files for the %{name} library
Requires:       %{name}-libs%{?_isa} = %{version}-%{release}
%description devel
ADMesh is a program for diagnosing and/or repairing commonly encountered
problems with STL (STereo Lithography) data files.

This package contains the development files needed for building new
applications that utilize the %{name} library.

%package libs
Summary:        Runtime library for the %{name} application
%description libs
This package contains the %{name} runtime library.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%oreon_prep
%build

%configure
%make_build CFLAGS="%{optflags}" LIBTOOLFLAGS="-v"
%install
%make_install
rm -rf %{buildroot}%{_defaultdocdir}/%{name}
rm -f %{buildroot}%{_libdir}/lib%{name}.la
%oreon_autofiles admesh-devel usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*
%oreon_autofiles admesh-libs usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%files -f %{oreon_filedir}/main.list
%files -n admesh-devel -f %{oreon_filedir}/admesh-devel.list
%files -n admesh-libs -f %{oreon_filedir}/admesh-libs.list

%changelog

%autochangelog
