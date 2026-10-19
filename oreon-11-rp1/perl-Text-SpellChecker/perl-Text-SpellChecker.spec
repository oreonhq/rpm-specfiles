%global source0_hash 8a87c118ea928d053ff3c4418bf300d74545a7439438092900f8c3a3aeb2c3da
Summary:        OO interface for spell-checking a block of text
Name:		perl-Text-SpellChecker
Version:	0.14
Release:        1%{?dist}
License:	GPL-1.0-or-later OR Artistic-1.0-Perl
URL:		https://metacpan.org/release/Text-SpellChecker
Source0:        https://cpan.metacpan.org/modules/by-module/Text/Text-SpellChecker-%{version}.tar.gz
BuildArch:	noarch
Requires:	perl(Text::Hunspell)
# oreon:deps
BuildRequires:  coreutils
BuildRequires:  findutils
BuildRequires:  hunspell-en
BuildRequires:  make
BuildRequires:  perl(Carp)
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(MIME::Base64)
BuildRequires:  perl(Storable)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(Test::Pod)
BuildRequires:  perl(Text::Hunspell)
BuildRequires:  perl(strict)
BuildRequires:  perl(utf8)
BuildRequires:  perl(warnings)
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
# /oreon:deps
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
%oreon_autofiles main

%check

LANG=en_US make test TEST_VERBOSE=1
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
