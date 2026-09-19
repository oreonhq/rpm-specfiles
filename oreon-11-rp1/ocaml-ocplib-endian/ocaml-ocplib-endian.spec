%global source0_hash 97ae74e8aeead46a0475df14af637ce78e2372c07258619ad8967506f2d4b320

# OCaml packages not built on i686 since OCaml 5 / Fedora 39.
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
Source0:        %{url}/archive/%{version}/ocplib-endian-%{version}.tar.gz
# Remove dependency on base-bytes
Patch0:         https://github.com/OCamlPro/ocplib-endian/pull/26.patch

BuildRequires:  ocaml >= 4.03.0
BuildRequires:  ocaml-cppo >= 1.1.0
BuildRequires:  ocaml-dune >= 1.0

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

%autosetup -n ocplib-endian-%{version} -p1

%build
%dune_build

%install
%dune_install

%check
%dune_check

%files -f .ofiles
%license COPYING.txt
%doc README.md CHANGES.md

%files devel -f .ofiles-devel

%changelog
%autochangelog
