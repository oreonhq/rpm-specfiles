%global source0_hash 63e22783e06d17db027367e82fc08954c55f81a7db40fb7057a73713c16f3523
ExcludeArch: %{ix86}
%ifnarch %{ocaml_native_compiler}
%global debug_package %{nil}
%endif
Name:           ocaml-astring
Version:        0.8.5
Release:        1%{?dist}
Summary:        Alternative String module for OCaml
License:        ISC
URL:            https://erratique.ch/software/astring
VCS:            git:https://erratique.ch/repos/astring/.git
Source0:        https://github.com/dbuenzli/astring/archive/v%{version}/astring-%{version}.tar.gz
Patch:          %{name}-ocaml5.patch
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
Astring exposes an alternative `String` module for OCaml.  This module tries
to balance minimality and expressiveness for basic, index-free, string
processing and provides types and functions for substrings, string sets and
string maps.

Remaining compatible with the OCaml `String` module is a non-goal.  The
`String` module exposed by Astring has exception safe functions, removes
deprecated and rarely used functions, alters some signatures and names, adds a
few missing functions and fully exploits OCaml's newfound string immutability.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
%description    devel
The %{name}-devel package contains libraries and signature files for
developing applications that use %{name}.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -N -n astring-%{version}
%ifarch %{ocaml_native_compiler}
%autopatch -p1
%endif

%conf
# Topkg does watermark replacements only if run inside a git checkout.  Github
# tarballs do not come with a .git directory.  Therefore, we do the watermark
# replacement manually.
for fil in $(find . -type f); do
  sed -e 's,%%%%NAME%%%%,astring,' \
      -e 's,%%%%PKG_HOMEPAGE%%%%,%{url},' \
      -e 's,%%%%VERSION%%%%,v%{version},' \
      -e 's,%%%%VERSION_NUM%%%%,%{version},' \
      -i.orig $fil
  touch -r $fil.orig $fil
  rm $fil.orig
done

%build

ocaml pkg/pkg.ml build --tests true
%install
%ocaml_install
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*

%check

ocaml pkg/pkg.ml test
%files -f %{oreon_filedir}/main.list
%files -n ocaml-astring-devel -f %{oreon_filedir}/ocaml-astring-devel.list

%changelog

%autochangelog
