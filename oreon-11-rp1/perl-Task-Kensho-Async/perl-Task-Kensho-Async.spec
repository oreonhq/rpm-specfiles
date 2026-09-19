%global source0_hash ba912823b15c22e0b59b93c5d631ade37344f660d69c1226aecdd7828a40aeae

Name:           perl-Task-Kensho-Async
Version:        0.41
Release:        13%{?dist}
Summary:        Glimpse at an Enlightened Perl (Async Programming)
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/Task-Kensho-Async
Source0:        https://cpan.metacpan.org/authors/id/E/ET/ETHER/Task-Kensho-Async-%{version}.tar.gz
BuildArch:      noarch
# Build
BuildRequires:  coreutils
BuildRequires:  make
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  perl(ExtUtils::MakeMaker) >= 6.76
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
# Run-Time
BuildRequires:  perl(Future)
BuildRequires:  perl(IO::Async)
BuildRequires:  perl(MCE)
BuildRequires:  perl(Mojo::IOLoop)
BuildRequires:  perl(Parallel::ForkManager)
BuildRequires:  perl(POE)
# Tests
BuildRequires:  perl(File::Spec)
BuildRequires:  perl(Test::More)
Requires:       perl(Future)
Requires:       perl(IO::Async)
Requires:       perl(MCE)
Requires:       perl(Mojo::IOLoop)
Requires:       perl(Parallel::ForkManager)
Requires:       perl(POE)

%description
Task::Kensho is a list of recommended modules for Enlightened Perl
development. CPAN is wonderful, but there are too many wheels and you have
to pick and choose amongst the various competing technologies.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n Task-Kensho-Async-%{version}

%build
perl Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1 NO_PERLLOCAL=1
%{make_build}

%install
%{make_install}
%{_fixperms} %{buildroot}/*

%check
make test

%files
%license LICENCE
%doc Changes README
%{perl_vendorlib}/*
%{_mandir}/man3/*

%changelog
%autochangelog
