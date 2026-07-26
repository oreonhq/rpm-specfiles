%global source0_hash 344b3b03f95f03ef0013a935f443d6d367b5a6c78313b1e86c6481fd9c0b7287

# OCaml packages not built on i686 since OCaml 5 / Fedora 39.
ExcludeArch: %{ix86}

Name:           ocaml-lacaml
Version:        11.1.1
Release:        6%{?dist}
Summary:        BLAS/LAPACK-interface for OCaml

License:        LGPL-2.1-or-later WITH OCaml-LGPL-linking-exception
URL:            https://github.com/mmottl/lacaml
VCS:            git:%{url}.git
Source0:        %{url}/releases/download/%{version}/lacaml-%{version}.tbz

BuildRequires:  ocaml >= 4.08
BuildRequires:  ocaml-dune >= 2.7
BuildRequires:  ocaml-dune-configurator-devel
BuildRequires:  pkgconfig(flexiblas)

# Do not require ocaml-compiler-libs at runtime
%global __ocaml_requires_opts -i Asttypes -i Build_path_prefix_map -i Cmi_format -i Env -i Format_doc -i Ident -i Identifiable -i Load_path -i Location -i Longident -i Misc -i Oprint -i Outcometree -i Parsetree -i Path -i Primitive -i Shape -i Subst -i Toploop -i Type_immediacy -i Types -i Unit_info -i Warnings

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

%autosetup -n lacaml-%{version}

%build
export LACAML_LIBS=-lflexiblas
%dune_build

%install
export LACAML_LIBS=-lflexiblas
%dune_install

%check
export LACAML_LIBS=-lflexiblas
%dune_check

%files -f .ofiles
%doc README.md
%license LICENSE.md

%files devel -f .ofiles-devel
%doc CHANGES.md
%license LICENSE.md

%changelog
%autochangelog
