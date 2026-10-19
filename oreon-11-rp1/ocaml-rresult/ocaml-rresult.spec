%global source0_hash 11aa7f5b83460e60431e3154e3e32c071d46e151ea5760cf24377805bf975540
ExcludeArch: %{ix86}
%ifnarch %{ocaml_native_compiler}
%global debug_package %{nil}
%endif
Name:           ocaml-rresult
Version:        0.7.0
Release:        1%{?dist}
Summary:        Result value combinators for OCaml
License:        ISC
URL:            https://erratique.ch/software/rresult
VCS:            git:https://erratique.ch/repos/rresult.git
Source0:        https://erratique.ch/software/rresult/releases/rresult-%{version}.tbz
%global __ocaml_requires_opts -i Asttypes -i Build_path_prefix_map -i Cmi_format -i Env -i Format_doc -i Ident -i Identifiable -i Load_path -i Location -i Longident -i Misc -i Oprint -i Outcometree -i Parsetree -i Path -i Primitive -i Shape -i Subst -i Toploop -i Type_immediacy -i Types -i Unit_info -i Warnings
# oreon:deps
BuildRequires:  ocaml
BuildRequires:  ocaml-compiler-libs
BuildRequires:  ocaml-findlib
BuildRequires:  ocaml-ocamlbuild
BuildRequires:  ocaml-rpm-macros
BuildRequires:  ocaml-topkg-devel
# /oreon:deps
%description
Rresult is an OCaml module for handling computation results and errors in an
explicit and declarative manner without resorting to exceptions.  It defines
combinators to operate on the values of the result type available from OCaml
4.03 in the standard library.

OCaml 4.08 provides the Stdlib.Result module which you should prefer to
Rresult.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
%description    devel
The %{name}-devel package contains libraries and signature
files for developing applications that use %{name}.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%global oreon_srcdir rresult-%{version}
%oreon_prep
%build

ocaml pkg/pkg.ml build --dev-pkg false --tests true
%install
%ocaml_install
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*

%check

ocaml pkg/pkg.ml test
%files -f %{oreon_filedir}/main.list
%files -n ocaml-rresult-devel -f %{oreon_filedir}/ocaml-rresult-devel.list

%changelog

%autochangelog
