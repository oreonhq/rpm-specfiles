%global source0_hash cd17a33f58d903f7e4c26493cdaccf042b3ee029252ad6963bd83d4f5263bed3
ExcludeArch: %{ix86}
%global giturl  https://gitlab.com/irill/camlbz2
Name:           ocaml-camlbz2
Version:        0.8.0
Release:        1%{?dist}
Summary:        OCaml bindings for bzip2
License:        LGPL-3.0-or-later WITH OCaml-LGPL-linking-exception
URL:            https://irill.gitlab.io/camlbz2
VCS:            git:%{giturl}.git
Source0:        %{giturl}/-/archive/%{version}/camlbz2-%{version}.tar.gz
Patch:          %{name}-io-h.patch
Patch:          %{name}-shims.patch
# oreon:deps
BuildRequires:  ocaml
BuildRequires:  ocaml-dune
BuildRequires:  pkgconfig(bzip2)
# /oreon:deps
%description
This package contains OCaml bindings for bzip2.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       bzip2-devel%{?_isa}
%description    devel
The %{name}-devel package contains libraries and signature files for
developing applications that use %{name}.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n camlbz2-%{version} -p1

%conf
# Fix the version number
sed -i 's/0\.7\.1/%{version}/' dune-project

# Make sure we don't use the bundled copy of io.h
rm src/io.h

%build

%dune_build
%install
%dune_install
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*

%check

%dune_check
%files -f %{oreon_filedir}/main.list
%files -n ocaml-camlbz2-devel -f %{oreon_filedir}/ocaml-camlbz2-devel.list

%changelog

%autochangelog
