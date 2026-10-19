%global source0_hash 344b3b03f95f03ef0013a935f443d6d367b5a6c78313b1e86c6481fd9c0b7287
ExcludeArch: %{ix86}
Name:           ocaml-lacaml
Version:        11.1.1
Release:        6%{?dist}
Summary:        BLAS/LAPACK-interface for OCaml
License:        LGPL-2.1-or-later WITH OCaml-LGPL-linking-exception
URL:            https://github.com/mmottl/lacaml
VCS:            git:%{url}.git
Source0:        https://github.com/mmottl/lacaml/releases/download/%{version}/lacaml-%{version}.tbz
%global __ocaml_requires_opts -i Asttypes -i Build_path_prefix_map -i Cmi_format -i Env -i Format_doc -i Ident -i Identifiable -i Load_path -i Location -i Longident -i Misc -i Oprint -i Outcometree -i Parsetree -i Path -i Primitive -i Shape -i Subst -i Toploop -i Type_immediacy -i Types -i Unit_info -i Warnings
# oreon:deps
BuildRequires:  ocaml
BuildRequires:  ocaml-dune
BuildRequires:  ocaml-dune-configurator-devel
BuildRequires:  pkgconfig(flexiblas)
# /oreon:deps
%description
This OCaml-library interfaces the BLAS-library (Basic Linear Algebra
Subroutines) and LAPACK-library (Linear Algebra routines), which are
written in FORTRAN.

This allows people to write high-performance numerical code for
applications that need linear algebra.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
%description    devel
The %{name}-devel package contains libraries and signature files for
developing applications that use %{name}.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%global oreon_srcdir lacaml-%{version}
%oreon_prep
%build

export LACAML_LIBS=-lflexiblas
%dune_build
%install
export LACAML_LIBS=-lflexiblas
%dune_install
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*

%check

export LACAML_LIBS=-lflexiblas
%dune_check
%files -f %{oreon_filedir}/main.list
%files -n ocaml-lacaml-devel -f %{oreon_filedir}/ocaml-lacaml-devel.list

%changelog

%autochangelog
