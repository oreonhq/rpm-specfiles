%global source0_hash 38c659f03a4d7362e16832a3489d17f86a2ea36471d335e17ce323457df5bc60

Name:           perl-Test-Spelling
Version:        0.25
Release:        20%{?dist}
Summary:        Check for spelling errors in POD files
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/Test-Spelling
Source0:        https://cpan.metacpan.org/modules/by-module/Test/Test-Spelling-%{version}.tar.gz
BuildArch:      noarch
# Module Build
BuildRequires:  coreutils
BuildRequires:  make
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  perl(ExtUtils::MakeMaker) >= 6.76
# Module Runtime
BuildRequires:  hunspell
BuildRequires:  perl(Carp)
BuildRequires:  perl(Exporter) >= 5.57
BuildRequires:  perl(File::Spec)
BuildRequires:  perl(IPC::Run3) >= 0.044
BuildRequires:  perl(Pod::Spell) >= 1.01
BuildRequires:  perl(strict)
BuildRequires:  perl(Symbol)
BuildRequires:  perl(Test::Builder)
BuildRequires:  perl(Text::Wrap)
BuildRequires:  perl(warnings)
# Test Suite
BuildRequires:  glibc-langpack-en
BuildRequires:  hunspell-en
BuildRequires:  perl(Test::More) >= 0.88
BuildRequires:  perl(Test::Tester)
BuildRequires:  perl(utf8)
# Optional Tests
BuildRequires:  perl(CPAN::Meta) >= 2.120900
# Dependencies
Requires:       hunspell
Requires:       perl(Carp)

Provides:       perl(Test::Spelling)
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

%check
LANG=en_US make test

%files
%license LICENSE
%doc Changes README
%{perl_vendorlib}/Test/
%{_mandir}/man3/Test::Spelling.3*

%changelog
%autochangelog
