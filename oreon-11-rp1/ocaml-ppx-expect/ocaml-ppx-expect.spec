%global source0_hash 3027664caaa475e07e4dbcc9e67b6c7f8ddc86f2858f7c4fee89e964e0c9a7de
ExcludeArch: %{ix86}
%bcond test 0
Name:           ocaml-ppx-expect
Version:        0.17.3
Release:        1%{?dist}
Summary:        Framework for writing tests in OCaml
License:        MIT
URL:            https://github.com/janestreet/ppx_expect
VCS:            git:%{url}.git
Source0:        https://github.com/janestreet/ppx_expect/archive/v%{version}/ppx_expect-%{version}.tar.gz
%if %{with test}
%endif
# oreon:deps
BuildRequires:  ocaml
BuildRequires:  ocaml-base-devel
BuildRequires:  ocaml-dune
BuildRequires:  ocaml-ppx-here-devel
BuildRequires:  ocaml-ppx-inline-test-devel
BuildRequires:  ocaml-ppx-jane-devel
BuildRequires:  ocaml-ppxlib-devel
BuildRequires:  ocaml-stdio-devel
# /oreon:deps
%description
Ppx_expect is a framework for writing tests in OCaml, similar to Cram
(https://bitheap.org/cram/).  Ppx_expect mimics the existing inline tests
framework with the `let%%expect_test` construct.  The body of an expect-test
can contain output-generating code, interleaved with `%%expect` extension
expressions to denote the expected output.

When run, these tests will pass iff the output matches what was expected.  If
a test fails, a corrected file with the suffix ".corrected" will be produced
with the actual output, and the `inline_tests_runner` will output a diff.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       ocaml-base-devel%{?_isa}
Requires:       ocaml-ppx-here-devel%{?_isa}
Requires:       ocaml-ppx-inline-test-devel%{?_isa}
Requires:       ocaml-ppxlib-devel%{?_isa}
Requires:       ocaml-stdio-devel%{?_isa}
%description    devel
The %{name}-devel package contains libraries and signature files for
developing applications that use %{name}.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%global oreon_srcdir ppx_expect-%{version}
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
%files -n ocaml-ppx-expect-devel -f %{oreon_filedir}/ocaml-ppx-expect-devel.list

%changelog

%autochangelog
