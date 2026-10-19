%global source0_hash 06c710404b360aae7effe1fbaf36b3a0f7fde934a1712ce32029838e49a02e82
ExcludeArch: %{ix86}
%ifnarch %{ocaml_native_compiler}
%global debug_package %{nil}
%endif
Name:           ocaml-ppx-variants-conv
Version:        0.17.1
Release:        1%{?dist}
Summary:        Generate accessor & iteration functions for OCaml variant types
License:        MIT
URL:            https://github.com/janestreet/ppx_variants_conv
VCS:            git:%{url}.git
Source0:        https://github.com/janestreet/ppx_variants_conv/archive/v%{version}/ppx_variants_conv-%{version}.tar.gz
# oreon:deps
BuildRequires:  ocaml
BuildRequires:  ocaml-base-devel
BuildRequires:  ocaml-dune
BuildRequires:  ocaml-ppx-inline-test-devel
BuildRequires:  ocaml-ppxlib-devel
BuildRequires:  ocaml-variantslib-devel
# /oreon:deps
%description
Ppx_variants_conv is a ppx rewriter that can be used to define first-class
values representing variant constructors, and additional routines to fold,
iterate and map over all constructors of a variant type.  It provides
corresponding functionality for variant types as ppx_fields_conv provides for
record types.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       ocaml-base-devel%{?_isa}
Requires:       ocaml-ppxlib-devel%{?_isa}
Requires:       ocaml-variantslib-devel%{?_isa}
%description    devel
The %{name}-devel package contains libraries and signature
files for developing applications that use %{name}.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%global oreon_srcdir ppx_variants_conv-%{version}
%oreon_prep
%build

%dune_build
%install
%dune_install
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*

%check

%dune_check
%files -f %{oreon_filedir}/main.list
%files -n ocaml-ppx-variants-conv-devel -f %{oreon_filedir}/ocaml-ppx-variants-conv-devel.list

%changelog

%autochangelog
