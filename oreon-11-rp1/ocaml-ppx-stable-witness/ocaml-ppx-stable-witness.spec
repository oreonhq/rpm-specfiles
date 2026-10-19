%global source0_hash 052db5d52ccacaab30ead1a4192ad021ee00c235a73c09b7918acabcee4a0cda
ExcludeArch: %{ix86}
%ifnarch %{ocaml_native_compiler}
%global debug_package %{nil}
%endif
Name:           ocaml-ppx-stable-witness
Version:        0.17.0
Release:        1%{?dist}
Summary:        Derive a witness that a type is intended to be stable
License:        MIT
URL:            https://github.com/janestreet/ppx_stable_witness
VCS:            git:%{url}.git
Source0:        https://github.com/janestreet/ppx_stable_witness/archive/v%{version}/ppx_stable_witness-%{version}.tar.gz
# oreon:deps
BuildRequires:  ocaml
BuildRequires:  ocaml-base-devel
BuildRequires:  ocaml-dune
BuildRequires:  ocaml-ppxlib-devel
# /oreon:deps
%description
Ppx_stable_witnesss is a ppx extension for deriving a witness that a type is
intended to be stable.  In this context, stable means that the serialization
format will never change.  This allows programs running at different versions
of the code to communicate safely.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       ocaml-base-devel%{?_isa}
Requires:       ocaml-ppxlib-devel%{?_isa}
%description    devel
The %{name}-devel package contains libraries and signature
files for developing applications that use %{name}.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%global oreon_srcdir ppx_stable_witness-%{version}
%oreon_prep
%build

%dune_build
%install
%dune_install
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*

%check

%dune_check
%files -f %{oreon_filedir}/main.list
%files -n ocaml-ppx-stable-witness-devel -f %{oreon_filedir}/ocaml-ppx-stable-witness-devel.list

%changelog

%autochangelog
