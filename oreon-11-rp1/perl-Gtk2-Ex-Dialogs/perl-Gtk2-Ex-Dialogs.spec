%global source0_hash 69e853459a348170ed911e3c667d61f15b434fa87868b1a72a8379329670e7a5
Name:           perl-Gtk2-Ex-Dialogs
Version:        0.11
Release:        1%{?dist}
Summary:        Useful tools for GNOME2/GTK2 Perl GUI design
License:        LGPL-2.1-or-later
URL:            https://metacpan.org/release/Gtk2-Ex-Dialogs
Source0:        https://cpan.metacpan.org/authors/id/K/KC/KCK/Gtk2-Ex-Dialogs-%{version}.tar.gz
BuildArch:      noarch
Requires:       perl(File::Type) >= 0.22
Requires:       perl(Gtk2) >= 1.04
Requires:       perl(Gtk2::Ex::Utils) >= 0.08
%global __requires_exclude %{?__requires_exclude:%__requires_exclude|}^perl\\(File::Type|Gtk2::Ex::Utils\\)$
# oreon:deps
BuildRequires:  coreutils
BuildRequires:  make
BuildRequires:  perl(Carp)
BuildRequires:  perl(Cwd)
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(File::Basename)
BuildRequires:  perl(File::Type)
BuildRequires:  perl(Glib)
BuildRequires:  perl(Gtk2)
BuildRequires:  perl(Gtk2::Ex::Constants)
BuildRequires:  perl(Gtk2::Ex::Utils)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(constant)
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
# /oreon:deps
%description
This module provides a clean, simple, quick API to generate and use common
Gtk2 dialogs, either from within a full-blown Gtk2 application or as a one-off
deal inside a non-Gtk2 perl application.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n Gtk2-Ex-Dialogs-%{version}

%build

perl Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1 NO_PERLLOCAL=1
%{make_build}
%install
%{make_install}
%{_fixperms} %{buildroot}/*
%oreon_autofiles main

%check

make test
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
