%global source0_hash 2ba6857f2991b7f69368e8db818b163d31cf5a367f15f5953bf8f01a77b3d4fc
ExcludeArch: %{ix86}
%ifnarch %{ocaml_native_compiler}
%global debug_package %{nil}
%endif
Name:          ocaml-ocamlbuild
Version:       0.16.1
Release:        1%{?dist}
Summary:        Build tool for OCaml libraries and programs
License:       LGPL-2.1-or-later WITH OCaml-LGPL-linking-exception
URL:           https://github.com/ocaml/ocamlbuild
VCS:           git:%{url}.git
Source0:        https://github.com/ocaml/ocamlbuild/archive/refs/tags/0.16.1.tar.gz#/ocamlbuild-0.16.1.tar.gz
Requires:      ncurses
Obsoletes:     %{name}-devel < 0.14.0-37
Provides:      %{name}-devel = %{version}-%{release}
# oreon:deps
BuildRequires:  asciidoc
BuildRequires:  make
BuildRequires:  ncurses
BuildRequires:  ocaml
BuildRequires:  ocaml-rpm-macros
BuildRequires:  python3-pygments
# /oreon:deps
%description
OCamlbuild is a build tool for building OCaml libraries and programs.

%package doc
Summary:       Documentation for %{name}
License:       CC0-1.0
BuildArch:     noarch
%description doc
This package contains the manual for %{name}.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%global oreon_srcdir ocamlbuild-%{version}
%oreon_prep
%build

make configure \
  OCAMLBUILD_PREFIX=%{_prefix} \
  OCAMLBUILD_BINDIR=%{_bindir} \
  OCAMLBUILD_LIBDIR=%{_libdir}/ocaml \
  OCAMLBUILD_MANDIR=%{_mandir} \
%ifarch %{ocaml_native_compiler}
  OCAML_NATIVE=true \
  OCAML_NATIVE_TOOLS=true
%else
  OCAML_NATIVE=false \
  OCAML_NATIVE_TOOLS=false
%endif
make \
%ifarch %{ocaml_native_compiler}
     OCAMLC="ocamlc.opt -g" \
     OCAMLOPT="ocamlopt.opt -g"
%else
     OCAMLC="ocamlc -g" \
     OCAMLOPT="ocamlopt -g"
%endif
asciidoc manual/manual.adoc
%install
%make_install CHECK_IF_PREINSTALLED=false
pushd $RPM_BUILD_ROOT/usr/bin
%ifarch %{ocaml_native_compiler}
ln -sf ocamlbuild.native ocamlbuild
%else
ln -sf ocamlbuild.byte ocamlbuild
%endif
popd
%ocaml_files -n
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%files -f %{oreon_filedir}/main.list
%files -n ocaml-ocamlbuild-doc -f %{oreon_filedir}/ocaml-ocamlbuild-doc.list

%changelog

* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 0.16.1-5
- Prepare for Oreon 11 (RP1)
