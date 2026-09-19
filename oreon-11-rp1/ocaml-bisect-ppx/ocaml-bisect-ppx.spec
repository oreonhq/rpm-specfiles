%global source0_hash 27ddeb2f60fbae50dc504e63e63cd5f012689084a76d5fdd4d1371d5341ff8db

# OCaml packages not built on i686 since OCaml 5 / Fedora 39.
ExcludeArch: %{ix86}

# Running the tests requires ocaml-ounit, which introduces a circular
# dependency (also involving ocaml-lwt).  The tests also require ocamlformat,
# introducing a second circular dependency.  Break the cycles with this
# conditional.
%bcond test 0

%global giturl  https://github.com/aantron/bisect_ppx

Name:           ocaml-bisect-ppx
Version:        2.8.3
Release:        20%{?dist}
Summary:        Code coverage for OCaml and Reason

# The project as a whole is MIT.
# The embedded copy of highlight.js is BSD-3-Clause.
License:        MIT AND BSD-3-Clause
URL:            https://aantron.github.io/bisect_ppx/
VCS:            git:%{giturl}.git
Source:         %{giturl}/archive/%{version}/bisect_ppx-%{version}.tar.gz
# Support ppxlib 0.36.0
Patch:          %{giturl}/pull/448.patch

# Support cmdliner 2.0
# https://github.com/aantron/bisect_ppx/commit/2d8dffbbfc0c431a37319d4d9a143836c9ec542e
Patch:          %{giturl}/commit/2d8dffbbfc0c431a37319d4d9a143836c9ec542e.patch

BuildRequires:  git-core
BuildRequires:  ocaml >= 4.03.0
BuildRequires:  ocaml-cmdliner-devel >= 1.0.0
BuildRequires:  ocaml-dune >= 2.7.0
BuildRequires:  ocaml-ppxlib-devel >= 0.28.0

%if %{with test}
BuildRequires:  ocamlformat
%endif

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

%autosetup -n bisect_ppx-%{version} -p1

%build
%dune_build

%install
%dune_install

# Install the man page
mkdir -p %{buildroot}%{_mandir}/man1
_build/install/default/bin/bisect-ppx-report --help groff > \
  %{buildroot}%{_mandir}/man1/bisect-ppx-report.1

%if %{with test}
%check
%dune_check
%endif

%files -f .ofiles
%doc doc/advanced.md doc/CHANGES README.md
%license LICENSE.md
%{_mandir}/man1/bisect-ppx-report.1*

%files devel -f .ofiles-devel

%changelog
%autochangelog
