%global source0_hash f7409acb5952dc33bf1e1bc960533a7aa6b01df38cbb8e7b3c2e134bc0373b33

Name:           perl-Text-Emoticon
Version:        0.04
Release:        47%{?dist}
Summary:        Factory class for Yahoo! and MSN emoticons
# Automatically converted from old format: GPL+ or Artistic - review is highly recommended.
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/Text-Emoticon
Source0:        https://cpan.metacpan.org/authors/id/M/MI/MIYAGAWA/Text-Emoticon-%{version}.tar.gz
BuildArch:      noarch
# Build
BuildRequires:  make
BuildRequires:  perl-interpreter
BuildRequires:  perl-generators
BuildRequires:  perl(ExtUtils::MakeMaker) >= 6.76
# Runtime
BuildRequires:  perl(strict)
BuildRequires:  perl(UNIVERSAL::require)
# Tests only
BuildRequires:  perl(Test::More) >= 0.32

%description
Text::Emoticon is a factory class to dispatch MSN/YIM emoticon set.
It's made to become handy to be used in other applications like
Kwiki/MT plugins.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n Text-Emoticon-%{version}

%build
perl Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1
make %{?_smp_mflags}

%install
make pure_install DESTDIR=%{buildroot}
%{_fixperms} %{buildroot}/*

%check
make test

%files
%doc Changes
%{perl_vendorlib}/*
%{_mandir}/man3/*

%changelog
%autochangelog
