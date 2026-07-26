%global source0_hash 8a87c118ea928d053ff3c4418bf300d74545a7439438092900f8c3a3aeb2c3da

Summary:	OO interface for spell-checking a block of text 
Name:		perl-Text-SpellChecker
Version:	0.14
Release:	35%{?dist}
License:	GPL-1.0-or-later OR Artistic-1.0-Perl
URL:		https://metacpan.org/release/Text-SpellChecker
Source0:	https://cpan.metacpan.org/modules/by-module/Text/Text-SpellChecker-%{version}.tar.gz
BuildArch:	noarch
# Module Build
BuildRequires:	coreutils
BuildRequires:	findutils
BuildRequires:	make
BuildRequires:	perl-generators
BuildRequires:	perl-interpreter
BuildRequires:	perl(ExtUtils::MakeMaker)
# Module Runtime
BuildRequires:	perl(Carp)
BuildRequires:	perl(MIME::Base64)
BuildRequires:	perl(Storable)
BuildRequires:	perl(strict)
BuildRequires:	perl(Text::Hunspell)
BuildRequires:	perl(warnings)
# Test Suite
%if 0%{?fedora} > 23 || 0%{?rhel} > 7
BuildRequires:	glibc-langpack-en
%endif
BuildRequires:	hunspell-en
BuildRequires:	perl(Test::More)
BuildRequires:	perl(utf8)
# Optional Tests
BuildRequires:	perl(Test::Pod)
%if 0%{?fedora:1} && 0%{?fedora} < 39
BuildRequires:	perl(Text::Aspell), aspell-en
%endif
# Dependencies
# hunspell is the preferred spell checking backend in Fedora
Requires:	perl(Text::Hunspell)

%description
This module is a thin layer above Text::Hunspell and allows one to spellcheck
a body of text. Whereas Text::Hunspell deals with words, Text::Spellchecker
deals with blocks of text. For instance, we provide methods for iterating
through the text, serializing the object (thus remembering where we left off),
and highlighting the current misspelled word within the text.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n Text-SpellChecker-%{version}

%build
perl Makefile.PL INSTALLDIRS=vendor
make %{?_smp_mflags}

%install
make pure_install DESTDIR=%{buildroot}
find %{buildroot} -type f -name .packlist -delete
%{_fixperms} -c %{buildroot}

%check
LANG=en_US make test TEST_VERBOSE=1

%files
%doc Changes README
%{perl_vendorlib}/Text/
%{_mandir}/man3/Text::SpellChecker.3*

%changelog
%autochangelog
