%global source0_hash ee111a6ff3e22e070a652e0867fdd3db183a49e436feffc1ff89ca3c876c445c

Name:           perl-Web-ID
Version:        1.927
Release:        22%{?dist}
Summary:        Implementation of WebID (a.k.a. FOAF+SSL)
# Automatically converted from old format: GPL+ or Artistic - review is highly recommended.
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            http://search.cpan.org/dist/Web-ID/
Source0:        http://www.cpan.org/modules/by-module/Web/Web-ID-%{version}.tar.gz
BuildArch:      noarch
BuildRequires: make
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  perl(base)
BuildRequires:  perl(Carp)
BuildRequires:  perl(constant)
BuildRequires:  perl(strict)
BuildRequires:  perl(utf8)
BuildRequires:  perl(Crypt::X509)
BuildRequires:  perl(DateTime)
BuildRequires:  perl(Digest::SHA)
BuildRequires:  perl(Exporter::Tiny)
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(File::ShareDir)
BuildRequires:  perl(File::Spec)
BuildRequires:  perl(File::Temp)
BuildRequires:  perl(List::MoreUtils)
BuildRequires:  perl(match::simple) >= 0.008
BuildRequires:  perl(Math::BigInt)
BuildRequires:  perl(MIME::Base64)
BuildRequires:  perl(Moose) >= 2.0600
BuildRequires:  perl(Moose::Role)
BuildRequires:  perl(Moose::Util)
BuildRequires:  perl(namespace::sweep)
BuildRequires:  perl(Path::Tiny) >= 0.017
BuildRequires:  perl(Plack)
BuildRequires:  perl(Plack::Middleware)
BuildRequires:  perl(Plack::Util)
BuildRequires:  perl(Plack::Util::Accessor)
BuildRequires:  perl(RDF::Query) >= 2.900
BuildRequires:  perl(RDF::Trine) >= 1.000
BuildRequires:  perl(RDF::Trine::NamespaceMap)
BuildRequires:  perl(Test::More) >= 0.96
BuildRequires:  perl(Type::Library)
BuildRequires:  perl(Types::DateTime)
BuildRequires:  perl(Types::Standard) >= 0.040
BuildRequires:  perl(Types::URI)
BuildRequires:  perl(Type::Utils)
BuildRequires:  perl(URI)
BuildRequires:  perl(URI::Escape)

%description
WebID is a simple authentication protocol based on TLS (Transaction Layer
Security, better known as Secure Socket Layer, SSL) and the Semantic Web.
This module provides a Perl implementation for authenticating clients
using WebID.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n Web-ID-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
%make_build

%install
make pure_install DESTDIR=$RPM_BUILD_ROOT

find $RPM_BUILD_ROOT -type f -name .packlist -exec rm -f {} \;
find $RPM_BUILD_ROOT -depth -type d -exec rmdir {} 2>/dev/null \;

%{_fixperms} $RPM_BUILD_ROOT/*

%check
make test

%files
%doc Changes CONTRIBUTING COPYRIGHT CREDITS README
%license LICENSE
%{perl_vendorlib}/*
%{_mandir}/man3/*

%changelog
%autochangelog
