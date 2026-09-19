%global source0_hash d5f3cff8526e110a7bb6daa2f3313f04d4c6ce55555d5a8513353cc10c106398

Name:           perl-Task-Kensho-Exceptions
Version:        0.41
Release:        13%{?dist}
Summary:        A Glimpse at an Enlightened Perl (Exceptions)
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/Task-Kensho-Exceptions
Source0:        https://cpan.metacpan.org/authors/id/E/ET/ETHER/Task-Kensho-Exceptions-%{version}.tar.gz
BuildArch:      noarch
BuildRequires:  coreutils
BuildRequires:  make
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  perl(ExtUtils::MakeMaker) >= 6.76
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
# Run-time
# No run-time dependencies are needed for tests
# Test
BuildRequires:  perl(File::Spec)
BuildRequires:  perl(Test::More)
Requires:       perl(autodie)
Requires:       perl(Syntax::Keyword::Try)
Requires:       perl(Try::Tiny)

%description
Task::Kensho is a list of recommended modules for Enlightened Perl
development. CPAN is wonderful, but there are too many wheels and you have
to pick and choose amongst the various competing technologies.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n Task-Kensho-Exceptions-%{version}

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
