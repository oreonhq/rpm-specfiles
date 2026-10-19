%global source0_hash 0a191e99b77e68fcb0c88d2affaa79752baa633a8b65a786dfaba79f930a8719
Name:           perl-Text-MultiMarkdown
Version:        1.005000
Release:        1%{?dist}
Summary:        Convert MultiMarkdown syntax to (X)HTML
License:        BSD-3-Clause
URL:            https://metacpan.org/release/Text-MultiMarkdown
Source0:        https://cpan.metacpan.org/authors/id/B/BR/BRIANDFOY/Text-MultiMarkdown-1.005.tar.gz
BuildArch:      noarch
Requires:       perl(Text::Markdown) >= 1.000026
%{?perl_default_filter}
%global __requires_exclude %{?__requires_exclude:%__requires_exclude|}^perl\\(Text::Markdown\\)$
# oreon:deps
BuildRequires:  make
BuildRequires:  perl(Carp)
BuildRequires:  perl(Digest::MD5)
BuildRequires:  perl(Encode)
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(File::Spec)
BuildRequires:  perl(File::Spec::Functions)
BuildRequires:  perl(FindBin)
BuildRequires:  perl(HTML::Entities)
BuildRequires:  perl(List::MoreUtils)
BuildRequires:  perl(Test::Exception)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(Test::Pod)
BuildRequires:  perl(Test::Pod::Coverage)
BuildRequires:  perl(Test::Spelling)
BuildRequires:  perl(Text::Diff)
BuildRequires:  perl(Text::Markdown)
BuildRequires:  perl(Text::Unidecode)
BuildRequires:  perl(Unicode::Normalize)
BuildRequires:  perl(base)
BuildRequires:  perl(open)
BuildRequires:  perl(re)
BuildRequires:  perl(strict)
BuildRequires:  perl(utf8)
BuildRequires:  perl(warnings)
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  perl-podlators
# /oreon:deps
%description
Markdown is a text-to-HTML filter; it translates an easy-to-read / easy-to-
write structured text format into HTML. Markdown's text format is most
similar to that of plain text email, and supports features such as headers,
*emphasis*, code blocks, block quotes, and links.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n Text-MultiMarkdown-1.005

%build

/usr/bin/perl Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1 NO_PERLLOCAL=1
%{make_build}
%install
%{make_install}
%{_fixperms} $RPM_BUILD_ROOT/*
%oreon_autofiles main

%check

TEST_POD=1 TEST_SPELLING=1 %{make_build} test
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
