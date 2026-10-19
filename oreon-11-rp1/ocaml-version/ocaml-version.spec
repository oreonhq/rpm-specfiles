%global source0_hash 813e01f67a25dd4673158d39d9cf48d73c9261d8a41bf29172bc5b7a70c11746
ExcludeArch: %{ix86}
%ifnarch %{ocaml_native_compiler}
%global debug_package %{nil}
%endif
%global giturl  https://github.com/ocurrent/ocaml-version
Name:           ocaml-version
Version:        4.1.4
Release:        1%{?dist}
Summary:        Manipulate, parse and generate OCaml compiler version strings
License:        ISC
URL:            https://ocurrent.github.io/ocaml-version/
VCS:            git:%{giturl}.git
Source0:        %{giturl}/archive/v%{version}/%{name}-%{version}.tar.gz
# oreon:deps
BuildRequires:  ocaml
BuildRequires:  ocaml-alcotest-devel
BuildRequires:  ocaml-dune
# /oreon:deps
%description
This library provides facilities to parse version numbers of the OCaml
compiler, and enumerates the various official OCaml releases and configuration
variants.

OCaml version numbers are of the form `major.minor.patch+extra`, where the
`patch` and `extra` fields are optional.  This library offers the following
functionality:

- Functions to parse and serialize OCaml compiler version numbers
- Enumeration of official OCaml compiler version releases
- Test compiler versions for a particular feature (e.g. the `bytes` type)
- opam compiler switch enumeration

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
%description    devel
The %{name}-devel package contains libraries and signature files for
developing applications that use %{name}.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%oreon_prep
%build

%dune_build
%install
%dune_install
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*

%check

%dune_check
%files -f %{oreon_filedir}/main.list
%files -n ocaml-version-devel -f %{oreon_filedir}/ocaml-version-devel.list

%changelog

%autochangelog
