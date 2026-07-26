%global source0_hash fa04b6d15da976c2a87c84f850a9598f177ba50a68397cfebdf9c8314cb7a78d

# OCaml packages not built on i686 since OCaml 5 / Fedora 39.
ExcludeArch: %{ix86}

%ifnarch %{ocaml_native_compiler}
%global debug_package %{nil}
%endif

%global giturl  https://github.com/Chris00/ocaml-benchmark

Name:           ocaml-benchmark
Version:        1.7
Release:        5%{?dist}
Summary:        Benchmarking module for OCaml

License:        LGPL-3.0-only WITH OCaml-LGPL-linking-exception
URL:            https://chris00.github.io/ocaml-benchmark/doc/
VCS:            git:%{giturl}.git
Source0:        %{giturl}/archive/v%{version}/%{name}-%{version}.tar.gz

BuildRequires:  ocaml
BuildRequires:  ocaml-dune

%description
Benchmark provides functions to measure and compare the run-time of functions.
It is inspired by the Perl module of the same name.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    devel
The %{name}-devel package contains libraries and signature files for
developing applications that use %{name}.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n %{name}-%{version}

%build
%dune_build

%install
%dune_install

%check
%dune_check

%files -f .ofiles
%doc README.md CHANGES.md
%license LICENSE.md

%files devel -f .ofiles-devel
%doc README.md CHANGES.md
%license LICENSE.md

%changelog
%autochangelog
