%global source0_hash 2dddc8ab9dc8986980151e4ba836a6bbf091f45cf195be1768ebdb4a993ed59b

Name:           perl-HTTP-Server-Simple-Authen
Version:        0.04
Release:        40%{?dist}
Summary:        Authentication plugin for HTTP::Server::Simple
# https://rt.cpan.org/Public/Bug/Display.html?id=71033
# You can redistribute it and/or modify it under the same terms as Perl itself.
# Automatically converted from old format: GPL+ or Artistic - review is highly recommended.
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/HTTP-Server-Simple-Authen
Source0:        https://cpan.metacpan.org/modules/by-module/HTTP/HTTP-Server-Simple-Authen-%{version}.tar.gz

BuildArch:      noarch
BuildRequires: make
BuildRequires:  perl-generators
BuildRequires:  perl(Authen::Simple) >= 0.04
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(HTTP::Server::Simple) >= 0.16
BuildRequires:  perl(Test::More) >= 0.32

Requires:       perl(Authen::Simple) >= 0.04
Requires:       perl(HTTP::Server::Simple) >= 0.16
Requires:       perl(Test::More) >= 0.32

%{?perl_default_filter}

%description
HTTP::Server::Simple::Authen is an HTTP::Server::Simple plugin to allow
HTTP authentication. Authentication scheme is pluggable and you can use
whatever Authentication protocol that Authen::Simple supports.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n HTTP-Server-Simple-Authen-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
make %{?_smp_mflags}

%install
make pure_install PERL_INSTALL_ROOT=%{buildroot}

find %{buildroot} -type f -name .packlist -exec rm -f {} \;
find %{buildroot} -depth -type d -exec rmdir {} 2>/dev/null \;

%{_fixperms} %{buildroot}/*

%check
make test

%files
%doc Changes
%{perl_vendorlib}/HTTP/Server/Simple/*
%{_mandir}/man3/HTTP*

%changelog
%autochangelog
