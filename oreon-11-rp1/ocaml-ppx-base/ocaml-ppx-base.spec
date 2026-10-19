%global source0_hash 80e7e6c6a704114d1d0989ee9bc01bca45278096c0caf3f2c4ef28d3c12ae61c
ExcludeArch: %{ix86}
Name:           ocaml-ppx-base
Version:        0.17.0
Release:        1%{?dist}
Summary:        Base set of OCaml ppx rewriters
License:        MIT
URL:            https://github.com/janestreet/ppx_base
VCS:            git:%{url}.git
Source0:        https://github.com/janestreet/ppx_base/archive/v%{version}/ppx_base-%{version}.tar.gz
# oreon:deps
BuildRequires:  ocaml
BuildRequires:  ocaml-dune
BuildRequires:  ocaml-ppx-cold-devel
BuildRequires:  ocaml-ppx-compare-devel
BuildRequires:  ocaml-ppx-enumerate-devel
BuildRequires:  ocaml-ppx-globalize-devel
BuildRequires:  ocaml-ppx-hash-devel
BuildRequires:  ocaml-ppx-sexp-conv-devel
BuildRequires:  ocaml-ppxlib-devel
# /oreon:deps
%description
Ppx_base is the set of ppx rewriters used for Base.  Note that Base doesn't
need ppx to build; it is only used as a verification tool.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       ocaml-ppx-cold-devel%{?_isa}
Requires:       ocaml-ppx-compare-devel%{?_isa}
Requires:       ocaml-ppx-enumerate-devel%{?_isa}
Requires:       ocaml-ppx-globalize-devel%{?_isa}
Requires:       ocaml-ppx-hash-devel%{?_isa}
Requires:       ocaml-ppx-sexp-conv-devel%{?_isa}
Requires:       ocaml-ppxlib-devel%{?_isa}
Requires:       ocaml-sexplib0-devel%{?_isa}
%description    devel
The %{name}-devel package contains libraries and signature files for
developing applications that use %{name}.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%global oreon_srcdir ppx_base-%{version}
%oreon_prep
%build

%dune_build
%install
%dune_install
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*

%check

%dune_check
%files -f %{oreon_filedir}/main.list
%files -n ocaml-ppx-base-devel -f %{oreon_filedir}/ocaml-ppx-base-devel.list

%changelog

%autochangelog
