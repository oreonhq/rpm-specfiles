%global source0_hash 093c97fac15b47a8fe4d2936ef2df377abf77cc8ab74092d2128bb945d1fb46f

Name:           perl-Mail-IMAPClient
Version:        3.43
Release:        15%{?dist}
Summary:        An IMAP Client API
# Automatically converted from old format: GPL+ or Artistic - review is highly recommended.
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/Mail-IMAPClient
Source0:        https://cpan.metacpan.org/authors/id/P/PL/PLOBBES/Mail-IMAPClient-%{version}.tar.gz
BuildRequires: make
BuildRequires:  perl-generators
BuildRequires:  perl(ExtUtils::MakeMaker), perl(IO::Socket), perl(constant), perl(Socket)
BuildRequires:  perl(IO::File), perl(IO::Select), perl(Fcntl), perl(Errno), perl(Carp)
BuildRequires:  perl(Data::Dumper), perl(Parse::RecDescent), perl(Test::More)
BuildRequires:	perl(Authen::SASL), perl(Test::Pod)
BuildArch:      noarch

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
# the extended tests cannot be run without an IMAP server
yes n | %{__perl} Makefile.PL INSTALLDIRS=vendor
make

%install
rm -rf $RPM_BUILD_ROOT
make pure_install PERL_INSTALL_ROOT=$RPM_BUILD_ROOT
find $RPM_BUILD_ROOT -type f -name .packlist -exec rm -f {} ';'
chmod -R u+w $RPM_BUILD_ROOT/*

%check
make test

%files
%doc Changes README examples/
%{perl_vendorlib}/Mail/
%{_mandir}/man3/*.3*

%changelog
%autochangelog
