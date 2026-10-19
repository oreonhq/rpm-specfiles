%global source0_hash 670ee6f4efef2020a4bedf91b72cc2cd97ea0d74b47dad2f8f6b72d722a7452d
ExcludeArch: %{ix86}
Name:           ocaml-ppx-cold
Version:        0.17.0
Release:        1%{?dist}
Summary:        OCaml definition of [@@cold] attribute
License:        MIT
URL:            https://github.com/janestreet/ppx_cold
VCS:            git:%{url}.git
Source0:        https://github.com/janestreet/ppx_cold/archive/v%{version}/ppx_cold-%{version}.tar.gz
# oreon:deps
BuildRequires:  ocaml
BuildRequires:  ocaml-base-devel
BuildRequires:  ocaml-dune
BuildRequires:  ocaml-ppxlib-devel
# /oreon:deps
%description
Ppx_cold translates `[@@cold]` attributes to:

`[@@inline never] [@@local never] [@@specialise never]`

See the discussion in https://github.com/ocaml/ocaml/issues/8563.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       ocaml-base-devel%{?_isa}
Requires:       ocaml-ppxlib-devel%{?_isa}
%description    devel
The %{name}-devel package contains libraries and signature files for
developing applications that use %{name}.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%global oreon_srcdir ppx_cold-%{version}
%oreon_prep
%build

%dune_build
%install
%dune_install
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*

%check

%dune_check
%files -f %{oreon_filedir}/main.list
%files -n ocaml-ppx-cold-devel -f %{oreon_filedir}/ocaml-ppx-cold-devel.list

%changelog

%autochangelog
