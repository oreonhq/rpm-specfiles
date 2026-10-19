%global source0_hash 6fab6e1e894207db268f2103beba5ec9cdc10c066f6ed4f12e748ce97b027757
ExcludeArch: %{ix86}
%global giturl  https://github.com/ocaml-ppx/ppx_deriving
Name:           ocaml-ppx-deriving
Version:        6.2.0
Release:        1%{?dist}
Summary:        Type-driven code generation for OCaml
License:        MIT
URL:            https://ocaml-ppx.github.io/ppx_deriving/
VCS:            git:%{giturl}.git
Source0:        %{giturl}/archive/v%{version}/ppx_deriving-%{version}.tar.gz
# oreon:deps
BuildRequires:  ocaml
BuildRequires:  ocaml-cppo
BuildRequires:  ocaml-dune
BuildRequires:  ocaml-findlib-devel
BuildRequires:  ocaml-ounit-devel
BuildRequires:  ocaml-ppx-derivers-devel
BuildRequires:  ocaml-ppxlib-devel
# /oreon:deps
%description
Deriving is a library simplifying type-driven code generation on OCaml.  It
includes a set of useful plugins: show, eq, ord (eq), enum, iter, map (iter),
fold (iter), make, yojson, and protobuf.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       ocaml-ppx-derivers-devel%{?_isa}
Requires:       ocaml-ppxlib-devel%{?_isa}
%description    devel
The %{name}-devel package contains libraries and signature files
for developing applications that use %{name}.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%global oreon_srcdir ppx_deriving-%{version}
%oreon_prep
%build

%dune_build
%install
%dune_install
cd _build/default
ln -s ../../src/ppx_deriving_main.cppo.ml
ln -s ../../src/api/ppx_deriving.cppo.ml .
ln -s ../../src/runtime/ppx_deriving_runtime.cppo.ml .
ln -s ../../src_plugins/create/ppx_deriving_create.cppo.ml .
ln -s ../../src_plugins/enum/ppx_deriving_enum.cppo.ml .
ln -s ../../src_plugins/eq/ppx_deriving_eq.cppo.ml .
ln -s ../../src_plugins/fold/ppx_deriving_fold.cppo.ml .
ln -s ../../src_plugins/iter/ppx_deriving_iter.cppo.ml .
ln -s ../../src_plugins/make/ppx_deriving_make.cppo.ml .
ln -s ../../src_plugins/map/ppx_deriving_map.cppo.ml .
ln -s ../../src_plugins/ord/ppx_deriving_ord.cppo.ml
ln -s ../../src_plugins/show/ppx_deriving_show.cppo.ml
cd -
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*

%check

%dune_check
%files -f %{oreon_filedir}/main.list
%files -n ocaml-ppx-deriving-devel -f %{oreon_filedir}/ocaml-ppx-deriving-devel.list

%changelog

%autochangelog
