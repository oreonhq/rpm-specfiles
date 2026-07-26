%global source0_hash 4a962ff593f66f276500535dbc7a018c098dfd166168df38cbeddb3c20128617

Name:           perl-Net-OpenID-Server
Version:        1.09
Release:        32%{?dist}
Summary:        Library for building your own OpenID server/provider
# LicenseRef-Fedora-Public-Domain: examples/server.cgi
# GPL-1.0-or-later OR Artistic-1.0-Perl: the rest of the distribution
License:        (GPL-1.0-or-later OR Artistic-1.0-Perl) AND LicenseRef-Fedora-Public-Domain
URL:            https://metacpan.org/release/Net-OpenID-Server
Source0:        https://cpan.metacpan.org/authors/id/R/RO/ROBN/Net-OpenID-Server-%{version}.tar.gz
BuildArch:      noarch
BuildRequires:  coreutils
BuildRequires:  make
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  perl(ExtUtils::MakeMaker) >= 6.31
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
# Run-time
BuildRequires:  perl(Carp)
BuildRequires:  perl(Digest::SHA)
BuildRequires:  perl(fields)
BuildRequires:  perl(MIME::Base64)
BuildRequires:  perl(Net::OpenID::Common) >= 1.11
BuildRequires:  perl(Net::OpenID::IndirectMessage)
BuildRequires:  perl(Time::Local)
BuildRequires:  perl(URI)
# Tests
BuildRequires:  perl(Test::More)
Requires:       perl(Net::OpenID::Common) >= 1.11

%global __requires_exclude %{?__requires_exclude:%__requires_exclude|}^perl\\(Net::OpenID::Common\\)$

%description
This is the Perl API for (the server half of) OpenID, a distributed
identity system based on proving you own a URL, which is then your
identity.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n Net-OpenID-Server-%{version}

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
%doc Changes examples README
%{perl_vendorlib}/*
%{_mandir}/man3/*

%changelog
%autochangelog
