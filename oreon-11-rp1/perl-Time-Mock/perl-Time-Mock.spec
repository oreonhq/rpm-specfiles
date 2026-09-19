%global source0_hash 9bd2f7436bd2bdd9b947d70939c62c425801cae3a4321cb864a8a2f4d1f3982f

Name:           perl-Time-Mock
Version:        0.0.2
Release:        37%{?dist}
Summary:        Replaces actual time with simulated time - alternative to Test::MockTime
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/Time-Mock
Source0:        https://cpan.metacpan.org/authors/id/E/EW/EWILHELM/Time-Mock-v%{version}.tar.gz

BuildArch:      noarch
BuildRequires:  perl-generators
BuildRequires:  perl(Date::Parse) >= 2.27
BuildRequires:  perl(Module::Build)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(Time::HiRes)
BuildRequires:  perl(Carp)
BuildRequires:  perl(strict), perl(version), perl(warnings)

Requires:       perl(Date::Parse) >= 2.27

%description
This is an alternative to Test::MockTime which enables test suites to 
test code at specific points in time. Test::MockTime is nice, but doesn't
allow you to accelerate the time step and doesn't deal with Time::HiRes or 
give you any way to change the time across forks.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n Time-Mock-v%{version}

%build
perl Build.PL installdirs=vendor
./Build

%install
./Build install destdir=$RPM_BUILD_ROOT create_packlist=0

%{_fixperms} $RPM_BUILD_ROOT/*

%check
./Build test

%files
%doc Changes README
%{perl_vendorlib}/*
%{_mandir}/man3/*

%changelog
%autochangelog
