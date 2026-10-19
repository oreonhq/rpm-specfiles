%global source0_hash 9e290179fd1ab8574f7a2297baf015ea4fef3703a99d48798f61ec9347b4905b
Name:		perl-CPAN-Requirements-Dynamic
Version:	0.002
Release:        1%{?dist}
Summary:        Dynamic prerequisites in meta files
License:	GPL-1.0-or-later OR Artistic-1.0-Perl
URL:		https://metacpan.org/release/CPAN-Requirements-Dynamic
Source0:        https://cpan.metacpan.org/authors/id/L/LE/LEONT/CPAN-Requirements-Dynamic-%{version}.tar.gz
BuildArch:	noarch
Requires:	perl(CPAN::Meta::Prereqs)
Requires:	perl(CPAN::Meta::Requirements::Range)
Requires:	perl(ExtUtils::Config)
Requires:	perl(ExtUtils::HasCompiler)
Requires:	perl(IPC::Cmd)
Requires:	perl(Perl::OSType)
Provides:       perl(CPAN::Requirements::Dynamic)
# oreon:deps
BuildRequires:  coreutils
BuildRequires:  make
BuildRequires:  perl(:VERSION)
BuildRequires:  perl(CPAN::Meta::Prereqs)
BuildRequires:  perl(CPAN::Meta::Requirements::Range)
BuildRequires:  perl(Carp)
BuildRequires:  perl(Config)
BuildRequires:  perl(ExtUtils::Config)
BuildRequires:  perl(ExtUtils::HasCompiler)
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(IPC::Cmd)
BuildRequires:  perl(Parse::CPAN::Meta)
BuildRequires:  perl(Perl::OSType)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
# /oreon:deps
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
%oreon_autofiles main

%check

make test
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
