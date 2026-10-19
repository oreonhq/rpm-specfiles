%global source0_hash bbe76e8ecd9ccccfa631dbd21d6a801d23bd6fa982aae6839bb3fb7829a8cea1
Name:           ocaml-pcre2
Version:        8.0.4
Release:        1%{?dist}
Summary:        OCaml bindings to the pcre2 library
License:        LGPL-2.1-or-later WITH OCaml-LGPL-linking-exception
URL:            https://github.com/camlp5/pcre2-ocaml
VCS:            git:%{url}.git
Source0:        https://github.com/camlp5/pcre2-ocaml/archive/%{version}/pcre2-%{version}.tar.gz
ExcludeArch:    %{ix86}
# oreon:deps
BuildRequires:  ocaml
BuildRequires:  ocaml-dune
BuildRequires:  ocaml-dune-configurator-devel
BuildRequires:  ocaml-ounit-devel
BuildRequires:  pkgconfig(libpcre2-8)
# /oreon:deps
%description
This packages offers library functions for string pattern matching and
substitution, similar to the functionality offered by the Perl language.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       pcre2-devel%{?_isa}
%description    devel
The %{name}-devel package contains libraries and signature files for
developing applications that use %{name}.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n pcre2-ocaml-%{version}

%conf
# dune-compiledb functionality not needed for an RPM build
sed -i '/dune-compiledb/d' dune-project pcre2.opam

%build

%dune_build
%install
%dune_install
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*

%check

%dune_check
%files -f %{oreon_filedir}/main.list
%files -n ocaml-pcre2-devel -f %{oreon_filedir}/ocaml-pcre2-devel.list

%changelog

%autochangelog
