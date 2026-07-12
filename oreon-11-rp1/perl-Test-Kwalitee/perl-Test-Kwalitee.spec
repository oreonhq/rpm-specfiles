%global source0_hash b4536cdd755b59772232d4325da7bd4fb7f5be50b4585dbbaf758eec306243a3

Name:		perl-Test-Kwalitee
Version:	1.28
Release:	20%{?dist}
Summary:	Test the Kwalitee of a distribution before you release it
License:	GPL-1.0-or-later OR Artistic-1.0-Perl
URL:		http://metacpan.org/module/Test::Kwalitee
Source0:	https://cpan.metacpan.org/modules/by-module/Test/Test-Kwalitee-%{version}.tar.gz
BuildArch:	noarch
# Build
BuildRequires:	coreutils
BuildRequires:	make
BuildRequires:	perl-generators
BuildRequires:	perl-interpreter
BuildRequires:	perl(ExtUtils::MakeMaker) >= 6.76
# Module
BuildRequires:	perl(Cwd)
BuildRequires:	perl(Exporter)
BuildRequires:	perl(Module::CPANTS::Analyse) >= 0.92
BuildRequires:	perl(parent)
BuildRequires:	perl(strict)
BuildRequires:	perl(Test::Builder) >= 0.88
BuildRequires:	perl(warnings)
# Test Suite
BuildRequires:	perl(CPAN::Meta) >= 2.120900
BuildRequires:	perl(CPAN::Meta::Check) >= 0.011
BuildRequires:	perl(File::Spec)
BuildRequires:	perl(File::Temp)
BuildRequires:	perl(lib)
BuildRequires:	perl(Scalar::Util)
BuildRequires:	perl(Test::Deep)
BuildRequires:	perl(Test::More) >= 0.96
BuildRequires:	perl(Test::Tester) >= 0.108
BuildRequires:	perl(Test::Warnings) >= 0.009
# Dependencies
# (none)

Provides:       perl(Test::Kwalitee)
%description
Kwalitee is an automatically-measurable gauge of how good your software
is. That's very different from quality, which a computer really can't
measure in a general sense (if you can, you've solved a hard problem in
computer science).

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%setup -q -n Test-Kwalitee-%{version}

%build
perl Makefile.PL INSTALLDIRS=vendor NO_PERLLOCAL=1 NO_PACKLIST=1
%make_build

%install
%make_install
%{_fixperms} -c %{buildroot}

%check
make test

%files
%license LICENSE
%doc Changes CONTRIBUTING README
%{_bindir}/kwalitee-metrics
%{perl_vendorlib}/Test/
%{_mandir}/man1/kwalitee-metrics.1*
%{_mandir}/man3/Test::Kwalitee.3*

%changelog
%autochangelog
