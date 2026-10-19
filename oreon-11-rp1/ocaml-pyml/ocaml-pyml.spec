%global source0_hash a49398c86adb8fabcb79a4d737733ac49c8dec1a60df9d28c764a5b870bff9e7
Name:           ocaml-pyml
Version:        20250807
Release:        1%{?dist}
Summary:        OCaml bindings for Python
License:        BSD-2-Clause AND LGPL-2.1-or-later
URL:            https://github.com/ocamllibs/pyml
VCS:            git:%{url}.git
Source0:        https://github.com/ocamllibs/pyml/archive/%{version}/pyml-%{version}.tar.gz
Patch:          %{name}-python3.13.patch
Patch:          %{name}-memcpy.patch
ExcludeArch:    %{ix86}
# oreon:deps
BuildRequires:  ocaml
BuildRequires:  ocaml-dune
BuildRequires:  ocaml-findlib
BuildRequires:  ocaml-stdcompat-devel
BuildRequires:  python3-devel
BuildRequires:  python3dist(ipython)
BuildRequires:  python3dist(numpy)
# /oreon:deps
%description
py.ml provides OCaml bindings for Python 2 and Python 3.  This library
subsumes the pycaml library, which is no longer actively maintained.

The Python library is linked at runtime and the same executable can be run in
a Python 2 or a Python 3 environment.  py.ml does not require any Python
library at compile time.  The only compile time dependency is Stdcompat to
ensure compatibility with all OCaml compiler versions from 3.12.

Bindings are split in three modules:

- Py provides the initialization functions and some high-level bindings, with
  error handling and naming conventions closer to OCaml usages.

- Pycaml provides a signature close to the old Pycaml module, so as to ease
  migration.

- Pywrappers provides low-level bindings, which follow closely the conventions
  of the C bindings for Python.  Submodules `Pywrappers.Python2` and
  `Pywrappers.Python3` contain version-specific bindings.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       ocaml-stdcompat-devel%{?_isa}
%description    devel
The %{name}-devel package contains libraries and signature files for
developing applications that use %{name}.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%global oreon_srcdir pyml-%{version}
%oreon_prep
%build

%dune_build
%install
%dune_install
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*

%check

%dune_check
%files -f %{oreon_filedir}/main.list
%files -n ocaml-pyml-devel -f %{oreon_filedir}/ocaml-pyml-devel.list

%changelog

%autochangelog
