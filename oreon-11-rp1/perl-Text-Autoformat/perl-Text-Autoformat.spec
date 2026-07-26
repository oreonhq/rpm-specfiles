%global source0_hash 9dd4f4ce3daec4b4dbf5b59dac4568a8946aed12c28b4e5988c8e8c602c6b771

Name:           perl-Text-Autoformat
Version:        1.750000
Release:        19%{?dist}
Summary:        Automatic text wrapping and reformatting
# Automatically converted from old format: GPL+ or Artistic - review is highly recommended.
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/Text-Autoformat
Source0:        https://cpan.metacpan.org/authors/id/N/NE/NEILB/Text-Autoformat-1.75.tar.gz
BuildArch:      noarch
# Build
BuildRequires:  coreutils
BuildRequires:  make
BuildRequires:  perl-interpreter
BuildRequires:  perl-generators
BuildRequires:  perl(ExtUtils::MakeMaker) >= 6.76
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
# Runtime
BuildRequires:  perl(Carp)
BuildRequires:  perl(Exporter)
BuildRequires:  perl(overload)
BuildRequires:  perl(Text::Reform)
BuildRequires:  perl(Text::Tabs)
# Tests only
BuildRequires:  perl(Test::More) >= 0.88
BuildRequires:  perl(utf8)

%description
Text::Autoformat provides intelligent formatting of plain text without the
need for any kind of embedded mark-up. The module recognizes Internet
quoting conventions, a wide range of bulleting and number schemes, centered
text, and block quotations, and reformats each appropriately. Other options
allow the user to adjust inter-word and inter-paragraph spacing, justify
text, and impose various capitalization schemes.

The module also supplies a re-entrant, highly configurable replacement for
the built-in Perl format() mechanism.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n Text-Autoformat-1.75
chmod -c -x config.*

%build
/usr/bin/perl Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1 NO_PERLLOCAL=1
%{make_build}

%install
%{make_install}
%{_fixperms} %{buildroot}/*

%check
%{make_build}

%files
%license LICENSE
%doc Changes README config.emacs config.vim
%{perl_vendorlib}/Text
%{_mandir}/man3/Text::Autoformat.3pm*

%changelog
%autochangelog
