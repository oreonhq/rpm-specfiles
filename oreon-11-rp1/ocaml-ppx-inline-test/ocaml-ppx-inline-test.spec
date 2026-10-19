%global source0_hash f77d12f2115e83f6b82929a7cec1a5602be47cf13a04a09e1ac2a9b68445e833
ExcludeArch: %{ix86}
%bcond test 0
Name:           ocaml-ppx-inline-test
Version:        0.17.1
Release:        1%{?dist}
Summary:        Syntax extension for writing inline tests in OCaml code
License:        MIT
URL:            https://github.com/janestreet/ppx_inline_test
VCS:            git:%{url}.git
Source0:        https://github.com/janestreet/ppx_inline_test/archive/v%{version}/ppx_inline_test-%{version}.tar.gz
%if %{with test}
%endif
# oreon:deps
BuildRequires:  ocaml
BuildRequires:  ocaml-base-devel
BuildRequires:  ocaml-dune
BuildRequires:  ocaml-ppx-jane-devel
BuildRequires:  ocaml-ppxlib-devel
BuildRequires:  ocaml-time-now-devel
# /oreon:deps
%description
Ppx_inline_test is a syntax extension for writing inline tests in OCaml code.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       ocaml-base-devel%{?_isa}
Requires:       ocaml-ppxlib-devel%{?_isa}
Requires:       ocaml-time-now-devel%{?_isa}
%description    devel
The %{name}-devel package contains libraries and signature files
for developing applications that use %{name}.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%global oreon_srcdir ppx_inline_test-%{version}
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
%files -n ocaml-ppx-inline-test-devel -f %{oreon_filedir}/ocaml-ppx-inline-test-devel.list

%changelog

%autochangelog
