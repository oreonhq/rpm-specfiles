%global source0_hash e32eb4c6f319ff74241da9e1b00032f990241347271baf3adb468faaaa616147
ExcludeArch: %{ix86}
%ifnarch %{ocaml_native_compiler}
%global debug_package %{nil}
%endif
%bcond test 0
Name:           ocaml-re
Version:        1.14.0
Release:        1%{?dist}
Summary:        A regular expression library for OCaml
License:        LGPL-2.1-or-later WITH OCaml-LGPL-linking-exception
URL:            https://github.com/ocaml/ocaml-re
VCS:            git:%{url}.git
Source0:        https://github.com/ocaml/%{name}/archive/%{version}/%{name}-%{version}.tar.gz
%if %{with test}
%endif
# oreon:deps
BuildRequires:  ocaml
BuildRequires:  ocaml-dune
BuildRequires:  ocaml-ounit-devel
# /oreon:deps
%description
A pure OCaml regular expression library. Supports Perl-style regular
expressions, Posix extended regular expressions, Emacs-style regular
expressions, and shell-style file globbing.  It is also possible to
build regular expressions by combining simpler regular expressions.
There is also a subset of the PCRE interface available in the Re.pcre
library.

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
%if %{with test}
%check

%dune_check
%endif
%files -f %{oreon_filedir}/main.list
%files -n ocaml-re-devel -f %{oreon_filedir}/ocaml-re-devel.list

%changelog

%autochangelog
