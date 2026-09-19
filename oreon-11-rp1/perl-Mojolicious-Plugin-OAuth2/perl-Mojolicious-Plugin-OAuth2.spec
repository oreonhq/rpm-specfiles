%global source0_hash 13490fb9c68947e65b143ade9d6b0f4270b412157eac57721f7ad497c3472181

Name:           perl-Mojolicious-Plugin-OAuth2
Version:        2.02
Release:        11%{?dist}
Summary:        A Mojolicious plugin that allows OAuth2 authentication

License:        Artistic-2.0
URL:            https://metacpan.org/release/Mojolicious-Plugin-OAuth2
Source0:        https://cpan.metacpan.org/authors/id/J/JH/JHTHORSEN/Mojolicious-Plugin-OAuth2-%{version}.tar.gz

BuildArch:      noarch

BuildRequires:  coreutils
BuildRequires:  make
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  perl(ExtUtils::MakeMaker) >= 6.76
BuildRequires:  perl(utf8)
# Run-time
BuildRequires:  perl(Carp)
BuildRequires:  perl(constant)
BuildRequires:  perl(Crypt::OpenSSL::Bignum) >= 0.09
BuildRequires:  perl(Crypt::OpenSSL::RSA) >= 0.31
BuildRequires:  perl(IO::Socket::SSL) >= 1.94
BuildRequires:  perl(MIME::Base64)
BuildRequires:  perl(Mojo::Base)
BuildRequires:  perl(Mojo::JWT) >= 0.09
BuildRequires:  perl(Mojo::Promise)
BuildRequires:  perl(Mojo::URL)
BuildRequires:  perl(Mojo::UserAgent)
BuildRequires:  perl(Mojo::Util)
BuildRequires:  perl(Mojolicious) >= 8.25
BuildRequires:  perl(Mojolicious::Plugin)
# Tests
BuildRequires:  perl(File::Find)
BuildRequires:  perl(lib)
BuildRequires:  perl(Mojo::JSON)
BuildRequires:  perl(Mojolicious::Lite)
BuildRequires:  perl(Test::Mojo)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)

Requires:   perl(IO::Socket::SSL) >= 1.94
Requires:   perl(Mojolicious) >= 8.25
Requires:   perl(Mojolicious::Plugin)
Requires:   perl(Mojo::Util)
Recommends: perl(Crypt::OpenSSL::Bignum) >= 0.09
Recommends: perl(Crypt::OpenSSL::RSA) >= 0.31
Recommends: perl(Mojo::JWT) >= 0.09

%{?perl_default_filter}

%description
This Mojolicious plugin allows you to easily authenticate against a OAuth2
provider. It includes configurations for a few popular providers, but you can
add your own easily as well.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n Mojolicious-Plugin-OAuth2-%{version}

%build
/usr/bin/perl Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1 NO_PERLLOCAL=1 OPTIMIZE="$RPM_OPT_FLAGS"
%{make_build}

%install
%{make_install}
%{_fixperms} $RPM_BUILD_ROOT/*

%check
%{make_build} test

%files
%doc Changes README README.md
%{perl_vendorlib}/*
%{_mandir}/man3/*

%changelog
%autochangelog
