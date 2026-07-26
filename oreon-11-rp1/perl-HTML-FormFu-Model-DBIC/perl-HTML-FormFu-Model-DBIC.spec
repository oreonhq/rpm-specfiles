%global source0_hash 7f68dd879418585d6df69d787bc0b56a7f329dccecac47cb993b866a723804de

Name:           perl-HTML-FormFu-Model-DBIC
Summary:        Integrate HTML::FormFu with DBIx::Class
Version:        2.03
Release:        25%{?dist}
# Automatically converted from old format: GPL+ or Artistic - review is highly recommended.
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
Source0:        https://cpan.metacpan.org/authors/id/C/CF/CFRANKS/HTML-FormFu-Model-DBIC-%{version}.tar.gz
URL:            https://metacpan.org/release/HTML-FormFu-Model-DBIC
BuildArch:      noarch

BuildRequires:  coreutils
BuildRequires:  findutils
BuildRequires:  make
BuildRequires:  perl-interpreter
BuildRequires:  perl-generators
BuildRequires:  perl(ExtUtils::MakeMaker) >= 6.30
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
# Run-time:
BuildRequires:  perl(base)
BuildRequires:  perl(Carp)
BuildRequires:  perl(HTML::FormFu::Constraint)
# HTML::FormFu::Model version from Makefile.PL's HTML::FormFu declaration
BuildRequires:  perl(HTML::FormFu::Model) >= 2.00
BuildRequires:  perl(HTML::FormFu::Util)
BuildRequires:  perl(List::MoreUtils)
BuildRequires:  perl(List::Util)
BuildRequires:  perl(Moose)
BuildRequires:  perl(MooseX::Attribute::Chained)
BuildRequires:  perl(Scalar::Util)
BuildRequires:  perl(Storable)
BuildRequires:  perl(Task::Weaken)
# Tests:
BuildRequires:  perl(DateTime)
# DateTime::Format::SQLite needed by tests using SQLite via DBIx::Class
BuildRequires:  perl(DateTime::Format::SQLite)
# DBD::SQLite needed by connect('dbi:SQLite:…') in t/lib/DBICTestLib.pm
BuildRequires:  perl(DBD::SQLite)
BuildRequires:  perl(DBI)
BuildRequires:  perl(DBIx::Class) >= 0.08108
BuildRequires:  perl(DBIx::Class::ResultSet)
BuildRequires:  perl(DBIx::Class::Schema)
BuildRequires:  perl(Exporter)
BuildRequires:  perl(HTML::FormFu) >= 2.00
BuildRequires:  perl(lib)
BuildRequires:  perl(Locale::Maketext)
BuildRequires:  perl(Test::More)

# DBIx::Class is used nowhere by the installed code, but let's assume this
# package is not compatible with former DBIx::Class versions
Requires:       perl(DBIx::Class) >= 0.08108
Requires:       perl(HTML::FormFu::Constraint)
# HTML::FormFu::Model version from Makefile.PL's HTML::FormFu declaration
Requires:       perl(HTML::FormFu::Model) >= 2.00

%{?perl_default_filter}
%{?perl_default_subpackage_tests}

# Remove under-specifed dependency
%global __requires_exclude %{?__requires_exclude:%__requires_exclude|}^perl\\(HTML::FormFu::Model\\)$

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

%check
make test

%files
%doc Changes
%{perl_vendorlib}/*
%{_mandir}/man3/*.3*

%changelog
%autochangelog
