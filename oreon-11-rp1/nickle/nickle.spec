%global source0_hash 0b68a2f3e123f27c32b971029658abaae00b4c3ae6e79c3f2c18c5dbbfe554d3
%bcond_with docs
%if ! %{defined conf}
%global conf %nil
%endif
Name:           nickle
Version:        2.108
Release:        1%{?dist}
Summary:        A programming language-based prototyping environment
License:        MIT
URL:            https://nickle.org
Source0:        https://nickle.org/release/nickle-%{version}.tar.xz
%if %{with docs}
%endif
# oreon:deps
BuildRequires:  bc
BuildRequires:  bison
BuildRequires:  flex
BuildRequires:  gcc
BuildRequires:  gmp-devel
BuildRequires:  meson
BuildRequires:  ncurses-devel
BuildRequires:  readline-devel
# /oreon:deps
%description
Nickle is a programming language based prototyping environment with
powerful programming and scripting capabilities. Nickle supports a
variety of datatypes, especially arbitrary precision numbers. The
programming language vaguely resembles C. Some things in C which do
not translate easily are different, some design choices have been made
differently, and a very few features are simply missing.

Nickle provides the functionality of UNIX bc, dc and expr in
much-improved form. It is also an ideal environment for prototyping
complex algorithms. Nickle's scripting capabilities make it a nice
replacement for spreadsheets in some applications, and its numeric
features nicely complement the limited numeric functionality of
text-oriented languages such as AWK and PERL.

%package devel
Summary:  Include files for Nickle
Requires: %{name}%{?_isa} = %{version}-%{release}
%description devel
Include files for Nickle, used for building external FFI (foreign
function interface) libraries (e.g. the Cairo interface for Nickle).

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1

%conf
%meson

%build

%meson_build
%check

%meson_test
%install
%meson_install
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*

%files -f %{oreon_filedir}/main.list
%files -n nickle-devel -f %{oreon_filedir}/nickle-devel.list

%changelog

%autochangelog
