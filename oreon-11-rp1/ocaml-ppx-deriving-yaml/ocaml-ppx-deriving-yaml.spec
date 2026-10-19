%global source0_hash dc2bef3043aaff7237589e97e44ca8a6268c8ec859a0430f9362b82f1d25752a
ExcludeArch: %{ix86}
%ifnarch %{ocaml_native_compiler}
%global debug_package %{nil}
%endif
Name:           ocaml-ppx-deriving-yaml
Version:        0.4.1
Release:        1%{?dist}
Summary:        Derive conversion functions between OCaml types and YAML
License:        ISC
URL:            https://github.com/patricoferris/ppx_deriving_yaml
VCS:            git:%{url}.git
Source0:        https://github.com/patricoferris/ppx_deriving_yaml/releases/download/v%{version}/ppx_deriving_yaml-%{version}.tbz
# oreon:deps
BuildRequires:  ocaml
BuildRequires:  ocaml-alcotest-devel
BuildRequires:  ocaml-dune
BuildRequires:  ocaml-mdx-devel
BuildRequires:  ocaml-ppx-deriving-devel
BuildRequires:  ocaml-ppxlib-devel
BuildRequires:  ocaml-yaml-devel
# /oreon:deps
%description
This ppx is based on ppx_yojson [1] and ppx_deriving_yojson [2] because of the
many similarities between JSON and yaml.  In particular many of the ways OCaml
values are encoded to yaml types are the same as those implemented by the
Yojson ppx.

References:
[1] https://github.com/NathanReb/ppx_yojson
[2] https://github.com/ocaml-ppx/ppx_deriving_yojson

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       ocaml-ppx-deriving-devel%{?_isa}
Requires:       ocaml-ppxlib-devel%{?_isa}
Requires:       ocaml-yaml-devel%{?_isa}
%description    devel
The %{name}-devel package contains libraries and signature
files for developing applications that use %{name}.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%global oreon_srcdir ppx_deriving_yaml-%{version}
%oreon_prep
%build

%dune_build -p ppx_deriving_yaml
%install
%dune_install ppx_deriving_yaml
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*

%check

%dune_check -p ppx_deriving_yaml
%files -f %{oreon_filedir}/main.list
%files -n ocaml-ppx-deriving-yaml-devel -f %{oreon_filedir}/ocaml-ppx-deriving-yaml-devel.list

%changelog

%autochangelog
