%global source0_hash 559b2dd654b65de900414468d5870856fa9dbaf759cfefac88c00e0659eb1776

Name:           perl-Test-Email
Version:        0.07
Release:        35%{?dist}
Summary:        Test Email Contents
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/Test-Email
Source0:        https://cpan.metacpan.org/authors/id/J/JA/JAMES/Test-Email-%{version}.tar.gz
BuildArch:      noarch

BuildRequires:  %{__make}
BuildRequires:  perl-generators
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(Mail::POP3Client)
BuildRequires:  perl(Mail::Sendmail)
BuildRequires:  perl(MIME::Entity)
BuildRequires:  perl(MIME::Parser)
BuildRequires:  perl(Test::Builder)

%description
Test::Email is a subclass of MIME::Entity, with the above methods.
If you want the messages fetched from a POP3 account, use Test::POP3.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n Test-Email-%{version}

# Fix permissions
find -type f -exec chmod -x {} \;

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1 NO_PERLLOCAL=1
%{make_build}

%install
%{make_install}
%{_fixperms} $RPM_BUILD_ROOT/*

%check
%{__make} test

%files
%doc Changes README
%{perl_vendorlib}/*
%{_mandir}/man3/*

%changelog
%autochangelog
