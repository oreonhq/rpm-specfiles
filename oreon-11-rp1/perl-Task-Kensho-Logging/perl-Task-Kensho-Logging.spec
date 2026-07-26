%global source0_hash aa7b96eaeed3999899b2f6cbcca56e8d34380e76423c0dd795df18a831120c3d

Name:           perl-Task-Kensho-Logging
Version:        0.41
Release:        13%{?dist}
Summary:        A Glimpse at an Enlightened Perl (Logging)
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/Task-Kensho-Logging
Source0:        https://cpan.metacpan.org/authors/id/E/ET/ETHER/Task-Kensho-Logging-%{version}.tar.gz
BuildArch:      noarch
BuildRequires:  coreutils
BuildRequires:  make
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  perl(ExtUtils::MakeMaker) >= 6.76
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
# Run-time
BuildRequires:  perl(Log::Any)
BuildRequires:  perl(Log::Contextual)
BuildRequires:  perl(Log::Dispatch)
BuildRequires:  perl(Log::Log4perl)
# Tests
BuildRequires:  perl(File::Spec)
BuildRequires:  perl(Test::More)
Requires:       perl(Log::Any)
Requires:       perl(Log::Contextual)
Requires:       perl(Log::Dispatch)
Requires:       perl(Log::Log4perl)

%description
Task::Kensho is a list of recommended modules for Enlightened Perl
development. CPAN is wonderful, but there are too many wheels and you have
to pick and choose amongst the various competing technologies.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n Task-Kensho-Logging-%{version}

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
