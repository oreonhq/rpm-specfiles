%global source0_hash 97ae74e8aeead46a0475df14af637ce78e2372c07258619ad8967506f2d4b320
ExcludeArch: %{ix86}
%ifnarch %{ocaml_native_compiler}
%global debug_package %{nil}
%endif
Name:           ocaml-ocplib-endian
Version:        1.2
Release:        24%{?dist}
Summary:        Functions to read/write int16/32/64 from strings, bigarrays
License:        LGPL-2.1-or-later WITH OCaml-LGPL-linking-exception
URL:            https://github.com/OCamlPro/ocplib-endian
VCS:            git:%{url}.git
Source0:        https://github.com/OCamlPro/ocplib-endian/archive/%{version}/ocplib-endian-%{version}.tar.gz
Patch0:         https://github.com/OCamlPro/ocplib-endian/pull/26.patch
# oreon:deps
BuildRequires:  ocaml
BuildRequires:  ocaml-cppo
BuildRequires:  ocaml-dune
# /oreon:deps
%description
Optimized functions to read and write int16/32/64 from strings,
bytes and bigarrays, based on primitives added in version 4.01.

The library implements three modules:

- EndianString works directly on strings, and provides submodules
  BigEndian and LittleEndian, with their unsafe counterparts;
- EndianBytes works directly on bytes, and provides submodules
  BigEndian and LittleEndian, with their unsafe counterparts;
- EndianBigstring works on bigstrings (Bigarrays of chars),
  and provides submodules BigEndian and LittleEndian, with their
  unsafe counterparts.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
%description    devel
The %{name}-devel package contains libraries and
signature files for developing applications that use %{name}.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%global oreon_srcdir ocplib-endian-%{version}
%oreon_prep
%build

%dune_build
%install
%dune_install
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*

%check

%dune_check
%files -f %{oreon_filedir}/main.list
%files -n ocaml-ocplib-endian-devel -f %{oreon_filedir}/ocaml-ocplib-endian-devel.list

%changelog

%autochangelog
