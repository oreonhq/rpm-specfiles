%global source0_hash 27ddeb2f60fbae50dc504e63e63cd5f012689084a76d5fdd4d1371d5341ff8db
ExcludeArch: %{ix86}
%bcond test 0
%global giturl  https://github.com/aantron/bisect_ppx
Name:           ocaml-bisect-ppx
Version:        2.8.3
Release:        1%{?dist}
Summary:        Code coverage for OCaml and Reason
License:        MIT AND BSD-3-Clause
URL:            https://aantron.github.io/bisect_ppx/
VCS:            git:%{giturl}.git
Source0:        %{giturl}/archive/%{version}/bisect_ppx-%{version}.tar.gz
Patch:          %{giturl}/pull/448.patch
Patch:          %{giturl}/commit/2d8dffbbfc0c431a37319d4d9a143836c9ec542e.patch
%if %{with test}
%endif
# oreon:deps
BuildRequires:  git-core
BuildRequires:  ocaml
BuildRequires:  ocaml-cmdliner-devel
BuildRequires:  ocaml-dune
BuildRequires:  ocaml-ppxlib-devel
BuildRequires:  ocamlformat
# /oreon:deps
%description
Bisect_ppx is a code coverage tool for OCaml.  It helps you test thoroughly by
showing which parts of your code are *not* tested.  It is a small preprocessor
that inserts instrumentation at places in your code, such as if-then-else and
match expressions.  After you run tests, Bisect_ppx gives a nice HTML report
showing which places were visited and which were missed.

Usage is simple — add package bisect_ppx when building tests, run your tests,
then run the Bisect_ppx report tool on the generated visitation files.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       ocaml-ppxlib-devel%{?_isa}
%description    devel
The %{name}-devel package contains libraries and signature files for
developing applications that use %{name}.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%global oreon_srcdir bisect_ppx-%{version}
%oreon_prep
%build

%dune_build
%install
%dune_install
mkdir -p %{buildroot}%{_mandir}/man1
_build/install/default/bin/bisect-ppx-report --help groff > \
  %{buildroot}%{_mandir}/man1/bisect-ppx-report.1
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*
%if %{with test}
%check

%dune_check
%endif
%files -f %{oreon_filedir}/main.list
%files -n ocaml-bisect-ppx-devel -f %{oreon_filedir}/ocaml-bisect-ppx-devel.list

%changelog

%autochangelog
