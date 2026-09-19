%global source0_hash e31fba94b8091863bb4f8a337dac855df5c171289803acc53ede98171b341773

%global __requires_exclude %{?__requires_exclude:%{__requires_exclude}|}^perl\\(AnyEvent|Digest::SHA1|JSON::XS\\)$

Name:           perl-AnyEvent-HTTP-Server
Version:        1.99998
Release:        9%{?dist}
Summary:        AnyEvent HTTP/1.1 Server
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://github.com/Mons/AnyEvent-HTTP-Server-II
Source0:        https://github.com/Mons/AnyEvent-HTTP-Server-II/archive/refs/tags/%{version}/AnyEvent-HTTP-Server-II-%{version}.tar.gz

BuildArch:      noarch

BuildRequires:  make
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  perl(:VERSION) >= 5.10
BuildRequires:  perl(AnyEvent) >= 5
BuildRequires:  perl(AnyEvent::Handle)
BuildRequires:  perl(AnyEvent::Socket)
BuildRequires:  perl(AnyEvent::Util)
BuildRequires:  perl(Config)
BuildRequires:  perl(constant)
BuildRequires:  perl(Data::Dumper)
BuildRequires:  perl(Digest::SHA1) >= 2
BuildRequires:  perl(Encode)
BuildRequires:  perl(ExtUtils::MakeMaker) >= 6.76
BuildRequires:  perl(feature)
BuildRequires:  perl(JSON::XS) >= 3
BuildRequires:  perl(MIME::Base64)
BuildRequires:  perl(overload)
BuildRequires:  perl(Scalar::Util)
BuildRequires:  perl(Socket)
BuildRequires:  perl(strict)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(Time::HiRes)
BuildRequires:  perl(utf8)
BuildRequires:  perl(warnings)
# tests
BuildRequires:  perl(EV)
BuildRequires:  perl(Class::XSAccessor)
BuildRequires:  perl(Compress::Zlib)
BuildRequires:  perl(FindBin)
BuildRequires:  perl(HTTP::Easy) >= 0.04
BuildRequires:  perl(Test::Pod)

Requires:       perl(AnyEvent) >= 5
Requires:       perl(Digest::SHA1) >= 2
Requires:       perl(JSON::XS) >= 3

%description
AnyEvent::HTTP::Server is a very fast asynchronous HTTP server written in
perl. It has been tested in high load production environments and may be
considered both fast and stable.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n AnyEvent-HTTP-Server-II-%{version}
perl -MConfig -pi -e 's,#!.*perl,$Config{startperl},' ex/*.pl

%build
unset AUTHOR
perl Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1 NO_PERLLOCAL=1
%{make_build}

%install
%{make_install}

%{_fixperms} $RPM_BUILD_ROOT/*

%check
make test

%files
%doc Changes ex README.md
%license LICENSE
%{perl_vendorlib}/*
%{_mandir}/man3/*

%changelog
%autochangelog
