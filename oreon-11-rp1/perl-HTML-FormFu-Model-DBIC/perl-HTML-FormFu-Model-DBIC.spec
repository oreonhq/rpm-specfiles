%global source0_hash 7f68dd879418585d6df69d787bc0b56a7f329dccecac47cb993b866a723804de
Name:           perl-HTML-FormFu-Model-DBIC
Summary:        Integrate HTML::FormFu with DBIx::Class
Version:        2.03
Release:        25%{?dist}
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
Source0:        https://cpan.metacpan.org/authors/id/C/CF/CFRANKS/HTML-FormFu-Model-DBIC-%{version}.tar.gz
URL:            https://metacpan.org/release/HTML-FormFu-Model-DBIC
BuildArch:      noarch
Requires:       perl(DBIx::Class) >= 0.08108
Requires:       perl(HTML::FormFu::Constraint)
Requires:       perl(HTML::FormFu::Model) >= 2.00
%{?perl_default_filter}
%{?perl_default_subpackage_tests}
%global __requires_exclude %{?__requires_exclude:%__requires_exclude|}^perl\\(HTML::FormFu::Model\\)$
# oreon:deps
BuildRequires:  coreutils
BuildRequires:  findutils
BuildRequires:  make
BuildRequires:  perl(Carp)
BuildRequires:  perl(DBD::SQLite)
BuildRequires:  perl(DBI)
BuildRequires:  perl(DBIx::Class)
BuildRequires:  perl(DBIx::Class::ResultSet)
BuildRequires:  perl(DBIx::Class::Schema)
BuildRequires:  perl(DateTime)
BuildRequires:  perl(DateTime::Format::SQLite)
BuildRequires:  perl(Exporter)
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(HTML::FormFu)
BuildRequires:  perl(HTML::FormFu::Constraint)
BuildRequires:  perl(HTML::FormFu::Model)
BuildRequires:  perl(HTML::FormFu::Util)
BuildRequires:  perl(List::MoreUtils)
BuildRequires:  perl(List::Util)
BuildRequires:  perl(Locale::Maketext)
BuildRequires:  perl(Moose)
BuildRequires:  perl(MooseX::Attribute::Chained)
BuildRequires:  perl(Scalar::Util)
BuildRequires:  perl(Storable)
BuildRequires:  perl(Task::Weaken)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(base)
BuildRequires:  perl(lib)
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
# /oreon:deps
%description
Integrate your HTML::FormFu forms with a DBIx::Class model.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n HTML-FormFu-Model-DBIC-%{version}

%build

%{__perl} Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1
make %{?_smp_mflags}
%install
make pure_install DESTDIR=%{buildroot}
%{_fixperms} %{buildroot}/*
%oreon_autofiles main

%check

make test
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
