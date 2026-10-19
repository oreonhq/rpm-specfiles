%global source0_hash badedc7c583a7a7b423763badb97f9fd4b969906b9345c854227c38ded6323fc
%ifnarch %{ocaml_native_compiler}
%global debug_package %{nil}
%endif
Name:           ocaml-uucp
Version:        18.0.0
Release:        1%{?dist}
Summary:        Unicode character properties for OCaml
License:        ISC
URL:            https://erratique.ch/software/uucp
VCS:            git:https://erratique.ch/repos/uucp.git
Source0:        https://erratique.ch/software/uucp/releases/uucp-%{version}.tbz
ExcludeArch:    %{ix86}
# oreon:deps
BuildRequires:  ocaml
BuildRequires:  ocaml-cmdliner-devel
BuildRequires:  ocaml-compiler-libs
BuildRequires:  ocaml-findlib
BuildRequires:  ocaml-ocamlbuild
BuildRequires:  ocaml-rpm-macros
BuildRequires:  ocaml-topkg-devel
BuildRequires:  ocaml-uucd-devel
BuildRequires:  ocaml-uunf-devel
# /oreon:deps
%description
Uucp is an OCaml library providing efficient access to a selection of
character properties of the Unicode character database
(http://www.unicode.org/reports/tr44/).

Uucp is independent from any Unicode text data structure and has no
dependencies.  It is distributed under the ISC license.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
%description    devel
The %{name}-devel package contains libraries and signature files for
developing applications that use %{name}.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%global oreon_srcdir uucp-%{version}
%oreon_prep
%build

ocaml pkg/pkg.ml build --dev-pkg false --with-uunf true --with-cmdliner true \
  --tests true
%install
%ocaml_install
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*

%check

ocaml pkg/pkg.ml test
%files -f %{oreon_filedir}/main.list
%files -n ocaml-uucp-devel -f %{oreon_filedir}/ocaml-uucp-devel.list

%changelog

%autochangelog
