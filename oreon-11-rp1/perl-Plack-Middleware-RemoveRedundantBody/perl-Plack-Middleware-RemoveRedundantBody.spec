%global source0_hash 80d45f93d6b7290b0bd8b3cedd84a37fc501456cc3dec02ec7aad81c0018087e

Name:           perl-Plack-Middleware-RemoveRedundantBody
Version:        0.09
Release:        20%{?dist}
Summary:        Plack::Middleware which sets removes body for HTTP response if it's not required
# Automatically converted from old format: GPL+ or Artistic - review is highly recommended.
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/Plack-Middleware-RemoveRedundantBody
Source0:        https://cpan.metacpan.org/modules/by-module/Plack/Plack-Middleware-RemoveRedundantBody-%{version}.tar.gz
BuildArch:      noarch
BuildRequires:  make
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  perl(ExtUtils::MakeMaker) >= 6.76
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
# Run-time
BuildRequires:  perl(parent)
BuildRequires:  perl(Plack::Middleware)
BuildRequires:  perl(Plack::Util)
# Tests
BuildRequires:  perl(HTTP::Request::Common)
BuildRequires:  perl(Plack::Builder)
BuildRequires:  perl(Plack::Test)
BuildRequires:  perl(Test::More)

%description
This module removes body in HTTP response, if it's not required.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n Plack-Middleware-RemoveRedundantBody-%{version}

%build
perl Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1 NO_PERLLOCAL=1
%{make_build}

%install
%{make_install}
%{_fixperms} $RPM_BUILD_ROOT/*

%check
make test

%files
%license LICENSE
%doc Changes README
%{perl_vendorlib}/*
%{_mandir}/man3/*

%changelog
%autochangelog
