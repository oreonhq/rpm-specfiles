%global source0_hash 2c1a06235bf811813caac9eaa9daa71af758667cdf7b082cb59863220fcaeed1

Name:           perl-Time-ParseDate
Version:        2015.103
Release:        32%{?dist}
Summary:        Perl modules for parsing dates and times
# See https://fedoraproject.org/wiki/Licensing/TPDL
License:        TPDL AND LicenseRef-Fedora-Public-Domain
URL:            https://metacpan.org/release/Time-ParseDate

Source0:        https://cpan.metacpan.org/authors/id/M/MU/MUIR/modules/Time-ParseDate-%{version}.tar.gz
BuildArch:      noarch

Provides:       perl-Time-modules = %{version}-%{release}
Obsoletes:      perl-Time-modules <= 2013.0912-3

BuildRequires:  findutils
BuildRequires:  make
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  perl(ExtUtils::MakeMaker)
# Run-time:
BuildRequires:  perl(Carp)
BuildRequires:  perl(Exporter)
BuildRequires:  perl(integer)
BuildRequires:  perl(strict)
BuildRequires:  perl(vars)
# Testing
BuildRequires:  perl(POSIX)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(Time::Local)
BuildRequires:  perl(Time::Piece)
BuildRequires:  perl(warnings)
BuildRequires:  tzdata

%description
Time-ParseDate provides several Perl modules, including Time::CTime,
Time::DaysInMonth, Time::JulianDay, Time::ParseDate, and Time::Timezone.
These modules can be useful for parsing and manipulating dates and times.
There are numerous options to control what is recognized and what is not.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n Time-ParseDate-%{version}

%build
perl Makefile.PL INSTALLDIRS=vendor
%make_build

%install
make pure_install DESTDIR=$RPM_BUILD_ROOT

find $RPM_BUILD_ROOT -type f -name .packlist -delete

%{_fixperms} $RPM_BUILD_ROOT/*

%check
make test

%files
%doc Changes README
%{perl_vendorlib}/*
%{_mandir}/man3/*

%changelog
%autochangelog
