%global source0_hash 35a642662c349420d44be6e0ef7d8765ea743eb12ad14399aa3a232bb94e6e9a
%{?!oreon_bootstrap:%global oreon_bootstrap %{nil}}
%oreon_bootstrap
Name:           perl-SQL-Abstract
Version:        2.000001
Release:        1%{?dist}
Summary:        Generate SQL from Perl data structures
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/SQL-Abstract
Source0:        https://cpan.metacpan.org/modules/by-module/SQL/SQL-Abstract-%{version}.tar.gz
BuildArch:      noarch
%if !%{defined perl_bootstrap}
%endif
%if !%{defined perl_bootstrap}
%endif
Requires:       perl(Data::Dumper)
Requires:       perl(Exporter) >= 5.57
Requires:       perl(Hash::Merge) >= 0.12
Requires:       perl(Moo) >= 2.000001
Requires:       perl(mro)
Requires:       perl(Sub::Quote) >= 2.000001
Requires:       perl(Test::Deep) >= 0.101
Requires:       perl(Text::Balanced) >= 2.00
%{?perl_default_filter}
%global __requires_exclude %{?__requires_exclude:%__requires_exclude|}^perl\\((Exporter|Test::Deep)\\)$
%global __requires_exclude %__requires_exclude|^perl\\((Moo|Sub::Quote)\\)$
# oreon:deps
BuildRequires:  make
BuildRequires:  perl(Carp)
BuildRequires:  perl(DBIx::Class)
BuildRequires:  perl(DBIx::Class::Storage::Statistics)
BuildRequires:  perl(Data::Dumper::Concise)
BuildRequires:  perl(Exporter)
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(Hash::Merge)
BuildRequires:  perl(List::Util)
BuildRequires:  perl(Moo)
BuildRequires:  perl(Scalar::Util)
BuildRequires:  perl(Storable)
BuildRequires:  perl(Sub::Quote)
BuildRequires:  perl(Test::Builder)
BuildRequires:  perl(Test::Builder::Module)
BuildRequires:  perl(Test::Deep)
BuildRequires:  perl(Test::Exception)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(Test::Warn)
BuildRequires:  perl(Text::Balanced)
BuildRequires:  perl(base)
BuildRequires:  perl(constant)
BuildRequires:  perl(mro)
BuildRequires:  perl(overload)
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
# /oreon:deps
%description
%{summary}.

%package -n perl-DBIx-Class-Storage-Debug-PrettyPrint
Summary:        Pretty Printing DebugObj
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
%description -n perl-DBIx-Class-Storage-Debug-PrettyPrint
%{summary}.

%package -n perl-DBIx-Class-SQLMaker-Role-SQLA2Passthrough
Summary:	A test of future possibilities
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
%oreon_autofiles perl-DBIx-Class-Storage-Debug-PrettyPrint usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles perl-DBIx-Class-SQLMaker-Role-SQLA2Passthrough usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%check

make test
%files -f %{oreon_filedir}/main.list
%files -n perl-DBIx-Class-Storage-Debug-PrettyPrint -f %{oreon_filedir}/perl-DBIx-Class-Storage-Debug-PrettyPrint.list
%files -n perl-DBIx-Class-SQLMaker-Role-SQLA2Passthrough -f %{oreon_filedir}/perl-DBIx-Class-SQLMaker-Role-SQLA2Passthrough.list

%changelog

%autochangelog
