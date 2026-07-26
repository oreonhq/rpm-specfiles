%global source0_hash 1dbf051e9f68574dde6e2e254a66b9c524ca425e80b36e99af96ed964ab610c3

# OCaml packages not built on i686 since OCaml 5 / Fedora 39.
ExcludeArch: %{ix86}

%ifnarch %{ocaml_native_compiler}
%global debug_package %{nil}
%endif

%global libname easy-format

Name:           ocaml-%{libname}
Version:        1.3.4
Release:        17%{?dist}
Summary:        High-level and functional interface to the Format module

License:        BSD-3-Clause
URL:            https://github.com/ocaml-community/%{libname}
VCS:            git:%{url}.git
Source0:        %{url}/releases/download/%{version}/%{libname}-%{version}.tbz

BuildRequires:  ocaml >= 4.08
BuildRequires:  ocaml-dune >= 3.2

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

%check
%dune_check

%files -f .ofiles
%license LICENSE
%doc README.md

%files devel -f .ofiles-devel
%doc CHANGES.md

%changelog
%autochangelog
