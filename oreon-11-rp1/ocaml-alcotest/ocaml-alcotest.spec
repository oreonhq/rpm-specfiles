%global source0_hash 9659376cc5434220bcbc8fe8649588208eeb32126f6b9cc7d649c35f653627fa
ExcludeArch: %{ix86}
%bcond async 0
%global srcname alcotest
%global giturl  https://github.com/mirage/alcotest
Name:           ocaml-%{srcname}
Version:        1.9.1
Release:        1%{?dist}
Summary:        Lightweight and colorful test framework for OCaml
License:        ISC
URL:            https://mirage.github.io/alcotest/
VCS:            git:%{giturl}.git
Source0:        %{giturl}/archive/%{version}/%{srcname}-%{version}.tar.gz
Patch:          0001-Drop-the-stdlib-shims-subpackage.patch
%if %{with async}
%endif
# oreon:deps
BuildRequires:  ocaml
BuildRequires:  ocaml-astring-devel
BuildRequires:  ocaml-cmdliner-devel
BuildRequires:  ocaml-dune
BuildRequires:  ocaml-fmt-devel
BuildRequires:  ocaml-re-devel
BuildRequires:  ocaml-uutf-devel
# /oreon:deps
%description
Alcotest is a lightweight and colorful test framework.

Alcotest exposes a simple interface to perform unit tests, including a
simple `TESTABLE` module type, a `check` function to assert test
predicates, and a `run` function to perform a list of `unit -> unit`
test callbacks.

Alcotest provides quiet and colorful output where only faulty runs are
fully displayed at the end of the run (with the full logs ready to
inspect), with a simple (yet expressive) query language to select the
tests to run.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       ocaml-astring-devel%{?_isa}
Requires:       ocaml-cmdliner-devel%{?_isa}
Requires:       ocaml-fmt-devel%{?_isa}
Requires:       ocaml-re-devel%{?_isa}
Requires:       ocaml-uutf-devel%{?_isa}
%if %{with async}
Requires:       ocaml-async-devel
Requires:       ocaml-lwt-devel
%endif
%description    devel
The %{name}-devel package contains libraries and signature files for
developing applications that use %{name}.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n %{srcname}-%{version} -p1

%build

%dune_build %{!?with_async:-p alcotest}
%install
%dune_install %{!?with_async:alcotest}
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*

%check

%dune_check %{!?with_async:-p alcotest}
%files -f %{oreon_filedir}/main.list
%files -n ocaml-alcotest-devel -f %{oreon_filedir}/ocaml-alcotest-devel.list

%changelog

%autochangelog
