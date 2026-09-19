%global source0_hash 35a642662c349420d44be6e0ef7d8765ea743eb12ad14399aa3a232bb94e6e9a

Name:           perl-SQL-Abstract
Version:        2.000001
Release:        19%{?dist}
Summary:        Generate SQL from Perl data structures
# Automatically converted from old format: GPL+ or Artistic - review is highly recommended.
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/SQL-Abstract
Source0:        https://cpan.metacpan.org/modules/by-module/SQL/SQL-Abstract-%{version}.tar.gz
BuildArch:      noarch
BuildRequires:  make
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  perl(ExtUtils::MakeMaker) >= 6.76
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
# Run-time:
BuildRequires:  perl(base)
BuildRequires:  perl(Carp)
BuildRequires:  perl(constant)
BuildRequires:  perl(Data::Dumper::Concise)
%if !%{defined perl_bootstrap}
# DBIx::Class::Storage::Statistic used only with optional tests
BuildRequires:  perl(DBIx::Class::Storage::Statistics)
%endif
BuildRequires:  perl(Exporter) >= 5.57
BuildRequires:  perl(Hash::Merge) >= 0.12
BuildRequires:  perl(List::Util)
BuildRequires:  perl(Moo) >= 2.000001
BuildRequires:  perl(mro)
# MRO::Compat 0.12 not needed since perl 5.9
BuildRequires:  perl(Scalar::Util)
BuildRequires:  perl(Sub::Quote) >= 2.000001
BuildRequires:  perl(Test::Builder)
BuildRequires:  perl(Test::Builder::Module)
BuildRequires:  perl(Test::Deep) >= 0.101
BuildRequires:  perl(Text::Balanced) >= 2.00
# Optional run-time:
# Term::ANSIColor not usefull for tests
# Tests:
BuildRequires:  perl(overload)
BuildRequires:  perl(Storable)
BuildRequires:  perl(Test::Exception) >= 0.31
BuildRequires:  perl(Test::More) >= 0.92
BuildRequires:  perl(Test::Warn)
%if !%{defined perl_bootstrap}
# Optional tests:
BuildRequires:  perl(DBIx::Class) >= 0.08124
%endif
Requires:       perl(Data::Dumper)
Requires:       perl(Exporter) >= 5.57
Requires:       perl(Hash::Merge) >= 0.12
Requires:       perl(Moo) >= 2.000001
Requires:       perl(mro)
# MRO::Compat 0.12 not needed since perl 5.9
Requires:       perl(Sub::Quote) >= 2.000001
Requires:       perl(Test::Deep) >= 0.101
Requires:       perl(Text::Balanced) >= 2.00

%{?perl_default_filter}
# Remove under-speciefed dependencies
%global __requires_exclude %{?__requires_exclude:%__requires_exclude|}^perl\\((Exporter|Test::Deep)\\)$
%global __requires_exclude %__requires_exclude|^perl\\((Moo|Sub::Quote)\\)$

%description
%{summary}.

%package -n perl-DBIx-Class-Storage-Debug-PrettyPrint
Summary:        Pretty Printing DebugObj
# Automatically converted from old format: GPL+ or Artistic - review is highly recommended.
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
# Optional run-time:
# Term::ANSIColor

%description -n perl-DBIx-Class-Storage-Debug-PrettyPrint
%{summary}.

%package -n perl-DBIx-Class-SQLMaker-Role-SQLA2Passthrough
Summary:	A test of future possibilities
# Automatically converted from old format: GPL+ or Artistic - review is highly recommended.
License:	GPL-1.0-or-later OR Artistic-1.0-Perl

%description -n perl-DBIx-Class-SQLMaker-Role-SQLA2Passthrough
%{summary}.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n SQL-Abstract-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1
make

%install
make pure_install DESTDIR=$RPM_BUILD_ROOT
%{_fixperms} $RPM_BUILD_ROOT/*

%check
make test

%files
%doc Changes README
%license LICENSE
# %%{_bindir}/format-sql
%{perl_vendorlib}/SQL/
%{_mandir}/man3/DBIx::Class::SQLMaker::Role::SQLA2Passthrough.3pm*
%{_mandir}/man3/SQL::Abstract.3pm*
%{_mandir}/man3/SQL::Abstract::Plugin::BangOverrides.3pm*
%{_mandir}/man3/SQL::Abstract::Plugin::ExtraClauses.3pm*
%{_mandir}/man3/SQL::Abstract::Reference.3pm*
%{_mandir}/man3/SQL::Abstract::Role::Plugin.3pm*
%{_mandir}/man3/SQL::Abstract::Test.3pm*
%{_mandir}/man3/SQL::Abstract::Tree.3pm*

%files -n perl-DBIx-Class-Storage-Debug-PrettyPrint
%license LICENSE
%{perl_vendorlib}/DBIx/Class/Storage/
%{_mandir}/man3/DBIx::Class::Storage::Debug::PrettyPrint.3pm*

%files -n perl-DBIx-Class-SQLMaker-Role-SQLA2Passthrough
%license LICENSE
%{perl_vendorlib}/DBIx/Class/SQLMaker/
%{_mandir}/man3/DBIx::Class::SQLMaker::Role::SQLA2Passthrough.3pm*

%changelog
%autochangelog
