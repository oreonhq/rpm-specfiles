%global source0_hash 4e2a4701b584b7fc27f8df33bb345b653a28d0733ecf5c66ee3cbbcff3fd1557
Name:           ocaml-afl-persistent
Version:        1.4
Release:        1%{?dist}
Summary:        Persistent-mode American Fuzzy Lop for OCaml
License:        MIT
URL:            https://github.com/stedolan/ocaml-afl-persistent
VCS:            git:%{url}.git
Source0:        https://github.com/stedolan/%{name}/archive/v%{version}/%{name}-%{version}.tar.gz
ExclusiveArch:  %{x86_64}
Requires:       american-fuzzy-lop
# oreon:deps
BuildRequires:  american-fuzzy-lop
BuildRequires:  ocaml
BuildRequires:  ocaml-dune
# /oreon:deps
%description
This package enables running the American Fuzzy Lop fuzzing tool in persistent
mode in OCaml projects.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
%description    devel
The %{name}-devel package contains libraries and signature
files for developing applications that use %{name}.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%oreon_prep
%build

./config.sh
%dune_build
%install
%dune_install
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*

%check

cd test
./test.sh
%files -f %{oreon_filedir}/main.list
%files -n ocaml-afl-persistent-devel -f %{oreon_filedir}/ocaml-afl-persistent-devel.list

%changelog

%autochangelog
