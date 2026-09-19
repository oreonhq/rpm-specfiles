%global source0_hash ab6bb80508f4fddaf2d51b20ca876aab038582a86b5228e6435411348af53c82

Name:           perl-Object-Event
Version:        1.23
Release:        40%{?dist}
Summary:        Class that provides an event callback interface
# Automatically converted from old format: GPL+ or Artistic - review is highly recommended.
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/Object-Event
Source0:        https://cpan.metacpan.org/authors/id/E/EL/ELMEX/Object-Event-%{version}.tar.gz
BuildArch:      noarch
BuildRequires:  coreutils
BuildRequires:  findutils
BuildRequires:  make
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  perl(AnyEvent::Util)
BuildRequires:  perl(base)
BuildRequires:  perl(Carp)
BuildRequires:  perl(common::sense)
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(sort)
BuildRequires:  perl(strict)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(warnings)

%{?perl_default_filter}

%description
This module was mainly written for Net::XMPP2, Net::IRC3, AnyEvent::HTTPD
and BS to provide a consistent API for registering and emitting events.
Even though I originally wrote it for those modules I released it
separately in case anyone may find this module useful.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n Object-Event-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
make %{?_smp_mflags}

%install
make pure_install DESTDIR=$RPM_BUILD_ROOT

find $RPM_BUILD_ROOT -type f -name .packlist -exec rm -f {} \;
find $RPM_BUILD_ROOT -depth -type d -exec rmdir {} 2>/dev/null \;

%{_fixperms} $RPM_BUILD_ROOT/*

%check
make test

%files
%doc Changes README
%{perl_vendorlib}/*
%{_mandir}/man3/*

%changelog
%autochangelog
