%global source0_hash debd1345ac0116232390af64552d15948b5dc7200e287730235f7ff42098f3c5
Name:           ocaml-crowbar
Version:        0.2.2
Release:        1%{?dist}
Summary:        Code fuzzer for OCaml
License:        MIT
URL:            https://github.com/stedolan/crowbar
VCS:            git:%{url}.git
Source0:        https://github.com/stedolan/crowbar/archive/v%{version}/crowbar-%{version}.tar.gz
ExclusiveArch:  %{x86_64}
Requires:       american-fuzzy-lop
# oreon:deps
BuildRequires:  american-fuzzy-lop
BuildRequires:  ocaml
BuildRequires:  ocaml-afl-persistent-devel
BuildRequires:  ocaml-calendar-devel
BuildRequires:  ocaml-cmdliner-devel
BuildRequires:  ocaml-dune
BuildRequires:  ocaml-fpath-devel
BuildRequires:  ocaml-pprint-devel
BuildRequires:  ocaml-uucp-devel
BuildRequires:  ocaml-uunf-devel
BuildRequires:  ocaml-uutf-devel
# /oreon:deps
%description
Crowbar is a library for testing code, combining QuickCheck-style
property-based testing and the magical bug-finding powers of American Fuzzy
Lop.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       ocaml-afl-persistent-devel%{?_isa}
Requires:       ocaml-cmdliner-devel%{?_isa}
Requires:       ocaml-ocplib-endian-devel%{?_isa}
%description    devel
The %{name}-devel package contains libraries and signature
files for developing applications that use %{name}.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%global oreon_srcdir crowbar-%{version}
%oreon_prep
%build

%dune_build
%install
%dune_install
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*

%check

%dune_check
%files -f %{oreon_filedir}/main.list
%files -n ocaml-crowbar-devel -f %{oreon_filedir}/ocaml-crowbar-devel.list

%changelog

%autochangelog
