%global source0_hash f11af57e97039c1d6717590353c77466789b612c78c7960c9448639b97d88508
Name:           perl-Schedule-Cron-Events
Version:        1.96
Release:        1%{?dist}
Summary:        Take a line from a crontab and find out when events will occur
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/Schedule-Cron-Events
Source0:        Schedule-Cron-Events-%{version}-noplx.tar.gz
BuildArch:      noarch
# oreon:deps
BuildRequires:  coreutils
BuildRequires:  make
BuildRequires:  perl(Carp)
BuildRequires:  perl(Data::Dumper)
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(File::Spec)
BuildRequires:  perl(Set::Crontab)
BuildRequires:  perl(Test)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(Time::Local)
BuildRequires:  perl(lib)
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
BuildRequires:  perl-devel
BuildRequires:  perl-generators
# /oreon:deps
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
%{_fixperms} $RPM_BUILD_ROOT/*
%oreon_autofiles main

%check

make test
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
