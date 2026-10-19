%global source0_hash 6893bf156bbaa4254ec5ec2ea5fe539030f2395bc5cd83ccb8fe3930cff89cb0
ExcludeArch: %{ix86}
%ifnarch %{ocaml_native_compiler}
%global debug_package %{nil}
%endif
%global giturl  https://github.com/c-cube/gen
Name:           ocaml-gen
Version:        1.1
Release:        18%{?dist}
Summary:        Simple, efficient iterators for OCaml
License:        BSD-2-Clause
URL:            https://c-cube.github.io/gen/
VCS:            git:%{giturl}.git
Source0:        %{giturl}/archive/v%{version}/gen-%{version}.tar.gz
Patch:          %{name}-seq.patch
# oreon:deps
BuildRequires:  ocaml
BuildRequires:  ocaml-dune
BuildRequires:  ocaml-ounit-devel
BuildRequires:  ocaml-qcheck-devel
BuildRequires:  ocaml-qtest-devel
# /oreon:deps
%description
Iterators for OCaml, both restartable and consumable.  The implementation
keeps a good balance between simplicity and performance.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
%description    devel
The %{name}-devel package contains libraries and signature files for
developing applications that use %{name}.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%global oreon_srcdir gen-%{version}
%oreon_prep
%build

%dune_build
%install
%dune_install
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*

%check

%dune_check
%files -f %{oreon_filedir}/main.list
%files -n ocaml-gen-devel -f %{oreon_filedir}/ocaml-gen-devel.list

%changelog

%autochangelog
