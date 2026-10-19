%global source0_hash 8398f8a58d8a059d2773b51392c758b825783cbf3980b4a6bc5c22f7f8690b18
Name:           perl-Text-Emoticon-MSN
Version:        0.04
Release:        1%{?dist}
Summary:        Emoticon filter of MSN Messenger
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/Text-Emoticon-MSN
Source0:        https://cpan.metacpan.org/authors/id/M/MI/MIYAGAWA/Text-Emoticon-MSN-%{version}.tar.gz
BuildArch:      noarch
%global __requires_exclude %{?__requires_exclude:%__requires_exclude|}^perl\\(Text::Emoticon\\)$
# oreon:deps
BuildRequires:  make
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(Text::Emoticon)
BuildRequires:  perl(base)
BuildRequires:  perl(strict)
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
# /oreon:deps
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
%oreon_autofiles main

%check

make test
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
