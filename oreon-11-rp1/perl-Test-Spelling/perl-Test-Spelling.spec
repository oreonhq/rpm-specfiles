%global source0_hash 38c659f03a4d7362e16832a3489d17f86a2ea36471d335e17ce323457df5bc60
Name:           perl-Test-Spelling
Version:        0.25
Release:        20%{?dist}
Summary:        Check for spelling errors in POD files
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/Test-Spelling
Source0:        https://cpan.metacpan.org/modules/by-module/Test/Test-Spelling-%{version}.tar.gz
BuildArch:      noarch
Requires:       hunspell
Requires:       perl(Carp)
Provides:       perl(Test::Spelling)
# oreon:deps
BuildRequires:  coreutils
BuildRequires:  glibc-langpack-en
BuildRequires:  hunspell
BuildRequires:  hunspell-en
BuildRequires:  make
BuildRequires:  perl(CPAN::Meta)
BuildRequires:  perl(Carp)
BuildRequires:  perl(Exporter)
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(File::Spec)
BuildRequires:  perl(IPC::Run3)
BuildRequires:  perl(Pod::Spell)
BuildRequires:  perl(Symbol)
BuildRequires:  perl(Test::Builder)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(Test::Tester)
BuildRequires:  perl(Text::Wrap)
BuildRequires:  perl(strict)
BuildRequires:  perl(utf8)
BuildRequires:  perl(warnings)
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
# /oreon:deps
%description
"Test::Spelling" lets you check the spelling of a POD file, and report
its results in standard "Test::Simple" fashion. This module requires the
hunspell program.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%setup -q -n Test-Spelling-%{version}

%build

perl Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1 NO_PERLLOCAL=1
%{make_build}
%install
%{make_install}
%{_fixperms} -c %{buildroot}
%oreon_autofiles main

%check

LANG=en_US make test
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
