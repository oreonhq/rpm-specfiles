%global source0_hash 7d7b5e151c92ad3c0edb48e508f9cb847bd06cf44403754bd0465844446a0cb2

Name:           perl-WWW-xkcd
Version:        0.009
Release:        22%{?dist}
Summary:        Synchronous and asynchronous interfaces to xkcd comics

# Automatically converted from old format: GPL+ or Artistic - review is highly recommended.
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/WWW-xkcd
Source0:        https://cpan.metacpan.org/authors/id/X/XS/XSAWYERX/WWW-xkcd-%{version}.tar.gz

BuildArch:      noarch

BuildRequires: make
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  perl(blib)
BuildRequires:  perl(ExtUtils::MakeMaker) >= 6.76
BuildRequires:  perl(File::Spec)
BuildRequires:  perl(IO::Handle)
BuildRequires:  perl(IPC::Open3)
BuildRequires:  perl(JSON::MaybeXS)
BuildRequires:  perl(strict)
BuildRequires:  perl(Test::Fatal)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(warnings)

Recommends:     perl(AnyEvent)
Recommends:     perl(AnyEvent::HTTP)

%{?perl_default_filter}

%description
This module allows you to access xkcd comics (http://www.xkcd.com/) using
the official API in synchronous mode (what people are used to) or in
asynchronous mode.

The asynchronous mode requires you have AnyEvent and AnyEvent::HTTP
available. However, since it's just supported and not necessary, it is not
declared as a prerequisite.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n WWW-xkcd-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1 OPTIMIZE="$RPM_OPT_FLAGS"
%{__make} %{?_smp_mflags}

%install
%{__make} pure_install DESTDIR=$RPM_BUILD_ROOT
%{_fixperms} $RPM_BUILD_ROOT/*

%check
# This test requires network access. Disable for Koji builds.
%{?!_with_network_tests: rm t/sync.t }
%{__make} test

%files
%doc Changes
%license LICENSE
%{perl_vendorlib}/*
%{_mandir}/man3/*

%changelog
%autochangelog
