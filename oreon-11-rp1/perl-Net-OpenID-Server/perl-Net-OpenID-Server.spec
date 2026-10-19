%global source0_hash 4a962ff593f66f276500535dbc7a018c098dfd166168df38cbeddb3c20128617
Name:           perl-Net-OpenID-Server
Version:        1.09
Release:        1%{?dist}
Summary:        Library for building your own OpenID server/provider
License:        (GPL-1.0-or-later OR Artistic-1.0-Perl) AND LicenseRef-Fedora-Public-Domain
URL:            https://metacpan.org/release/Net-OpenID-Server
Source0:        https://cpan.metacpan.org/authors/id/R/RO/ROBN/Net-OpenID-Server-%{version}.tar.gz
BuildArch:      noarch
Requires:       perl(Net::OpenID::Common) >= 1.11
%global __requires_exclude %{?__requires_exclude:%__requires_exclude|}^perl\\(Net::OpenID::Common\\)$
# oreon:deps
BuildRequires:  coreutils
BuildRequires:  make
BuildRequires:  perl(Carp)
BuildRequires:  perl(Digest::SHA)
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(MIME::Base64)
BuildRequires:  perl(Net::OpenID::Common)
BuildRequires:  perl(Net::OpenID::IndirectMessage)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(Time::Local)
BuildRequires:  perl(URI)
BuildRequires:  perl(fields)
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
# /oreon:deps
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
%oreon_autofiles main

%check

make test
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
