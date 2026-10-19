%global source0_hash 3d019aa0bb6f890f82cdbeb878416ddd02507ca272868dad16c3c6f78f6098d8
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
Source0:        %{giturl}/archive/v%{version}/%{name}-%{version}.tar.gz
Patch:          %{name}-mathlib.patch
Requires:       %{name}-core%{?_isa} = %{version}-%{release}
Requires:       %{name}-ounit%{?_isa} = %{version}-%{release}
%global _desc %{expand:Qcheck enables checking invariants (properties of a type) over randomly
generated instances of the type.  It provides combinators for generating
instances and printing them.}
# oreon:deps
BuildRequires:  asciidoc
BuildRequires:  ocaml
BuildRequires:  ocaml-alcotest-devel
BuildRequires:  ocaml-dune
BuildRequires:  ocaml-ounit-devel
BuildRequires:  ocaml-ppx-deriving-devel
BuildRequires:  ocaml-ppxlib-devel
BuildRequires:  python3-pygments
# /oreon:deps
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
%global oreon_srcdir qcheck-%{version}
%oreon_prep
%build

%dune_build
asciidoc README.adoc
%install
%dune_install -s
%oreon_autofiles ocaml-ppx-deriving-qcheck usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles ocaml-ppx-deriving-qcheck-devel usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*

%check

%dune_check
%files -f %{oreon_filedir}/main.list
%files -n ocaml-qcheck-devel -f %{oreon_filedir}/ocaml-qcheck-devel.list
%files -n ocaml-qcheck-core -f %{oreon_filedir}/ocaml-qcheck-core.list
%files -n ocaml-qcheck-core-devel -f %{oreon_filedir}/ocaml-qcheck-core-devel.list
%files -n ocaml-qcheck-ounit -f %{oreon_filedir}/ocaml-qcheck-ounit.list
%files -n ocaml-qcheck-ounit-devel -f %{oreon_filedir}/ocaml-qcheck-ounit-devel.list
%files -n ocaml-qcheck-alcotest -f %{oreon_filedir}/ocaml-qcheck-alcotest.list
%files -n ocaml-qcheck-alcotest-devel -f %{oreon_filedir}/ocaml-qcheck-alcotest-devel.list
%files -n ocaml-ppx-deriving-qcheck -f %{oreon_filedir}/ocaml-ppx-deriving-qcheck.list
%files -n ocaml-ppx-deriving-qcheck-devel -f %{oreon_filedir}/ocaml-ppx-deriving-qcheck-devel.list

%changelog

%autochangelog
