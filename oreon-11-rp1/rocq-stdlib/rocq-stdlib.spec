%global source0_hash 2d66421c52ed32719a15cb039c368e063c4d85f670e3d142f5eb7415fb427985
%global debug_package %{nil}
%global stdlibdir %{ocamldir}/coq/user-contrib/Stdlib
%global rocqver   9.1.1
%global giturl    https://github.com/rocq-prover/stdlib
Name:           rocq-stdlib
Version:        9.2.0
Release:        1%{?dist}
Summary:        The Rocq proof assistant standard library
License:        LGPL-2.1-only
URL:            https://rocq-prover.org/
VCS:            git:%{giturl}.git
Source0:        %{giturl}/archive/V%{version}/%{name}-%{version}.tar.gz
ExclusiveArch:  %{ocaml_native_compiler}
Requires:       rocq-core%{?_isa} = %{rocqver}
%global _desc %{expand:Rocq is a formal proof management system.  It provides a formal language
to write mathematical definitions, executable algorithms and theorems together
with an environment for semi-interactive development of machine-checked proofs.}
# oreon:deps
BuildRequires:  coq-core-compat
BuildRequires:  ocaml
BuildRequires:  ocaml-dune
BuildRequires:  ocaml-findlib
BuildRequires:  rocq
# /oreon:deps
%description
%_desc

This package includes the Rocq Standard Library, that is to say, the set of
modules usually bound to the Stdlib.* namespace.

%package        source
Summary:        Source files of the Rocq proof assistant standard library
Requires:       %{name}%{?_isa} = %{version}-%{release}
%description    source
%_desc

This package contains the source Rocq files for the standard library.  These
files are not needed to use the standard library.  They are made available for
informational purposes.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%global oreon_srcdir stdlib-%{version}
%oreon_prep
%build

%dune_build -p rocq-stdlib
%install
%dune_install -n rocq-stdlib
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%files -f %{oreon_filedir}/main.list
%files -n rocq-stdlib-source -f %{oreon_filedir}/rocq-stdlib-source.list

%changelog

%autochangelog
