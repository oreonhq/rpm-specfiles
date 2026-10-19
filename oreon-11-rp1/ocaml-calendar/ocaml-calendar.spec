%global source0_hash ea04d31762d3f18837af0311cdbfe7b7788aa0f2e7e9f98d2b0decec1e506e9e
ExcludeArch: %{ix86}
%ifnarch %{ocaml_native_compiler}
%global debug_package %{nil}
%endif
%bcond tests %[!0%{?rhel}]
%global giturl  https://github.com/ocaml-community/calendar
Name:           ocaml-calendar
Epoch:          1
Version:        3.0.0
Release:        1%{?dist}
Summary:        Objective Caml library for managing dates and times
License:        LGPL-2.1-or-later WITH OCaml-LGPL-linking-exception
URL:            https://ocaml-community.github.io/calendar/
VCS:            git:%{giturl}.git
Source0:        https://github.com/ocaml-community/calendar/archive/refs/tags/v3.0.0.tar.gz#/calendar-3.0.0.tar.gz
Patch:          %{name}-timezone-test.patch
%if %{with tests}
%endif
# oreon:deps
BuildRequires:  ocaml
BuildRequires:  ocaml-alcotest-devel
BuildRequires:  ocaml-dune
BuildRequires:  ocaml-re-devel
# /oreon:deps
%description
Objective Caml library for managing dates and times.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{epoch}:%{version}-%{release}
%description    devel
The %{name}-devel package contains libraries and signature files for
developing applications that use %{name}.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%global oreon_srcdir calendar-%{version}
%oreon_prep
%build

%dune_build
%install
%dune_install
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*
%if %{with tests}
%check

%dune_check
%endif
%files -f %{oreon_filedir}/main.list
%files -n ocaml-calendar-devel -f %{oreon_filedir}/ocaml-calendar-devel.list

%changelog

* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 3.0.0-21
- Prepare for Oreon 11 (RP1)
