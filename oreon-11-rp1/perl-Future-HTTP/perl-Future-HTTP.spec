%global source0_hash f76301d9b5acf2ddc80374db0f84b0b340bf1475e091fba73f9ab39d1f3c8cc2
%bcond network_tests 0
Name:           perl-Future-HTTP
Version:        0.17
Release:        5%{?dist}
Summary:        HTTP client with a Future API
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/dist/Future-HTTP
Source0:        https://cpan.metacpan.org/authors/id/C/CO/CORION/Future-HTTP-%{version}.tar.gz
BuildArch:      noarch
Requires:       perl(Fcntl)
Requires:       perl(IO::Async::Loop)
Requires:       perl(IO::Uncompress::Bunzip2)
Requires:       perl(IO::Uncompress::Gunzip)
Requires:       perl(IO::Uncompress::Inflate)
Requires:       perl(IO::Uncompress::RawInflate)
Requires:       perl(MIME::Base64)
Requires:       perl(MIME::QuotedPrint)
Requires:       perl(warnings)
Requires:       perl(HTTP::Request) >= 6.07
%global __requires_exclude ^perl\\(HTTP::Request\\)$
# oreon:deps
BuildRequires:  coreutils
BuildRequires:  make
BuildRequires:  perl(:VERSION)
BuildRequires:  perl(AnyEvent)
BuildRequires:  perl(AnyEvent::Future)
BuildRequires:  perl(AnyEvent::HTTP)
BuildRequires:  perl(Data::Dumper)
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(Fcntl)
BuildRequires:  perl(Future)
BuildRequires:  perl(Future::Mojo)
BuildRequires:  perl(HTTP::Request)
BuildRequires:  perl(HTTP::Tiny)
BuildRequires:  perl(HTTP::Tiny::Paranoid)
BuildRequires:  perl(IO::Async::Future)
BuildRequires:  perl(IO::Async::Loop)
BuildRequires:  perl(IO::Uncompress::Bunzip2)
BuildRequires:  perl(IO::Uncompress::Gunzip)
BuildRequires:  perl(IO::Uncompress::Inflate)
BuildRequires:  perl(IO::Uncompress::RawInflate)
BuildRequires:  perl(MIME::Base64)
BuildRequires:  perl(MIME::QuotedPrint)
BuildRequires:  perl(Mojo::UserAgent)
BuildRequires:  perl(Mojolicious)
BuildRequires:  perl(Moo)
BuildRequires:  perl(Moo::Role)
BuildRequires:  perl(Net::Async::HTTP)
BuildRequires:  perl(Pod::Markdown)
BuildRequires:  perl(Test::HTTP::LocalServer)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(Test::Without::Module)
BuildRequires:  perl(URI)
BuildRequires:  perl(experimental)
BuildRequires:  perl(feature)
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
# /oreon:deps
%description
This module is a wrapper combining Future with the API provided by
AnyEvent::HTTP. The backend used for the HTTP protocols depends on
whether one of the event loops is loaded.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n Future-HTTP-%{version}
%if %{without network_tests}
rm t/01-http-tiny-paranoid.t
%endif
perl -pi -e 's/\r//' Changes

%build

perl Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1 NO_PERLLOCAL=1
%{make_build}
%install
%{make_install}
%{_fixperms} %{buildroot}/*
%oreon_autofiles main

%check

make test
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
