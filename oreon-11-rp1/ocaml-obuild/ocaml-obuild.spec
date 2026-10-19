%global source0_hash fc1decfd710acdc10db898b594bfbe7d1107f1cbef2aefebe9e1780e40ff23d4
ExcludeArch: %{ix86}
%global debug_package %{nil}
Name:           ocaml-obuild
Version:        0.3.0
Summary:        Simple package build system for OCaml
%forgemeta
Release:        1%{?dist}
License:        BSD-2-Clause
URL:            https://github.com/ocaml-obuild/obuild
VCS:            git:%{url}.git
Source0:        https://github.com/%{name}/obuild/archive/obuild-v%{version}.tar.gz
Patch0:         %{name}-partial.patch
Requires:       ocaml-findlib%{?_isa}
# oreon:deps
BuildRequires:  help2man
BuildRequires:  ocaml
BuildRequires:  ocaml-findlib
# /oreon:deps
%description
A parallel, incremental and declarative build system for OCaml.

The goal is to make a very simple build system for users and developers of
OCaml libraries and programs.

Obuild acts as a building black box: users only declare what they want to
build and with which sources; the build system will consistently build it.

The design is based on Haskell's Cabal and borrows most of the layout and
way of working, adapting parts where necessary to fully support OCaml.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%global oreon_srcdir obuild-obuild-v%{version}
%oreon_prep
%build

./bootstrap
%install
mkdir -p $RPM_BUILD_ROOT%{_bindir}
cp "dist/build/obuild/obuild" "dist/build/obuild-simple/obuild-simple" "$RPM_BUILD_ROOT%{_bindir}"
mkdir -p $RPM_BUILD_ROOT%{_mandir}/man1
help2man \
    --output "$RPM_BUILD_ROOT%{_mandir}/man1/obuild.1" \
    --name "parallel, incremental and declarative build system for OCaml" \
    --help-option "" \
    --no-discard-stderr \
    --no-info \
    dist/build/obuild/obuild
help2man \
    --output "$RPM_BUILD_ROOT%{_mandir}/man1/obuild-simple.1" \
    --name "simple package build system for OCaml" \
    --version-string " " \
    --no-discard-stderr \
    --no-info \
    dist/build/obuild-simple/obuild-simple
%oreon_autofiles main

%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
