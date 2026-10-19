%global source0_hash 0e6c61aff150d19a0f89cb3e354ab36189e4bc23e28ab8bce03b6c6b6004f237
ExcludeArch: %{ix86}
Name:           ocaml-bin-prot
Version:        0.17.0
Epoch:          1
Release:        1%{?dist}
Summary:        Read and write OCaml values in a type-safe binary protocol
License:        MIT AND BSD-3-Clause
URL:            https://github.com/janestreet/bin_prot
VCS:            git:%{url}.git
Source0:        https://github.com/janestreet/bin_prot/archive/v%{version}/bin_prot-%{version}.tar.gz
# oreon:deps
BuildRequires:  ocaml
BuildRequires:  ocaml-base-devel
BuildRequires:  ocaml-dune
BuildRequires:  ocaml-ppx-compare-devel
BuildRequires:  ocaml-ppx-custom-printf-devel
BuildRequires:  ocaml-ppx-fields-conv-devel
BuildRequires:  ocaml-ppx-optcomp-devel
BuildRequires:  ocaml-ppx-sexp-conv-devel
BuildRequires:  ocaml-ppx-stable-witness-devel
BuildRequires:  ocaml-ppx-variants-conv-devel
# /oreon:deps
%description
This library contains functionality for reading and writing OCaml values in a
type-safe binary protocol.  These functions are extremely efficient and
provide users with a convenient and safe way of performing I/O on any
extensionally defined data type.  This means that functions, objects, and
values whose type is bound through a polymorphic record field are not
supported, but everything else is.

As of now, there is no support for cyclic or shared values.  Cyclic values
will lead to non-termination whereas shared values, besides requiring
significantly more space when encoded, may lead to a substantial increase in
memory footprint when they are read back in.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name} = 1:%{version}-%{release}
Requires:       ocaml-base-devel%{?_isa}
Requires:       ocaml-fieldslib-devel%{?_isa}
Requires:       ocaml-ppx-compare-devel%{?_isa}
Requires:       ocaml-ppx-sexp-conv-devel%{?_isa}
Requires:       ocaml-sexplib0-devel%{?_isa}
Requires:       ocaml-ppx-stable-witness-devel%{?_isa}
Requires:       ocaml-variantslib-devel%{?_isa}
%description    devel
The %{name}-devel package contains libraries and signature files for
developing applications that use %{name}.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%global oreon_srcdir bin_prot-%{version}
%oreon_prep
%build

%dune_build
%install
%dune_install
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*

%check

%dune_check
%files -f %{oreon_filedir}/main.list
%files -n ocaml-bin-prot-devel -f %{oreon_filedir}/ocaml-bin-prot-devel.list

%changelog

%autochangelog
