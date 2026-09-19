%global source0_hash 3d019aa0bb6f890f82cdbeb878416ddd02507ca272868dad16c3c6f78f6098d8

# OCaml packages not built on i686 since OCaml 5 / Fedora 39.
ExcludeArch: %{ix86}

%ifnarch %{ocaml_native_compiler}
%global debug_package %{nil}
%endif

%global giturl  https://github.com/c-cube/qcheck

Name:           ocaml-qcheck
Version:        0.91
Release:        2%{?dist}
Summary:        QuickCheck inspired property-based testing for OCaml

License:        BSD-2-Clause
URL:            https://c-cube.github.io/qcheck/
VCS:            git:%{giturl}.git
Source:         %{giturl}/archive/v%{version}/%{name}-%{version}.tar.gz
# Expose a dependency on the math library so RPM can see it
Patch:          %{name}-mathlib.patch

BuildRequires:  asciidoc
BuildRequires:  ocaml >= 4.08.0
BuildRequires:  ocaml-dune >= 2.8.0
BuildRequires:  ocaml-alcotest-devel >= 1.4.0
BuildRequires:  ocaml-ounit-devel
BuildRequires:  ocaml-ppxlib-devel >= 0.36.0
BuildRequires:  ocaml-ppx-deriving-devel >= 6.1.0
BuildRequires:  python3-pygments

Requires:       %{name}-core%{?_isa} = %{version}-%{release}
Requires:       %{name}-ounit%{?_isa} = %{version}-%{release}

%global _desc %{expand:Qcheck enables checking invariants (properties of a type) over randomly
generated instances of the type.  It provides combinators for generating
instances and printing them.}

%description
%_desc

This package is a compatibility wrapper for qcheck.  New code should use
either %{name}-alcotest or %{name}-ounit.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       %{name}-core-devel%{?_isa} = %{version}-%{release}
Requires:       %{name}-ounit-devel%{?_isa} = %{version}-%{release}

%description    devel
%_desc

The %{name}-devel package contains libraries and signature files for
developing applications that use the qcheck compatibility wrapper.  New code
should instead use %{name}-alcotest-devel or %{name}-ounit-devel.

%package        core
Summary:        QuickCheck inspired property-based testing for OCaml

%description    core
%_desc

This package provides the common code for alcotest.

%package        core-devel
Summary:        Development files for %{name}-core
Requires:       %{name}-core%{?_isa} = %{version}-%{release}

%description    core-devel
%_desc

The %{name}-core-devel package contains libraries and signature files
for developing applications that use %{name}-core.

%package        ounit
Summary:        OUnit support for %{name}
Requires:       %{name}-core%{?_isa} = %{version}-%{release}

%description    ounit
%_desc

This package provides ounit support for qcheck.

%package        ounit-devel
Summary:        Development files for %{name}-ounit
Requires:       %{name}-ounit%{?_isa} = %{version}-%{release}
Requires:       %{name}-core-devel%{?_isa} = %{version}-%{release}
Requires:       ocaml-ounit-devel%{?_isa}

%description    ounit-devel
%_desc

The %{name}-ounit-devel package contains libraries and signature files
for developing applications that use %{name}-ounit.

%package        alcotest
Summary:        Alcotest support for %{name}
Requires:       %{name}-core%{?_isa} = %{version}-%{release}

%description    alcotest
%_desc

This package provides alcotest support for qcheck.

%package        alcotest-devel
Summary:        Development files for %{name}-alcotest
Requires:       %{name}-alcotest%{?_isa} = %{version}-%{release}
Requires:       %{name}-core-devel%{?_isa} = %{version}-%{release}
Requires:       ocaml-alcotest-devel%{?_isa}

%description    alcotest-devel
%_desc

The %{name}-alcotest-devel package contains libraries and signature files
for developing applications that use %{name}-alcotest.

%package     -n ocaml-ppx-deriving-qcheck
Summary:        PPX deriver for QCheck
Requires:       %{name}-core%{?_isa} = %{version}-%{release}

%description  -n ocaml-ppx-deriving-qcheck
%_desc

This package provides a PPX deriver for QCheck.

%package     -n ocaml-ppx-deriving-qcheck-devel
Summary:        Development files for ocaml-ppx-deriving-qcheck
Requires:       %{name}-core-devel%{?_isa} = %{version}-%{release}
Requires:       ocaml-ppxlib-devel%{?_isa}

%description -n ocaml-ppx-deriving-qcheck-devel
%_desc

The ocaml-ppx-deriving-qcheck-devel package contains libraries and signature
files for developing applications that use ocaml-ppx-deriving-qcheck.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n qcheck-%{version} -p1

%build
%dune_build
asciidoc README.adoc

%install
%dune_install -s

%check
%dune_check

%files -f .ofiles-qcheck
%doc README.html CHANGELOG.md
%license LICENSE

%files devel -f .ofiles-qcheck-devel
%doc README.html CHANGELOG.md
%license LICENSE

%files core -f .ofiles-qcheck-core

%files core-devel -f .ofiles-qcheck-core-devel

%files ounit -f .ofiles-qcheck-ounit

%files ounit-devel -f .ofiles-qcheck-ounit-devel

%files alcotest -f .ofiles-qcheck-alcotest

%files alcotest-devel -f .ofiles-qcheck-alcotest-devel

%files -n ocaml-ppx-deriving-qcheck -f .ofiles-ppx_deriving_qcheck

%files -n ocaml-ppx-deriving-qcheck-devel -f .ofiles-ppx_deriving_qcheck-devel

%changelog
%autochangelog
