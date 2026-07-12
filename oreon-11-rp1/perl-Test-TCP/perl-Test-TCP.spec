%global source0_hash 3e53c3c06d6d0980a2bfeb915602b714e682ee211ae88c11748cf2cc714e7b57

Name:           perl-Test-TCP
Version:        2.22
Release:        19%{?dist}
Summary:        Testing TCP program
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/Test-TCP
Source0:        https://cpan.metacpan.org/authors/id/M/MI/MIYAGAWA/Test-TCP-%{version}.tar.gz
BuildArch:      noarch

BuildRequires:  %{__make}
BuildRequires:  %{__perl}

BuildRequires:  perl-interpreter >= 0:5.008001
BuildRequires:  perl-generators
BuildRequires:  perl(base)
BuildRequires:  perl(Carp)
BuildRequires:  perl(Config)
BuildRequires:  perl(Exporter)
BuildRequires:  perl(ExtUtils::MakeMaker) >= 6.64
BuildRequires:  perl(File::Temp)
BuildRequires:  perl(File::Which)
BuildRequires:  perl(IO::Socket::INET)
BuildRequires:  perl(IO::Socket::IP)
BuildRequires:  perl(POSIX)
BuildRequires:  perl(Socket)
BuildRequires:  perl(strict)
BuildRequires:  perl(Test::More) >= 0.98
BuildRequires:  perl(Test::SharedFork) >= 0.29
BuildRequires:  perl(Time::HiRes)
BuildRequires:  perl(warnings)


Provides:       perl(Test::TCP)
%description
Test::TCP is test utilities for TCP/IP program.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%setup -q -n Test-TCP-%{version}

# FIXME: Work around to inconsistency in Test-TCP-2.07
sed -i -e 's,use Test::SharedFork 0.12;,use Test::SharedFork 0.29;,' lib/Test/TCP.pm

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1 NO_PERLLOCAL=1
%{make_build}

%install
%{make_install}
%{_fixperms} $RPM_BUILD_ROOT/*

%check
%{__make} test

%files
%doc Changes README*
%{perl_vendorlib}/*
%{_mandir}/man3/*

%changelog
%autochangelog
