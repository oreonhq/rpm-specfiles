%global source0_hash adbc89ffbb758259e8ed18a9b99308ec853cac2f828a7c6530ce636d1056de3b

Name:           perl-Algorithm-Cron
Version:        0.10
Release:        31%{?dist}
Summary:        Abstract implementation of the cron(8) scheduling algorithm
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/Algorithm-Cron
Source0:        https://cpan.metacpan.org/authors/id/P/PE/PEVANS/Algorithm-Cron-%{version}.tar.gz
BuildArch:      noarch
BuildRequires:  perl-interpreter
BuildRequires:  perl-generators
BuildRequires:  perl(Module::Build)
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
# Run-time
BuildRequires:  perl(Carp)
BuildRequires:  perl(constant)
BuildRequires:  perl(POSIX)
BuildRequires:  perl(Time::timegm)
# Tests
BuildRequires:  perl(Test::Fatal)
BuildRequires:  perl(Test::More) >= 0.88

%description
Objects in this class implement a time scheduling algorithm such as used by
cron(8). Objects are stateless once constructed, and represent a single
schedule as defined by a crontab(5) entry. The object implements a method
next_time which returns an epoch timestamp value to indicate the next time
included in the crontab schedule.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n Algorithm-Cron-%{version}

%build
perl Build.PL installdirs=vendor
./Build

%install
./Build install destdir=$RPM_BUILD_ROOT create_packlist=0
%{_fixperms} $RPM_BUILD_ROOT/*

%check
./Build test

%files
%license LICENSE
%doc Changes README
%{perl_vendorlib}/*
%{_mandir}/man3/*

%changelog
%autochangelog
