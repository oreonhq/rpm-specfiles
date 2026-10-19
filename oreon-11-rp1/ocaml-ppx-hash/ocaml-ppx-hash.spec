%global source0_hash 8c8acae276a349d412eab9112cc3afa996d26ad4a01f2882121fc0adee0dd05e
ExcludeArch: %{ix86}
%ifnarch %{ocaml_native_compiler}
%global debug_package %{nil}
%endif
Name:           ocaml-ppx-hash
Version:        0.17.0
Release:        1%{?dist}
Summary:        Generate hash functions from type expressions and definitions
License:        MIT
URL:            https://github.com/janestreet/ppx_hash
VCS:            git:%{url}.git
Source0:        https://github.com/janestreet/ppx_hash/archive/v%{version}/ppx_hash-%{version}.tar.gz
# oreon:deps
BuildRequires:  ocaml
BuildRequires:  ocaml-base-devel
BuildRequires:  ocaml-dune
BuildRequires:  ocaml-ppx-compare-devel
BuildRequires:  ocaml-ppx-sexp-conv-devel
BuildRequires:  ocaml-ppxlib-devel
BuildRequires:  ocaml-ppxlib-jane-devel
# /oreon:deps
%description
Ppx_hash is a ppx rewriter that generates hash functions from type expressions
and definitions.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       ocaml-base-devel%{?_isa}
Requires:       ocaml-ppx-compare-devel%{?_isa}
Requires:       ocaml-ppx-sexp-conv-devel%{?_isa}
Requires:       ocaml-ppxlib-devel%{?_isa}
Requires:       ocaml-ppxlib-jane-devel%{?_isa}
Requires:       ocaml-sexplib0-devel%{?_isa}
%description    devel
The %{name}-devel package contains libraries and signature files for
developing applications that use %{name}.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%global oreon_srcdir ppx_hash-%{version}
%oreon_prep
%build

%dune_build
%install
%dune_install
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*

%check

%dune_check
%files -f %{oreon_filedir}/main.list
%files -n ocaml-ppx-hash-devel -f %{oreon_filedir}/ocaml-ppx-hash-devel.list

%changelog

%autochangelog
