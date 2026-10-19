%global source0_hash 78e7571a779ea4952e752ecef57c62fb26463947e29ef7f4b31b11988d88ca07
Name:          maeparser
Version:       1.3.3
Release:        1%{?dist}
Summary:        A parser for Schrodinger Maestro files
License:       MIT
URL:           https://github.com/schrodinger/%{name}/
Source0:        https://github.com/schrodinger/%{name}/archive/refs/tags/v%{version}.tar.gz
%global common_description %{expand: \
 Maestro is a commercial "all-purpose molecular modeling environment",
 produced and distributed by the company Schrödinger. Maestro has its
 own cognate file format, typically associated with the ".mae" file
 extension. This package provides an open-source parser for the Maestro
 file format, released and maintained by the Maestro developers.
 This facilitates a lossless transition from the widely accepted suite
 of Schrödinger into local custom developments or the open-source world
 at large. Maeparser handles output from:
 * Molecular Dynamics applications, such as Desmond and FEP+
 * Ligand-Protein Docking applications, such as Glide
 * Homology Modeling and folding applications, such as Prime
 * Ligand-based search applications, such as Phase and Phase Shape
 * Quantum Mechanics applications, such as Jaguar
 * Protein-Protein Docking applications
 * ... many other backends used in both Life and Material Sciences}
# oreon:deps
BuildRequires:  boost-devel
BuildRequires:  cmake
BuildRequires:  gcc-c++
BuildRequires:  git
BuildRequires:  make
BuildRequires:  zlib-devel
# /oreon:deps
%description
%{common_description}

%package devel
Requires: %{name}%{_isa} = %{version}-%{release}
Summary: Header files for maeparser
%description devel
 .
 This package contains header files needed for developing applications with
 maeparser.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%global oreon_srcdir %{name}-%{version}
%oreon_prep
%build

%set_build_flags
%cmake
%cmake_build
%install
%cmake_install
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*

%files -f %{oreon_filedir}/main.list
%files -n maeparser-devel -f %{oreon_filedir}/maeparser-devel.list

%changelog

%autochangelog
