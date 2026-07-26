%global source0_hash 0e1c386fe7c1843071dd996bdcaca610910664ae4b5d127c95feaefd99364f38

Name:           perl-Net-OpenID-Consumer
Version:        1.18
Release:        29%{?dist}
Summary:        Library for consumers of OpenID identities
# LicenseRef-Fedora-Public-Domain: examples/consumer.cgi
# GPL-1.0-or-later OR Artistic-1.0-Perl: the rest of the distribution
License:        (GPL-1.0-or-later OR Artistic-1.0-Perl) AND LicenseRef-Fedora-Public-Domain
URL:            https://metacpan.org/release/Net-OpenID-Consumer
Source0:        https://cpan.metacpan.org/authors/id/W/WR/WROG/Net-OpenID-Consumer-%{version}.tar.gz
BuildArch:      noarch
BuildRequires:  coreutils
BuildRequires:  make
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  perl(ExtUtils::MakeMaker) >= 6.76
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
# Run-time
BuildRequires:  perl(Carp)
BuildRequires:  perl(Digest::SHA)
BuildRequires:  perl(fields)
BuildRequires:  perl(HTML::Parser)
BuildRequires:  perl(HTTP::Request)
BuildRequires:  perl(JSON)
BuildRequires:  perl(LWP::UserAgent)
BuildRequires:  perl(MIME::Base64)
BuildRequires:  perl(Net::OpenID::Common) >= 1.19
BuildRequires:  perl(Net::OpenID::IndirectMessage)
BuildRequires:  perl(Net::OpenID::URIFetch)
BuildRequires:  perl(Net::OpenID::Yadis)
BuildRequires:  perl(Storable)
BuildRequires:  perl(Time::Local)
BuildRequires:  perl(URI)
BuildRequires:  perl(URI::Escape)
# Tests
BuildRequires:  perl(base)
BuildRequires:  perl(CGI)
BuildRequires:  perl(HTTP::Response)
BuildRequires:  perl(integer)
BuildRequires:  perl(lib)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(utf8)
BuildRequires:  perl(vars)

%description
This is the Perl API for (the consumer half of) OpenID, a distributed
identity system based on proving you own a URL, which is then your
identity.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n Net-OpenID-Consumer-%{version}

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
