%global source0_hash 669a06f573024b5517abb1a89f0cc6eea4a217cb4f17de6cfe618001cbe7df20
ExcludeArch: %{ix86}
%ifnarch %{ocaml_native_compiler}
%global debug_package %{nil}
%endif
Name:           ocaml-ppx-deriving-yojson
Version:        3.10.0
Release:        1%{?dist}
Summary:        JSON codec generator for OCaml
License:        MIT
URL:            https://github.com/ocaml-ppx/ppx_deriving_yojson
VCS:            git:%{url}.git
Source0:        https://github.com/ocaml-ppx/ppx_deriving_yojson/archive/v%{version}/ppx_deriving_yojson-%{version}.tar.gz
Patch:          %{url}/pull/164.patch
Patch:          %{url}/pull/165.patch
# oreon:deps
BuildRequires:  ocaml
BuildRequires:  ocaml-dune
BuildRequires:  ocaml-ounit-devel
BuildRequires:  ocaml-ppx-deriving-devel
BuildRequires:  ocaml-ppxlib-devel
BuildRequires:  ocaml-yojson-devel
# /oreon:deps
%description
Deriving_Yojson is a ppx_deriving plugin that generates JSON serializers and
deserializers that use the Yojson library from an OCaml type definition.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       ocaml-ppx-deriving-devel%{?_isa}
Requires:       ocaml-ppxlib-devel%{?_isa}
Requires:       ocaml-yojson-devel%{?_isa}
%description    devel
The %{name}-devel package contains libraries and signature
files for developing applications that use %{name}.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%global oreon_srcdir ppx_deriving_yojson-%{version}
%oreon_prep
%build

%dune_build
%install
%dune_install
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*

%check

%dune_check
%files -f %{oreon_filedir}/main.list
%files -n ocaml-ppx-deriving-yojson-devel -f %{oreon_filedir}/ocaml-ppx-deriving-yojson-devel.list

%changelog

%autochangelog
