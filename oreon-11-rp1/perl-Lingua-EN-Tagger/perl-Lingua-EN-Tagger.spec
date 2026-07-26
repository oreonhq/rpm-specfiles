%global source0_hash 949e8c87e4808f7ba096b979220ff081bbe03b6d57890d2eecd4b83ae872e993

Name:           perl-Lingua-EN-Tagger
Version:        0.31
Release:        19%{?dist}
Summary:        Part-of-speech tagger for English natural language processing
License:        GPL-3.0-only
URL:            https://metacpan.org/release/Lingua-EN-Tagger
Source0:        https://cpan.metacpan.org/authors/id/A/AC/ACOBURN/Lingua-EN-Tagger-%{version}.tar.gz
# Build
BuildRequires:  coreutils
BuildRequires:  make
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(File::Spec) >= 0.84
BuildRequires:  perl(FileHandle)
BuildRequires:  perl(Storable) >= 2.10
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
# Runtime
BuildRequires:  perl(Carp)
BuildRequires:  perl(HTML::TokeParser)
BuildRequires:  perl(Lingua::Stem::En)
BuildRequires:  perl(Memoize) >= 1.01
# Tests only
BuildRequires:  perl(Test::More)
BuildRequires:  perl(threads)
BuildRequires:  perl(threads::shared)
Requires:       perl(File::Spec) >= 0.84
Requires:       perl(Memoize) >= 1.01
Requires:       perl(Storable) >= 2.10

# despite being arch-dependent, there are no binaries
# so avoid empty debug package
%global debug_package %{nil}
%{?perl_default_filter}
%global __requires_exclude %{?__requires_exclude|%__requires_exclude|}^perl\\(File::Spec\\)$
%global __requires_exclude %{?__requires_exclude|%__requires_exclude|}^perl\\(Memoize\\)$
%global __requires_exclude %{?__requires_exclude|%__requires_exclude|}^perl\\(Storable\\)$

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

%check
make test

%files
%doc Changes README
%{perl_vendorarch}/*
%{_mandir}/man3/*

%changelog
%autochangelog
