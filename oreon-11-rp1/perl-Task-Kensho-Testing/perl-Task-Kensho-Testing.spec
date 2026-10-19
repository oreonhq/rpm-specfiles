%global source0_hash 8dabdcd3f99ef5657cdddeaa043f85bd59444bf988292859a034ba0333d7e591
Name:           perl-Task-Kensho-Testing
Version:        0.41
Release:        13%{?dist}
Summary:        A Glimpse at an Enlightened Perl (Testing)
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/Task-Kensho-Testing
Source0:        https://cpan.metacpan.org/authors/id/E/ET/ETHER/Task-Kensho-Testing-%{version}.tar.gz
BuildArch:      noarch
Requires:       perl(Devel::Cover)
Requires:       perl(Test::Deep)
Requires:       perl(Test::Fatal)
Requires:       perl(Test::Memory::Cycle)
Requires:       perl(Test::Pod)
Requires:       perl(Test::Pod::Coverage)
Requires:       perl(Test::Requires)
Requires:       perl(Test::Simple)
Requires:       perl(Test::Warnings)
Requires:       perl(Test2::Suite)
%{?perl_default_filter}
# oreon:deps
BuildRequires:  coreutils
BuildRequires:  make
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(File::Spec)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
# /oreon:deps
%description
Task::Kensho is a list of recommended modules for Enlightened Perl
development. CPAN is wonderful, but there are too many wheels and you have
to pick and choose amongst the various competing technologies.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n Task-Kensho-Testing-%{version}

%build

perl Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1 NO_PERLLOCAL=1
%{make_build}
%install
%{make_install}
%{_fixperms} %{buildroot}/*
%oreon_autofiles main

%check

make test
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
