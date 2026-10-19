%global source0_hash 3f3f64789ab25bb5cb7f5f907dd651dec9cc9440981822fe75df6b94344b7208
ExcludeArch: %{ix86}
%bcond test 0
%global giturl  https://github.com/janestreet/base
Name:           ocaml-base
Version:        0.17.3
Release:        1%{?dist}
Summary:        Jane Street standard library for OCaml
License:        MIT AND Apache-2.0
URL:            https://opensource.janestreet.com/base/
VCS:            git:%{giturl}.git
Source0:        %{giturl}/archive/v%{version}/base-%{version}.tar.gz
Patch:          %{name}-mathlib.patch
Patch:          %{name}-popcount.patch
%if %{with test}
%endif
# oreon:deps
BuildRequires:  ocaml
BuildRequires:  ocaml-core-devel
BuildRequires:  ocaml-dune
BuildRequires:  ocaml-dune-configurator-devel
BuildRequires:  ocaml-expect-test-helpers-core-devel
BuildRequires:  ocaml-intrinsics-kernel-devel
BuildRequires:  ocaml-num-devel
BuildRequires:  ocaml-ppx-jane-devel
BuildRequires:  ocaml-sexplib-devel
BuildRequires:  ocaml-sexplib0-devel
BuildRequires:  ocaml-stdio-devel
# /oreon:deps
%description
Base is a standard library for OCaml.  It provides a standard set of general
purpose modules that are well-tested, performant, and fully-portable across
any environment that can run OCaml code.  Unlike other standard library
projects, Base is meant to be used as a wholesale replacement of the standard
library distributed with the OCaml compiler.  In particular it makes different
choices and doesn't re-export features that are not fully portable such as
I/O, which are left to other libraries.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       ocaml-intrinsics-kernel-devel%{?_isa}
Requires:       ocaml-sexplib0-devel%{?_isa}
%description    devel
The %{name}-devel package contains libraries and signature files for
developing applications that use %{name}.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%global oreon_srcdir base-%{version}
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
%files -n ocaml-base-devel -f %{oreon_filedir}/ocaml-base-devel.list

%changelog

%autochangelog
