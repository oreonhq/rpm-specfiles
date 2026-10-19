%global source0_hash ee111a6ff3e22e070a652e0867fdd3db183a49e436feffc1ff89ca3c876c445c
Name:           perl-Web-ID
Version:        1.927
Release:        22%{?dist}
Summary:        Implementation of WebID (a.k.a. FOAF+SSL)
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            http://search.cpan.org/dist/Web-ID/
Source0:        http://www.cpan.org/modules/by-module/Web/Web-ID-%{version}.tar.gz
BuildArch:      noarch
# oreon:deps
BuildRequires:  make
BuildRequires:  perl(Carp)
BuildRequires:  perl(Crypt::X509)
BuildRequires:  perl(DateTime)
BuildRequires:  perl(Digest::SHA)
BuildRequires:  perl(Exporter::Tiny)
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(File::ShareDir)
BuildRequires:  perl(File::Spec)
BuildRequires:  perl(File::Temp)
BuildRequires:  perl(List::MoreUtils)
BuildRequires:  perl(MIME::Base64)
BuildRequires:  perl(Math::BigInt)
BuildRequires:  perl(Moose)
BuildRequires:  perl(Moose::Role)
BuildRequires:  perl(Moose::Util)
BuildRequires:  perl(Path::Tiny)
BuildRequires:  perl(Plack)
BuildRequires:  perl(Plack::Middleware)
BuildRequires:  perl(Plack::Util)
BuildRequires:  perl(Plack::Util::Accessor)
BuildRequires:  perl(RDF::Query)
BuildRequires:  perl(RDF::Trine)
BuildRequires:  perl(RDF::Trine::NamespaceMap)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(Type::Library)
BuildRequires:  perl(Type::Utils)
BuildRequires:  perl(Types::DateTime)
BuildRequires:  perl(Types::Standard)
BuildRequires:  perl(Types::URI)
BuildRequires:  perl(URI)
BuildRequires:  perl(URI::Escape)
BuildRequires:  perl(base)
BuildRequires:  perl(constant)
BuildRequires:  perl(match::simple)
BuildRequires:  perl(namespace::sweep)
BuildRequires:  perl(strict)
BuildRequires:  perl(utf8)
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
# /oreon:deps
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
%oreon_autofiles main

%check

make test
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
