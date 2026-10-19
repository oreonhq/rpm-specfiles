%global source0_hash bdd7caf1e5e55e65e4ece96eeeb3e5894c195ca5a9a274ddc27ac50a321d5c75
ExclusiveArch: %{ocaml_native_compiler}
%global _smp_ncpus_max 1
Name: ocaml-cpdf
Version: 2.8.1
Release:        1%{?dist}
Summary:        OCaml library and command line tool for processing PDFs
License: AGPL-3.0-only and ISC and BSD-3-Clause and CC-BY-4.0 and Unicode-DFS-2015
URL: https://github.com/johnwhitington/cpdf-source
Source0:        https://github.com/johnwhitington/cpdf-source/archive/v%{version}/cpdf-source-%{version}.tar.gz
Patch0: patch.patch
Provides: bundled(ocaml-yojson)
Provides: bundled(ocaml-xmlm)
# oreon:deps
BuildRequires:  gcc
BuildRequires:  make
BuildRequires:  ocaml
BuildRequires:  ocaml-camlpdf-devel
BuildRequires:  ocaml-findlib
BuildRequires:  ocaml-ocamldoc
BuildRequires:  ocaml-rpm-macros
# /oreon:deps
%description
OCaml library and command line tool for processing PDFs, for example
merging and splitting, adding text, or compressing.

%package devel
Summary: Development files to %{name}
Requires: %{name}%{?_isa} = %{version}-%{release}
%description devel
The %{name}-devel package contains libraries and signature files for
developing applications that use %{name}.

%package -n cpdf
Summary: Command line tool for processing PDFs
%description -n cpdf
PDF command line tool for processing PDFs, for example merging and
splitting, adding text, or compressing.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%global oreon_srcdir cpdf-source-%{version}
%oreon_prep
%build

%make_build
%install
export OCAMLFIND_DESTDIR=%{buildroot}%{ocamldir}
mkdir -p $OCAMLFIND_DESTDIR/stublibs
%make_install
%ocaml_files
mkdir -p %{buildroot}%{_bindir}
cp -a cpdf %{buildroot}%{_bindir}
mkdir -p %{buildroot}%{_mandir}/man1
cp -a cpdf.1 %{buildroot}%{_mandir}/man1
%oreon_autofiles cpdf usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%check

./cpdf -create-pdf -o out.pdf
test -f out.pdf
%files -f %{oreon_filedir}/main.list
%files -n ocaml-cpdf-devel -f %{oreon_filedir}/ocaml-cpdf-devel.list
%files -n cpdf -f %{oreon_filedir}/cpdf.list

%changelog

%autochangelog
