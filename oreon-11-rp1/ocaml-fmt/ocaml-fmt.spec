%global source0_hash 857cfd47a54b52429cd9b3e2665e44173cd1bd3b435bece7172f984ad5376a1b
ExcludeArch: %{ix86}
%ifnarch %{ocaml_native_compiler}
%global debug_package %{nil}
%endif
Name:           ocaml-fmt
Version:        0.11.0
Release:        1%{?dist}
Summary:        OCaml Format pretty-printer combinators
License:        ISC
URL:            https://erratique.ch/software/fmt
VCS:            git:https://erratique.ch/repos/fmt.git
Source0:        https://erratique.ch/software/fmt/releases/fmt-%{version}.tbz
%global __ocaml_requires_opts -i Asttypes -i Build_path_prefix_map -i Cmi_format -i Env -i Format_doc -i Ident -i Identifiable -i Load_path -i Location -i Longident -i Misc -i Oprint -i Outcometree -i Parsetree -i Path -i Primitive -i Shape -i Subst -i Toploop -i Type_immediacy -i Types -i Unit_info -i Warnings
# oreon:deps
BuildRequires:  ocaml
BuildRequires:  ocaml-cmdliner-devel
BuildRequires:  ocaml-findlib
BuildRequires:  ocaml-ocamlbuild
BuildRequires:  ocaml-ocamldoc
BuildRequires:  ocaml-rpm-macros
BuildRequires:  ocaml-topkg-devel
# /oreon:deps
%description
Fmt exposes combinators to devise `Format` pretty-printing functions.

Fmt depends only on the OCaml standard library.  The optional Fmt_tty library
that enables setting up formatters for terminal color output depends on the
Unix library.  The optional Fmt_cli library that provides command line support
for Fmt depends on Cmdliner.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       ocaml-cmdliner-devel%{?_isa}
%description    devel
The %{name}-devel package contains libraries and signature files for
developing applications that use %{name}.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n fmt-%{version} -p1

%conf
# link with the math library
sed -i 's/safe_string/&, cclib(-lm)/' _tags

%build

ocaml pkg/pkg.ml build \
  --dev-pkg false \
  --tests true \
  --with-base-unix true \
  --with-cmdliner true
mkdir html
ocamldoc -html -d html -I +cmdliner -I _build/src _build/src/*.mli
%install
%ocaml_install
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*

%check

ocaml pkg/pkg.ml test
%files -f %{oreon_filedir}/main.list
%files -n ocaml-fmt-devel -f %{oreon_filedir}/ocaml-fmt-devel.list

%changelog

%autochangelog
