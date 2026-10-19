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
Requires:       perl(AnyEvent) >= 5
Requires:       perl(Digest::SHA1) >= 2
Requires:       perl(JSON::XS) >= 3
# oreon:deps
BuildRequires:  make
BuildRequires:  perl(:VERSION)
BuildRequires:  perl(AnyEvent)
BuildRequires:  perl(AnyEvent::Handle)
BuildRequires:  perl(AnyEvent::Socket)
BuildRequires:  perl(AnyEvent::Util)
BuildRequires:  perl(Class::XSAccessor)
BuildRequires:  perl(Compress::Zlib)
BuildRequires:  perl(Config)
BuildRequires:  perl(Data::Dumper)
BuildRequires:  perl(Digest::SHA1)
BuildRequires:  perl(EV)
BuildRequires:  perl(Encode)
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(FindBin)
BuildRequires:  perl(HTTP::Easy)
BuildRequires:  perl(JSON::XS)
BuildRequires:  perl(MIME::Base64)
BuildRequires:  perl(Scalar::Util)
BuildRequires:  perl(Socket)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(Test::Pod)
BuildRequires:  perl(Time::HiRes)
BuildRequires:  perl(constant)
BuildRequires:  perl(feature)
BuildRequires:  perl(overload)
BuildRequires:  perl(strict)
BuildRequires:  perl(utf8)
BuildRequires:  perl(warnings)
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
# /oreon:deps
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
%oreon_autofiles main

%check

make test
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
