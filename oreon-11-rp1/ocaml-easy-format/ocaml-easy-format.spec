%global source0_hash 1dbf051e9f68574dde6e2e254a66b9c524ca425e80b36e99af96ed964ab610c3
ExcludeArch: %{ix86}
%ifnarch %{ocaml_native_compiler}
%global debug_package %{nil}
%endif
%global libname easy-format
Name:           ocaml-%{libname}
Version:        1.3.4
Release:        1%{?dist}
Summary:        High-level and functional interface to the Format module
License:        BSD-3-Clause
URL:            https://github.com/ocaml-community/%{libname}
VCS:            git:%{url}.git
Source0:        https://github.com/ocaml-community/%{libname}/releases/download/%{version}/%{libname}-%{version}.tbz
# oreon:deps
BuildRequires:  ocaml
BuildRequires:  ocaml-dune
# /oreon:deps
%description
This module offers a high-level and functional interface to the Format
module of the OCaml standard library. It is a pretty-printing
facility, i.e. it takes as input some code represented as a tree and
formats this code into the most visually satisfying result, breaking
and indenting lines of code where appropriate.

Input data must be first modeled and converted into a tree using 3
kinds of nodes:

    atoms
    lists
    labeled nodes

Atoms represent any text that is guaranteed to be printed as-is. Lists
can model any sequence of items such as arrays of data or lists of
definitions that are labeled with something like "int main", "let x
=" or "x:".

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
%description    devel
The %{name}-devel package contains libraries and signature files for
developing applications that use %{name}.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n %{libname}-%{version}

%build

%dune_build
%install
%dune_install
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*

%check

%dune_check
%files -f %{oreon_filedir}/main.list
%files -n ocaml-easy-format-devel -f %{oreon_filedir}/ocaml-easy-format-devel.list

%changelog

%autochangelog
