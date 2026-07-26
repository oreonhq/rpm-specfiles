%global source0_hash 7168b46de737647fce719989259bbbdded33300f1504d50d0133da0307ed8ec1

Name:           perl-Task-Kensho-OOP
Version:        0.41
Release:        13%{?dist}
Summary:        A Glimpse at an Enlightened Perl (OOP)
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/Task-Kensho-OOP
Source0:        https://cpan.metacpan.org/authors/id/E/ET/ETHER/Task-Kensho-OOP-%{version}.tar.gz
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
# Tests
BuildRequires:  perl(File::Spec)
BuildRequires:  perl(Test::More)
Requires:       perl(Moo)
Requires:       perl(Moose)
Requires:       perl(MooseX::Aliases)
Requires:       perl(MooseX::Getopt)
Requires:       perl(MooseX::NonMoose)
Requires:       perl(MooseX::Role::Parameterized)
Requires:       perl(MooseX::SimpleConfig)
Requires:       perl(MooseX::StrictConstructor)
Requires:       perl(namespace::autoclean)
Requires:       perl(Package::Variant)
Requires:       perl(Type::Tiny)

%description
Task::Kensho is a list of recommended modules for Enlightened Perl
development. CPAN is wonderful, but there are too many wheels and you have
to pick and choose amongst the various competing technologies.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n Task-Kensho-OOP-%{version}

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
