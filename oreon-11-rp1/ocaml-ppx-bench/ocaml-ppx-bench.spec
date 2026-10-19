%global source0_hash e5c120bf63446bff8bc87e9613160e53d54d4fd3c2e27ad5551812bc62e99b8d
Name:           ocaml-ppx-bench
Version:        113.33.03
Release:        1%{?dist}
Summary:        Syntax extension for writing inline benchmarks in OCaml code
License:        MIT
URL:            https://github.com/janestreet/ppx_bench
VCS:            git:%{url}.git
Source0:        https://github.com/janestreet/ppx_bench/archive/v%{version}/ppx_bench-%{version}.tar.gz
ExcludeArch:    %{ix86}
# oreon:deps
BuildRequires:  ocaml
BuildRequires:  ocaml-dune
BuildRequires:  ocaml-ppx-inline-test-devel
BuildRequires:  ocaml-ppxlib-devel
# /oreon:deps
%description
Ppx_bench is an OCaml syntax extension for writing inline benchmarks in OCaml
code.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       ocaml-ppx-inline-test-devel%{?_isa}
Requires:       ocaml-ppxlib-devel%{?_isa}
%description    devel
The %{name}-devel package contains libraries and signature files for
developing applications that use %{name}.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%global oreon_srcdir ppx_bench-%{version}
%oreon_prep
%build

%dune_build
%install
%dune_install
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*

%check

%dune_check
%files -f %{oreon_filedir}/main.list
%files -n ocaml-ppx-bench-devel -f %{oreon_filedir}/ocaml-ppx-bench-devel.list

%changelog

%autochangelog
