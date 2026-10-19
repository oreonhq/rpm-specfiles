%global source0_hash 62df53d0da396aba8e96aee06d869a77b8cf54af2ebd9df885b7aef2d5a207b5
Name:           perl-Gtk2-Ex-Simple-List
Version:        0.50
Release:        1%{?dist}
Summary:        Simple interface to Gtk2's complex MVC list widget
License:        LGPL-2.1-or-later
URL:            https://metacpan.org/release/Gtk2-Ex-Simple-List
Source0:        https://cpan.metacpan.org/authors/id/R/RM/RMCFARLA/Gtk2-Perl-Ex/Gtk2-Ex-Simple-List-%{version}.tar.gz
BuildArch:      noarch
# oreon:deps
BuildRequires:  coreutils
BuildRequires:  make
BuildRequires:  perl(Carp)
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(Glib::MakeHelper)
BuildRequires:  perl(Gtk2)
BuildRequires:  perl(Gtk2::TestHelper)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
# /oreon:deps
%description
Gtk2 has a powerful, but complex MVC (Model, View, Controller) system used
to implement list and tree widgets. Gtk2::Ex::Simple::List automates the
complex setup work and allows you to treat the list model as a more natural
list of lists structure.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n Gtk2-Ex-Simple-List-%{version}

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
