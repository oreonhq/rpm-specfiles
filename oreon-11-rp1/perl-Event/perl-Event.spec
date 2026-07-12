%global source0_hash 0504242229a2bcef418eeb04e29044f5a1854fcd7fcdce1276068d3b21510cc4

Name:		perl-Event
Version:	1.28
Release:	17%{?dist}
Summary:	Event loop processing
License:	GPL-1.0-or-later OR Artistic-1.0-Perl
URL:		https://metacpan.org/release/Event
Source0:	https://cpan.metacpan.org/modules/by-module/Event/Event-%{version}.tar.gz
# Module Build
BuildRequires:	coreutils
BuildRequires:	findutils
BuildRequires:	gcc
BuildRequires:	make
BuildRequires:	perl-devel
BuildRequires:	perl-generators
BuildRequires:	perl-interpreter
BuildRequires:	perl(ExtUtils::MakeMaker)
# Module Runtime
BuildRequires:	perl(base)
BuildRequires:	perl(Carp)
BuildRequires:	perl(Config)
BuildRequires:	perl(DynaLoader)
BuildRequires:	perl(Exporter)
BuildRequires:	perl(integer)
BuildRequires:	perl(strict)
BuildRequires:	perl(Time::HiRes)
BuildRequires:	perl(vars)
# Test Suite
BuildRequires:	perl(Symbol)
BuildRequires:	perl(Test) >= 1
BuildRequires:	perl(Test::More)
# Dependencies
Requires:	perl(Time::HiRes)

%{?perl_default_filter}

Provides:       perl(Event)
%description
The Event module provide a central facility to watch for various types of
events and invoke a callback when these events occur. The idea is to delay the
handling of events so that they may be dispatched in priority order when it is
safe for callbacks to execute.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%setup -q -n Event-%{version}

# Fix up permissions and shellbangs
perl -pi -e 's|#!./perl|#!/usr/bin/perl|' demo/*.t t/*.t util/bench.pl
%{_fixperms} -c demo/ util/

%build
perl Makefile.PL INSTALLDIRS=vendor OPTIMIZE="%{optflags}"
make %{?_smp_mflags}

%install
make pure_install DESTDIR=%{buildroot}
find %{buildroot} -type f -name .packlist -delete
find %{buildroot} -type f -name '*.bs' -empty -delete
%{_fixperms} -c %{buildroot}

%check
make test

%files
%doc ANNOUNCE Changes README README.EV TODO
%doc Tutorial.pdf Tutorial.pdf-errata.txt demo/ t/ util/
%doc %{perl_vendorarch}/Event.pod
%{perl_vendorarch}/auto/Event/
%{perl_vendorarch}/Event.pm
%{perl_vendorarch}/Event/
%{_mandir}/man3/Event.3*
%{_mandir}/man3/Event::MakeMaker.3*
%{_mandir}/man3/Event::generic.3*

%changelog
%autochangelog
