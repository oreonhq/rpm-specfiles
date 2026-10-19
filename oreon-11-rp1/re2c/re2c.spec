%global source0_hash 75bf2696445e831d0d44e0d9f2909eeffc18c09757f222b2fb025f7e59fe130b
Summary:        Tool for generating C, C++, and go recognizers from regular expressions
Name: re2c
Version: 4.6
Release:        1%{?dist}
License: LicenseRef-Public-Domain
URL: https://re2c.org/
Source0:        https://github.com/skvadrik/re2c/releases/download/%{version}/re2c-%{version}.tar.xz
# oreon:deps
BuildRequires:  gcc
BuildRequires:  gcc-c++
BuildRequires:  make
BuildRequires:  python3
# /oreon:deps
%description
re2c is a tool for writing very fast and very flexible scanners. Unlike any
other such tool, re2c focuses on generating high efficient code for regular
expression matching. As a result this allows a much broader range of use than
any traditional lexer offers. And Last but not least re2c generates warning
free code that is equal to hand-written code in terms of size, speed and
quality.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%setup -q

%build

%configure --disable-silent-rules
%make_build
%install
%make_install
%oreon_autofiles main

%check

make tests
%files -f %{oreon_filedir}/main.list

%changelog

* Mon May 25 2026 Oreon Packaging Team <packaging@oreonhq.com> - 3.1-6
- Import
%{_bindir}/re2d
%{_bindir}/re2hs
%{_bindir}/re2js
%{_bindir}/re2ocaml
%{_bindir}/re2py
%{_bindir}/re2swift
%{_bindir}/re2v
%{_bindir}/re2zig
%{_mandir}/man1/re2d.1.gz
%{_mandir}/man1/re2hs.1.gz
%{_mandir}/man1/re2js.1.gz
%{_mandir}/man1/re2ocaml.1.gz
%{_mandir}/man1/re2py.1.gz
%{_mandir}/man1/re2swift.1.gz
%{_mandir}/man1/re2v.1.gz
%{_mandir}/man1/re2zig.1.gz
