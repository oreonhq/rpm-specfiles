%global source0_hash b4536cdd755b59772232d4325da7bd4fb7f5be50b4585dbbaf758eec306243a3
Name:		perl-Test-Kwalitee
Version:	1.28
Release:        1%{?dist}
Summary:        Test the Kwalitee of a distribution before you release it
License:	GPL-1.0-or-later OR Artistic-1.0-Perl
URL:		http://metacpan.org/module/Test::Kwalitee
Source0:        https://cpan.metacpan.org/modules/by-module/Test/Test-Kwalitee-%{version}.tar.gz
BuildArch:	noarch
Provides:       perl(Test::Kwalitee)
# oreon:deps
BuildRequires:  coreutils
BuildRequires:  make
BuildRequires:  perl(CPAN::Meta)
BuildRequires:  perl(CPAN::Meta::Check)
BuildRequires:  perl(Cwd)
BuildRequires:  perl(Exporter)
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(File::Spec)
BuildRequires:  perl(File::Temp)
BuildRequires:  perl(Module::CPANTS::Analyse)
BuildRequires:  perl(Scalar::Util)
BuildRequires:  perl(Test::Builder)
BuildRequires:  perl(Test::Deep)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(Test::Tester)
BuildRequires:  perl(Test::Warnings)
BuildRequires:  perl(lib)
BuildRequires:  perl(parent)
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
# /oreon:deps
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
%oreon_autofiles main

%check

make test
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
