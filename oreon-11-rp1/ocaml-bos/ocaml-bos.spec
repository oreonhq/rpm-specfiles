%global source0_hash 089f369ed00967e92d89cc5fcd848c56bdab5c02737da4d483550bf56b5a79bc
ExcludeArch: %{ix86}
%ifnarch %{ocaml_native_compiler}
%global debug_package %{nil}
%endif
Name:           ocaml-bos
Version:        0.3.0
Release:        1%{?dist}
Summary:        Basic OS interaction for OCaml
License:        ISC
URL:            https://erratique.ch/software/bos
VCS:            git:https://erratique.ch/repos/bos.git
Source0:        https://erratique.ch/software/bos/releases/bos-%{version}.tbz
%global __ocaml_requires_opts -i Asttypes -i Build_path_prefix_map -i Cmi_format -i Env -i Format_doc -i Ident -i Identifiable -i Load_path -i Location -i Longident -i Misc -i Oprint -i Outcometree -i Parsetree -i Path -i Primitive -i Shape -i Subst -i Toploop -i Type_immediacy -i Types -i Unit_info -i Warnings
# oreon:deps
BuildRequires:  ocaml
BuildRequires:  ocaml-astring-devel
BuildRequires:  ocaml-compiler-libs
BuildRequires:  ocaml-findlib
BuildRequires:  ocaml-fmt-devel
BuildRequires:  ocaml-fpath-devel
BuildRequires:  ocaml-logs-devel
BuildRequires:  ocaml-mtime-devel
BuildRequires:  ocaml-ocamlbuild
BuildRequires:  ocaml-rpm-macros
BuildRequires:  ocaml-rresult-devel
BuildRequires:  ocaml-topkg-devel
# /oreon:deps
%description
Bos provides support for basic and robust interaction with the operating
system in OCaml.  It has functions to access the process environment, parse
command line arguments, interact with the file system and run command line
programs.  Bos works equally well on POSIX and Windows operating systems.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       ocaml-astring-devel%{?_isa}
Requires:       ocaml-fmt-devel%{?_isa}
Requires:       ocaml-fpath-devel%{?_isa}
Requires:       ocaml-logs-devel%{?_isa}
Requires:       ocaml-rresult-devel%{?_isa}
%description    devel
The %{name}-devel package contains libraries and signature files for
developing applications that use %{name}.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%global oreon_srcdir bos-%{version}
%oreon_prep
%build

ocaml pkg/pkg.ml build --dev-pkg false --tests true
%install
%ocaml_install
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*

%check

ocaml pkg/pkg.ml test
%files -f %{oreon_filedir}/main.list
%files -n ocaml-bos-devel -f %{oreon_filedir}/ocaml-bos-devel.list

%changelog

%autochangelog
