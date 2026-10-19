%global source0_hash fa04b6d15da976c2a87c84f850a9598f177ba50a68397cfebdf9c8314cb7a78d
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
# oreon:deps
BuildRequires:  ocaml
BuildRequires:  ocaml-dune
# /oreon:deps
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
%global oreon_srcdir %{name}-%{version}
%oreon_prep
%build

%dune_build
%install
%dune_install
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*

%check

%dune_check
%files -f %{oreon_filedir}/main.list
%files -n ocaml-benchmark-devel -f %{oreon_filedir}/ocaml-benchmark-devel.list

%changelog

%autochangelog
