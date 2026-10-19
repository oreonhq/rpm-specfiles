%global source0_hash 3eddd10895d7abe792bdfb3af39af169d4aaacc41b4a4e9a11250f60bcd6ebf0
Name:           ocaml-pprint
Version:        20230830
Release:        1%{?dist}
Summary:        A pretty-printing combinator library for OCaml
License:        LGPL-2.0-only WITH OCaml-LGPL-linking-exception
URL:            https://github.com/fpottier/pprint
Source0:        https://github.com/fpottier/pprint/archive/%{version}/pprint-%{version}.tar.gz
ExcludeArch:    %{ix86}
%ifnarch %{ocaml_native_compiler}
%global debug_package %{nil}
%endif
# oreon:deps
BuildRequires:  ocaml
BuildRequires:  ocaml-dune
# /oreon:deps
%description
PPrint is an OCaml library for pretty-printing textual documents.
It takes care of indentation and line breaks,
and is typically used to pretty-print code.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
%description    devel
The %{name}-devel package contains libraries and signature files for
developing applications that use %{name}.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%global oreon_srcdir pprint-%{version}
%oreon_prep
%build

%dune_build
%install
%dune_install
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*

%check

dune exec test/PPrintTest.exe
%files -f %{oreon_filedir}/main.list
%files -n ocaml-pprint-devel -f %{oreon_filedir}/ocaml-pprint-devel.list

%changelog

%autochangelog
