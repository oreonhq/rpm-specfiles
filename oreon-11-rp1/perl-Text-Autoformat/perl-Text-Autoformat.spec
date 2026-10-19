%global source0_hash 9dd4f4ce3daec4b4dbf5b59dac4568a8946aed12c28b4e5988c8e8c602c6b771
Name:           perl-Text-Autoformat
Version:        1.750000
Release:        1%{?dist}
Summary:        Automatic text wrapping and reformatting
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/Text-Autoformat
Source0:        https://cpan.metacpan.org/authors/id/N/NE/NEILB/Text-Autoformat-1.75.tar.gz
BuildArch:      noarch
# oreon:deps
BuildRequires:  coreutils
BuildRequires:  make
BuildRequires:  perl(Carp)
BuildRequires:  perl(Exporter)
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(Text::Reform)
BuildRequires:  perl(Text::Tabs)
BuildRequires:  perl(overload)
BuildRequires:  perl(strict)
BuildRequires:  perl(utf8)
BuildRequires:  perl(warnings)
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
# /oreon:deps
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
%oreon_autofiles main

%check

%{make_build}
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
