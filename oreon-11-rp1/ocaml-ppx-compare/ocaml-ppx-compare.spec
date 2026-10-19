%global source0_hash f0b23eb78082ef4dc71a66939bbc63c6b0cc2cf6a4744a906b7a2c016cbe3098
ExcludeArch: %{ix86}
%ifnarch %{ocaml_native_compiler}
%global debug_package %{nil}
%endif
%bcond test 0
Name:           ocaml-ppx-compare
Version:        0.17.0
Release:        1%{?dist}
Summary:        Generate comparison functions from types
License:        MIT
URL:            https://github.com/janestreet/ppx_compare
VCS:            git:%{url}.git
Source0:        https://github.com/janestreet/ppx_compare/archive/v%{version}/ppx_compare-%{version}.tar.gz
%if %{with test}
%endif
# oreon:deps
BuildRequires:  ocaml
BuildRequires:  ocaml-base-devel
BuildRequires:  ocaml-dune
BuildRequires:  ocaml-ppx-inline-test-devel
BuildRequires:  ocaml-ppxlib-devel
BuildRequires:  ocaml-ppxlib-jane-devel
# /oreon:deps
%description
Ppx_compare is a ppx rewriter that derives comparison and equality functions
from type representations.  The scaffolded functions are usually much faster
than OCaml's `Stdlib.compare` and `Stdlib.(=)`.  Scaffolding functions also
give more flexibility by allowing them to be overridden for a specific type,
and more safety by making sure that only comparable values are compared.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       ocaml-base-devel%{?_isa}
Requires:       ocaml-ppxlib-devel%{?_isa}
Requires:       ocaml-ppxlib-jane-devel%{?_isa}
%description    devel
The %{name}-devel package contains libraries and signature files for
developing applications that use %{name}.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%global oreon_srcdir ppx_compare-%{version}
%oreon_prep
%build

%dune_build
%install
%dune_install
%if %{with test}
%ifnarch %{ocaml_native_compiler}
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*

%check

%dune_check
%endif
%endif
%files -f %{oreon_filedir}/main.list
%files -n ocaml-ppx-compare-devel -f %{oreon_filedir}/ocaml-ppx-compare-devel.list

%changelog

%autochangelog
