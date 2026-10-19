%global source0_hash 23ef065897821337bdd16487e65e2a3798383348225c72cd762bb3741ad009b5
Name:           perl-MIME-EncWords
Version:        1.015.0
Release:        1%{?dist}
Summary:        Deal with RFC 2047 encoded words (improved)
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/MIME-EncWords
Source0:        https://cpan.metacpan.org/authors/id/N/NE/NEZUMI/MIME-EncWords-%{version}.tar.gz
BuildArch:      noarch
Requires:       perl(Encode) >= 1.98
Requires:       perl(MIME::Base64) >= 2.13
Requires:       perl(MIME::Charset) >= 1.10.1
%global __requires_exclude %{?__requires_exclude:%{__requires_exclude}|}^perl\\((MIME::Base64|MIME::Charset)\\)$
# oreon:deps
BuildRequires:  coreutils
BuildRequires:  make
BuildRequires:  perl(CPAN::Meta::Requirements)
BuildRequires:  perl(Carp)
BuildRequires:  perl(Encode)
BuildRequires:  perl(Encode::Encoding)
BuildRequires:  perl(Exporter)
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(MIME::Base64)
BuildRequires:  perl(MIME::Charset)
BuildRequires:  perl(Test)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(Test::Pod)
BuildRequires:  perl(base)
BuildRequires:  perl(charnames)
BuildRequires:  perl(strict)
BuildRequires:  perl(utf8)
BuildRequires:  perl(vars)
BuildRequires:  perl(warnings)
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  sed
# /oreon:deps
%description
MIME::EncWords is aimed to be another implementation of MIME::Words so that it
will achieve more exact conformance with RFC 2047 (former RFC 1522)
specifications. Additionally, it contains some improvements. Following synopsis
and descriptions are inherited from its inspirer, then added descriptions on
improvements (**) or changes and clarifications (*).

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n MIME-EncWords-%{version}

%build

perl Makefile.PL INSTALLDIRS=vendor NO_PERLLOCAL=1 NO_PACKLIST=1
%make_build
%install
%make_install
%{_fixperms} %{buildroot}/*
%oreon_autofiles main

%check

make test
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
