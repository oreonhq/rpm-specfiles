%global source0_hash 093c97fac15b47a8fe4d2936ef2df377abf77cc8ab74092d2128bb945d1fb46f
Name:           perl-Mail-IMAPClient
Version:        3.43
Release:        15%{?dist}
Summary:        An IMAP Client API
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/Mail-IMAPClient
Source0:        https://cpan.metacpan.org/authors/id/P/PL/PLOBBES/Mail-IMAPClient-%{version}.tar.gz
BuildArch:      noarch
# oreon:deps
BuildRequires:  make
BuildRequires:  perl(Authen::SASL)
BuildRequires:  perl(Carp)
BuildRequires:  perl(Data::Dumper)
BuildRequires:  perl(Errno)
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(Fcntl)
BuildRequires:  perl(IO::File)
BuildRequires:  perl(IO::Select)
BuildRequires:  perl(IO::Socket)
BuildRequires:  perl(Parse::RecDescent)
BuildRequires:  perl(Socket)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(Test::Pod)
BuildRequires:  perl(constant)
BuildRequires:  perl-generators
# /oreon:deps
%description
This module provides perl routines that simplify a sockets connection
to and an IMAP conversation with an IMAP server.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n Mail-IMAPClient-%{version}
sed -i 's#/usr/local/bin/perl#/usr/bin/perl#' examples/*.pl

# Turn off exec bits in examples to avoid docfile dependencies
chmod -c -x examples/*.pl

# Fix character encoding in documentation
iconv -f iso-8859-1 -t utf-8 < Changes > Changes.utf8
mv Changes.utf8 Changes

%build

yes n | %{__perl} Makefile.PL INSTALLDIRS=vendor
make
%install
rm -rf $RPM_BUILD_ROOT
make pure_install PERL_INSTALL_ROOT=$RPM_BUILD_ROOT
find $RPM_BUILD_ROOT -type f -name .packlist -exec rm -f {} ';'
chmod -R u+w $RPM_BUILD_ROOT/*
%oreon_autofiles main

%check

make test
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
