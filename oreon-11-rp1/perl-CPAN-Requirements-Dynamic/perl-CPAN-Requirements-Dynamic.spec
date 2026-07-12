%global source0_hash 9e290179fd1ab8574f7a2297baf015ea4fef3703a99d48798f61ec9347b4905b

Name:		perl-CPAN-Requirements-Dynamic
Version:	0.002
Release:	3%{?dist}
Summary:	Dynamic prerequisites in meta files
License:	GPL-1.0-or-later OR Artistic-1.0-Perl
URL:		https://metacpan.org/release/CPAN-Requirements-Dynamic
Source0:	https://cpan.metacpan.org/modules/by-module/CPAN/CPAN-Requirements-Dynamic-%{version}.tar.gz
BuildArch:	noarch
# Build
BuildRequires:	coreutils
BuildRequires:	make
BuildRequires:	perl-generators
BuildRequires:	perl-interpreter
BuildRequires:	perl(:VERSION) >= 5.6
BuildRequires:	perl(ExtUtils::MakeMaker) >= 6.76
# Module
BuildRequires:	perl(Carp)
BuildRequires:	perl(CPAN::Meta::Prereqs)
BuildRequires:	perl(CPAN::Meta::Requirements::Range)
BuildRequires:	perl(ExtUtils::Config)
BuildRequires:	perl(ExtUtils::HasCompiler)
BuildRequires:	perl(IPC::Cmd)
BuildRequires:	perl(Parse::CPAN::Meta)
BuildRequires:	perl(Perl::OSType)
BuildRequires:	perl(strict)
BuildRequires:	perl(warnings)
# Test Suite
BuildRequires:	perl(Config)
BuildRequires:	perl(Test::More) >= 0.88
# Dependencies
Requires:	perl(CPAN::Meta::Prereqs)
Requires:	perl(CPAN::Meta::Requirements::Range)
Requires:	perl(ExtUtils::Config)
Requires:	perl(ExtUtils::HasCompiler)
Requires:	perl(IPC::Cmd)
Requires:	perl(Perl::OSType)

Provides:       perl(CPAN::Requirements::Dynamic)
%description
This module implements a format for describing dynamic prerequisites of
a distribution.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%setup -q -n CPAN-Requirements-Dynamic-%{version}

%build
perl Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1 NO_PERLLOCAL=1
%{make_build}

%install
%{make_install}
%{_fixperms} -c %{buildroot}

%check
make test

%files
%license LICENSE
%doc Changes README
%{perl_vendorlib}/CPAN/
%{_mandir}/man3/CPAN::Requirements::Dynamic.3*

%changelog
%autochangelog
