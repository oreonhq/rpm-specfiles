%global source0_hash b850556d05203aa6d97fcbe4be75abc9679b161be059e474c0d934bc0e12fe86
ExcludeArch: %{ix86}
%ifnarch %{ocaml_native_compiler}
%global debug_package %{nil}
%endif
%bcond test 0
Name:           ocaml-ppx-sexp-conv
Version:        0.17.1
Release:        1%{?dist}
Summary:        Generate S-expression conversion functions from type definitions
License:        MIT
URL:            https://github.com/janestreet/ppx_sexp_conv
VCS:            git:%{url}.git
Source0:        https://github.com/janestreet/ppx_sexp_conv/archive/v%{version}/ppx_sexp_conv-%{version}.tar.gz
%if %{with test}
%endif
# oreon:deps
BuildRequires:  ocaml
BuildRequires:  ocaml-base-devel
BuildRequires:  ocaml-dune
BuildRequires:  ocaml-ppx-inline-test-devel
BuildRequires:  ocaml-ppxlib-devel
BuildRequires:  ocaml-ppxlib-jane-devel
BuildRequires:  ocaml-sexplib0-devel
# /oreon:deps
%description
Ppx_sexp_conv is a PPX syntax extension that generates code for converting
OCaml types to and from s-expressions, as defined in the sexplib0 library.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       ocaml-base-devel%{?_isa}
Requires:       ocaml-ppxlib-devel%{?_isa}
Requires:       ocaml-ppxlib-jane-devel%{?_isa}
Requires:       ocaml-sexplib0-devel%{?_isa}
%description    devel
The %{name}-devel package contains libraries and signature files
for developing applications that use %{name}.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%global oreon_srcdir ppx_sexp_conv-%{version}
%oreon_prep
%build

%dune_build
%install
%dune_install
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*
%if %{with test}
%check

%dune_check
%endif
%files -f %{oreon_filedir}/main.list
%files -n ocaml-ppx-sexp-conv-devel -f %{oreon_filedir}/ocaml-ppx-sexp-conv-devel.list

%changelog

%autochangelog
