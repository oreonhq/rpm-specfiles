%global source0_hash 62df53d0da396aba8e96aee06d869a77b8cf54af2ebd9df885b7aef2d5a207b5

Name:           perl-Gtk2-Ex-Simple-List
Version:        0.50
Release:        51%{?dist}
Summary:        Simple interface to Gtk2's complex MVC list widget
License:        LGPL-2.1-or-later
URL:            https://metacpan.org/release/Gtk2-Ex-Simple-List
Source0:        https://cpan.metacpan.org/authors/id/R/RM/RMCFARLA/Gtk2-Perl-Ex/Gtk2-Ex-Simple-List-%{version}.tar.gz
BuildArch:      noarch

BuildRequires:  coreutils
BuildRequires:  make
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  perl(ExtUtils::MakeMaker) >= 6.76
BuildRequires:  perl(Glib::MakeHelper)
BuildRequires:  perl(Gtk2)
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
# Run-time
BuildRequires:  perl(Carp)
# Tests
BuildRequires:  perl(Gtk2::TestHelper)
BuildRequires:  perl(Test::More)

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

%check
make test

%files
%doc examples/ 
%{perl_vendorlib}/*
%{_mandir}/man3/*

%changelog
%autochangelog
