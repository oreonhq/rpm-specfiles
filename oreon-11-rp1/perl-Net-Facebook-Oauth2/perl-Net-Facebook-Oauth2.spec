%global source0_hash f97a97a1cb7eb1fb8e5d115a74c058b462646a1b7ea43227ed2cd8011f580225
Name:           perl-Net-Facebook-Oauth2
Version:        0.12
Release:        18%{?dist}
Summary:        Simple Perl wrapper around Facebook OAuth 2.0 protocol
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/pod/Net::Facebook::Oauth2/
Source0:        https://cpan.metacpan.org/modules/by-module/Net/Net-Facebook-Oauth2-%{version}.tar.gz
BuildArch:      noarch
Requires:       perl(LWP::Protocol::https)
%{?perl_default_filter}
# oreon:deps
BuildRequires:  coreutils
BuildRequires:  findutils
BuildRequires:  make
BuildRequires:  perl(Carp)
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(JSON::MaybeXS)
BuildRequires:  perl(LWP::Protocol::https)
BuildRequires:  perl(LWP::UserAgent)
BuildRequires:  perl(Plack::Loader)
BuildRequires:  perl(Plack::Request)
BuildRequires:  perl(Test::Exception)
BuildRequires:  perl(Test::MockModule)
BuildRequires:  perl(Test::MockObject)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(Test::Requires)
BuildRequires:  perl(Test::TCP)
BuildRequires:  perl(URI)
BuildRequires:  perl(URI::Escape)
BuildRequires:  perl(parent)
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
BuildRequires:  perl-generators
# /oreon:deps
%description
Net::Facebook::Oauth2 gives you a way to simply access FaceBook Oauth
2.0 protocol.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n Net-Facebook-Oauth2-%{version}

%build

%{__perl} Makefile.PL INSTALLDIRS=vendor
%make_build
%install
make pure_install DESTDIR=$RPM_BUILD_ROOT
find $RPM_BUILD_ROOT -type f -name .packlist -exec rm -f {} \;
find $RPM_BUILD_ROOT -depth -type d -exec rmdir {} 2>/dev/null \;
%{_fixperms} $RPM_BUILD_ROOT/*
%oreon_autofiles main

%check

make test
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
