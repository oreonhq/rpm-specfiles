%global source0_hash 45227d0205049addb74190a4eb41132179a42611bb92741efacf30371c481e6e
Name:           ocaml-stdcompat
Version:        21.1
Release:        1%{?dist}
Summary:        Compatibility module for the OCaml standard library
License:        LGPL-2.1-or-later
URL:            https://github.com/ocamllibs/stdcompat
VCS:            git:%{url}.git
Source0:        https://github.com/ocamllibs/stdcompat/archive/%{version}/stdcompat-%{version}.tar.gz
Patch:          %{name}-ocaml5.4.patch
ExcludeArch:    %{ix86}
# oreon:deps
BuildRequires:  ocaml
BuildRequires:  ocaml-dune
# /oreon:deps
%description
Stdcompat is a compatibility layer allowing programs to use some recent
additions to the OCaml standard library while preserving the ability to be
compiled on former versions of OCaml.

The Stdcompat API is not intended to be stable, but there will be efforts to
allow future versions of Stdcompat to be compiled on a large range of versions
of OCaml: Stdcompat should compile (at least) on every version of OCaml from
3.08 (inclusive).

The module Stdcompat provides some definitions for values and types introduced
in recent versions of the standard library.  These definitions are just
aliases to the matching definition of the standard library if the latter is
recent enough.  Otherwise, the module Stdcompat provides an alternative
implementation.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
%description    devel
The %{name}-devel package contains libraries and signature files for
developing applications that use %{name}.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%global oreon_srcdir stdcompat-%{version}
%oreon_prep
%build

%dune_build
%install
%dune_install
%ifarch %{ocaml_native_compiler}
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*

%check

%dune_check
%endif
%files -f %{oreon_filedir}/main.list
%files -n ocaml-stdcompat-devel -f %{oreon_filedir}/ocaml-stdcompat-devel.list

%changelog

%autochangelog
