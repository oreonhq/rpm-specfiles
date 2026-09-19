%global source0_hash 8398f8a58d8a059d2773b51392c758b825783cbf3980b4a6bc5c22f7f8690b18

Name:           perl-Text-Emoticon-MSN
Version:        0.04
Release:        47%{?dist}
Summary:        Emoticon filter of MSN Messenger
# Automatically converted from old format: GPL+ or Artistic - review is highly recommended.
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/Text-Emoticon-MSN
Source0:        https://cpan.metacpan.org/authors/id/M/MI/MIYAGAWA/Text-Emoticon-MSN-%{version}.tar.gz
BuildArch:      noarch
# Build
BuildRequires:  make
BuildRequires:  perl-interpreter
BuildRequires:  perl-generators
BuildRequires:  perl(ExtUtils::MakeMaker) >= 6.76
# Runtime
BuildRequires:  perl(base)
BuildRequires:  perl(strict)
BuildRequires:  perl(Text::Emoticon) >= 0.03
# Tests only
BuildRequires:  perl(Test::More) >= 0.32

%global __requires_exclude %{?__requires_exclude:%__requires_exclude|}^perl\\(Text::Emoticon\\)$

%description
Text::Emoticon::MSN is a text filter that replaces text emoticons like 
":-)", ";-P", etc. to the icons of MSN Messenger, detailed in
http://messenger.msn.com/Resource/Emoticons.aspx

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n Text-Emoticon-MSN-%{version}

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
