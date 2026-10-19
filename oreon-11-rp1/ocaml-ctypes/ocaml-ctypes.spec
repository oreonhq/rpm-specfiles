%global source0_hash 249c5604c8554659761a7282db4ad200aa8c0fdc408cdb53102bd70feeb51955
ExcludeArch: %{ix86}
%global giturl  https://github.com/yallop/ocaml-ctypes
Name:           ocaml-ctypes
Version:        0.24.0
Release:        1%{?dist}
Summary:        Combinators for binding to C libraries without writing any C
License:        MIT
URL:            https://yallop.github.io/ocaml-ctypes/
VCS:            git:%{giturl}.git
Source0:        %{giturl}/archive/%{version}/%{name}-%{version}.tar.gz
Obsoletes:      %{name}-doc < 0.21.0
Provides:       %{name}-doc = %{version}-%{release}
%global __ocaml_requires_opts -i Asttypes -i Build_path_prefix_map -i Cmi_format -i Env -i Format_doc -i Ident -i Identifiable -i Load_path -i Location -i Longident -i Misc -i Oprint -i Outcometree -i Parsetree -i Path -i Primitive -i Shape -i Subst -i Toploop -i Type_immediacy -i Types -i Unit_info -i Warnings
# oreon:deps
BuildRequires:  ocaml
BuildRequires:  ocaml-bisect-ppx-devel
BuildRequires:  ocaml-dune
BuildRequires:  ocaml-dune-configurator-devel
BuildRequires:  ocaml-integers-devel
BuildRequires:  ocaml-lwt-devel
BuildRequires:  ocaml-ounit-devel
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(libffi)
BuildRequires:  pkgconfig(ncurses)
# /oreon:deps
%description
Ctypes is a library for binding to C libraries using pure OCaml.  The primary
aim is to make writing C extensions as straightforward as possible.

The core of ctypes is a set of combinators for describing the structure of C
types — numeric types, arrays, pointers, structs, unions and functions.  You
can use these combinators to describe the types of the functions that you want
to call, then bind directly to those functions — all without writing or
generating any C!

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       ocaml-integers-devel%{?_isa}
%description    devel
The %{name}-devel package contains libraries and signature files for
developing applications that use %{name}.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1

%conf
# Use Fedora flags
sed -i 's/ "-cclib"; "-Wl,--no-as-needed";//' src/ctypes-foreign/config/discover.ml

%build

%dune_build
%install
%dune_install
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*

%check

%dune_check
%files -f %{oreon_filedir}/main.list
%files -n ocaml-ctypes-devel -f %{oreon_filedir}/ocaml-ctypes-devel.list

%changelog

%autochangelog
