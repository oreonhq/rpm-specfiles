%global source0_hash 7d7b5e151c92ad3c0edb48e508f9cb847bd06cf44403754bd0465844446a0cb2
Name:           perl-WWW-xkcd
Version:        0.009
Release:        22%{?dist}
Summary:        Synchronous and asynchronous interfaces to xkcd comics
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/WWW-xkcd
Source0:        https://cpan.metacpan.org/authors/id/X/XS/XSAWYERX/WWW-xkcd-%{version}.tar.gz
BuildArch:      noarch
Recommends:     perl(AnyEvent)
Recommends:     perl(AnyEvent::HTTP)
%{?perl_default_filter}
# oreon:deps
BuildRequires:  make
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(File::Spec)
BuildRequires:  perl(IO::Handle)
BuildRequires:  perl(IPC::Open3)
BuildRequires:  perl(JSON::MaybeXS)
BuildRequires:  perl(Test::Fatal)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(blib)
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
# /oreon:deps
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
%oreon_autofiles main

%check

%{?!_with_network_tests: rm t/sync.t }
%{__make} test
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
