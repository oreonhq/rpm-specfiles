%global source0_hash f11af57e97039c1d6717590353c77466789b612c78c7960c9448639b97d88508

Name:           perl-Schedule-Cron-Events
Version:        1.96
Release:        17%{?dist}
Summary:        Take a line from a crontab and find out when events will occur
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/Schedule-Cron-Events
# http://www.cpan.org/modules/by-module/Schedule/Schedule-Cron-Events-%%{version}.tar.gz
# is the original upstream source. Unfortunately Schedule-Cron-Events includes the file
# cron_event_predict.plx - being not covered by any of the license statements inside of
# the upstream tarball. And per Fedora Legal, we have to remove this file once upstream
# has clarified the licensing of this file. Cleaning sources can be simply done using:
#   tar zxvf Schedule-Cron-Events-<version>.tar.gz
#   rm Schedule-Cron-Events-<version>/cron_event_predict.plx
#   comment out some lines in Schedule-Cron-Events-1.93/Makefile.PL
#   tar cvfz Schedule-Cron-Events-<version>-noplx.tar.gz Schedule-Cron-Events-<version>
Source0:        Schedule-Cron-Events-%{version}-noplx.tar.gz
BuildRequires:  coreutils
BuildRequires:  make
BuildRequires:  perl-devel
BuildRequires:  perl-generators
%if 0%{?rhel} && 0%{?rhel} <= 7
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  findutils
%else
BuildRequires:  perl(ExtUtils::MakeMaker) >= 6.76
%endif
# Run-time
BuildRequires:  perl(Carp)
BuildRequires:  perl(Set::Crontab)
BuildRequires:  perl(strict)
BuildRequires:  perl(Time::Local)
BuildRequires:  perl(warnings)
# Tests
BuildRequires:  perl(Data::Dumper)
BuildRequires:  perl(File::Spec)
BuildRequires:  perl(lib)
BuildRequires:  perl(Test)
BuildRequires:  perl(Test::More)
BuildArch:      noarch

%description
Given a line from a crontab, tells you the time at which cron will next run
the line, or when the last event occurred, relative to any date you choose.
The object keeps that reference date internally, and updates it when you
call nextEvent() or previousEvent() - such that successive calls will give
you a sequence of events going forward, or backwards, in time.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n Schedule-Cron-Events-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1 NO_PERLLOCAL=1
%{make_build}

%install
%{make_install}

%if 0%{?rhel} && 0%{?rhel} <= 7
find $RPM_BUILD_ROOT \( -name perllocal.pod -o -name .packlist \) -delete
find $RPM_BUILD_ROOT -depth -type d -exec rmdir {} 2>/dev/null \;
%endif

%{_fixperms} $RPM_BUILD_ROOT/*

%check
make test

%files
%doc README
%{perl_vendorlib}/*
%{_mandir}/man3/*

%changelog
%autochangelog
