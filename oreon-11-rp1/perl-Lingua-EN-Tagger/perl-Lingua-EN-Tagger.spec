%global source0_hash 949e8c87e4808f7ba096b979220ff081bbe03b6d57890d2eecd4b83ae872e993
Name:           perl-Lingua-EN-Tagger
Version:        0.31
Release:        1%{?dist}
Summary:        Part-of-speech tagger for English natural language processing
License:        GPL-3.0-only
URL:            https://metacpan.org/release/Lingua-EN-Tagger
Source0:        https://cpan.metacpan.org/authors/id/A/AC/ACOBURN/Lingua-EN-Tagger-%{version}.tar.gz
Requires:       perl(File::Spec) >= 0.84
Requires:       perl(Memoize) >= 1.01
Requires:       perl(Storable) >= 2.10
%global debug_package %{nil}
%{?perl_default_filter}
%global __requires_exclude %{?__requires_exclude|%__requires_exclude|}^perl\\(File::Spec\\)$
%global __requires_exclude %{?__requires_exclude|%__requires_exclude|}^perl\\(Memoize\\)$
%global __requires_exclude %{?__requires_exclude|%__requires_exclude|}^perl\\(Storable\\)$
# oreon:deps
BuildRequires:  coreutils
BuildRequires:  make
BuildRequires:  perl(Carp)
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(File::Spec)
BuildRequires:  perl(FileHandle)
BuildRequires:  perl(HTML::TokeParser)
BuildRequires:  perl(Lingua::Stem::En)
BuildRequires:  perl(Memoize)
BuildRequires:  perl(Storable)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(strict)
BuildRequires:  perl(threads)
BuildRequires:  perl(threads::shared)
BuildRequires:  perl(warnings)
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
# /oreon:deps
%description
The module is a probability based, corpus-trained tagger that assigns POS
tags to English text based on a lookup dictionary and a set of probability
values. The tagger assigns appropriate tags based on conditional
probabilities - it examines the preceding tag to determine the appropriate
tag for the current word. Unknown words are classified according to word
morphology or can be set to be treated as nouns or other parts of speech.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n Lingua-EN-Tagger-%{version}

%build

perl Makefile.PL INSTALLDIRS=vendor INSTALLVENDORLIB=%{perl_vendorarch} NO_PACKLIST=1 NO_PERLLOCAL=1
%{make_build}
%install
%{make_install}
%{_fixperms} %{buildroot}/*
%oreon_autofiles main

%check

make test
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
