%global source0_hash d0b7618fe9f324e536addbddf63fe323e84295755643744df08f3e3464619565

Name:           perl-POE-Component-DBIAgent
Version:        0.26
Release:        50%{?dist}
Summary:        POE Component for running asynchronous DBI calls
# Automatically converted from old format: GPL+ or Artistic - review is highly recommended.
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/POE-Component-DBIAgent
Source0:        https://cpan.metacpan.org/authors/id/R/RD/RDB/POE-Component-DBIAgent-%{version}.tar.gz
BuildArch:      noarch
# Build
BuildRequires:  make
BuildRequires:  perl-interpreter
BuildRequires:  perl-generators
BuildRequires:  perl(ExtUtils::MakeMaker) >= 6.76
# Runtime
BuildRequires:  perl(Carp)
BuildRequires:  perl(Class::MethodMaker)
BuildRequires:  perl(constant)
BuildRequires:  perl(Data::Dumper)
BuildRequires:  perl(DBI)
BuildRequires:  perl(POE) >= 0.17
BuildRequires:  perl(POE::Filter::Reference)
BuildRequires:  perl(POE::Session)
BuildRequires:  perl(POE::Wheel::Run)
BuildRequires:  perl(Storable)
BuildRequires:  perl(strict)
BuildRequires:  perl(Time::HiRes)
BuildRequires:  perl(vars)
# Tests only
Requires:       perl(POE) >= 0.17
Requires:       perl(Time::HiRes)

%global __requires_exclude %{?__requires_exclude:%__requires_exclude|}^perl\\(POE\\)$

%description
DBIAgent is your answer to non-blocking DBI in POE.

DBIAgent forks off a configurable number of helper processes for
running DBI queries.  The states that depend on the output of the
queries only get called when there is data for them to process.  No
more agonizing about query optimization in terms of milliseconds
because the rest of your program will suffer.  Leave that to the
operating system!  POE is designed for doing a lot of things
concurrently.  Waiting isn't doing, it's waiting... :-)

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n POE-Component-DBIAgent-%{version}

%build
perl Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1
make %{?_smp_mflags}

%install
make pure_install DESTDIR=%{buildroot}
%{_fixperms} %{buildroot}/*

%check
make test

%files
%doc Changes README
%{perl_vendorlib}/*
%{_mandir}/man3/*

%changelog
%autochangelog
