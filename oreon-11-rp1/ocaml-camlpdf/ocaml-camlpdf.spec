%global source0_hash 1885549dbb2e243b12d1b3752f443efc460400283ce318ec56fbe2f438a57ac8
ExclusiveArch: %{ocaml_native_compiler}
%global _smp_ncpus_max 1
Name: ocaml-camlpdf
Version: 2.9.2
Release:        1%{?dist}
Summary:        OCaml library for reading, writing and modifying PDFs
License: LGPL-2.1-or-later WITH OCaml-LGPL-linking-exception and LicenseRef-Fedora-Public-Domain and BSD-3-Clause and MIT and Unlicense and APAFML
URL: https://github.com/johnwhitington/camlpdf
Source0:        https://github.com/johnwhitington/camlpdf/archive/v%{version}/camlpdf-%{version}.tar.gz
Patch0: patch.patch
Provides: bundled(sha2.c)
Provides: bundled(rijndael-alg-fst.c) = 3.0
Provides: bundled(miniz) = 2.1.0
# oreon:deps
BuildRequires:  gcc
BuildRequires:  make
BuildRequires:  ocaml
BuildRequires:  ocaml-findlib
BuildRequires:  ocaml-ocamldoc
BuildRequires:  ocaml-rpm-macros
# /oreon:deps
%description
OCaml library for reading, writing and modifying PDFs. The basis of the Cpdf
command line tools.

%package devel
Summary: Development files to %{name}
Requires: %{name}%{?_isa} = %{version}-%{release}
%description devel
The %{name}-devel package contains libraries and signature files for
developing applications that use %{name}.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%global oreon_srcdir camlpdf-%{version}
%oreon_prep
%build

%make_build
%install
export OCAMLFIND_DESTDIR=%{buildroot}%{ocamldir}
mkdir -p $OCAMLFIND_DESTDIR/stublibs
%make_install
%ocaml_files
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*

%check

cd examples
ocamlopt -I .. ../*.cmxa pdfhello.ml
./a.out
test -f hello.pdf
cd ..
%files -f %{oreon_filedir}/main.list
%files -n ocaml-camlpdf-devel -f %{oreon_filedir}/ocaml-camlpdf-devel.list

%changelog

%autochangelog
