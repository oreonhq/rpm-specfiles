%global source0_hash 796d5791e2bf7b3bff200cf5057a7a1878439ebcd74ed0f1088cf86756d52be6
ExcludeArch: %{ix86}
%ifnarch %{ocaml_native_compiler}
%global debug_package %{nil}
%endif
%global giturl  https://github.com/gildor478/ocaml-fileutils
Name:           ocaml-fileutils
Version:        0.6.6
Release:        7%{?dist}
Summary:        OCaml library for common file and filename operations
License:        LGPL-2.1-or-later WITH OCaml-LGPL-linking-exception
URL:            https://gildor478.github.io/ocaml-fileutils/
VCS:            git:%{giturl}.git
Source0:        https://github.com/gildor478/ocaml-fileutils/releases/download/v0.6.6/fileutils-0.6.6.tbz
# oreon:deps
BuildRequires:  ocaml
BuildRequires:  ocaml-dune
# /oreon:deps
%description
This library is intended to provide a basic interface to the most
common file and filename operations.  It provides several different
filename functions: reduce, make_absolute, make_relative...  It also
enables you to manipulate real files: cp, mv, rm, touch...

It is separated into two modules: SysUtil and SysPath.  The first one
manipulates real files, the second one is made for manipulating
abstract filenames.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
%description    devel
The %{name}-devel package contains libraries and signature files for
developing applications that use %{name}.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%global oreon_srcdir fileutils-%{version}
%oreon_prep
%build

%dune_build
%install
%dune_install
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*

%files -f %{oreon_filedir}/main.list
%files -n ocaml-fileutils-devel -f %{oreon_filedir}/ocaml-fileutils-devel.list

%changelog

* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 0.6.6-7
- Prepare for Oreon 11 (RP1)
