%global source0_hash 90f6e63bd1240a51d8b9b2f722059bd79ce00b5276bdd6238b8f5c613c0e7388

# OCaml packages not built on i686 since OCaml 5 / Fedora 39.
ExcludeArch: %{ix86}

%ifnarch %{ocaml_native_compiler}
%global debug_package %{nil}
%endif

Name:           ocaml-ounit
Version:        2.2.7
Release:        18%{?dist}
Summary:        Unit test framework for OCaml

License:        MIT
URL:            https://github.com/gildor478/ounit
VCS:            git:%{url}.git
Source0:        %{url}/releases/download/v%{version}/ounit-%{version}.tbz

# Remove seq and stdlib-shims downstream.  Not needed in Fedora.
Patch0001:      0001-Remove-stdlib-shims.patch

BuildRequires:  ocaml >= 4.04.0
BuildRequires:  ocaml-dune >= 3.0
BuildRequires:  ocaml-findlib
BuildRequires:  ocaml-lwt-devel >= 2.5.2

# The ounit name is now just an alias for ounit2
Provides:       %{name}2 = %{version}-%{release}

%description
OUnit is a unit test framework for OCaml.  It allows one to easily create
unit-tests for OCaml code.  It is loosely based on HUnit, a unit testing
framework for Haskell.  It is similar to JUnit, and other xUnit testing
frameworks.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
Provides:       %{name}2-devel = %{version}-%{release}

%description    devel
The %{name}-devel package contains libraries and signature files for
developing applications that use %{name}.

%package        lwt
Summary:        Helper functions for building Lwt tests using OUnit
Requires:       %{name}%{?_isa} = %{version}-%{release}
Provides:       %{name}2-lwt = %{version}-%{release}

%description    lwt
This package contains helper functions for building Lwt tests using
OUnit.

%package        lwt-devel
Summary:        Development files for %{name}-lwt
Requires:       %{name}-devel%{?_isa} = %{version}-%{release}
Requires:       %{name}-lwt%{?_isa} = %{version}-%{release}
Requires:       ocaml-lwt-devel%{?_isa}
Provides:       %{name}2-lwt-devel = %{version}-%{release}

%description    lwt-devel
The %{name}-lwt-devel package contains libraries and signature
files for developing applications that use %{name}-lwt.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n ounit-%{version} -p1

%build
%dune_build

%check
%dune_check

%install
%dune_install -s

%files -f .ofiles-ounit2
%doc CHANGES.md README.md
%license LICENSE.txt
%dir %{ocamldir}/ounit/
%{ocamldir}/ounit/META

%files devel -f .ofiles-ounit2-devel
%{ocamldir}/ounit/dune-package
%{ocamldir}/ounit/opam

%files lwt -f .ofiles-ounit2-lwt
%dir %{ocamldir}/ounit-lwt/
%{ocamldir}/ounit-lwt/META

%files lwt-devel -f .ofiles-ounit2-lwt-devel
%{ocamldir}/ounit-lwt/dune-package
%{ocamldir}/ounit-lwt/opam

%changelog
%autochangelog
