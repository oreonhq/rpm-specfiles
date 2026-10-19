%global source0_hash 2efe65a0210ed7bda8ddd9e076385b76619f23ac3aee1db5b6140ac1a1feb99d
ExcludeArch: %{ix86}
%ifnarch %{ocaml_native_compiler}
%global debug_package %{nil}
%endif
%bcond test 0
Name:           ocaml-ppx-optcomp
Version:        0.17.1
Release:        1%{?dist}
Summary:        Optional compilation for OCaml
License:        MIT
URL:            https://github.com/janestreet/ppx_optcomp
VCS:            git:%{url}.git
Source0:        https://github.com/janestreet/ppx_optcomp/archive/v%{version}/ppx_optcomp-%{version}.tar.gz
%if %{with test}
%endif
# oreon:deps
BuildRequires:  ocaml
BuildRequires:  ocaml-base-devel
BuildRequires:  ocaml-dune
BuildRequires:  ocaml-ppx-inline-test-devel
BuildRequires:  ocaml-ppxlib-devel
BuildRequires:  ocaml-stdio-devel
# /oreon:deps
%description
Ppx_optcomp provides optional compilation for OCaml.  It is a tool used to
handle optional compilations of pieces of code depending of the word size, the
version of the compiler, etc.  The syntax is based on OCaml item extension
nodes, with keywords similar to cpp.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       ocaml-base-devel%{?_isa}
Requires:       ocaml-ppxlib-devel%{?_isa}
Requires:       ocaml-stdio-devel%{?_isa}
%description    devel
The %{name}-devel package contains libraries and signature files for
developing applications that use %{name}.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%global oreon_srcdir ppx_optcomp-%{version}
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
%files -n ocaml-ppx-optcomp-devel -f %{oreon_filedir}/ocaml-ppx-optcomp-devel.list

%changelog

%autochangelog
