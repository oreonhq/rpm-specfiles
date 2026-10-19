%global source0_hash e87485ef61010fb554009f8f32bbc55b1a7b0c5d69efbd4b8ccec935145f6074
%ifnarch %{ocaml_native_compiler}
%global debug_package %{nil}
%endif
Name:           ocaml-uucd
Version:        18.0.0
Release:        1%{?dist}
Summary:        Unicode character database decoder for OCaml
License:        ISC
URL:            https://erratique.ch/software/uucd
VCS:            git:https://erratique.ch/repos/uucd.git
Source0:        https://erratique.ch/software/uucd/releases/uucd-%{version}.tbz
ExcludeArch:    %{ix86}
# oreon:deps
BuildRequires:  ocaml
BuildRequires:  ocaml-compiler-libs
BuildRequires:  ocaml-findlib
BuildRequires:  ocaml-ocamlbuild
BuildRequires:  ocaml-rpm-macros
BuildRequires:  ocaml-topkg-devel
BuildRequires:  ocaml-xmlm-devel
# /oreon:deps
%description
Uucd is an OCaml module to decode the data of the Unicode character database
(http://www.unicode.org/reports/tr44/) from its XML representation
(http://www.unicode.org/reports/tr42/).  It provides high-level (but not
necessarily efficient) access to the data so that efficient representations
can be extracted.

Uucd is made of a single module, depends on Xmlm and is distributed under the
ISC license.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       ocaml-xmlm-devel%{?_isa}
%description    devel
The %{name}-devel package contains libraries and signature files for
developing applications that use %{name}.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%global oreon_srcdir uucd-%{version}
%oreon_prep
%build

ocaml pkg/pkg.ml build --dev-pkg false --tests true
%install
%ocaml_install
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*

%check

ocaml pkg/pkg.ml test
%files -f %{oreon_filedir}/main.list
%files -n ocaml-uucd-devel -f %{oreon_filedir}/ocaml-uucd-devel.list

%changelog

%autochangelog
